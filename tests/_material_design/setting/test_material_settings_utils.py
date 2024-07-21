import apysc as ap
from apysc._expression import expression_data_util
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

    @apply_test_settings()
    def test__set_color_scheme_value_and_append_expression(self) -> None:
        target_color: ap.Color = ap.Colors.RED_DIRT_7F5217.copy()
        ap.MaterialSettingsUtils._set_color_scheme_value_and_append_expression(
            color_scheme=None,
            color_name="primary",
            target_color=target_color,
        )
        assert target_color == ap.Colors.RED_DIRT_7F5217

        color_scheme: ap.MaterialColorScheme = (
            ap.MaterialColorSchemeSamples.create_dark_color_scheme_sample_brown_1()
        )
        ap.MaterialSettingsUtils._set_color_scheme_value_and_append_expression(
            color_scheme=color_scheme,
            color_name="primary",
            target_color=target_color,
        )
        assert target_color == color_scheme.primary
        expression: str = expression_data_util.get_current_expression()
        assert f"{target_color.variable_name} = " in expression

    @apply_test_settings()
    def test__get_target_color_and_add_expressions_by_color_name(self) -> None:
        target_color: ap.Color = ap.Colors.RED_DIRT_7F5217.copy()
        target_color = ap.MaterialSettingsUtils._get_target_color_and_add_expressions_by_color_name(  # noqa
            color_name="primary",
            argument_color=target_color,
        )
        assert target_color == ap.Colors.RED_DIRT_7F5217

        target_color = ap.MaterialSettingsUtils._get_target_color_and_add_expressions_by_color_name(  # noqa
            color_name="primary",
            argument_color=None,
        )
        assert isinstance(target_color, ap.Color)
        expression: str = expression_data_util.get_current_expression()
        assert expression.count("if (") == 3
        assert expression.count("else if (") == 1
        assert expression.count("else") == 2

    @apply_test_settings()
    def test_get_primary_color(self) -> None:
        target_color: ap.Color = ap.MaterialSettingsUtils.get_primary_color(
            argument_color=None
        )
        assert target_color == ap.MaterialSettingsUtils._fixed_color_scheme.primary

    @apply_test_settings()
    def test_get_on_primary_color(self) -> None:
        target_color: ap.Color = ap.MaterialSettingsUtils.get_on_primary_color(
            argument_color=None
        )
        assert target_color == ap.MaterialSettingsUtils._fixed_color_scheme.on_primary

    @apply_test_settings()
    def test_get_secondary_color(self) -> None:
        target_color: ap.Color = ap.MaterialSettingsUtils.get_secondary_color(
            argument_color=None
        )
        assert target_color == ap.MaterialSettingsUtils._fixed_color_scheme.secondary

    @apply_test_settings()
    def test_get_on_secondary_color(self) -> None:
        target_color: ap.Color = ap.MaterialSettingsUtils.get_on_secondary_color(
            argument_color=None
        )
        assert target_color == ap.MaterialSettingsUtils._fixed_color_scheme.on_secondary

    @apply_test_settings()
    def test_get_error_color(self) -> None:
        target_color: ap.Color = ap.MaterialSettingsUtils.get_error_color(
            argument_color=None
        )
        assert target_color == ap.MaterialSettingsUtils._fixed_color_scheme.error

    @apply_test_settings()
    def test_get_on_error_color(self) -> None:
        target_color: ap.Color = ap.MaterialSettingsUtils.get_on_error_color(
            argument_color=None
        )
        assert target_color == ap.MaterialSettingsUtils._fixed_color_scheme.on_error

    @apply_test_settings()
    def test_get_surface(self) -> None:
        surface: ap.Color = ap.MaterialSettingsUtils.get_surface(argument_color=None)
        assert surface == ap.MaterialSettingsUtils._fixed_color_scheme.surface

    @apply_test_settings()
    def test_on_surface_color(self) -> None:
        on_surface: ap.Color = ap.MaterialSettingsUtils.on_surface_color(
            argument_color=None
        )
        assert on_surface == ap.MaterialSettingsUtils._fixed_color_scheme.on_surface

    @apply_test_settings()
    def test_get_primary_container_color(self) -> None:
        primary_container: ap.Color = (
            ap.MaterialSettingsUtils.get_primary_container_color(argument_color=None)
        )
        assert primary_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.primary_container
        )

    @apply_test_settings()
    def test_get_on_primary_container_color(self) -> None:
        on_primary_container: ap.Color = (
            ap.MaterialSettingsUtils.get_on_primary_container_color(argument_color=None)
        )
        assert on_primary_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.on_primary_container
        )

    @apply_test_settings()
    def test_get_secondary_container_color(self) -> None:
        secondary_container: ap.Color = (
            ap.MaterialSettingsUtils.get_secondary_container_color(argument_color=None)
        )
        assert secondary_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.secondary_container
        )

    @apply_test_settings()
    def test_get_on_secondary_container_color(self) -> None:
        on_secondary_container: ap.Color = (
            ap.MaterialSettingsUtils.get_on_secondary_container_color(
                argument_color=None
            )
        )
        assert on_secondary_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.on_secondary_container
        )

    @apply_test_settings()
    def test_get_tertiary_color(self) -> None:
        tertiary: ap.Color = ap.MaterialSettingsUtils.get_tertiary_color(
            argument_color=None
        )
        assert tertiary == ap.MaterialSettingsUtils._fixed_color_scheme.tertiary

    @apply_test_settings()
    def test_get_on_tertiary_color(self) -> None:
        on_tertiary: ap.Color = ap.MaterialSettingsUtils.get_on_tertiary_color(
            argument_color=None
        )
        assert on_tertiary == ap.MaterialSettingsUtils._fixed_color_scheme.on_tertiary

    @apply_test_settings()
    def test_get_tertiary_container_color(self) -> None:
        tertiary_container: ap.Color = (
            ap.MaterialSettingsUtils.get_tertiary_container_color(argument_color=None)
        )
        assert tertiary_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.tertiary_container
        )

    @apply_test_settings()
    def test_get_on_tertiary_container_color(self) -> None:
        on_tertiary_container: ap.Color = (
            ap.MaterialSettingsUtils.get_on_tertiary_container_color(
                argument_color=None
            )
        )
        assert on_tertiary_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.on_tertiary_container
        )

    @apply_test_settings()
    def test_get_error_container_color(self) -> None:
        error_container: ap.Color = ap.MaterialSettingsUtils.get_error_container_color(
            argument_color=None
        )
        assert error_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.error_container
        )

    @apply_test_settings()
    def test_get_on_error_container_color(self) -> None:
        on_error_container: ap.Color = (
            ap.MaterialSettingsUtils.get_on_error_container_color(argument_color=None)
        )
        assert on_error_container == (
            ap.MaterialSettingsUtils._fixed_color_scheme.on_error_container
        )

    @apply_test_settings()
    def test_get_outline_color(self) -> None:
        outline: ap.Color = ap.MaterialSettingsUtils.get_outline_color(
            argument_color=None
        )
        assert outline == ap.MaterialSettingsUtils._fixed_color_scheme.outline

    @apply_test_settings()
    def test_get_outline_variant_color(self) -> None:
        outline_variant: ap.Color = ap.MaterialSettingsUtils.get_outline_variant_color(
            argument_color=None
        )
        assert outline_variant == (
            ap.MaterialSettingsUtils._fixed_color_scheme.outline_variant
        )

    @apply_test_settings()
    def test__initialize_fixed_font_family_if_not_initialized(self) -> None:
        if hasattr(ap.MaterialSettingsUtils, "_fixed_font_family"):
            del ap.MaterialSettingsUtils._fixed_font_family
        ap.MaterialSettingsUtils._initialize_fixed_font_family_if_not_initialized()
        assert isinstance(ap.MaterialSettingsUtils._fixed_font_family, ap.Array)
        assert len(ap.MaterialSettingsUtils._fixed_font_family._value) > 0

        ap.MaterialSettingsUtils._initialize_fixed_font_family_if_not_initialized()
        assert isinstance(ap.MaterialSettingsUtils._fixed_font_family, ap.Array)

        if hasattr(ap.MaterialSettingsUtils, "_fixed_font_family"):
            del ap.MaterialSettingsUtils._fixed_font_family

    @apply_test_settings()
    def test_get_font_family(self) -> None:
        ap.MaterialSettings._reset_settings()
        font_family_1: ap.Array[ap.String] = ap.Array([ap.String("Arial")])
        font_family_2: ap.Array[ap.String] = ap.Array([ap.String("Times New Roman")])
        ap.MaterialSettings.set_font_family(font_family=font_family_2)

        target_font_family: ap.Array[ap.String] = (
            ap.MaterialSettingsUtils.get_font_family(argument_font_family=font_family_1)
        )
        assert target_font_family == font_family_1

        target_font_family = ap.MaterialSettingsUtils.get_font_family(
            argument_font_family=None
        )
        assert target_font_family == font_family_2

        ap.MaterialSettings._reset_settings()
        target_font_family = ap.MaterialSettingsUtils.get_font_family(
            argument_font_family=None
        )
        assert target_font_family == ap.MaterialSettingsUtils._fixed_font_family
