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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_bezier_3d_continual_pre_data() -> None:
    move_to: ap.PathMoveTo = ap.PathMoveTo(x=0, y=50)
    bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
        control_x1=100, control_y1=0, control_x2=150, control_y2=0,
        dest_x=100, dest_y=100)
    bezier_3d_continual: ap.PathBezier3DContinual = ap.PathBezier3DContinual(
        control_x=200, control_y=200, dest_x=250, dest_y=100)

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation._validate_bezier_3d_continual_pre_data,
        kwargs={'path_data_list': [bezier_3d_continual]},
        match='`PathBezier3DContinual` instance can not be set '
              'at the first position of `path_data_list`.')

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation._validate_bezier_3d_continual_pre_data,
        kwargs={'path_data_list': [move_to, bezier_3d_continual]},
        match='`PathBezier3DContinual` instance in a '
              '`path_data_list` argument can set only after a '
              '`PathBezier3D` or `PathBezier3DContinual` one.')

    path_validation._validate_bezier_3d_continual_pre_data(
        path_data_list=[
            move_to,
            bezier_3d,
            bezier_3d_continual,
            bezier_3d_continual,
        ])


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_path_data_list() -> None:
    move_to: ap.PathMoveTo = ap.PathMoveTo(x=0, y=50)
    bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
        x=100, y=100)
    bezier_3d_continual: ap.PathBezier3DContinual = ap.PathBezier3DContinual(
        control_x=200, control_y=200, dest_x=250, dest_y=100)
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation.validate_path_data_list,
        kwargs={'path_data_list': []},
        match='`path_data_list` argument can not be empty.',
    )
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation.validate_path_data_list,
        kwargs={'path_data_list': [bezier_2d_continual]},
    )
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=path_validation.validate_path_data_list,
        kwargs={'path_data_list': [bezier_3d_continual]},
    )

    path_validation.validate_path_data_list(
        path_data_list=[move_to])
