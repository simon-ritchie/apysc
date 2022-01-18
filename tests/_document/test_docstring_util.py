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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_replaced_docstring_section_from_md_txt() -> None:
    md_txt: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n**Parameters**'
        '\n\n- a: str'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n**Parameters**'
        '\n\n- b: str'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    md_txt = docstring_util._remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt,
        matches=[
            '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
            '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
        ])
    expected: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    assert md_txt == expected
