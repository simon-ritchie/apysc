from typing import Any
from typing import Dict

import apysc as ap
from apysc._event import handler
from apysc._event.handler import HandlerData
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestClass1(VariableNameMixIn):
    def __init__(self) -> None:
        """
        Test class for handler's tests.
        """
        self.variable_name = "test_class_1"

    def on_click_1(self, e: ap.Event, options: Dict[str, Any]) -> None:
        """
        Test handler.

        Parameters
        ----------
        e : Event
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_click_2(self, e: ap.Event, options: Dict[str, Any]) -> None:
        """
        Test handler.

        Parameters
        ----------
        e : Event
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """
        int_1: ap.Int = options["int_1"]
        int_1.value = 20


@apply_test_settings()
def test_get_handler_name() -> None:
    test_instance: _TestClass1 = _TestClass1()
    handler_name: str = handler.get_handler_name(
        handler=test_instance.on_click_1, instance=test_instance
    )
    assert "tests__event_test_handler" in handler_name
    assert "_TestClass1_" in handler_name
    assert "on_click_1_" in handler_name
    assert handler_name.endswith(f"_{test_instance.variable_name}")


@apply_test_settings()
def test_append_handler_expression() -> None:
    ap.Stage()
    test_instance: _TestClass1 = _TestClass1()
    int_1: ap.Int = ap.Int(10)
    handler_data: HandlerData[ap.Event] = HandlerData(
        handler=test_instance.on_click_2,
        options={"int_1": int_1},
    )
    handler_name: str = handler.get_handler_name(
        handler=handler_data.handler, instance=test_instance
    )
    e: ap.Event = ap.Event(this=test_instance)
    handler.append_handler_expression(
        handler_data=handler_data, handler_name=handler_name, e=e
    )
    expression: str = expression_data_util.get_current_event_handler_scope_expression()
    expected: str = (
        f"function {handler_name}({e.variable_name}) {{"
        f"\n  {int_1.variable_name} = 20;"
        "\n}"
    )
    assert expected in expression
    assert int_1 == 10

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=handler.append_handler_expression,
        handler_data=handler_data,
        handler_name=handler_name,
        e=100,
    )

    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance):
                handler.append_handler_expression(
                    handler_data=handler_data, handler_name="test_handler_b_2", e=e
                )
    expression = expression_data_util.get_current_event_handler_scope_expression()
    assert "test_handler_b" not in expression

    ap.Stage()
    handler.append_handler_expression(
        handler_data=handler_data,
        handler_name="test_handler",
        e=e,
        in_handler_head_expression='console.log("hello");',
    )
    expression = expression_data_util.get_current_event_handler_scope_expression()
    expected = '{\n  console.log("hello");\n'
    assert expected in expression


@apply_test_settings()
def test_append_unbinding_expression() -> None:
    ap.Stage()
    int_1: ap.Int = ap.Int(10)
    handler.append_unbinding_expression(
        this=int_1, handler_name="on_click_1", mouse_event_type=ap.MouseEventType.CLICK
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f'{int_1.variable_name}.off("{ap.MouseEventType.CLICK.value}", ' "on_click_1);"
    )
    assert expected in expression


@apply_test_settings()
def test_append_unbinding_all_expression() -> None:
    ap.Stage()
    int_1: ap.Int = ap.Int(10)
    handler.append_unbinding_all_expression(
        this=int_1, mouse_event_type=ap.MouseEventType.CLICK
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = f'{int_1.variable_name}.off("{ap.MouseEventType.CLICK.value}");'
    assert expected in expression


@apply_test_settings()
def test__append_in_handler_head_expression() -> None:
    expression_data_util.empty_expression()
    handler._append_in_handler_head_expression(in_handler_head_expression="")
    expression: str = expression_data_util.get_current_expression()
    assert expression == ""

    ap.Stage()
    handler._append_in_handler_head_expression(
        in_handler_head_expression='console.log("hello");'
    )
    expression = expression_data_util.get_current_expression()
    assert 'console.log("hello");' in expression
