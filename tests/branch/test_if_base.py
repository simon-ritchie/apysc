from random import randint
from typing import Any, Dict, Type, Match, Optional
import re

from retrying import retry

from apysc.expression import expression_file_util, indent_num
from apysc.branch.if_base import IfBase
from apysc.type import Boolean, Int
from tests import testing_helper


class IfSubClass(IfBase):

    _entered: bool = False
    _last_scope_is_set: bool = False

    def _append_enter_expression(self) -> None:
        """
        Append branch instruction start expression to file.
        """
        self._entered = True

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        self._last_scope_is_set = True


class TestIfBase:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        condition: Boolean = Boolean(True)
        locals_: Dict[str, Any] = {'value1': 10}
        globals_: Dict[str, Any] = {'value2': 20}
        instance: IfSubClass = IfSubClass(
            condition=condition, locals_=locals_, globals_=globals_)
        testing_helper.assert_attrs(
            expected_attrs={
                '_condition': condition,
                '_locals': locals_,
                '_globals': globals_,
            },
            any_obj=instance)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___enter__(self) -> None:
        expression_file_util.remove_expression_file()
        indent_num.reset()
        int_1: Int = Int(10)
        condition: Boolean = Boolean(True)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': 20}
        instance: IfSubClass
        with IfSubClass(
                condition=condition, locals_=locals_,
                globals_=globals_) as instance:
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
            assert instance._entered
            assert instance._snapshot_name

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___exit__(self) -> None:
        expression_file_util.remove_expression_file()
        indent_num.reset()
        int_1: Int = Int(10)
        condition: Boolean = Boolean(True)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': 20}
        instance: IfSubClass
        with IfSubClass(
                condition=condition, locals_=locals_,
                globals_=globals_) as instance:
            pass
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0
        assert instance._last_scope_is_set
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=r'^}',
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_exit_expression(self) -> None:
        expression_file_util.remove_expression_file()
        indent_num.reset()
        with IfSubClass(condition=Boolean(True), locals_={}, globals_={}):
            pass
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=r'^}',
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None
