import pytest

@pytest.mark.usefixtures("initialize_driver")
class Base:
    pass
