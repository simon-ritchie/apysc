"""Test project for `For` class.

Command examples:
$ python test_projects/For/main.py
$ python For/main.py
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

    arr_1: ap.Array = ap.Array([ap.Int(1), ap.Int(2), ap.Int(3)])
    with ap.For(arr_1, locals(), globals()) as i:
        arr_1[i] += 10
    ap.assert_arrays_equal(
        expected=[11, 12, 13], actual=arr_1)

    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    arr_2: ap.Array = ap.Array(list(range(3)))
    with ap.For(arr_2, locals(), globals()) as i:
        sprite.graphics.draw_rect(
            x=(i * 100) + 50,
            y=(i * 100) + 50,
            width=(i + 1) * 50,
            height=(i + 1) * 50)

    dict_1: ap.Dictionary[ap.String, ap.Int] = ap.Dictionary({
        'a': ap.Int(10), 'b': ap.Int(20)})
    with ap.For[ap.String](dict_1) as key:
        dict_1[key] *= ap.Int(2)
    ap.trace('dict_1:', dict_1)
    ap.assert_dicts_equal(
        expected={'a': 20, 'b': 40},
        actual=dict_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
