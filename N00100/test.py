from main import solve


def test_1():
    assert solve(1, 10) == 20


def test_2():
    assert solve(100, 200) == 125


def test_3():
    assert solve(201, 210) == 89


def test_4():
    assert solve(900, 1000) == 174
