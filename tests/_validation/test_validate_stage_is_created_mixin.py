import apysc as ap
from apysc._display.stage import StageNotCreatedError
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._validation.validate_stage_is_created_mixin import (
    ValidateStageIsCreatedMixIn,
)


class TestValidateStageIsCreatedMixIn:
    @apply_test_settings()
    def test__validate_stage_is_created(self) -> None:
        mixin: ValidateStageIsCreatedMixIn = ValidateStageIsCreatedMixIn()
        expression_data_util.empty_expression()
        assert_raises(
            expected_error_class=StageNotCreatedError,
            callable_=mixin._validate_stage_is_created,
        )

        ap.Stage()
        mixin._validate_stage_is_created()
