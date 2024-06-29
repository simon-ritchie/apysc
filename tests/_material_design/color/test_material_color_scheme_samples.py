import apysc as ap
from apysc._testing.testing_helper import apply_test_settings



class TestMaterialColorSchemeSamples:
    @apply_test_settings()
    def test_create_dark_color_schema_sample_brown_1(self) -> None:
        color_scheme: ap.MaterialColorScheme = (
            ap.MaterialColorSchemeSamples.create_light_color_schema_sample_brown_1()
        )
        assert color_scheme.primary == ap.Color("#8F4C38")
        assert color_scheme.on_primary == ap.Color("#FFFFFF")
        assert color_scheme.secondary == ap.Color("#77574E")
        assert color_scheme.on_secondary == ap.Color("#FFFFFF")
        assert color_scheme.error == ap.Color("#BA1A1A")
        assert color_scheme.on_error == ap.Color("#FFFFFF")
        assert color_scheme.surface == ap.Color("#FFF8F6")
        assert color_scheme.on_surface == ap.Color("#231917")
        assert color_scheme.primary_container == ap.Color("#FFDBD1")
        assert color_scheme.on_primary_container == ap.Color("#3A0B01")
        assert color_scheme.secondary_container == ap.Color("#FFDBD1")
        assert color_scheme.on_secondary_container == ap.Color("#2C150F")
        assert color_scheme.tertiary == ap.Color("#6C5D2F")
        assert color_scheme.on_tertiary == ap.Color("#FFFFFF")
        assert color_scheme.tertiary_container == ap.Color("#F5E1A7")
        assert color_scheme.on_tertiary_container == ap.Color("#231B00")
        assert color_scheme.error_container == ap.Color("#FFDAD6")
        assert color_scheme.on_error_container == ap.Color("#410002")
        assert color_scheme.outline == ap.Color("#85736E")
        assert color_scheme.outline_variant == ap.Color("#D8C2BC")
