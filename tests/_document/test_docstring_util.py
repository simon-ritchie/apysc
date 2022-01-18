from random import randint
from typing import List

from retrying import retry

from apysc._document import docstring_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_docstring_path_comment_matches() -> None:
    matches: List[str] = docstring_util._get_docstring_path_comment_matches(
        md_txt=(
            '# Test title'
            '\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
            '\n## Sub heading'
            '\n<!-- Docstring:apysc._display.sprite.Sprite.add_child-->'
        ))
    assert matches == [
        '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
        '<!-- Docstring:apysc._display.sprite.Sprite.add_child-->',
    ]
