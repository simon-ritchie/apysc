"""This module is for the Japanese fixed-translation mappings
settings.
"""

from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mappings

MAPPINGS: Mappings = Mappings(
    mappings=[
        Mapping(
            key='## See also',
            value='## 関連資料'),
        Mapping(
            key='**[Parameters]**',
            value='**[引数]**'),
        Mapping(
            key='**[Returns]**',
            value='**[返却値]**'),
        Mapping(
            key='**[Parameters]**',
            value='**[引数]**'),
        Mapping(
            key='**[Examples]**',
            value='**[コードサンプル]**'),
        Mapping(
            key='**[References]**',
            value='**[関連資料]**'),
        Mapping(
            key=(
                '<span class="inconspicuous-txt">Note: the document build '
                'script generates and updates this API document section '
                'automatically. Maybe this section is duplicated '
                'compared with previous sections.</span>'
            ),
            value=(
                '<span class="inconspicuous-txt">特記事項: このAPI'
                'ドキュメントはドキュメントビルド用のスクリプトによって自動で'
                '生成・同期されています。そのためもしかしたらこの節の'
                '内容は前節までの内容と重複している場合があります。</span>'
            )),
        Mapping(
            key='Graphics class',
            value='Graphicsクラス'),
        Mapping(
            key='Graphics begin_fill interface',
            value='Graphicsクラス begin_fill インターフェイス'),
        Mapping(
            key='Graphics line_style interface',
            value='Graphicsクラス line_style インターフェイス'),
        Mapping(
            key='Graphics draw_rect interface',
            value='Graphicsクラス draw_rect インターフェイス'),
        Mapping(
            key='Graphics draw_circle interface',
            value='Graphicsクラス draw_circle インターフェイス'),
        Mapping(
            key='add_child and remove_child interfaces',
            value='add_child と remove_child インターフェイス'),
        Mapping(
            key='contains interface',
            value='contains インターフェイス'),
        Mapping(
            key='num_children interface',
            value='num_children インターフェイス'),
        Mapping(
            key='get_child_at interface',
            value='get_child_at インターフェイス'),
        Mapping(
            key='DisplayObject class parent interfaces',
            value='DisplayObjectクラス parent インターフェイス'),
        Mapping(
            key='contains interface',
            value='contains インターフェイス'),
        Mapping(
            key='**[Notes]**',
            value='**[特記事項]**'),
        Mapping(
            key='**[Raises]**',
            value='**[エラー発生条件]**'),
        Mapping(
            key='About the handler options\\\' type document',
            value='ハンドラのoptions引数の型について'),
        Mapping(
            key='## Basic usage',
            value='## 使い方例'),
    ])
