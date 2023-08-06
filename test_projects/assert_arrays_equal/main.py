"""The test project for the `assert_arrays_equal` and `assert_arrays_not_equal`
interfaces.

Command examples:
$ python test_projects/assert_arrays_equal/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color=ap.Color("#333"))

    ap.assert_arrays_equal(left=[1, 2, 3], right=[1, 2, 3])
    ap.assert_arrays_equal(left=(1, 2, 3), right=[1, 2, 3])
    ap.assert_arrays_equal(left=[1, 2, 3], right=(1, 2, 3))
    ap.assert_arrays_equal(left=(1, 2, 3), right=(1, 2, 3))
    ap.assert_arrays_equal(left=ap.Array([1, 2, 3]), right=[1, 2, 3])
    ap.assert_arrays_equal(left=[1, 2, 3], right=ap.Array([1, 2, 3]))
    ap.assert_arrays_equal(left=ap.Array([1, 2, 3]), right=ap.Array([1, 2, 3]))

    ap.assert_arrays_not_equal(left=[1, 2, 3], right=[1, 2])
    ap.assert_arrays_not_equal(left=(1, 2, 3), right=[1, 2])
    ap.assert_arrays_not_equal(left=[1, 2, 3], right=ap.Array([1, 2]))
    ap.assert_arrays_not_equal(left=ap.Array([1, 2, 3]), right=ap.Array([1, 2]))

    ap.assert_equal(left=ap.Array([1, 2, 3]), right=ap.Array([1, 2, 3]))
    ap.assert_equal(left=[1, 2, 3], right=ap.Array([1, 2, 3]))

    ap.assert_not_equal(left=ap.Array([1, 2, 3]), right=ap.Array([1, 2]))
    ap.assert_not_equal(left=[1, 2, 3], right=ap.Array([1, 2]))

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
