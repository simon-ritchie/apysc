from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.handler import get_handler_name
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


def on_mouse_wheel_1(e: ap.WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler for mouse wheel event.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    assert options["msg"] == "Hello!"


def on_mouse_wheel_2(e: ap.WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler for mouse wheel event.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    assert options == {}


@apply_test_settings()
def test_bind_wheel_event_to_document() -> None:
    ap.Stage()
    name: str = ap.bind_wheel_event_to_document(
        handler=on_mouse_wheel_1, options={"msg": "Hello!"}
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = f'$({ap.document.variable_name}).on("mousewheel", {name});'
    assert expected in expression

    expression = expression_data_util.get_current_event_handler_scope_expression()
    expected = f"function {name}({var_names.WHEEL_EVENT}_"
    assert expected in expression

    _ = ap.bind_wheel_event_to_document(handler=on_mouse_wheel_2)


@apply_test_settings()
def test_unbind_wheel_event_from_document() -> None:
    ap.Stage()
    ap.unbind_wheel_event_from_document(handler=on_mouse_wheel_1)
    name: str = get_handler_name(handler=on_mouse_wheel_1, instance=ap.document)
    expression: str = expression_data_util.get_current_expression()
    expected: str = f'$({ap.document.variable_name}).off("mousewheel", {name});'
    assert expected in expression


@apply_test_settings()
def test_unbind_wheel_event_all_from_document() -> None:
    ap.Stage()
    ap.unbind_wheel_event_all_from_document()
    expression: str = expression_data_util.get_current_expression()
    expected: str = f'$({ap.document.variable_name}).off("mousewheel");'
    assert expected in expression
