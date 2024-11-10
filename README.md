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

### Directory Architecture
`
project-root/
├── src/                                # Source code for the CLI script
│   ├── connect_cluster.py              # Connects and configures Kubernetes cluster
│   ├── install_tools.py                # Installs Helm and KEDA
│   ├── create_deployment.py            # Creates deployment and configures scaling
│   ├── health_status.py                # Checks deployment health
│   └── __main__.py                     # Main script entry point for CLI
├── scripts/                            # Optional deployment and automation scripts
│   └── cd_pipeline.sh                  # Continuous Deployment pipeline setup
├── config/                             # Configuration files
│   └── keda-config.yaml                # KEDA configurations
├── docs/                               # Documentation
│   ├── architecture.png                # Architecture design diagram
│   └── README.md                       # Main documentation file
├── tests/                              # Unit and integration tests
│   ├── test_connect_cluster.py         # Tests for connection setup
│   ├── test_install_tools.py           # Tests for tool installation
│   ├── test_create_deployment.py       # Tests for deployment creation
│   └── test_health_status.py           # Tests for health checks
├── .gitignore                          # Files to ignore in version control
└── README.md                           # Project setup and usage guide
`

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
