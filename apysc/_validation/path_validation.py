"""Path's validation implementations.
"""

from typing import List

from apysc._geom.path_bezier_2d import PathBezier2D
from apysc._geom.path_bezier_2d_continual import PathBezier2DContinual
from apysc._geom.path_bezier_3d import PathBezier3D
from apysc._geom.path_bezier_3d_continual import PathBezier3DContinual
from apysc._geom.path_data_base import PathDataBase


def validate_path_data_list(
        path_data_list: List[PathDataBase]) -> None:
    """
    Validate a specified path data list.

    Parameters
    ----------
    path_data_list : list of PathDataBase
        Target path data settings, such as the ap.PathData.MoveTo.

    Raises
    ------
    ValueError
        - If a specified path data list is empty.
        - If a preceding data of `PathBezier2DContinual` instance is
            not a `PathBezier2D` or `PathBezier2DContinual` one.
        - If a preceding data of `PathBezier3DContinual` instance is
            not a `PathBezier3D` or `PathBezier3DContinual` one.
    """
    if not path_data_list:
        raise ValueError(
            '`path_data_list` argument can not be empty.')
    _validate_bezier_2d_continual_pre_data(path_data_list=path_data_list)
    _validate_bezier_3d_continual_pre_data(path_data_list=path_data_list)


def _validate_bezier_3d_continual_pre_data(
        path_data_list: List[PathDataBase]) -> None:
    """
    Validate a preceding data of `PathBezier3DContinual` instance
    in list is a `PathBezier3D` or `PathBezier3DContinual`.

    Parameters
    ----------
    path_data_list : list of PathDataBase
        Target path data settings, such as the ap.PathData.MoveTo.

    Raises
    ------
    ValueError
        If a preceding data of `PathBezier3DContinual` instance is
        not a `PathBezier3D` or `PathBezier3DContinual` one.
    """
    for i, path_data in enumerate(path_data_list):
        if i == 0 and isinstance(path_data, PathBezier3DContinual):
            raise ValueError(
                '`PathBezier3DContinual` instance can not be set '
                'at the first position of `path_data_list`.')
        if i == 0:
            continue
        if not isinstance(path_data, PathBezier3DContinual):
            continue
        pre_data: PathDataBase = path_data_list[i - 1]
        if (not isinstance(pre_data, PathBezier3D)
                and not isinstance(pre_data, PathBezier3DContinual)):
            raise ValueError(
                '`PathBezier3DContinual` instance in a '
                '`path_data_list` argument can set only after a '
                '`PathBezier3D` or `PathBezier3DContinual` one.'
                f'\nActual: {type(pre_data)}'
                f'\nIndex: {i}')


def _validate_bezier_2d_continual_pre_data(
        path_data_list: List[PathDataBase]) -> None:
    """
    Validate a preceding data of `PathBezier2DContinual` instance
    in list is a `PathBezier2D` or `PathBezier2DContinual`.

    Parameters
    ----------
    path_data_list : list of PathDataBase
        Target path data settings, such as the ap.PathData.MoveTo.

    Raises
    ------
    ValueError
        If a preceding data of `PathBezier2DContinual` instance is
        not a `PathBezier2D` or `PathBezier2DContinual` one.
    """
    for i, path_data in enumerate(path_data_list):
        if i == 0 and isinstance(path_data, PathBezier2DContinual):
            raise ValueError(
                '`PathBezier2DContinual` instance can not be set '
                'at the first position of `path_data_list`.')
        if i == 0:
            continue
        if not isinstance(path_data, PathBezier2DContinual):
            continue
        pre_data: PathDataBase = path_data_list[i - 1]
        if (not isinstance(pre_data, PathBezier2D)
                and not isinstance(pre_data, PathBezier2DContinual)):
            raise ValueError(
                '`PathBezier2DContinual` instance in a '
                '`path_data_list` argument can set only after a '
                '`PathBezier2D` or `PathBezier2DContinual` one.'
                f'\nActual: {type(pre_data)}'
                f'\nIndex: {i}')
