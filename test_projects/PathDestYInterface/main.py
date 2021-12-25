"""The test project for the PathDestYInterface class.

Command examples:
$ python test_projects/PathDestYInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util
from apysc._geom.path_dest_y_interface import PathDestYInterface

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)

class _InterfaceOptions(TypedDict):
    interface: PathDestYInterface


def main() -> None:
    """
    Entry point of this test project.
    """
    _ = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    interface: PathDestYInterface = PathDestYInterface()
    interface.dest_y = ap.Int(10)
    options: _InterfaceOptions = {'interface': interface}
    ap.Timer(
        on_timer_1, delay=1000, repeat_count=1, options=options).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer_1(e: ap.TimerEvent, options: _InterfaceOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.assert_equal(10, options['interface'].dest_y)
    options['interface'].dest_y = ap.Int(20)
    ap.Timer(
        on_timer_2, delay=1000, repeat_count=1, options=options).start()


def on_timer_2(e: ap.TimerEvent, options: _InterfaceOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.assert_equal(20, options['interface'].dest_y)
    options['interface'].dest_y = ap.Int(10)
    ap.Timer(
        on_timer_1, delay=1000, repeat_count=1, options=options).start()


if __name__ == '__main__':
    main()
