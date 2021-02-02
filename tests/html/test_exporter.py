import os
import shutil
from typing import List

from apyscript.html import exporter


def test__export_js_libs() -> None:
    tmp_dir_path: str = '../.tmp_action_py_script_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths: List[str] = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path)
    for saved_js_file_path in saved_js_file_paths:
        assert os.path.isfile(saved_js_file_path)

    expected_file_path: str = os.path.join(
        tmp_dir_path, 'jquery.min.js')
    assert expected_file_path in saved_js_file_paths

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
