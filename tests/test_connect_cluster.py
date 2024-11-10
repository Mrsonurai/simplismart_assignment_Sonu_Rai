from src.connect_cluster import connect_to_cluster

def test_connect_to_cluster():
    # You could use mocks for subprocess calls in actual tests
    assert connect_to_cluster() is None