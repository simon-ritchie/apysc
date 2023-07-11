import pytest

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class Test_True:
    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()
        assert ap.True_ == ap.Boolean(True)
        assert "true" in ap.True_.variable_name
        with pytest.raises(TypeError):  # type: ignore
            ap.True_.value = False
