import os
from helpers.destroy_terraform import destroy_terraform
from helpers.init_terraform import init_terraform


def destroy():
    terraform = init_terraform(
        working_dir=os.path.join(os.getcwd(), "src", "terraform")
    )

    destroy_terraform(
        terraform=terraform,
        # var={}, # Uncomment to pass variables to terraform
        # var_file=os.path.join(os.getcwd(), "config", "main.tfvars"), # Uncomment to pass variables file to terraform
    )


if __name__ == "__main__":
    destroy()
