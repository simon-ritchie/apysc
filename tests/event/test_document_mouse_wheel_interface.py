from apysc.event.handler import get_handler_name
from random import randint

from retrying import retry

from typing import Any, Dict
from apysc import bind_wheel_event_to_document, unbind_wheel_event_from_document
from apysc import WheelEvent
from apysc.expression import expression_file_util
from apysc.expression import var_names


def on_mouse_wheel_1(e: WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler for mouse wheel event.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    assert options['msg'] == 'Hello!'


def on_mouse_wheel_2(e: WheelEvent, options: Dict[str, Any]) -> None:
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_bind_wheel_event_to_document() -> None:
    expression_file_util.remove_expression_file()
    name: str = bind_wheel_event_to_document(
        handler=on_mouse_wheel_1, options={'msg': 'Hello!'})
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'$(document).on("mousewheel", {name});'
    )
    assert expected in expression

    expression = expression_file_util.\
        get_current_event_handler_scope_expression()
    expected = (
        f'function {name}({var_names.WHEEL_EVENT}_'
    )
    assert expected in expression

    _ = bind_wheel_event_to_document(handler=on_mouse_wheel_2)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_unbind_wheel_event_from_document() -> None:
    expression_file_util.remove_expression_file()
    unbind_wheel_event_from_document(handler=on_mouse_wheel_1)
    name: str = get_handler_name(handler=on_mouse_wheel_1)
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'$(document).off("mousewheel", {name});'
    )
    assert expected in expression
