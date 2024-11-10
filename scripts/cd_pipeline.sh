#!/bin/bash
set -e

# Environment variables
CLUSTER_NAME="my-cluster"
NAMESPACE="event-driven"

# Step 1: Connect to the Kubernetes cluster (assumes configured kubectl)
echo "Connecting to Kubernetes cluster..."
kubectl cluster-info

# Step 2: Deploy the application
echo "Deploying application..."
kubectl apply -f ../configs/deployment.yaml -n $NAMESPACE

# Step 3: Deploy KEDA scaling configuration
echo "Applying KEDA scaling configuration..."
kubectl apply -f ../configs/scaledobject.yaml -n $NAMESPACE

# Step 4: Verify Deployment
echo "Verifying deployment..."
kubectl rollout status deployment/my-deployment -n $NAMESPACE

echo "Deployment and autoscaling configured successfully."