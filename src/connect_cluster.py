import subprocess

def connect_to_cluster():
    try:
        # Check if kubectl is connected to the cluster
        print("Verifying Kubernetes cluster connection...")
        subprocess.run(["kubectl", "cluster-info"], check=True)
        print("Successfully connected to Kubernetes cluster.")
    except subprocess.CalledProcessError:
        print("Failed to connect to Kubernetes cluster. Please check your kubectl configuration.")

if __name__ == "__main__":
    connect_to_cluster()