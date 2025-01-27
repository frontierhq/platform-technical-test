import os
import yaml
from helpers.apply_terraform import apply_terraform
from helpers.init_terraform import init_terraform
from kubernetes import client, config, utils


def deploy():
    terraform = init_terraform(
        working_dir=os.path.join(os.getcwd(), "src", "terraform")
    )

    outputs = apply_terraform(
        terraform=terraform,
        # var={}, # Uncomment to pass variables to terraform
        # var_file=os.path.join(os.getcwd(), "config", "main.tfvars"), # Uncomment to pass variables file to terraform
    )

    # Uncomment below to deploy k8s resources

    # kube_config = yaml.load(outputs["kube_config_raw"]["value"], Loader=yaml.FullLoader)
    # config.load_kube_config_from_dict(
    #     config_dict=kube_config,
    # )
    # utils.create_from_directory(
    #     k8s_client=client.ApiClient(),
    #     yaml_dir=os.path.join(os.getcwd(), "src", "k8s"),
    #     apply=True,
    # )


if __name__ == "__main__":
    deploy()
