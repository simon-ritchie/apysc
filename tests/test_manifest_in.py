import os
from typing import List

from apysc._file import file_util


def test_manifest_in_file_exists() -> None:
    assert os.path.exists('./MANIFEST.in')


def test_manifest_in_directories_exist() -> None:
    manifest_in_txt: str = file_util.read_txt(file_path='./MANIFEST.in')
    lines: List[str] = manifest_in_txt.splitlines()
    for line in lines:
        if line.startswith('include '):
            line = line.replace('include ', '', 1)
        if line.endswith('*'):
            line = line[:-1]
        line = line.strip()
        if line == '':
            continue
        assert os.path.isdir(line)
