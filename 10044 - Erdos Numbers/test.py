from main import solve

def test_success():
    assert solve() == 'hello world'

def test_fail():
    assert solve() == 'hello kevin'
