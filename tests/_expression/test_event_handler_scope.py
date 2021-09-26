from random import randint
from typing import Optional
from typing import Tuple

from retrying import retry

from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._expression.event_handler_scope import TemporaryNotHandlerScope
from apysc._type.variable_name_interface import VariableNameInterface


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def teardown() -> None:
    """
    Function that will be called when test ended.
    """
    expression_data_util.empty_expression()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_event_handler_scope_count() -> None:
    expression_data_util.empty_expression()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 0

    event_handler_scope._save_current_scope_count(count=3)
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 3


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_current_scope_count() -> None:
    event_handler_scope._save_current_scope_count(count=3)
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 3

    event_handler_scope._save_current_scope_count(count=5)
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 5


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__increment_scope_count() -> None:
    expression_data_util.empty_expression()
    event_handler_scope._increment_scope_count()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 1

    event_handler_scope._increment_scope_count()
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__decrement_scope_count() -> None:
    expression_data_util.empty_expression()

    event_handler_scope._increment_scope_count()
    event_handler_scope._increment_scope_count()
    event_handler_scope._decrement_scope_count()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 1

    event_handler_scope._decrement_scope_count()
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 0

    event_handler_scope._decrement_scope_count()
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 0


class TestHandlerScope:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_instance'
        handler_scope: HandlerScope = HandlerScope(
            handler_name='test_handler_1', instance=instance)
        assert handler_scope._handler_name == 'test_handler_1'
        assert handler_scope._instance == instance

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        expression_data_util.empty_expression()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_instance'

        with HandlerScope(handler_name='test_handler_1', instance=instance):
            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 1

            with HandlerScope(
                    handler_name='test_handler_2', instance=instance):
                scope_count = event_handler_scope.\
                    get_current_event_handler_scope_count()
                assert scope_count == 2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        expression_data_util.empty_expression()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_instance'

        with HandlerScope(handler_name='test_handler_1', instance=instance):

            with HandlerScope(
                    handler_name='test_handler_2', instance=instance):
                pass

            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 1

        scope_count = event_handler_scope.\
            get_current_event_handler_scope_count()
        assert scope_count == 0


class TestTemporaryNotHandlerScope:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        event_handler_scope._save_current_scope_count(count=1)
        scope: TemporaryNotHandlerScope = TemporaryNotHandlerScope()
        event_handler_scope._save_current_scope_count(count=0)
        assert scope._original_scope_count == 1

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        event_handler_scope._save_current_scope_count(count=1)
        with TemporaryNotHandlerScope():
            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 0
        event_handler_scope._save_current_scope_count(count=0)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        event_handler_scope._save_current_scope_count(count=1)
        with TemporaryNotHandlerScope():
            pass
        scope_count: int = event_handler_scope.\
            get_current_event_handler_scope_count()
        assert scope_count == 1
        event_handler_scope._save_current_scope_count(count=0)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_handler_calling_stack() -> None:
    expression_data_util.empty_expression()
    instance: VariableNameInterface = VariableNameInterface()
    instance.variable_name = 'test_instance'
    with HandlerScope(handler_name='test_handler_a_1', instance=instance):
        query: str = (
            'SELECT scope_count, variable_name FROM '
            f'{expression_data_util.TableName.HANDLER_CALLING_STACK.value} '
            f"WHERE handler_name = 'test_handler_a_1' LIMIT 1;"
        )
        expression_data_util.exec_query(sql=query)
        result: Optional[Tuple[int, str]] = \
            expression_data_util.cursor.fetchone()
    assert result is not None
    assert result[0] == 1
    assert result[1] == 'test_instance'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__delete_handler_calling_stack() -> None:
    expression_data_util.empty_expression()
    instance: VariableNameInterface = VariableNameInterface()
    instance.variable_name = 'test_instance'
    with HandlerScope(handler_name='test_handler_a_1', instance=instance):
        pass
    query: str = (
        'SELECT scope_count FROM '
        f'{expression_data_util.TableName.HANDLER_CALLING_STACK.value} '
        f"WHERE handler_name = 'test_handler_a_1' LIMIT 1;"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    assert result is None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_remove_suffix_num_from_handler_name() -> None:
    handler_name: str = event_handler_scope.\
        remove_suffix_num_from_handler_name(
            handler_name='__main__on_timer_1_timer_5')
    assert handler_name == '__main__on_timer_1_timer'
