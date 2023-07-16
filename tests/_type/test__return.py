import apysc as ap
from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestReturn:
    @apply_test_settings()
    def test__validate_current_scope_is_event_handler(self) -> None:
        ap.Stage()
        instance: VariableNameMixIn = VariableNameMixIn()
        instance.variable_name = "test_instance"
        assert_raises(
            expected_error_class=Exception,
            callable_=ap.Return,
            match=(
                "The `Return` class can be instantiated only in an event "
                "handler scope."
            ),
        )

        with event_handler_scope.HandlerScope(
            handler_name="test_handler_1", instance=instance
        ):
            _: ap.Return = ap.Return()

    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()
        instance: VariableNameMixIn = VariableNameMixIn()
        instance.variable_name = "test_instance"
        with event_handler_scope.HandlerScope(
            handler_name="test_handler_1", instance=instance
        ):
            _: ap.Return = ap.Return()
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        assert "return;" in expression
