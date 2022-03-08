"""This module is for the Japanese link-text translation
mappings settings.
"""

from apysc._lint_and_doc.link_text_translation_mapping.data_model import \
    Mapping, Mappings

MAPPINGS: Mappings = Mappings(
    mappings=[
        Mapping(
            link_text='Graphics class',
            mapping_text='Graphicsクラス'),
        Mapping(
            link_text='Graphics begin_fill interface',
            mapping_text='Graphicsクラス begin_fill インターフェイス'),
        Mapping(
            link_text='Graphics line_style interface',
            mapping_text='Graphicsクラス line_style インターフェイス'),
        Mapping(
            link_text='Graphics draw_rect interface',
            mapping_text='Graphicsクラス draw_rect インターフェイス'),
        Mapping(
            link_text='Graphics draw_circle interface',
            mapping_text='Graphicsクラス draw_circle インターフェイス'),
    ])
