import subprocess

def get_health_status(deployment_id):
    try:
        # Check deployment status
        print(f"Fetching status for deployment {deployment_id}...")
        subprocess.run(["kubectl", "get", "deployment", deployment_id, "-n", "event-driven"], check=True)
        
        # Fetch Pod CPU and memory usage metrics
        print("Fetching resource usage...")
        subprocess.run(["kubectl", "top", "pods", "-n", "event-driven"], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error fetching health status: {e}")

if __name__ == "__main__":
    get_health_status("my-deployment")