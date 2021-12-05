from random import randint

from retrying import retry

from apysc._validation import path_validation
import apysc as ap
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_bezier_2d_continual_pre_data() -> None:
    move_to: ap.PathMoveTo = ap.PathMoveTo(x=0, y=50)
    bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
        control_x=0, control_y=0, dest_x=50, dest_y=50)
    bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
        x=100, y=100)

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation._validate_bezier_2d_continual_pre_data,
        kwargs={'path_data_list': [bezier_2d_continual]},
        match='`PathBezier2DContinual` instance can not be set '
              'at the first position of `path_data_list`.')

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation._validate_bezier_2d_continual_pre_data,
        kwargs={'path_data_list': [move_to, bezier_2d_continual]},
        match='`PathBezier2DContinual` instance in a '
              '`path_data_list` argument can set only after a '
              '`PathBezier2D` or `PathBezier2DContinual` one.')

    path_validation._validate_bezier_2d_continual_pre_data(
        path_data_list=[
            move_to,
            bezier_2d,
            bezier_2d_continual,
            bezier_2d_continual,
        ])
