# Documentation for Kubernetes Automation CLI

## Project Overview

This project provides a CLI tool for automating deployments on a Kubernetes cluster, enabling event-driven scaling with KEDA.

## Architecture

Refer to the architecture diagram (`architecture.png`) for a visual representation of the deployment process, KEDA configuration, and autoscaling setup.

## Detailed Documentation

### 1. Cluster Connection and Tool Installation
- The CLI connects to the Kubernetes cluster using `kubectl`, ensuring that the cluster configuration is valid.
- Helm and KEDA are installed to enable package management and event-driven autoscaling.

### 2. Deployment and Autoscaling Configuration
- Deployment resources are created, including CPU and memory configurations, ports, and environment variables.
- A `Service` is set up to expose the deployment.
- KEDA is configured to autoscale the deployment based on specified metrics.

### 3. Health Status Monitoring
- The CLI retrieves deployment status and resource metrics (CPU, memory) to ensure the application's health and performance.

Refer to the main `README.md` in the root directory for full setup and usage instructions.

## Architecture Diagram
`
└── Kubernetes Cluster
    ├── event-driven Namespace
    │   ├── Deployment
    │   │   ├── Container
    │   │   │   ├── Image: Public Docker image (e.g., nginx:latest)
    │   │   │   ├── Resources
    │   │   │   │   ├── CPU request and limit
    │   │   │   │   └── Memory request and limit
    │   │   │   └── Port: Exposed for external access (e.g., 80)
    │   │   └── Environment Variables
    │   ├── Service
    │   │   ├── Type: LoadBalancer (exposes deployment externally)
    │   │   └── Port Mappings: Maps external requests to container port
    │   ├── Horizontal Pod Autoscaler (HPA)
    │   │   ├── Metrics Target: Configured to scale based on CPU or custom metrics
    │   │   └── Min/Max Replicas: Adjusts the number of pods as per load
    │   └── KEDA ScaledObject
    │       ├── Trigger Type: Event-driven (e.g., CPU, memory, or external source like Kafka)
    │       └── Target: Links to the Deployment to trigger scaling
    └── Cluster Components
        ├── Helm
        │   ├── Purpose: Manages Kubernetes packages and installations
        │   └── Setup: Installs KEDA and other tools
        └── kubectl CLI
            ├── Purpose: Manages cluster interaction and configurations
            └── Uses: Connects CLI scripts to Kubernetes cluster
`
