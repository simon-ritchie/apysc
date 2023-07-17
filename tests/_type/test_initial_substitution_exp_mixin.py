import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestClass(InitialSubstitutionExpMixIn, VariableNameMixIn):
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        return "var test_value = true;"


class TestInitialSubstitutionExpMixIn:
    @apply_test_settings()
    def test__append_initial_substitution_expression_if_in_handler_scope(self) -> None:
        instance: _TestClass = _TestClass()
        instance.variable_name = "test_instance"
        ap.Stage()
        instance._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=False,
        )
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected_expression: str = "var test_value = true;"
        assert expected_expression not in expression

        ap.Stage()
        with HandlerScope(handler_name="test_handler", instance=instance):
            instance._append_initial_substitution_expression_if_in_handler_scope(
                skip_appending=False,
            )
        expression = expression_data_util.get_current_event_handler_scope_expression()
        assert expected_expression in expression

        ap.Stage()
        with HandlerScope(handler_name="test_handler", instance=instance):
            instance._append_initial_substitution_expression_if_in_handler_scope(
                skip_appending=True,
            )
        expression = expression_data_util.get_current_event_handler_scope_expression()
        assert expected_expression not in expression
