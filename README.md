# Kubernetes Automation CLI

## Overview
This CLI tool automates tasks on a Kubernetes cluster. It connects to the cluster, installs necessary tools, creates event-driven deployments with KEDA autoscaling, and retrieves health status for deployments.

## Getting Started

### Prerequisites
- `kubectl` configured for cluster access
- Helm installed
- Python 3.7+

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd project-root

## Directory Structure

The following is the directory structure of the project, with descriptions for each folder and file.

| Folder/File               | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `project-root/`            | Root directory of the project                                |
| `├── src/`                 | Source code for the CLI script                               |
| `│   ├── connect_cluster.py` | Connects and configures Kubernetes cluster                   |
| `│   ├── install_tools.py`  | Installs Helm and KEDA                                       |
| `│   ├── create_deployment.py` | Creates deployment and configures scaling                    |
| `│   ├── health_status.py`  | Checks deployment health                                     |
| `│   └── __main__.py`       | Main script entry point for CLI                              |
| `├── scripts/`              | Optional deployment and automation scripts                   |
| `│   └── cd_pipeline.sh`    | Continuous Deployment pipeline setup                         |
| `├── config/`               | Configuration files                                          |
| `│   └── keda-config.yaml`  | KEDA configurations                                           |
| `├── docs/`                 | Documentation for the project                                |
| `│   ├── architecture.png`  | Architecture design diagram                                  |
| `│   └── README.md`         | Main documentation file                                      |
| `├── tests/`                | Unit and integration tests                                   |
| `│   ├── test_connect_cluster.py` | Tests for connection setup                                  |
| `│   ├── test_install_tools.py`  | Tests for tool installation                                  |
| `│   ├── test_create_deployment.py` | Tests for deployment creation                               |
| `│   └── test_health_status.py` | Tests for health status retrieval                            |
| `├── .gitignore`            | Files to ignore in version control                           |
| `└── README.md`             | Project setup and usage guide                                |

### Folder and File Descriptions

- **`src/`**: Contains the main code files for the CLI script.
  - `connect_cluster.py`: Script to connect and configure the Kubernetes cluster.
  - `install_tools.py`: Installs necessary tools such as Helm and KEDA.
  - `create_deployment.py`: Manages deployment creation and scaling configurations.
  - `health_status.py`: Retrieves the health status of a deployment.
  - `__main__.py`: Entry point for the CLI, tying all functionalities together.

- **`scripts/`**: Optional scripts to automate deployment.
  - `cd_pipeline.sh`: A script for setting up a Continuous Deployment pipeline.

- **`config/`**: Contains configuration files used by the project.
  - `scaledobject.yaml`: Defines KEDA scaling configurations for event-driven autoscaling.
  - `deployment.yaml`: Defines KEDA deploying configurations for event-driven autoscaling.

- **`docs/`**: Documentation for the project.
  - `architecture.png`: Visual diagram illustrating the system architecture.
  - `README.md`: Contains an overview, instructions, and additional information about the project.

- **`tests/`**: Holds unit and integration test files to validate functionalities.
  - `test_connect_cluster.py`: Tests for cluster connection functionality.
  - `test_install_tools.py`: Tests for tool installation processes.
  - `test_create_deployment.py`: Tests deployment creation functionality.
  - `test_health_status.py`: Tests for health status retrieval.

- **`.gitignore`**: Specifies files and directories to be excluded from version control.

- **`README.md`**: The primary README for project setup and usage instructions.

### Commands to intall in local 
`
pip install -r requirements.txt
`

`
	1.	Connect to the Cluster
    python src/connect_cluster.py
    2.	Install Helm and KEDA
    python src/install_tools.py
    3.	Create a Deployment
    python src/create_deployment.py --image nginx:latest --cpu 100m --memory 256Mi --port 80 --metric cpu
    4.	Check Health Status
    python src/health_status.py --deployment-id my-deployment
`
