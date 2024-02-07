from typing import List
from typing import Optional
from typing import Tuple

import apysc as ap
from apysc._event import handler_circular_calling_util
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


@apply_test_settings()
def test__read_handler_names() -> None:
    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance):
            handler_names: List[str] = (
                handler_circular_calling_util._read_handler_names()
            )
            assert handler_names == ["test_handler_a", "test_handler_b"]

        handler_names = handler_circular_calling_util._read_handler_names()
        assert handler_names == ["test_handler_a"]

    handler_names = handler_circular_calling_util._read_handler_names()
    assert handler_names == []


def _is_circular_calling(handler_name: str) -> bool:
    """
    Get a current scope's boolean value.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    result : bool
        A boolean value whether the current scope is circular calling
        or not.
    """
    return handler_circular_calling_util.is_handler_circular_calling(
        handler_name=handler_name
    )


@apply_test_settings()
def test_is_handler_circular_calling() -> None:
    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        result: bool = _is_circular_calling("test_handler_a_1")
        assert not result
        with HandlerScope(handler_name="test_handler_b_1", instance=instance):
            result = _is_circular_calling("test_handler_b_1")
            assert not result
            with HandlerScope(handler_name="test_handler_c_1", instance=instance):
                result = _is_circular_calling("test_handler_c_1")
                assert not result
                with HandlerScope(handler_name="test_handler_a_2", instance=instance):
                    result = _is_circular_calling("test_handler_a_2")
                    assert not result
                    with HandlerScope(
                        handler_name="test_handler_b_2", instance=instance
                    ):
                        result = _is_circular_calling("test_handler_b_2")
                        assert result

    result = handler_circular_calling_util.is_handler_circular_calling(
        handler_name="test_handler_b_2"
    )
    assert result


@apply_test_settings()
def test__append_handler_name_to_last_of_list() -> None:
    handler_names: List[str] = (
        handler_circular_calling_util._append_handler_name_to_last_of_list(
            handler_name="test_handler_a", handler_names=[]
        )
    )
    assert handler_names == ["test_handler_a"]

    handler_names = handler_circular_calling_util._append_handler_name_to_last_of_list(
        handler_name="test_handler_a",
        handler_names=["test_handler_a", "test_handler_b", "test_handler_a"],
    )
    assert handler_names == ["test_handler_a", "test_handler_b", "test_handler_a"]

    handler_names = handler_circular_calling_util._append_handler_name_to_last_of_list(
        handler_name="test_handler_a",
        handler_names=["test_handler_a", "test_handler_b"],
    )
    assert handler_names == ["test_handler_a", "test_handler_b", "test_handler_a"]


@apply_test_settings()
def test__get_same_name_prev_hadler_name() -> None:
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance):
                same_name_prev_hadler_name: str = (
                    handler_circular_calling_util._get_same_name_prev_hadler_name(
                        handler_name="test_handler_a_2"
                    )
                )
    assert same_name_prev_hadler_name == "test_handler_a_1"


@apply_test_settings()
def test__save_circular_calling_handler_name() -> None:
    instance_1: VariableNameMixIn = VariableNameMixIn()
    instance_1.variable_name = "test_instance_1"
    instance_2: VariableNameMixIn = VariableNameMixIn()
    instance_2.variable_name = "test_instance_2"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance_1):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance_1):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance_2):
                handler_circular_calling_util._save_circular_calling_handler_name(
                    handler_name="test_handler_a_2"
                )
    table_name: str = expression_data_util.TableName.CIRCULAR_CALLING_HANDLER_NAME.value
    query: str = (
        "SELECT handler_name, prev_handler_name, prev_variable_name "
        f"FROM {table_name} "
        f"WHERE handler_name = 'test_handler_a_2'; "
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[str, str, str]] = expression_data_util.cursor.fetchone()
    assert result == ("test_handler_a_2", "test_handler_a_1", "test_instance_1")


@apply_test_settings()
def test__is_already_saved_circular_calling() -> None:
    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        handler_circular_calling_util.is_handler_circular_calling(
            handler_name="test_handler_a_1"
        )
        result: bool = handler_circular_calling_util._is_already_saved_circular_calling(
            handler_name="test_handler_a_1"
        )
    assert not result

    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance):
                with HandlerScope(handler_name="test_handler_b_2", instance=instance):
                    handler_circular_calling_util.is_handler_circular_calling(
                        handler_name="test_handler_b_2"
                    )
    result = handler_circular_calling_util._is_already_saved_circular_calling(
        handler_name="test_handler_b_2"
    )
    assert result


@apply_test_settings()
def test_get_prev_handler_name() -> None:
    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        handler_circular_calling_util.is_handler_circular_calling(
            handler_name="test_handler_a_1"
        )
        prev_handler_name: str = handler_circular_calling_util.get_prev_handler_name(
            handler_name="test_handler_a_1"
        )
    assert prev_handler_name == ""

    with HandlerScope(handler_name="test_handler_a_1", instance=instance):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance):
                with HandlerScope(handler_name="test_handler_b_2", instance=instance):
                    handler_circular_calling_util.is_handler_circular_calling(
                        handler_name="test_handler_b_2"
                    )
                    prev_handler_name = (
                        handler_circular_calling_util.get_prev_handler_name(
                            handler_name="test_handler_b_2"
                        )
                    )
    assert prev_handler_name == "test_handler_b_1"


@apply_test_settings()
def test__get_same_name_prev_data() -> None:
    instance_1: VariableNameMixIn = VariableNameMixIn()
    instance_1.variable_name = "test_instance_1"
    instance_2: VariableNameMixIn = VariableNameMixIn()
    instance_2.variable_name = "test_instance_2"

    prev_handler_name: str
    prev_variable_name: str
    with HandlerScope(handler_name="test_handler_a_1", instance=instance_1):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance_1):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance_2):
                (
                    prev_handler_name,
                    prev_variable_name,
                ) = handler_circular_calling_util._get_same_name_prev_data(
                    handler_name="test_handler_a_2"
                )
    assert prev_handler_name == "test_handler_a_1"
    assert prev_variable_name == "test_instance_1"

    with HandlerScope(handler_name="test_handler_a_1", instance=instance_1):
        assert_raises(
            expected_error_class=ValueError,
            callable_=handler_circular_calling_util._get_same_name_prev_hadler_name,
            match="Previous same name handler does not exitst in the SQLite.",
            handler_name="test_handler_a_1",
        )


@apply_test_settings()
def test__get_same_name_prev_variable_name() -> None:
    instance_1: VariableNameMixIn = VariableNameMixIn()
    instance_1.variable_name = "test_instance_1"
    instance_2: VariableNameMixIn = VariableNameMixIn()
    instance_2.variable_name = "test_instance_2"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance_1):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance_1):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance_2):
                prev_variable_name: str = (
                    handler_circular_calling_util._get_same_name_prev_variable_name(
                        handler_name="test_handler_a_2"
                    )
                )
    assert prev_variable_name == "test_instance_1"


@apply_test_settings()
def test_get_prev_variable_name() -> None:
    ap.Stage()
    prev_variable_name: str = handler_circular_calling_util.get_prev_variable_name(
        handler_name="test_handler_b_2"
    )
    assert prev_variable_name == ""

    instance_1: VariableNameMixIn = VariableNameMixIn()
    instance_1.variable_name = "test_instance_1"
    instance_2: VariableNameMixIn = VariableNameMixIn()
    instance_2.variable_name = "test_instance_2"
    with HandlerScope(handler_name="test_handler_a_1", instance=instance_1):
        with HandlerScope(handler_name="test_handler_b_1", instance=instance_1):
            with HandlerScope(handler_name="test_handler_a_2", instance=instance_2):
                with HandlerScope(handler_name="test_handler_b_2", instance=instance_2):
                    handler_circular_calling_util.is_handler_circular_calling(
                        handler_name="test_handler_b_2"
                    )
    prev_variable_name = handler_circular_calling_util.get_prev_variable_name(
        handler_name="test_handler_b_2"
    )
    assert prev_variable_name == "test_instance_1"
