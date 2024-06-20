import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettings:
    def teardown_method(self) -> None:
        ap.MaterialSettings.set_light_color_scheme(color_scheme=None)

    @apply_test_settings()
    def test_get_light_color_scheme(self) -> None:
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
        ap.MaterialSettings.set_light_color_scheme(color_scheme=None)

    @apply_test_settings()
    def test_set_light_color_scheme(self) -> None:
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
        ap.MaterialSettings.set_light_color_scheme(color_scheme=None)
