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
            key=' ・To start this animation, you need to call the '
                '`start` method of the returned instance. ',
            value=' ・アニメーションを開始するには返却されたインスタンスの'
                  '`start`メソッドを呼び出す必要があります。 '),
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
        Mapping(
            key='animation_width and animation_height interfaces document',
            value='animation_width （幅のアニメーション）と animation_height '
                  '（高さのアニメーション）のインターフェイス'),
        Mapping(
            key='animation_fill_color interface document',
            value='animation_fill_color （塗りの色のアニメーション）の'
                  'インターフェイス'),
        Mapping(
            key='animation_fill_alpha interface document',
            value='animation_fill_alpha （塗りの透明度のアニメーション）の'
                  'インターフェイス'),
        Mapping(
            key='animation_line_color interface document',
            value='animation_line_color （線色のアニメーション）の'
                  'インターフェイス'),
        Mapping(
            key='animation_line_alpha interface document',
            value='animation_line_alpha （線の透明度のアニメーション）'
                  'のインターフェイス'),
        Mapping(
            key='animation_line_thickness interface document',
            value='animation_line_thickness （線幅のアニメーション）の'
                  'インターフェイス'),
        Mapping(
            key='animation_radius interface document',
            value='animation_radius （半径のアニメーション）の'
                  'インターフェイス'),
        Mapping(
            key='animation_rotation_around_center interface document',
            value='animation_rotation_around_center （中央座標での'
                  '回転のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_rotation_around_point interface document',
            value='animation_rotation_around_point （指定座標に'
                  'よる回転のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_scale_x_from_center and '
                'animation_scale_y_from_center interfaces document',
            value='animation_scale_x_from_center （中央座標による水平方向の'
                  '拡縮アニメーション）と animation_scale_y_from_center '
                  '（中央座標による垂直方向の拡縮アニメーション）のインターフェイス'),
        Mapping(
            key='animation_scale_x_from_point and '
                'animation_scale_y_from_point interfaces document',
            value='animation_scale_x_from_point （指定座標による'
                  '水平方向の拡縮アニメーション）と animation_scale_y_from_point '
                  '（指定座標による垂直方向のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_skew_x interface document',
            value='animation_skew_x （水平方向の斜め変換の'
                  'アニメーション）のインターフェイス'),
        Mapping(
            key='This interface exists on a `GraphicsBase` subclass, '
                'such as the `Rectangle` or `Circle` class.',
            value='このインターフェイスは`Rectangle`や`Circle`'
                  'クラスなどの`GraphicsBase`のサブクラスで存在します。'),
        Mapping(
            key='**[Interface summary]** Set the line alpha '
                'animation setting.<hr>',
            value='**[インターフェイス概要]** 線の透明度の'
                  'アニメーションを設定します。<hr>'),
        Mapping(
            key='  - The final line alpha of the animation.',
            value='  - 線の透明度のアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Set the line color animation '
                'setting.<hr>',
            value='**[インターフェイス概要]** 線の色のアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='  - The final line color (hex color code) of the animation.',
            value='  - 16進数の線の色のアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Set the line thickness '
                'animation setting.<hr>',
            value='**[インターフェイス概要]** 線幅のアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='  - The final line thickness of the animation.',
            value='  - 線幅のアニメーションの最終値。'),
        Mapping(
            key='This interface exists on a `DisplayObject` subclass '
                'instance, such as the `Sprite` or `Rectangle` class.',
            value='このインターフェイスは`Sprite`や`Rectangle`'
            'などの`DisplayObject`の各サブクラスに存在します。'),
        Mapping(
            key='**[Interface summary]** Set the x and y '
                'coordinates animation settings.<hr>',
            value='**[インターフェイス概要]** XとY座標に対する'
                  'アニメーションを設定します。<hr>'),
        Mapping(
            key='  - Destination of the x-coordinate.',
            value='  - 最終的なX座標。'),
        Mapping(
            key='  - Destination of the y-coordinate.',
            value='  - 最終的なY座標。'),
        Mapping(
            key='## What interface are these?',
            value='## 各インターフェイス概要'),
        Mapping(
            key='These interfaces exist in the instances that '
                'have the animation interfaces (such as the '
                '`animation_x`\\, `animation_move`).',
            value='これらのインターフェイスは`animation_x`や'
                  '`animation_move`などのアニメーション関係のインターフェイスを'
                  '持つクラスのインスタンス上に存在します。'),
        Mapping(
            key='This interface exists on a `GraphicsBase` '
                'subclass, such as the `Circle` class.',
            value='このインターフェイスは`Circle`クラスなどの'
                  '`GraphicsBase`の各サブクラス上に存在します。'),
        Mapping(
            key='  - The final radius of the animation.',
            value='  - 半径のアニメーションの最終値。'),
        Mapping(
            key='This interface exists in the instances that '
                'have the animation interfaces (such as the '
                '`animation_x`\\, `animation_move`).',
            value='このインターフェイスは`animation_x`や`animation_move`'
                  'などのアニメーション関係のインターフェイスを持つクラスの'
                  'インスタンス上に存在します。'),
        Mapping(
            key='## Interface Notes',
            value='## インターフェイスの特記事項'),
        Mapping(
            key='**[Interface summary]** Reverse all running animations.<hr>',
            value='**[インターフェイス概要]** 動いている全ての'
                  'アニメーションを反転（逆再生）します。<hr>'),
        Mapping(
            key='**[Interface summary]** Set the rotation around the center '
                'animation setting.<hr>',
            value='**[インターフェイス概要]** 中央座標を使用した'
                  '回転のアニメーションの設定を行います。<hr>'),
        Mapping(
            key='  - The final rotation of the animation.',
            value='  - 回転のアニメーションの回転量の最終値。'),
    ])
