import re
from typing import Any
from typing import Dict
from typing import Match
from typing import Optional

import apysc as ap
from apysc._branch.if_base import IfBase
from apysc._expression import expression_data_util
from apysc._expression import indent_num
from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class IfSubClass(IfBase):

    _entered: bool = False
    _last_scope_is_set: bool = False

    def _append_enter_expression(self) -> None:
        """
        Append branch instruction start expression.
        """
        self._entered = True

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        self._last_scope_is_set = True


class TestIfBase:
    @apply_test_settings()
    def test___init__(self) -> None:
        condition: ap.Boolean = ap.Boolean(True)
        locals_: Dict[str, Any] = {"value1": 10}
        globals_: Dict[str, Any] = {"value2": 20}
        instance: IfSubClass = IfSubClass(
            condition=condition, locals_=locals_, globals_=globals_
        )
        testing_helper.assert_attrs(
            expected_attrs={
                "_condition": condition,
                "_locals": locals_,
                "_globals": globals_,
            },
            any_obj=instance,
        )

        instance = IfSubClass(condition=condition)
        testing_helper.assert_attrs(
            expected_attrs={
                "_locals": {},
                "_globals": {},
            },
            any_obj=instance,
        )

    @apply_test_settings()
    def test___enter__(self) -> None:
        ap.Stage()
        indent_num.reset()
        int_1: ap.Int = ap.Int(10)
        condition: ap.Boolean = ap.Boolean(True)
        locals_: Dict[str, Any] = {"value1": int_1}
        globals_: Dict[str, Any] = {"value2": 20}
        instance: IfSubClass
        with IfSubClass(
            condition=condition, locals_=locals_, globals_=globals_
        ) as instance:
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
            assert instance._entered
            assert instance._snapshot_name

    @apply_test_settings()
    def test___exit__(self) -> None:
        ap.Stage()
        indent_num.reset()
        int_1: ap.Int = ap.Int(10)
        condition: ap.Boolean = ap.Boolean(True)
        locals_: Dict[str, Any] = {"value1": int_1}
        globals_: Dict[str, Any] = {"value2": 20}
        instance: IfSubClass
        with IfSubClass(
            condition=condition, locals_=locals_, globals_=globals_
        ) as instance:
            pass
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0
        assert instance._last_scope_is_set
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=r"^}", string=expression, flags=re.MULTILINE | re.DOTALL
        )
        assert match is not None

    @apply_test_settings()
    def test__append_exit_expression(self) -> None:
        ap.Stage()
        indent_num.reset()
        with IfSubClass(condition=ap.Boolean(True), locals_={}, globals_={}):
            pass
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=r"^}", string=expression, flags=re.MULTILINE | re.DOTALL
        )
        assert match is not None

    @apply_test_settings()
    def test__last_scope_is_if_or_elif(self) -> None:
        last_scope.reset()
        boolean_1: ap.Boolean = ap.Boolean(True)
        if_instance: IfSubClass = IfSubClass(
            condition=boolean_1, locals_=locals(), globals_=globals()
        )
        result: bool = if_instance._last_scope_is_if_or_elif()
        assert not result

        last_scope.set_last_scope(value=LastScope.IF)
        result = if_instance._last_scope_is_if_or_elif()
        assert result

        last_scope.set_last_scope(value=LastScope.ELIF)
        result = if_instance._last_scope_is_if_or_elif()
        assert result

        last_scope.set_last_scope(value=LastScope.ELSE)
        result = if_instance._last_scope_is_if_or_elif()
        assert not result
