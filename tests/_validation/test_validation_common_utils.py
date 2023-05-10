import apysc as ap
from apysc._validation import validation_common_utils
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_append_additional_err_msg() -> None:
    err_msg: str = validation_common_utils.append_additional_err_msg(
        err_msg="test error.",
        additional_err_msg="",
    )
    assert err_msg == "test error."

    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg="test error.",
        additional_err_msg="test additional error.",
    )
    assert err_msg == "test error.\ntest additional error."
