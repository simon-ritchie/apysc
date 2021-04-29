from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apysc import WheelEvent, document
from apysc import bind_wheel_event_to_document
from apysc import unbind_wheel_event_all_from_document
from apysc import unbind_wheel_event_from_document
from apysc.event.handler import get_handler_name
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
        f'$({document.variable_name}).on("mousewheel", {name});'
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
    name: str = get_handler_name(handler=on_mouse_wheel_1, instance=document)
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'$({document.variable_name}).off("mousewheel", {name});'
    )
    assert expected in expression


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_unbind_wheel_event_all_from_document() -> None:
    expression_file_util.remove_expression_file()
    unbind_wheel_event_all_from_document()
    expression: str = expression_file_util.get_current_expression()
    expected: str = f'$({document.variable_name}).off("mousewheel");'
    assert expected in expression
