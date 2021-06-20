from random import randint

from retrying import retry

from apysc.expression import event_handler_scope
from apysc.expression import expression_file_util
from apysc.expression.event_handler_scope import HandlerScope
from apysc.expression.event_handler_scope import TemporaryNotHandlerScope
from apysc.file import file_util


def teardown() -> None:
    """
    Function that will be called when test ended.
    """
    file_path: str = expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    file_util.remove_file_if_exists(file_path=file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_event_handler_scope_count() -> None:
    file_path: str = expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    file_util.remove_file_if_exists(file_path=file_path)

    scope_count: int = \
        event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 0

    file_util.save_plain_txt(txt='', file_path=file_path)
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 0

    file_util.save_plain_txt(txt='2', file_path=file_path)
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 2

    file_util.remove_file_if_exists(file_path=file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_current_scope_count() -> None:
    event_handler_scope._save_current_scope_count(count=3)
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 3


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__increment_scope_count() -> None:
    file_path: str = expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    file_util.remove_file_if_exists(file_path=file_path)
    event_handler_scope._increment_scope_count()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 1

    event_handler_scope._increment_scope_count()
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 2

    file_util.remove_file_if_exists(file_path=file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__decrement_scope_count() -> None:
    file_path: str = expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    file_util.remove_file_if_exists(file_path=file_path)

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

    file_util.remove_file_if_exists(file_path=file_path)


class TestHandlerScope:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        file_path: str = \
            expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
        file_util.remove_file_if_exists(file_path=file_path)

        with HandlerScope():
            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 1

            with HandlerScope():
                scope_count = event_handler_scope.\
                    get_current_event_handler_scope_count()
                assert scope_count == 2

        file_util.remove_file_if_exists(file_path=file_path)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        file_path: str = \
            expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
        file_util.remove_file_if_exists(file_path=file_path)

        with HandlerScope():

            with HandlerScope():
                pass

            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 1

        scope_count = event_handler_scope.\
            get_current_event_handler_scope_count()
        assert scope_count == 0

        file_util.remove_file_if_exists(file_path=file_path)


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
