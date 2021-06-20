"""Test project for `For` class.

Command examples:
$ python test_projects/For/main.py
$ python For/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Array
from apysc import Dictionary
from apysc import For
from apysc import Int
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc import assert_arrays_equal
from apysc import assert_dicts_equal
from apysc import save_overall_html
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
    stage: Stage = Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)

    arr_1: Array = Array([Int(1), Int(2), Int(3)])
    with For(arr_1, locals(), globals()) as i:
        arr_1[i] += 10
    assert_arrays_equal(
        expected=[11, 12, 13], actual=arr_1)

    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    arr_2: Array = Array(list(range(3)))
    with For(arr_2, locals(), globals()) as i:
        sprite.graphics.draw_rect(
            x=(i * 100) + 50,
            y=(i * 100) + 50,
            width=(i + 1) * 50,
            height=(i + 1) * 50)

    dict_1: Dictionary = Dictionary({'a': 10, 'b': 20})
    with For[String](dict_1) as key:
        dict_1[key] *= 2
    assert_dicts_equal(
        expected={'a': 20, 'b': 40},
        actual=dict_1)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
