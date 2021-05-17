from apysc.validation import geom_validation
from apysc import Point2D
from tests.testing_helper import assert_raises


def test_validate_point_2d_type() -> None:
    point: Point2D = Point2D(x=10, y=20)
    geom_validation.validate_point_2d_type(point=point)

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=geom_validation.validate_point_2d_type,
        kwargs={'point': (10, 20)},
        match='Specified value\'s type is not Point2D: ')
