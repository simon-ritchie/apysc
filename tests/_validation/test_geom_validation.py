import apysc as ap
from apysc._testing.testing_helper import assert_raises
from apysc._validation import geom_validation


def test_validate_point_2d_type() -> None:
    point: ap.Point2D = ap.Point2D(x=10, y=20)
    geom_validation.validate_point_2d_type(point=point)

    assert_raises(
        expected_error_class=ValueError,
        callable_=geom_validation.validate_point_2d_type,
        match="Specified value's type is not Point2D: ",
        point=(10, 20),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=geom_validation.validate_point_2d_type,
        match="\nTest error!",
        point=(10, 20),
        additional_err_msg="Test error!",
    )
