"""The test project for the `Continue` class.

Command examples:
$ python test_projects/Continue/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)

    arr: ap.Array = ap.Array(range(2))
    i: ap.Int
    with ap.For(arr) as i:
        condition: ap.Boolean = i == 1
        condition = condition.not_
        with ap.If(condition):
            ap.Continue()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#0af')
        sprite.graphics.draw_rect(x=i * 50, y=50, width=50, height=50)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
