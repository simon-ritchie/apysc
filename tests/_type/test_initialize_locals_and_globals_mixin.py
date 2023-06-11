import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.initialize_locals_and_globals_mixin import (
    InitializeLocalsAndGlobalsMixIn,
)


class TestInitializeLocalsAndGlobalsMixIn:
    @apply_test_settings()
    def test__initialize_locals_and_globals(self) -> None:
        mixin: InitializeLocalsAndGlobalsMixIn = InitializeLocalsAndGlobalsMixIn()
        mixin._initialize_locals_and_globals(
            locals_=None,
            globals_=None,
        )
        assert mixin._locals == {}
        assert mixin._globals == {}

        mixin._initialize_locals_and_globals(
            locals_={"a": ap.Int(10)},
            globals_={"b": ap.String("test")},
        )
        assert mixin._locals == {"a": ap.Int(10)}
        assert mixin._globals == {"b": ap.String("test")}
