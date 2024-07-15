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
        target_color = (
            ap.MaterialSettingsUtils._get_target_color_and_add_expressions_by_color_name(  # noqa
                color_name="primary",
                argument_color=target_color,
            )
        )
        assert target_color == ap.Colors.RED_DIRT_7F5217

        target_color = (
            ap.MaterialSettingsUtils._get_target_color_and_add_expressions_by_color_name(  # noqa
                color_name="primary",
                argument_color=None,
            )
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
