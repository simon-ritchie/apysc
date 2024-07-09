import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsUtils:

    @apply_test_settings()
    def test__initialize_fixed_color_scheme_if_not_initialized(self) -> None:
        if hasattr(ap.MaterialSettingsUtils, "_fixed_color_scheme"):
            del ap.MaterialSettingsUtils._fixed_color_scheme

        ap.MaterialSettingsUtils._initialize_fixed_color_scheme_if_not_initialized()
        assert isinstance(
            ap.MaterialSettingsUtils._fixed_color_scheme, ap.MaterialColorScheme
        )
