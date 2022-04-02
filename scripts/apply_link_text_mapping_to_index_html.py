"""Apply table-of-contents text mappings to each index's
markdown file.

Command examples:
$ python scripts/apply_link_text_mapping_to_index_html.py
"""

import os
import subprocess as sp
import sys
from logging import Logger
from typing import Dict, List
import re

sys.path.append('./')

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()

_MAPPINGS: Dict[str, str] = {
    'save overall html': 'save_overall_html',
    'display on jupyter': 'display_on_jupyter',
    'display on google colaboratory': 'display_on_google_colaboratory',
    'append js expression': 'append_js_expression',
    'add child': 'add_child',
    'remove child': 'remove_child',
    'num children': 'num_children',
    'get child at': 'get_child_at',
    'insert at': 'insert_at',
    'remove at': 'remove_at',
    'index of': 'index_of',
    'get css': 'get_css',
    'set css': 'set_css',
    'rotation around center': 'rotation_around_center',
    'rotation around point': 'rotation_around_point',
    'scale from center': 'scale_from_center',
    'scale from point': 'scale_from_point',
    'skew x': 'skew_x',
    'skew y': 'skew_y',
    'begin fill': 'begin_fill',
    'line style': 'line_style',
    'draw rect': 'draw_rect',
    'draw round rect': 'draw_round_rect',
    'draw circle': 'draw_circle',
    'draw ellipse': 'draw_ellipse',
    'move to': 'move_to',
    'line to': 'line_to',
    'draw line': 'draw_line',
    'draw dotted line': 'draw_dotted_line',
    'draw dashed line': 'draw_dashed_line',
    'draw round dotted line': 'draw_round_dotted_line',
    'draw dash dotted line': 'draw_dash_dotted_line',
    'draw polygon': 'draw_polygon',
    'fill color': 'fill_color',
    'fill alpha': 'fill_alpha',
    'line color': 'line_color',
    'line alpha': 'line_alpha',
    'line thickness': 'line_thickness',
    'line dot setting': 'line_dot_setting',
    'line dash setting': 'line_dash_setting',
    'line round dot setting': 'line_round_dot_setting',
    'line dash dot setting': 'line_dash_dot_setting',
    'bind custom event': 'bind_custom_event',
    'trigger custom event': 'trigger_custom_event',
    'repeat count': 'repeat_count',
    'timer complete': 'timer_complete',
    'animation complete': 'animation_complete',
    'animation time': 'animation_time',
    'animation parallel': 'animation_parallel',
    'animation move': 'animation_move',
    'animation x': 'animation_x',
    'animation y': 'animation_y',
    'animation width': 'animation_width',
    'animation height': 'animation_height',
    'animation fill color': 'animation_fill_color',
    'animation fill alpha': 'animation_fill_alpha',
    'animation line color': 'animation_line_color',
    'animation line alpha': 'animation_line_alpha',
    'animation line thickness': 'animation_line_thickness',
    'animation radius': 'animation_radius',
    'animation rotation around center': 'animation_rotation_around_center',
    'animation rotation around point': 'animation_rotation_around_point',
    'animation scale x from center': 'animation_scale_x_from_center',
    'animation scale y from center': 'animation_scale_y_from_center',
    'animation scale x from point': 'animation_scale_x_from_point',
    'animation scale y from point': 'animation_scale_y_from_point',
    'animation skew x': 'animation_skew_x',
    'set debug mode': 'set_debug_mode',
    'unset debug mode': 'unset_debug_mode',
    'assert equal': 'assert_equal',
    'assert not equal': 'assert_not_equal',
    'assert true': 'assert_true',
    'assert false': 'assert_false',
    'assert arrays equal': 'assert_arrays_equal',
    'assert arrays not equal': 'assert_arrays_not_equal',
    'assert dicts equal': 'assert_dicts_equal',
    'assert dicts not equal': 'assert_dicts_not_equal',
    'assert defined': 'assert_defined',
    'assert undefined': 'assert_undefined',
}


def apply() -> None:
    """Apply table-of-contents text mappings to each index's
    markdown file.
    """
    from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
    from apysc._lint_and_doc import lint_and_doc_hash_util
    print('-' * 20)
    logger.info(
        msg='Applying index.md\'s table-of-contents text mappings...')
    html_paths: List[str] = _get_target_html_paths()
    for html_path in html_paths:
        is_file_updated: bool = lint_and_doc_hash_util.is_file_updated(
            file_path=html_path,
            hash_type=HashType.INDEX_HTML_LINK_TEXT_MAPPING)
        if not is_file_updated:
            continue
        logger.info(
            msg=f'Applying mappings to the {html_path}')
        _apply_mapping(html_path=html_path)
        lint_and_doc_hash_util.save_target_file_hash(
            file_path=html_path,
            hash_type=HashType.INDEX_HTML_LINK_TEXT_MAPPING)


def _apply_mapping(*, html_path: str) -> None:
    """
    Apply each link text mapping to a specified HTML file.

    Parameters
    ----------
    html_path : str
        A target HTML's file path.
    """
    from apysc._file import file_util
    html_txt: str = file_util.read_txt(file_path=html_path)
    for mapping_key, mapping_value in _MAPPINGS.items():
        html_txt = html_txt.replace(mapping_key, mapping_value)
    file_util.save_plain_txt(txt=html_txt, file_path=html_path)


def _get_target_html_paths() -> List[str]:
    """
    Get target index.html's file paths.

    Returns
    -------
    html_paths : list of str
        Target HTML files paths.
    """
    html_paths: List[str] = []
    DIR_PATH: str = './docs/'
    file_names: List[str] = os.listdir(DIR_PATH)
    for file_name in file_names:
        if not file_name.endswith('index.html'):
            continue
        html_path: str = os.path.join(
            DIR_PATH,
            file_name,
        )
        html_paths.append(html_path)
    return html_paths


if __name__ == '__main__':
    apply()
