from helpers.exec import exec


def test_k8s(working_dir: str):
    print(f"testing kubernetes resources in '{working_dir}'")
    exec("kubeconform", "-strict", "-summary", working_dir)


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
