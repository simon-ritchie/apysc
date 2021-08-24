"""Test project for the `BlankObjectInterface` class.

Command examples:
$ python test_projects/BlankObjectInterface/main.py
$ python BlankObjectInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._expression import expression_data_util
from apysc._file import file_util
from apysc._type.blank_object_interface import BlankObjectInterface

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)

    interface: BlankObjectInterface = BlankObjectInterface()
    variable_name = interface.blank_object_variable_name
    expression: str = (
        f'console.assert(_.isEqual({variable_name}, {{}}));'
    )
    expression_data_util.append_js_expression(expression=expression)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
