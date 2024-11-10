from src.health_status import get_health_status

def test_health_status(mocker):
    mock_subprocess = mocker.patch("subprocess.run")
    get_health_status("my-deployment")
    assert mock_subprocess.called