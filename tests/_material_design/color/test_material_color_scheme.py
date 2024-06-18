from typing import Optional
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
        assert on_secondary.variable_name != (
            ap.Colors.ALOE_VERA_GREEN_98F516.variable_name
        )

    @apply_test_settings()
    def test_error(self) -> None:
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
        error: ap.Color = color_scheme.error
        assert error == ap.Colors.ANTIQUE_BRONZE_665D1E
        assert error.variable_name != ap.Colors.ANTIQUE_BRONZE_665D1E.variable_name

    @apply_test_settings()
    def test_on_error(self) -> None:
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
        on_error: ap.Color = color_scheme.on_error
        assert on_error == ap.Colors.ANTIQUE_WHITE_FAEBD7
        assert on_error.variable_name != ap.Colors.ANTIQUE_WHITE_FAEBD7.variable_name

    @apply_test_settings()
    def test_surface(self) -> None:
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
        surface: ap.Color = color_scheme.surface
        assert surface == ap.Colors.AQUAMARINE_7FFFD4
        assert surface.variable_name != ap.Colors.AQUAMARINE_7FFFD4.variable_name

    @apply_test_settings()
    def test_on_surface(self) -> None:
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
        on_surface: ap.Color = color_scheme.on_surface
        assert on_surface == ap.Colors.AZURE_F0FFFF
        assert on_surface.variable_name != ap.Colors.AZURE_F0FFFF.variable_name

    @apply_test_settings()
    def test_primary_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            primary_container=ap.Colors.ARMY_BROWN_827B60,
        )
        primary_container: Optional[ap.Color] = color_scheme.primary_container
        assert primary_container is not None
        assert primary_container == ap.Colors.ARMY_BROWN_827B60
        assert primary_container.variable_name != (
            ap.Colors.ARMY_BROWN_827B60.variable_name
        )

    @apply_test_settings()
    def test_on_primary_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            on_primary_container=ap.Colors.AQUAMARINE_STONE_348781,
        )
        on_primary_container: Optional[ap.Color] = color_scheme.on_primary_container
        assert on_primary_container is not None
        assert on_primary_container == ap.Colors.AQUAMARINE_STONE_348781
        assert on_primary_container.variable_name != (
            ap.Colors.AQUAMARINE_STONE_348781.variable_name
        )

    @apply_test_settings()
    def test_secondary_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            secondary_container=ap.Colors.BALLOON_BLUE_2B60DE,
        )
        secondary_container: Optional[ap.Color] = color_scheme.secondary_container
        assert secondary_container is not None
        assert secondary_container == ap.Colors.BALLOON_BLUE_2B60DE
        assert secondary_container.variable_name != (
            ap.Colors.BALLOON_BLUE_2B60DE.variable_name
        )

    @apply_test_settings()
    def test_on_secondary_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            on_secondary_container=ap.Colors.BEE_YELLOW_E9AB17,
        )
        on_secondary_container: Optional[ap.Color] = color_scheme.on_secondary_container
        assert on_secondary_container is not None
        assert on_secondary_container == ap.Colors.BEE_YELLOW_E9AB17
        assert on_secondary_container.variable_name != (
            ap.Colors.BEE_YELLOW_E9AB17.variable_name
        )

    @apply_test_settings()
    def test_tertiary(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            tertiary=ap.Colors.BEIGE_F5F5DC,
        )
        tertiary: Optional[ap.Color] = color_scheme.tertiary
        assert tertiary is not None
        assert tertiary == ap.Colors.BEIGE_F5F5DC
        assert tertiary.variable_name != ap.Colors.BEIGE_F5F5DC.variable_name

    @apply_test_settings()
    def test_on_tertiary(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            on_tertiary=ap.Colors.BISQUE_FFE4C4,
        )
        on_tertiary: Optional[ap.Color] = color_scheme.on_tertiary
        assert on_tertiary is not None
        assert on_tertiary == ap.Colors.BISQUE_FFE4C4
        assert on_tertiary.variable_name != ap.Colors.BISQUE_FFE4C4.variable_name

    @apply_test_settings()
    def test_tertiary_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            tertiary_container=ap.Colors.BLACK_BEAN_3D0C02,
        )
        tertiary_container: Optional[ap.Color] = color_scheme.tertiary_container
        assert tertiary_container is not None
        assert tertiary_container == ap.Colors.BLACK_BEAN_3D0C02
        assert tertiary_container.variable_name != (
            ap.Colors.BLACK_BEAN_3D0C02.variable_name
        )

    @apply_test_settings()
    def test_on_tertiary_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            on_tertiary_container=ap.Colors.BLUE_0000FF,
        )
        on_tertiary_container: Optional[ap.Color] = color_scheme.on_tertiary_container
        assert on_tertiary_container is not None
        assert on_tertiary_container == ap.Colors.BLUE_0000FF
        assert on_tertiary_container.variable_name != (
            ap.Colors.BLUE_0000FF.variable_name
        )

    @apply_test_settings()
    def test_error_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            error_container=ap.Colors.BLOOD_NIGHT_551606,
        )
        error_container: Optional[ap.Color] = color_scheme.error_container
        assert error_container is not None
        assert error_container == ap.Colors.BLOOD_NIGHT_551606
        assert error_container.variable_name != (
            ap.Colors.BLOOD_NIGHT_551606.variable_name
        )

    @apply_test_settings()
    def test_on_error_container(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            on_error_container=ap.Colors.BLUE_VIOLET_8A2BE2,
        )
        on_error_container: Optional[ap.Color] = color_scheme.on_error_container
        assert on_error_container is not None
        assert on_error_container == ap.Colors.BLUE_VIOLET_8A2BE2
        assert on_error_container.variable_name != (
            ap.Colors.BLUE_VIOLET_8A2BE2.variable_name
        )

    @apply_test_settings()
    def test_outline(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            outline=ap.Colors.BRIGHT_GRAPE_6F2DA8,
        )
        outline: Optional[ap.Color] = color_scheme.outline
        assert outline is not None
        assert outline == ap.Colors.BRIGHT_GRAPE_6F2DA8
        assert outline.variable_name != ap.Colors.BRIGHT_GRAPE_6F2DA8.variable_name

    @apply_test_settings()
    def test_outline_variant(self) -> None:
        color_scheme = ap.MaterialColorScheme(
            primary=ap.Colors.ACID_GREEN_B0BF1A,
            on_primary=ap.Colors.ALICE_BLUE_F0F8FF,
            secondary=ap.Colors.ALGAE_GREEN_64E986,
            on_secondary=ap.Colors.ALOE_VERA_GREEN_98F516,
            error=ap.Colors.ANTIQUE_BRONZE_665D1E,
            on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
            surface=ap.Colors.AQUAMARINE_7FFFD4,
            on_surface=ap.Colors.AZURE_F0FFFF,
            outline_variant=ap.Colors.CORAL_FF7F50,
        )
        outline_variant: Optional[ap.Color] = color_scheme.outline_variant
        assert outline_variant is not None
        assert outline_variant == ap.Colors.CORAL_FF7F50
        assert outline_variant.variable_name != ap.Colors.CORAL_FF7F50.variable_name
