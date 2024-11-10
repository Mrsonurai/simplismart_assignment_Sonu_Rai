from src.install_tools import install_tools

def test_install_tools(mocker):
    mock_subprocess = mocker.patch("subprocess.run")
    install_tools()
    # Verify subprocess calls to ensure Helm and KEDA were installed
    assert mock_subprocess.called