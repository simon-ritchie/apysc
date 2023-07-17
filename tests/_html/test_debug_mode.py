import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._html import debug_mode
from apysc._html.debug_mode import DebugInfo
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


@apply_test_settings()
def test_set_debug_mode() -> None:
    ap.Stage()
    ap.set_debug_mode()
    assert debug_mode.is_debug_mode()


@apply_test_settings()
def test_is_debug_mode() -> None:
    ap.Stage()
    result: bool = ap.is_debug_mode()
    assert not result

    ap.set_debug_mode()
    result = ap.is_debug_mode()
    assert result

    ap.unset_debug_mode()
    result = ap.is_debug_mode()
    assert not result


@apply_test_settings()
def test__get_callable_count() -> None:
    ap.Stage()
    callable_count: int = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo,
    )
    assert callable_count == 0

    for _ in range(2):
        debug_mode._increment_callable_count(
            callable_=TestDebugInfo.test___init__,
            module_name=__name__,
            class_=TestDebugInfo,
        )
    callable_count = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo,
    )
    assert callable_count == 2


@apply_test_settings()
def test__increment_callable_count() -> None:
    ap.Stage()
    debug_mode._increment_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo,
    )
    callable_count: int = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo,
    )
    assert callable_count == 1


@apply_test_settings()
def test__get_callable_str() -> None:
    callable_str: str = debug_mode._get_callable_str(callable_=test__get_callable_str)
    assert callable_str == "test__get_callable_str"

    callable_str = debug_mode._get_callable_str(callable_="any_func")
    assert callable_str == "any_func"


@apply_test_settings()
def test_unset_debug_mode() -> None:
    ap.Stage()
    ap.set_debug_mode()
    assert ap.is_debug_mode()
    ap.unset_debug_mode()
    assert not ap.is_debug_mode()


@apply_test_settings()
def test__get_callable_path_name() -> None:
    path_name: str = debug_mode._get_callable_path_name(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo,
    )
    assert path_name == "tests__html_test_debug_mode_TestDebugInfo_test___init__"

    path_name = debug_mode._get_callable_path_name(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_="TestDebugInfo",
    )
    assert path_name == "tests__html_test_debug_mode_TestDebugInfo_test___init__"

    path_name = debug_mode._get_callable_path_name(
        callable_=TestDebugInfo.test___init__, module_name=__name__
    )
    assert path_name == "tests__html_test_debug_mode_test___init__"


@apply_test_settings()
def test_add_debug_info_setting() -> None:
    class _TestClass:
        @debug_mode.add_debug_info_setting(module_name=__name__)
        def test_method_1(self, a: int, *, b: str) -> int:
            return a * 2

        @classmethod
        @debug_mode.add_debug_info_setting(module_name=__name__)
        def test_method_2(cls, a: int) -> int:
            return a * 3

    ap.Stage()
    test_instance: _TestClass = _TestClass()
    ap.set_debug_mode()
    result: int = test_instance.test_method_1(10, b="Hello")
    ap.unset_debug_mode()
    assert result == 20
    expression: str = expression_data_util.get_current_expression()
    assert "// [test_method_1 1] started." in expression
    assert "// module name: tests._html.test_debug_mode" in expression
    match: Optional[Match] = re.search(
        pattern=r"\/\/ Positional arguments\: \[.*?10\]", string=expression
    )
    assert match
    assert "// Keyword arguments: {'b': 'Hello'}" in expression
    assert "class: _TestClass" in expression

    ap.Stage()
    ap.set_debug_mode()
    result = _TestClass.test_method_2(a=20)
    ap.unset_debug_mode()
    assert result == 60
    expression = expression_data_util.get_current_expression()
    assert "class: _TestClass" in expression


class TestDebugInfo:
    @apply_test_settings()
    def test___init__(self) -> None:
        debug_info: DebugInfo = DebugInfo(
            callable_=self.test___init__,
            args=[10, 20],
            kwargs={"c": 30},
            module_name=__name__,
            class_name="TestDebugInfo",
        )
        assert_attrs(
            expected_attrs={
                "_callable": self.test___init__,
                "_module_name": __name__,
                "_args": [10, 20],
                "_kwargs": {"c": 30},
                "_class_name": "TestDebugInfo",
            },
            any_obj=debug_info,
        )

    @apply_test_settings()
    def test___enter__(self) -> None:
        with DebugInfo(
            callable_=self.test___init__,
            args=[10],
            kwargs={"a": 10},
            module_name=__name__,
            class_name="TestDebugInfo",
        ):
            pass
        expression: str = expression_data_util.get_current_expression()
        assert f"\n// [{self.test___init__.__name__}" not in expression

        ap.set_debug_mode()
        with DebugInfo(
            callable_=self.test___init__,
            args=[10],
            kwargs={"a": 10},
            module_name=__name__,
            class_name="TestDebugInfo",
        ):
            pass
        expression = expression_data_util.get_current_expression()
        assert f"\n// [{self.test___init__.__name__}" in expression
        assert f"\n// module name: {__name__}" in expression
        assert "\n// class: TestDebugInfo" in expression
        assert "\n// Positional arguments: [10]" in expression
        assert "\n// Keyword arguments: {'a': 10}" in expression

    @apply_test_settings()
    def test__get_class_info(self) -> None:
        debug_info: DebugInfo = DebugInfo(
            callable_=self.test___init__,
            args=[],
            kwargs={},
            module_name=__name__,
            class_name="TestDebugInfo",
        )
        class_info: str = debug_info._get_class_info()
        assert class_info == "\n// class: TestDebugInfo"

        debug_info = DebugInfo(
            callable_=self.test___init__, args=[], kwargs={}, module_name=__name__
        )
        class_info = debug_info._get_class_info()
        assert class_info == ""

    @apply_test_settings()
    def test___exit__(self) -> None:
        with DebugInfo(
            callable_=self.test___init__,
            args=[],
            kwargs={},
            module_name=__name__,
            class_name="TestDebugInfo",
        ):
            pass
        expression: str = expression_data_util.get_current_expression()
        callable_name: str = self.test___init__.__name__
        match: Optional[Match] = re.search(
            pattern=(rf"// \[{callable_name} .+?\] ended\."),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is None

        ap.set_debug_mode()
        with DebugInfo(
            callable_=self.test___init__,
            args=[],
            kwargs={},
            module_name=__name__,
            class_name="TestDebugInfo",
        ):
            pass
        expression = expression_data_util.get_current_expression()
        match = re.search(
            pattern=(rf"// \[{callable_name} .+?\] ended\."),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None
