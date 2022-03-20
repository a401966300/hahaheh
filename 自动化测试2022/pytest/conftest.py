import pytest

@pytest.fixture(scope='session')
def handle():
    print('open browser')
