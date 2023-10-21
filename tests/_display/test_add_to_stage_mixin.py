import apysc as ap
from apysc._display.add_to_stage_mixin import AddToStageMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestValidObject(
    CssMixIn,
    ap.DisplayObject,
    AddToStageMixIn,
    VariableNameMixIn,
):
    def __init__(self) -> None:
        """
        A class for a valid test pattern.
        """
        super().__init__(variable_name="test_object")


class _TestInvalidObject(AddToStageMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """
        A class for an invalid test pattern.
        """


class TestAddToStageMixIn:
    @apply_test_settings()
    def test__add_to_stage(self) -> None:
        stage: ap.Stage = ap.get_stage()
        test_valid_object: _TestValidObject = _TestValidObject()
        test_valid_object._add_to_stage()
        assert test_valid_object.parent == stage

        test_invalid_object: _TestInvalidObject = _TestInvalidObject()
        assert_raises(
            expected_error_class=TypeError,
            callable_=test_invalid_object._add_to_stage,
        )
