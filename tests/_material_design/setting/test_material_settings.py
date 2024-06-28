import apysc as ap
from apysc._testing.testing_helper import apply_test_settings, assert_raises


class TestMaterialSettings:
    def teardown_method(self) -> None:
        ap.MaterialSettings._reset_settings()

    @apply_test_settings()
    def test_get_light_color_scheme(self) -> None:
        ap.MaterialSettings._reset_settings()
        assert ap.MaterialSettings.get_light_color_scheme() is None
        color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALGAE_GREEN_64E986,
            secondary=ap.Colors.ALICE_BLUE_F0F8FF,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.AQUAMARINE_7FFFD4,
            surface=ap.Colors.AQUAMARINE_STONE_348781,
            on_surface=ap.Colors.ARMY_GREEN_4B5320,
        )
        ap.MaterialSettings.set_light_color_scheme(color_scheme=color_scheme)
        assert ap.MaterialSettings.get_light_color_scheme() == color_scheme

    @apply_test_settings()
    def test_set_light_color_scheme(self) -> None:
        ap.MaterialSettings._reset_settings()
        color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALGAE_GREEN_64E986,
            secondary=ap.Colors.ALICE_BLUE_F0F8FF,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.AQUAMARINE_7FFFD4,
            surface=ap.Colors.AQUAMARINE_STONE_348781,
            on_surface=ap.Colors.ARMY_GREEN_4B5320,
        )
        ap.MaterialSettings.set_light_color_scheme(color_scheme=color_scheme)
        assert ap.MaterialSettings.get_light_color_scheme() == color_scheme

        assert_raises(
            expected_error_class=ValueError,
            callable_=ap.MaterialSettings.set_light_color_scheme,
            color_scheme=color_scheme,
        )

    @apply_test_settings()
    def test_get_dark_color_scheme(self) -> None:
        ap.MaterialSettings._reset_settings()
        assert ap.MaterialSettings.get_dark_color_scheme() is None
        color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALGAE_GREEN_64E986,
            secondary=ap.Colors.ALICE_BLUE_F0F8FF,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.AQUAMARINE_7FFFD4,
            surface=ap.Colors.AQUAMARINE_STONE_348781,
            on_surface=ap.Colors.ARMY_GREEN_4B5320,
        )
        ap.MaterialSettings.set_dark_color_scheme(color_scheme=color_scheme)
        assert ap.MaterialSettings.get_dark_color_scheme() == color_scheme

    @apply_test_settings()
    def test_set_dark_color_scheme(self) -> None:
        ap.MaterialSettings._reset_settings()
        color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALGAE_GREEN_64E986,
            secondary=ap.Colors.ALICE_BLUE_F0F8FF,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.AQUAMARINE_7FFFD4,
            surface=ap.Colors.AQUAMARINE_STONE_348781,
            on_surface=ap.Colors.ARMY_GREEN_4B5320,
        )
        ap.MaterialSettings.set_dark_color_scheme(color_scheme=color_scheme)
        assert ap.MaterialSettings.get_dark_color_scheme() == color_scheme

        assert_raises(
            expected_error_class=ValueError,
            callable_=ap.MaterialSettings.set_dark_color_scheme,
            color_scheme=color_scheme,
        )

    @apply_test_settings()
    def test__initialize_current_brightness_string_if_not_initialized(self) -> None:
        ap.MaterialSettings._initialize_current_brightness_string_if_not_initialized()
        assert ap.MaterialSettings._current_brightness_string == ap.String(
            ap.MaterialBrightness.LIGHT.value
        )

        ap.MaterialSettings._current_brightness_string = ap.String(
            value=ap.MaterialBrightness.DARK.value
        )
        ap.MaterialSettings._initialize_current_brightness_string_if_not_initialized()
        assert ap.MaterialSettings._current_brightness_string == ap.String(
            ap.MaterialBrightness.DARK.value
        )

    @apply_test_settings()
    def test__delete_current_brightness_string_attr(self) -> None:
        ap.MaterialSettings._initialize_current_brightness_string_if_not_initialized()
        ap.MaterialSettings._delete_current_brightness_string_attr()
        assert not hasattr(ap.MaterialSettings, "_current_brightness_string")

    @apply_test_settings()
    def test_switch_to_light_color_scheme(self) -> None:
        ap.MaterialSettings.switch_to_light_color_scheme()
        assert ap.MaterialSettings._current_brightness_string == ap.String(
            ap.MaterialBrightness.LIGHT.value
        )

    @apply_test_settings()
    def test_switch_to_dark_color_scheme(self) -> None:
        ap.MaterialSettings.switch_to_dark_color_scheme()
        assert ap.MaterialSettings._current_brightness_string == ap.String(
            ap.MaterialBrightness.DARK.value
        )

    @apply_test_settings()
    def test_current_color_scheme_is_light_color_scheme(self) -> None:
        assert ap.MaterialSettings.current_color_scheme_is_light_color_scheme() == (
            ap.True_
        )

        ap.MaterialSettings.switch_to_dark_color_scheme()
        assert ap.MaterialSettings.current_color_scheme_is_light_color_scheme() == (
            ap.False_
        )

        ap.MaterialSettings.switch_to_light_color_scheme()
        assert ap.MaterialSettings.current_color_scheme_is_light_color_scheme() == (
            ap.True_
        )

    @apply_test_settings()
    def test_current_color_scheme_is_dark_color_scheme(self) -> None:
        assert ap.MaterialSettings.current_color_scheme_is_dark_color_scheme() == (
            ap.False_
        )

        ap.MaterialSettings.switch_to_dark_color_scheme()
        assert ap.MaterialSettings.current_color_scheme_is_dark_color_scheme() == (
            ap.True_
        )

        ap.MaterialSettings.switch_to_light_color_scheme()
        assert ap.MaterialSettings.current_color_scheme_is_dark_color_scheme() == (
            ap.False_
        )

    @apply_test_settings()
    def test__reset_settings(self) -> None:
        ap.MaterialSettings.switch_to_dark_color_scheme()
        ap.MaterialSettings.current_color_scheme_is_dark_color_scheme()
        ap.MaterialSettings.current_color_scheme_is_dark_color_scheme()
        ap.MaterialSettings._reset_settings()
        assert not hasattr(ap.MaterialSettings, "_current_brightness_string")
        assert ap.MaterialSettings._light_color_scheme is None
        assert ap.MaterialSettings._dark_color_scheme is None
        assert not hasattr(ap.MaterialSettings, "_light_color_scheme_str")
        assert not hasattr(ap.MaterialSettings, "_dark_color_scheme_str")

    @apply_test_settings()
    def test__initialize_color_scheme_setting_is_enabled_if_not_initialized(
        self
    ) -> None:
        ap.MaterialSettings._reset_settings()
        ap.MaterialSettings._initialize_color_scheme_setting_is_enabled_if_not_initialized()  # noqa
        assert ap.MaterialSettings._color_scheme_setting_is_enabled == ap.Boolean(False)
        ap.MaterialSettings._color_scheme_setting_is_enabled = ap.Boolean(True)
        ap.MaterialSettings._initialize_color_scheme_setting_is_enabled_if_not_initialized()  # noqa
        assert ap.MaterialSettings._color_scheme_setting_is_enabled == ap.Boolean(True)
