"""The common utility implementations for the path data.
"""

from typing import List

from apysc._geom.path_data_base import PathDataBase


def make_paths_expression_from_list(
        *, path_data_list: List[PathDataBase]) -> str:
    """
    Make a paths expression from a specified list of path data.

    Parameters
    ----------
    path_data_list : list of PathDataBase
        Target path data settings, such as the ap.PathData.MoveTo.

    Returns
    -------
    expression : str
        Created expression string.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=make_paths_expression_from_list,
            locals_=locals(), module_name=__name__):
        expression: str = ''
        for path_data in path_data_list:
            if expression != '':
                expression += ' + " " + '
            expression += path_data._get_svg_str()
        return expression
