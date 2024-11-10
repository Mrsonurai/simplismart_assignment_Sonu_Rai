from src.create_deployment import create_deployment

def test_create_deployment(mocker):
    mock_subprocess = mocker.patch("subprocess.run")
    create_deployment("nginx:latest", "100m", "256Mi", 80, "cpu")
    assert mock_subprocess.called
    # Further assertions can be made for each step of the deployment process