"""Test project for the `Array` class's `clear` interface.

Command examples:
$ python test_projects/Array_clear/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _ArrOptions(TypedDict):
    arr: ap.Array


def _main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(background_color="#333", stage_width=1000, stage_height=500)
    arr_1: ap.Array = ap.Array([100, 200])
    arr_1.clear()
    ap.assert_equal(arr_1, [])

    arr_2: ap.Array = ap.Array([300, 400])
    options: _ArrOptions = {
        "arr": arr_2,
    }
    ap.Timer(
        on_timer,
        delay=100,
        repeat_count=1,
        options=options,
    ).start()
    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer(e: ap.TimerEvent, options: _ArrOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _ArrOptions
        Optional arguments dictionary.
    """
    options["arr"].clear()
    ap.assert_equal(options["arr"], [])


if __name__ == "__main__":
    _main()
