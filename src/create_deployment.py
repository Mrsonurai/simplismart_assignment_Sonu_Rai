import subprocess

def create_deployment(image, cpu, memory, port, metric):
    try:
        # Create a namespace for the deployment
        print("Creating namespace 'event-driven'...")
        subprocess.run(["kubectl", "create", "namespace", "event-driven"], check=True)

        # Create deployment YAML file
        deployment_yaml = f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
  namespace: event-driven
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: {image}
        ports:
        - containerPort: {port}
        resources:
          requests:
            cpu: {cpu}
            memory: {memory}
          limits:
            cpu: {cpu}
            memory: {memory}
---
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: event-driven
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: {port}
      targetPort: {port}
  type: LoadBalancer
"""
        with open("/tmp/deployment.yaml", "w") as file:
            file.write(deployment_yaml)

        # Apply deployment
        print("Deploying application...")
        subprocess.run(["kubectl", "apply", "-f", "/tmp/deployment.yaml"], check=True)

        # Configure KEDA autoscaler
        print("Configuring KEDA autoscaler...")
        autoscaler_yaml = f"""
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: my-scaledobject
  namespace: event-driven
spec:
  scaleTargetRef:
    name: my-deployment
  triggers:
    - type: {metric}
      metadata:
        # Add specific metric configuration here
"""
        with open("/tmp/scaledobject.yaml", "w") as file:
            file.write(autoscaler_yaml)
        
        # Apply the KEDA autoscaler
        subprocess.run(["kubectl", "apply", "-f", "/tmp/scaledobject.yaml"], check=True)
        print("Deployment and autoscaling configuration completed.")

    except subprocess.CalledProcessError as e:
        print(f"Error in deployment creation: {e}")

if __name__ == "__main__":
    # Example usage
    create_deployment("nginx:latest", "100m", "256Mi", 80, "cpu")