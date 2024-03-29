import apysc as ap
from apysc._display.cy_mixin import CyMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestAnimationCy:
    @apply_test_settings()
    def test___init__(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_cy"
        animation_cy: ap.AnimationCy = ap.AnimationCy(
            target=target,
            y=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_cy.variable_name.startswith(f"{var_names.ANIMATION_CY}_")
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_cy": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cy,
        )

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_cy"
        animation_cy: ap.AnimationCy = ap.AnimationCy(target=target, y=100)
        expression: str = animation_cy._get_animation_func_expression()
        assert expression == f"\n  .cy({animation_cy._cy.variable_name});"

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: CyMixIn = CyMixIn()
        target.variable_name = "test_animation_cy"
        animation_cy: ap.AnimationCy = ap.AnimationCy(target=target, y=100)
        expression: str = animation_cy._get_complete_event_in_handler_head_expression()
        expected: str = (
            f"{target._y.variable_name} = " f"{animation_cy._cy.variable_name};"
        )
        assert expression == expected
