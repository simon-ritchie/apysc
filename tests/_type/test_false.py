import pytest

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class Test_False:
    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()
        assert ap.False_ == ap.Boolean(False)
        assert "false" in ap.False_.variable_name
        with pytest.raises(TypeError):  # type: ignore
            ap.False_.value = True
