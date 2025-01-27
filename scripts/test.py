import os
from helpers.test_k8s import test_k8s
from helpers.test_terraform import test_terraform


if __name__ == "__main__":
    test_k8s(os.path.join(os.getcwd(), "src", "k8s"))
    test_terraform(os.path.join(os.getcwd(), "src", "terraform"))
