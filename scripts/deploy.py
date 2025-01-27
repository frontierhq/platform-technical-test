import os
from helpers.apply_terraform import apply_terraform
from helpers.init_terraform import init_terraform


def deploy():
    terraform = init_terraform(
        working_dir=os.path.join(os.getcwd(), "src", "terraform")
    )

    apply_terraform(
        terraform=terraform,
        # var={},
        # var_file=os.path.join(os.getcwd(), "config", "main.tfvars"),
    )


if __name__ == "__main__":
    deploy()
