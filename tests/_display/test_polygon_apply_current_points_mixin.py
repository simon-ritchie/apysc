import re
from typing import Match
from typing import Optional

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    PolygonApplyCurrentPointsMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestPolygonApplyCurrentPointsMixIn:
    @apply_test_settings()
    def test__apply_current_points(self) -> None:
        mixin: _TestObject = _TestObject()
        mixin.variable_name = "test_mixin"
        mixin._apply_current_points()
        expression: str = expression_data_util.get_current_expression()
        assert "for (var " in expression
        match: Optional[Match] = re.search(
            pattern=rf"{mixin.variable_name}\.plot\({var_names.ARRAY}\_.+?\)",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None
