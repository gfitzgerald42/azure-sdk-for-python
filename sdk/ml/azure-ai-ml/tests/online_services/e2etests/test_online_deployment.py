import uuid

import pytest

from azure.ai.ml import MLClient, load_online_deployment, load_online_endpoint
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import ManagedOnlineEndpoint, Model, ManagedOnlineDeployment

from devtools_testutils import AzureRecordedTestCase


@pytest.mark.e2etest
@pytest.mark.production_experience_test
class TestOnlineDeployment(AzureRecordedTestCase):
    @pytest.mark.skip(
        reason="Tests failing in internal automation due to lack of quota. Cannot record or run in live mode."
    )
    def test_online_deployment(self, client: MLClient) -> None:
        endpoint_yaml = "tests/test_configs/deployments/online/simple_online_endpoint_mir.yaml"
        deployment_yaml = "tests/test_configs/deployments/online/online_deployment_1.yaml"
        name = "online-ept-" + uuid.uuid4().hex[:15]
        endpoint = load_online_endpoint(endpoint_yaml)
        endpoint.name = name

        deployment = load_online_deployment(deployment_yaml)
        deployment.endpoint_name = name
        deployment.name = "online-dpm-" + uuid.uuid4().hex[:15]

        # create a endpoint
        client.online_endpoints.begin_create_or_update(endpoint)

        try:
            # create a deployment
            client.online_deployments.begin_create_or_update(deployment)
            dep = client.online_deployments.get(name=deployment.name, endpoint_name=endpoint.name)
            assert dep.name == deployment.name

            deps = client.online_deployments.list(endpoint_name=endpoint.name)
            assert len(list(deps)) > 0

            endpoint.traffic = {deployment.name: 100}
            client.online_endpoints.begin_create_or_update(endpoint)
            endpoint_updated = client.online_endpoints.get(endpoint.name)
            assert endpoint_updated.traffic[deployment.name] == 100
            client.online_endpoints.invoke(
                endpoint_name=endpoint.name,
                request_file="tests/test_configs/deployments/model-1/sample-request.json",
            )
        except Exception as ex:
            raise ex
        finally:
            client.online_endpoints.begin_delete(name=endpoint.name)

    @pytest.mark.skip(reason="Known failure")
    def test_online_deployment_skip_script_validation(self, client: MLClient,variable_recorder) -> None:
        online_endpoint_name = variable_recorder.get_or_record("online_endpoint_name", "online-endp" + uuid.uuid4().hex[:15])
        online_deployment_name = variable_recorder.get_or_record("online_deployment_name", "online-dpm" + uuid.uuid4().hex[:15])

        # create an online endpoint
        endpoint = ManagedOnlineEndpoint(
            name=online_endpoint_name,
            description="this is a sample online endpoint",
            auth_mode="key",
            tags={"foo": "bar"},
        )

        client.begin_create_or_update(endpoint).result()

        try:
            # create a blue deployment
            model = Model(
                name="test-model",
                version="4",
                path="tests/test_configs/deployments/sklearn-diabetes/model",
                type=AssetTypes.MLFLOW_MODEL,
                description="my sample mlflow model",
            )

            blue_deployment = ManagedOnlineDeployment(
                name=online_deployment_name,
                endpoint_name=online_endpoint_name,
                model=model,
                instance_type="Standard_F4s_v2",
                instance_count=1,
            )

            client.online_deployments.begin_create_or_update(blue_deployment).result()
        except Exception as ex:
            raise ex
        finally:
            client.online_endpoints.begin_delete(name=online_endpoint_name)