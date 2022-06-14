from random import randint
from typing import List

from retrying import retry

from scripts import check_docstring_references_docs_exist


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_file_names() -> None:
    file_names: List[str] = check_docstring_references_docs_exist.\
        _extract_file_names(dir_path='./apysc/_display/')
    for file_name in file_names:
        assert file_name.endswith('.html')
        assert '/' not in file_name
    expected_file_names: List[str] = [
        'sprite.html',
        'stage.html',
        'graphics_draw_rect.html',
    ]
    for expected_file_name in expected_file_names:
        assert expected_file_name in file_names
