from random import randint

from retrying import retry

import apysc as ap
from apysc._display.visible_mixin import VisibleMixIn
from apysc._expression import expression_data_util


class _TestVisible(VisibleMixIn):
    def __init__(self) -> None:
        """
        Test class for VisibleMixIn.
        """
        self.variable_name = "test_visible"


class TestVisibleMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_visible_if_not_initialized(self) -> None:
        mixin_1: VisibleMixIn = VisibleMixIn()
        mixin_1._initialize_visible_if_not_initialized()
        assert mixin_1._visible

        mixin_1._visible.value = False
        mixin_1._initialize_visible_if_not_initialized()
        assert not mixin_1._visible

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_visible(self) -> None:
        mixin_1: _TestVisible = _TestVisible()
        result: ap.Boolean = mixin_1.visible
        assert result
        assert mixin_1._visible.variable_name != result.variable_name

        bool_1: ap.Boolean = ap.Boolean(False)
        mixin_1.visible = bool_1
        assert not mixin_1.visible
        assert mixin_1._visible.variable_name == bool_1.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_visible_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestVisible = _TestVisible()
        mixin_1.visible = ap.Boolean(True)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"if ({mixin_1._visible.variable_name}) {{"
            f"\n  {mixin_1.variable_name}.show();"
            "\n}else {"
            f"\n  {mixin_1.variable_name}.hide();"
            "\n}"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin_1: _TestVisible = _TestVisible()
        snapshot_name: str = mixin_1._get_next_snapshot_name()
        mixin_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin_1._visible_snapshots == {snapshot_name: True}

        mixin_1.visible = ap.Boolean(False)
        mixin_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin_1._visible_snapshots == {snapshot_name: True}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin_1: _TestVisible = _TestVisible()
        snapshot_name: str = mixin_1._get_next_snapshot_name()
        mixin_1._run_all_revert_methods(snapshot_name=snapshot_name)

        mixin_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin_1.visible = ap.Boolean(False)
        mixin_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin_1.visible

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_visible_attr_linking_setting(self) -> None:
        mixin: _TestVisible = _TestVisible()
        mixin._initialize_visible_if_not_initialized()
        assert mixin._attr_linking_stack["visible"] == [ap.Boolean(True)]
