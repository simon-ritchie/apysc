import apysc as ap
from apysc._testing import testing_helper
from apysc._type.initialize_top_level_constants_mixin import (
    InitializeTopLevelConstantsMixIn
)
from apysc._testing.testing_helper import apply_test_settings


class TestInitializeTopLevelConstantsMixIn:
    @apply_test_settings()
    def test__initialize_top_level_constants(self) -> None:
        mixin: InitializeTopLevelConstantsMixIn = (
            InitializeTopLevelConstantsMixIn()
        )
        mixin._initialize_top_level_constants()
        assert ap.True_ == ap.Boolean(True)
        assert ap.False_ == ap.Boolean(False)
