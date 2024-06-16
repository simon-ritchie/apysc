import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialColorScheme:
    @apply_test_settings()
    def test___init__(self) -> None:
        color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            primary_container=ap.Colors.ARMY_BROWN_827B60,
            on_primary_container=ap.Colors.AQUAMARINE_STONE_348781,
            secondary_container=ap.Colors.BALLOON_BLUE_2B60DE,
            on_secondary_container=ap.Colors.BEE_YELLOW_E9AB17,
            tertiary=ap.Colors.BEIGE_F5F5DC,
            on_tertiary=ap.Colors.BISQUE_FFE4C4,
            tertiary_container=ap.Colors.BLACK_BEAN_3D0C02,
            on_tertiary_container=ap.Colors.BLUE_0000FF,
            error_container=ap.Colors.BLOOD_NIGHT_551606,
            on_error_container=ap.Colors.BLUE_VIOLET_8A2BE2,
            outline=ap.Colors.BRIGHT_GRAPE_6F2DA8,
            outline_variant=ap.Colors.CORAL_FF7F50,
        )
        assert color_scheme._primary == ap.Colors.ACID_GREEN_B0BF1A
        assert color_scheme._on_primary == ap.Colors.ALICE_BLUE_F0F8FF
        assert color_scheme._secondary == ap.Colors.ALGAE_GREEN_64E986
        assert color_scheme._on_secondary == ap.Colors.ALOE_VERA_GREEN_98F516
        assert color_scheme._error == ap.Colors.ANTIQUE_BRONZE_665D1E
        assert color_scheme._on_error == ap.Colors.ANTIQUE_WHITE_FAEBD7
        assert color_scheme._surface == ap.Colors.AQUAMARINE_7FFFD4
        assert color_scheme._on_surface == ap.Colors.AZURE_F0FFFF
        assert color_scheme._primary_container == ap.Colors.ARMY_BROWN_827B60
        assert color_scheme._on_primary_container == ap.Colors.AQUAMARINE_STONE_348781
        assert color_scheme._secondary_container == ap.Colors.BALLOON_BLUE_2B60DE
        assert color_scheme._on_secondary_container == ap.Colors.BEE_YELLOW_E9AB17
        assert color_scheme._tertiary == ap.Colors.BEIGE_F5F5DC
        assert color_scheme._on_tertiary == ap.Colors.BISQUE_FFE4C4
        assert color_scheme._tertiary_container == ap.Colors.BLACK_BEAN_3D0C02
        assert color_scheme._on_tertiary_container == ap.Colors.BLUE_0000FF
        assert color_scheme._error_container == ap.Colors.BLOOD_NIGHT_551606
        assert color_scheme._on_error_container == ap.Colors.BLUE_VIOLET_8A2BE2
        assert color_scheme._outline == ap.Colors.BRIGHT_GRAPE_6F2DA8
        assert color_scheme._outline_variant == ap.Colors.CORAL_FF7F50

        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
        )
        assert color_scheme._primary_container is None
        assert color_scheme._on_primary_container is None
        assert color_scheme._secondary_container is None
        assert color_scheme._on_secondary_container is None
        assert color_scheme._tertiary is None
        assert color_scheme._on_tertiary is None
        assert color_scheme._tertiary_container is None
        assert color_scheme._on_tertiary_container is None
        assert color_scheme._error_container is None
        assert color_scheme._on_error_container is None
        assert color_scheme._outline is None
        assert color_scheme._outline_variant is None


    @apply_test_settings()
    def test_primary(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
        )
        primary: ap.Color = color_scheme.primary
        assert primary == ap.Colors.ACID_GREEN_B0BF1A
        assert primary.variable_name != ap.Colors.ACID_GREEN_B0BF1A.variable_name

    @apply_test_settings()
    def test_on_primary(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
        )
        on_primary: ap.Color = color_scheme.on_primary
        assert on_primary == ap.Colors.ALICE_BLUE_F0F8FF
        assert on_primary.variable_name != ap.Colors.ALICE_BLUE_F0F8FF.variable_name

    @apply_test_settings()
    def test_secondary(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
        )
        secondary: ap.Color = color_scheme.secondary
        assert secondary == ap.Colors.ALGAE_GREEN_64E986
        assert secondary.variable_name != ap.Colors.ALGAE_GREEN_64E986.variable_name

    @apply_test_settings()
    def test_on_secondary(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
        )
        on_secondary: ap.Color = color_scheme.on_secondary
        assert on_secondary == ap.Colors.ALOE_VERA_GREEN_98F516
        assert on_secondary.variable_name != ap.Colors.ALOE_VERA_GREEN_98F516.variable_name
