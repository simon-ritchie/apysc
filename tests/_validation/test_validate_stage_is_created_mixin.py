import apysc as ap
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._validation.validate_stage_is_created_mixin import (
    ValidateStageIsCreatedMixIn
)
from apysc._display.stage import StageNotCreatedError


class TestValidateStageIsCreatedMixIn:
    @apply_test_settings()
    def test__validate_stage_is_created(self) -> None:
        ap.Stage()

        mixin: ValidateStageIsCreatedMixIn = ValidateStageIsCreatedMixIn()
        assert_raises(
            expected_error_class=StageNotCreatedError,
            callable_=mixin._validate_stage_is_created,
        )

        ap.Stage()
        mixin._validate_stage_is_created()
