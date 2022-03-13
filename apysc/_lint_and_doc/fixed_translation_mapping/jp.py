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
            value='Graphicsクラス begin_fill （塗り設定）の'
                  'インターフェイス'),
        Mapping(
            key='Graphics line_style interface',
            value='Graphicsクラス line_style （線設定）の'
                  'インターフェイス'),
        Mapping(
            key='Graphics draw_rect interface',
            value='Graphicsクラス draw_rect （四角描画）の'
                  'インターフェイス'),
        Mapping(
            key='Graphics draw_circle interface',
            value='Graphicsクラス draw_circle （円描画）の'
                  'インターフェイス'),
        Mapping(
            key='add_child and remove_child interfaces',
            value='add_child （子の追加）と remove_child （子の削除）'
                  'のインターフェイス'),
        Mapping(
            key='contains interface',
            value='contains インターフェイス'),
        Mapping(
            key='num_children interface',
            value='num_children （子の件数属性）のインターフェイス'),
        Mapping(
            key='get_child_at interface',
            value='get_child_at （特定位置の子の取得処理）の'
                  'インターフェイス'),
        Mapping(
            key='DisplayObject class parent interfaces',
            value='DisplayObjectクラス parent （親要素属性）の'
                  'インターフェイス'),
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
        Mapping(
            key='## What setting is this?',
            value='## 設定概要'),
        Mapping(
            key='## What class is this?',
            value='## クラス概要'),
        Mapping(
            key='## What interface is this?',
            value='## インターフェイス概要'),
        Mapping(
            key='Animation interfaces duration setting document',
            value='各アニメーションインターフェイスの duration '
                  '（アニメーション時間）設定'),
        Mapping(
            key='Each animation interface return value document',
            value='各アニメーションインターフェイスの返却値'),
        Mapping(
            key='Sequential animation setting document',
            value='連続したアニメーション設定'),
        Mapping(
            key='animation_parallel interface document',
            value='animation_parallel （並列アニメーション設定）の'
                  'インターフェイス'),
        Mapping(
            key='Easing enum document',
            value='イージングのenum'),
        Mapping(
            key='  - Milliseconds before an animation ends.',
            value='  - アニメーション完了までのミリ秒。'),
        Mapping(
            key='  - Milliseconds before an animation starts.',
            value='  - アニメーション開始までの遅延時間のミリ秒。'),
        Mapping(
            key='  - Easing setting.',
            value='  - イージング設定。'),
        Mapping(
            key='To start this animation, you need to call the '
                '`start` method of the returned instance.<hr>',
            value='アニメーションを開始するには返却されたインスタンスの'
                  '`start`メソッドを呼び出す必要があります。<hr>'),
        Mapping(
            key='Animation interfaces delay setting document',
            value='各アニメーションインターフェイスの delay （遅延時間）設定'),
        Mapping(
            key='  - Created animation setting instance.',
            value='  - 生成されたアニメーションのインスタンス。'),
        Mapping(
            key='<details>\\n<summary>Display the code block:</summary>',
            value='<details>\\n<summary>コードブロックを表示:</summary>'),
        Mapping(
            key='animation_x interface document',
            value='animation_x （X座標のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_y interface document',
            value='animation_y （Y座標のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_move interface document',
            value='animation_move （XとY座標のアニメーション）のインターフェイス'),
    ])
