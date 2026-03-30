import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (2,3,5),
    (5,5,10)
])
def test_add(a,b,expected):
    assert a + b == expected

@pytest.mark.xfail
@pytest.mark.parametrize("a,b,expected", [
    (1,2,-3),
    (2,3,6),
    (5,5,1)
])
def test_add_fail_scenarios(a,b,expected):
    assert a + b == expected

def test_divide():
    with pytest.raises(ZeroDivisionError):
        10 / 0

@pytest.fixture(autouse=True)
def setup_env():
    print("runs before every test")