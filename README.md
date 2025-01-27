# platform-technical-test

## Overview

This repo is part of a platform technical test. The intent is for read access to be granted to candidates, who should then fork it and complete the tasks below.

## Setup

1. Install Python >= 3.11 (check an existing installation with `python --version`) following the [vendor instructions](https://www.python.org/downloads/).
1. Install Poetry following the [vendor instructions](https://python-poetry.org/docs/#installation).
1. Install Terraform following the [vendor instructions](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform).
1. Install `kubeconform` following the [vendor instructions](https://github.com/yannh/kubeconform?tab=readme-ov-file#installation).
1. Run `poetry sync` to install Python dependencies.
1. Run `poetry run python scripts/test.py` to test your configuration.

## Tasks

For each task, there's a basic requirement and in some cases an additional advanced requirement. The advanced requirements are optional. Best approach is to complete the basic requirements and then circle back to the advanced if you want to.

| # | Title | Description |
|---|---|---|
| 1 | Resource Group | Using Terraform resources, configure an `Azure Resource Group`.<br><br>**Advanced:** (none) |
| 2 | Storage Account | Using Terraform resources, configure an `Azure Storage Account`. It should be for general purpose use, and provide redundancy across availability zones.<br><br>**Advanced:** Configure networking settings on the Storage Account to remove public access, except for Azure services on the [trusted services list](https://learn.microsoft.com/en-gb/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-to-trusted-azure-services). |
| 3 | Kubernetes Service | Using Terraform resources, configure an `Azure Kubernetes Service` cluster. It should have a single node of SKU `Standard_B4ms` and have Azure Policy enabled.<br><br>**Advanced:** Configure Diagnostic Logging to archive `Kubernetes Scheduler` logs to the Storage Account created in step 2. |
| 4 | Kubernetes Application | Using Kubernetes resources, configure a `Deployment` that runs a single replica of [hashicorp/http-echo](https://hub.docker.com/r/hashicorp/http-echo). It should be configured to respond to an HTTP request with `Hello, [your name]`. Configure a `Service` to expose the deployment to the cluster only.<br><br>**Advanced:** Re-configure the `Service` to expose the application to the internet using a public IP. Add configuration to enable a DNS label to be mapped to the public IP (hint: search for `service.beta.kubernetes.io/azure-dns-label-name`). |
| 5 | CI/CD | Using GitHub Actions, configure a workflow that will run the steps listed in [#setup](#setup) in automation.<br><br>**Advanced:** Re-configure the workflow to additionally then deploy your code. It should do this by logging into Azure using GitHub secrets (hint: search for `azure/login@v2`) and then running `poetry run python scripts/deploy.py`. |
