import subprocess

def install_tools():
    try:
        # Install Helm
        print("Installing Helm...")
        subprocess.run(["curl", "-fsSL", "-o", "/usr/local/bin/helm", "https://get.helm.sh/helm-v3.6.3-linux-amd64.tar.gz"], check=True)
        subprocess.run(["chmod", "+x", "/usr/local/bin/helm"], check=True)
        print("Helm installed successfully.")

        # Add KEDA Helm repository and install KEDA
        print("Adding KEDA Helm repo and installing KEDA...")
        subprocess.run(["helm", "repo", "add", "kedacore", "https://kedacore.github.io/charts"], check=True)
        subprocess.run(["helm", "repo", "update"], check=True)
        subprocess.run(["helm", "install", "keda", "kedacore/keda", "--namespace", "keda", "--create-namespace"], check=True)
        print("KEDA installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

if __name__ == "__main__":
    install_tools()