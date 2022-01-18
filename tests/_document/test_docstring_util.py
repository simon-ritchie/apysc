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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_docstring_path_specification_comment_from_line() -> None:
    docstring_path_specification_comment: str = docstring_util.\
        _extract_docstring_path_specification_comment_from_line(
            line='<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            matches=[
                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            ])
    assert (
        docstring_path_specification_comment ==
        '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->')

    docstring_path_specification_comment = docstring_util.\
        _extract_docstring_path_specification_comment_from_line(
            line='## Test sub heading',
            matches=[
                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            ])
    assert docstring_path_specification_comment == ''
