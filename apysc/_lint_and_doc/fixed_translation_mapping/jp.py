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
            value='Graphics クラス'),
        Mapping(
            key='Graphics begin_fill interface',
            value='Graphics クラス begin_fill （塗り設定）の'
                  'インターフェイス'),
        Mapping(
            key='Graphics line_style interface',
            value='Graphics クラス line_style （線設定）の'
                  'インターフェイス'),
        Mapping(
            key='Graphics draw_rect interface',
            value='Graphics クラス draw_rect （四角描画）の'
                  'インターフェイス'),
        Mapping(
            key='Graphics draw_circle interface',
            value='Graphics クラス draw_circle （円描画）の'
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
            value='## 基本的な使い方'),
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
            key='<details>\n<summary>Display the code block:</summary>',
            value='<details>\n<summary>コードブロックを表示:</summary>'),
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
        Mapping(
            key='**[Interface summary]** Set the rotation around '
                'the given point animation setting.<hr>',
            value='**[インターフェイス概要]** 指定された座標を'
                  '基準とした回転のアニメーションを設定します。<hr>'),
        Mapping(
            key='  - X-coordinate.',
            value='  - X座標。'),
        Mapping(
            key='  - Y-coordinate.',
            value='  - Y座標。'),
        Mapping(
            key='## What interfaces are these?',
            value='## 各インターフェイスの概要'),
        Mapping(
            key='**[Interface summary]** Set the scale-x from '
                'the center point animation setting.<hr>',
            value='**[インターフェイス概要]** 中央座標を基準とした'
                  'X軸の拡縮アニメーションを設定します。<hr>'),
        Mapping(
            key='  - The final scale-x of the animation.',
            value='  - X軸の拡縮のアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Set the scale-y from '
                'the center point animation setting.<hr>',
            value='**[インターフェイス概要]** 中央座標を基準とした'
                  'Y軸の拡縮アニメーションを設定します。<hr>'),
        Mapping(
            key='  - The final scale-y of the animation.',
            value='  - Y軸の拡縮のアニメーションの最終値。'),
        Mapping(
            key='This interface exists on a `GraphicsBase` '
                'subclass, such as the `Rectangle` class.',
            value='このインターフェイスは`Rectangle`などの'
                  '`GraphicsBase`の各サブクラス上に存在します。'),
        Mapping(
            key='**[Interface summary]** Set the skew-x animation '
                'setting.<hr>',
            value='**[インターフェイス概要]** X軸の傾きのアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='  - The final skew-x of the animation.',
            value='  - X軸の傾きのアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Get an animation elapsed '
                'millisecond.<hr>',
            value='**[インターフェイス概要]** アニメーションの'
                  '経過時間のミリ秒を取得します。<hr>'),
        Mapping(
            key='**[Interface summary]** Get an animation elapsed '
                'millisecond.<hr>',
            value='**[インターフェイス概要]** アニメーションの'
                  '経過時間のミリ秒を取得します。<hr>'),
        Mapping(
            key='  - An animation elapsed millisecond.',
            value='  - アニメーションの経過時間のミリ秒。'),
        Mapping(
            key='These interfaces exist on some `DisplayObject` '
                'instances, such as the `Rectangle` class.',
            value='これらの各インターフェイスは`Rectangle`クラスなどの'
                  '`DisplayObject`の各サブクラス上に存在します。'),
        Mapping(
            key='## Notes for the Ellipse instance',
            value='## Ellipse のインスタンスにおける特記事項'),
        Mapping(
            key='**[Interface summary]** Set the width animation '
                'setting.<hr>',
            value='**[インターフェイス概要]** 幅のアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='**[Interface summary]** Set the height '
                'animation setting.<hr>',
            value='**[インターフェイス概要]** 高さのアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='  - The final width of the animation.',
            value='  - 幅のアニメーションの最終値。'),
        Mapping(
            key='  - The final height of the animation.',
            value='  - 高さのアニメーションの最終値。'),
        Mapping(
            key='## Notes for the Circle and Ellipse classes',
            value='## Circle と Ellipse の各クラスの特記事項'),
        Mapping(
            key='**[Interface summary]** Set the x-coordinate '
                'animation setting.<hr>',
            value='**[インターフェイス概要]** X座標のアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='**[Interface summary]** Set the y-coordinate '
                'animation setting.<hr>',
            value='**[インターフェイス概要]** Y座標のアニメーションを'
                  '設定します。<hr>'),
        Mapping(
            key='  - Any value to append.',
            value='  - 追加対象の任意の値。'),
        Mapping(
            key='  - Other array-like values to concatenate.',
            value='  - 連結対象となる他の配列の（もしくはそれに近しい）値。'),
        Mapping(
            key='  - Any value to search.',
            value='  - 検索対象の任意の値。'),
        Mapping(
            key='  - Index to append value.',
            value='  - 値を追加するインデックス。'),
        Mapping(
            key='  - Separator string.',
            value='  - 区切り文字。'),
        Mapping(
            key='  - Joined string.',
            value='  - 連結された文字列。'),
        Mapping(
            key='  - Removed value.',
            value='  - 取り除かれた値。'),
        Mapping(
            key='  - Value to remove.',
            value='  - 取り除く対象の値。'),
        Mapping(
            key='  - Index to remove value.',
            value='  - 取り除く値のインデックス。'),
        Mapping(
            key='Array class sort interface',
            value='Array クラスの sort インターフェイス'),
        Mapping(
            key='An original array is not modified.',
            value='元々の配列の値は変更されません。'),
        Mapping(
            key='  - Slicing start index.',
            value='  - スライス範囲の開始インデックス。'),
        Mapping(
            key='  - Sliced array.',
            value='  - スライスされた配列。'),
        Mapping(
            key='Array class reverse interface',
            value='Array クラスの reverse インターフェイス'),
        Mapping(
            key='Before reading on, maybe it is helpful to '
                'read the following page:',
            value='事前に以下のページを確認しておくと読み進める上で'
                  '役に立つかもしれません:'),
        Mapping(
            key='Why the apysc library doesn\\\'t use the Python '
                'built-in data type',
            value='なぜapyscではPythonのビルトインのデータの'
                  '型を使用していないのか'),
        Mapping(
            key='Why the apysc library does not use the Python '
                'built-in data type',
            value='なぜapyscではPythonのビルトインのデータの'
                  '型を使用していないのか'),
        Mapping(
            key='## Constructor method',
            value='## コンストラクタメソッド'),
        Mapping(
            key='## Generic type annotation',
            value='## ジェネリックの型アノテーション'),
        Mapping(
            key='Funcdamental data classes common value interface',
            value='基本的なデータクラスの共通の value インターフェイス'),
        Mapping(
            key='Array class append and push interfaces',
            value='Array クラスの append と push のインターフェイス'),
        Mapping(
            key='Array class extend and concat interfaces',
            value='Array クラスの extend と concat のインターフェイス'),
        Mapping(
            key='Array class insert and insert_at interfaces',
            value='Array クラスの insert と insert_at のインターフェイス'),
        Mapping(
            key='Array class pop interface',
            value='Array クラスの pop インターフェイス'),
        Mapping(
            key='Array class remove and remove_at interfaces',
            value='Array クラスの remove と remove_at のインターフェイス'),
        Mapping(
            key='Array class slice interface',
            value='Array クラスの slice インターフェイス'),
        Mapping(
            key='Array class length interface',
            value='Array クラスの length (配列の長さ取得) のインターフェイス'),
        Mapping(
            key='Array class join interface',
            value='Array クラスの join (値の連結文字列生成) のインターフェイス'),
        Mapping(
            key='Array class index_of interface',
            value='Array クラスの index_of (値のインデックス取得) のインターフェイス'),
        Mapping(
            key='Array class comparison interfaces',
            value='Array クラスの比較の各インターフェイス'),
        Mapping(
            key='Array class comparison interfaces document',
            value='Array クラスの比較の各インターフェイス'),
        Mapping(
            key='## Array class constructor API',
            value='## Array クラスのコンストラクタのAPI'),
        Mapping(
            key='  - Initial array value.',
            value='  - 配列の初期値。'),
        Mapping(
            key='## value property API',
            value='## value 属性のAPI'),
        Mapping(
            key='  - Current array value.',
            value='  - 現在の配列の値。'),
        Mapping(
            key='apysc fundamental data classes value interface',
            value='apyscの基本的なデータクラスの value インターフェイス'),
        Mapping(
            key='JavaScript assertion interface basic behavior',
            value='JavaScriptの各アサーションのインターフェイスの基本的な挙動'),
        Mapping(
            key='## Notes for the assert_equal and assert_not_equal '
                'interfaces',
            value='## assert_equal と assert_not_equal の各インターフェイスに'
                  'おける特記事項'),
        Mapping(
            key='  - Left-side value to compare.',
            value='  - 比較用の左辺の値。'),
        Mapping(
            key='  - Left-side value to compare.',
            value='  - 比較用の左辺の値。'),
        Mapping(
            key='  - Right-side value to compare.',
            value='  - 比較用の右辺の値。'),
        Mapping(
            key='  - Message to display when assertion failed.',
            value='  - チェックに失敗した際に表示するメッセージ。'),
        Mapping(
            key='  - Target value to check.',
            value='  - チェック対象の値。'),
        Mapping(
            key='  - Target custom event type.',
            value='  - 対象の独自のイベントの種別値としての文字列。'),
        Mapping(
            key='  - Callable that this instance calls when its '
                'event\'s dispatching.',
            value='  - 対象のイベントが発生（発火）される時に実行される'
                  'ハンドラ。'),
        Mapping(
            key='  - Target custom event type.',
            value='  - 対象の独自のイベントの種別値としての文字列。'),
        Mapping(
            key='  - Event instance.',
            value='  - イベントのインスタンス。'),
        Mapping(
            key='  - Optional arguments dictionary to be passed '
                'to a handler.',
            value='  - ハンドラに渡される省略が可能な追加のパラメーター'
                  'としての辞書。'),
        Mapping(
            key='  - Handler\'s name.',
            value='  - ハンドラ名。'),
        Mapping(
            key='If class',
            value='If クラス'),
        Mapping(
            key='Elif class',
            value='Elif クラス'),
        Mapping(
            key='Else class',
            value='Else クラス'),
        Mapping(
            key='The following page describes basic mouse event interfaces.',
            value='以下のページでは基本的なマウスイベントの'
                  'インターフェイスについて説明しています。'),
        Mapping(
            key='Basic mouse event interfaces',
            value='基本的なマウスイベントの各インターフェイス'),
        Mapping(
            key='  - Unbinding target Callable.',
            value='  - イベント設定を取り除く対象の関数やメソッドなど。'),
        Mapping(
            key='  - Child instance to check.',
            value='  - チェック対象の子のインスタンス。'),
        Mapping(
            key='The following page describes the basic mouse '
                'event interfaces.',
            value='以下のページでは基本的なマウスイベントの'
                  '各インターフェイスについて説明しています。'),
        Mapping(
            key='  - Target key.',
            value='  - 対象のキー。'),
        Mapping(
            key='  - Any default value.',
            value='  - 任意のデフォルト値の値。'),
        Mapping(
            key='## Note for the len function',
            value='## len関数における特記事項'),
        Mapping(
            key='The Python built-in `len` function is not '
                'supported and raises an exception:',
            value='Pythonビルトインの`len`関数はサポートされて'
                  'おらずエラーとなります:'),
        Mapping(
            key='## Value setter interface',
            value='## 値のsetterのインターフェイス'),
        Mapping(
            key='## Value getter interface',
            value='## 値のgetterのインターフェイス'),
        Mapping(
            key='## Notes of the getter interface',
            value='## getterのインターフェイスの特記事項'),
        Mapping(
            key='## Value deletion interface',
            value='## 値の削除のインターフェイス'),
        Mapping(
            key='  - Initial dictionary value.',
            value='  - 辞書の初期値。'),
        Mapping(
            key='Dictionary class generic type settings document',
            value='Dictionary クラスのジェネリックの型設定'),
        Mapping(
            key='## value attribute API',
            value='## value 属性のAPI'),
        Mapping(
            key='  - Current dict value.',
            value='  - 現在の辞書の値。'),
        Mapping(
            key='## What apysc can do in its properties',
            value='## それらの属性でapyscができること'),
        Mapping(
            key='For more details, please see the following:',
            value='詳細については以下をご確認ください:'),
        Mapping(
            key='DisplayObject class x and y interfaces',
            value='DisplayObject クラスの x と y インターフェイス'),
        Mapping(
            key='## x and y properties',
            value='## x と y 属性'),
        Mapping(
            key='## visible property',
            value='## visible 属性'),
        Mapping(
            key='DisplayObject class visible interface',
            value='DisplayObject クラスの visible (表示・非表示) の'
            'インターフェイス'),
        Mapping(
            key='## rotation interfaces',
            value='## 回転の各インターフェイス'),
        Mapping(
            key='GraphicsBase class rotation_around_center interface',
            value='GraphicsBase クラスの rotation_around_center '
                  '(中央座標基準の回転) インターフェイス'),
        Mapping(
            key='GraphicsBase class rotation_around_point interfaces',
            value='GraphicsBase クラスの rotation_around_point '
                  '(指定座標基準の回転) の各インターフェイス'),
        Mapping(
            key='## scale interfaces',
            value='## 拡縮の各インターフェイス'),
        Mapping(
            key='GraphicsBase class scale_from_center interfaces',
            value='GraphicsBase クラスの scale_from_center (中央座標基準の拡縮) '
                  'の各インターフェイス'),
        Mapping(
            key='GraphicsBase class scale_from_point interfaces',
            value='GraphicsBase クラスの scale_from_point (指定座標基準の拡縮) '
                  'の各インターフェイス'),
        Mapping(
            key='## flip properties',
            value='## 反転の各属性'),
        Mapping(
            key='## GraphicsBase class flip_x and flip_y interfaces',
            value='## GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) '
                  'のインターフェイス'),
        Mapping(
            key='GraphicsBase class flip_x and flip_y interfaces',
            value='GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) '
                  'のインターフェイス'),
        Mapping(
            key='## skew properties',
            value='## 歪みの各属性'),
        Mapping(
            key='## skew properties',
            value='## 歪みの各属性'),
        Mapping(
            key='GraphicsBase class skew_x and skew_y interfaces',
            value='GraphicsBase クラスの skew_x (X軸の歪み) と skew_y (Y軸の歪み) '
                  'のインターフェイス'),
        Mapping(
            key='DisplayObject class',
            value='DisplayObject クラス'),
        Mapping(
            key='  - CSS name (e.g., \'display\').',
            value='  - CSS名（例 : \'display\'）。'),
        Mapping(
            key='For more details, please see the following pages:',
            value='詳細については以下の各ページをご確認ください:'),
        Mapping(
            key='click interface',
            value='click インターフェイス'),
        Mapping(
            key='mousedown and mouseup interfaces',
            value='mousedown と mouseup のインターフェイス'),
        Mapping(
            key='mouseover and mouseout interfaces',
            value='mouseover と mouseout インターフェイス'),
        Mapping(
            key='mousemove interface',
            value='mousemove インターフェイス'),
        Mapping(
            key='- ValueError: If a parent is None (there is no parent).',
            value='- ValueError: もしも親のインスタンスがNoneの'
                  '場合（親の無い状態の場合）。'),
        Mapping(
            key='## visible property API',
            value='## visible 属性のAPI'),
        Mapping(
            key='## Augmented assignment',
            value='## 累算代入演算'),
        Mapping(
            key='## x property API',
            value='## x属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a x-coordinate.<hr>',
            value='**[インターフェイス概要]** X座標を取得します。<hr>'),
        Mapping(
            key='## y property API',
            value='## y属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a y-coordinate.<hr>',
            value='**[インターフェイス概要]** Y座標を取得します。<hr>'),
        Mapping(
            key='DisplayObject class mouse event binding interfaces',
            value='DisplayObject クラスのマウスイベント設定の各インターフェイス'),
        Mapping(
            key='## Requirements',
            value='## 必要とされるインストールなどの対応'),
        Mapping(
            key='  - Boolean value whether minify a HTML or not. '
                'False setting is useful when debugging.',
            value='  - HTMLを最小化（minify）するかどうかの真偽値。'
                  'Falseの設定はデバッグ時などに役に立つことがあります。'),
        Mapping(
            key='For more information, please see:',
            value='詳細は以下をご確認ください:'),
        Mapping(
            key='## Notes',
            value='## 特記事項'),
        Mapping(
            key='  - The output HTML file name.',
            value='  - 出力されるHTMLのファイル名。'),
        Mapping(
            key='Graphics class draw_rect interface',
            value='Graphics クラスの draw_rect (四角の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_round_rect interface',
            value='Graphics クラスの draw_round_rect (角丸の四角の描画)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class draw_circle interface',
            value='Graphics クラスの draw_circle (円の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_round_rect interface',
            value='Graphics クラスの draw_round_rect (楕円の描画)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class move_to and line_to interfaces',
            value='Graphics クラスの move_to (線の描画位置の変更)と'
                  ' line_to (指定座標への線の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_line interface',
            value='Graphics クラスの draw_line (線の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_dotted_line interface',
            value='Graphics クラスの draw_dotted_line (点線の描画)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class draw_dashed_line interface',
            value='Graphics クラスの draw_dashed_line (破線の描画)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class draw_round_dotted_line interface',
            value='Graphics クラスの draw_round_dotted_line (点線(丸)の'
                  '描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_dash_dotted_line interface',
            value='Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)'
                  'のインターフェイス'),
        Mapping(
            key='Graphics class draw_polygon interface',
            value='Graphics クラスの draw_polygon (多角形描画)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class fill_color interface',
            value='Graphics クラスの fill_color (塗り設定)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class fill_alpha interface',
            value='Graphics クラスの fill_alpha (塗りの透明度設定)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class line_color interface',
            value='Graphics クラスの line_color (線の色設定)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class line_alpha interface',
            value='Graphics クラスの line_color (線の透明度設定)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class line_thickness interface',
            value='Graphics クラスの line_color (線幅設定)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class line_dot_setting interface',
            value='Graphics クラスの line_dot_setting (点線設定)'
                  'のインターフェイス'),
        Mapping(
            key='Graphics class line_dash_setting interface',
            value='Graphics クラスの line_dash_setting (破線設定)'
                  'のインターフェイス'),
        Mapping(
            key='Graphics class line_round_dot_setting interface',
            value='Graphics クラスの line_round_dot_setting (点線(丸)設定)'
                  'のインターフェイス'),
        Mapping(
            key='Graphics class line_dash_dot_setting interface',
            value='Graphics クラスの line_dash_dot_setting (一点'
                  '鎖線設定)のインターフェイス'),
        Mapping(
            key='For more details, please see:',
            value='詳細は以下をご確認ください:'),
        Mapping(
            key='Graphics class begin_fill interface',
            value='Graphics クラスの begin_fill (塗りの設定)の'
                  'インターフェイス'),
        Mapping(
            key='Graphics class line_style interface',
            value='Graphics クラスの line_style (線のスタイル設定)'
                  'のインターフェイス'),
        Mapping(
            key='Graphics class draw_ellipse interface',
            value='Graphics クラスの draw_ellipse (楕円描画) の'
                  'インターフェイス'),
        Mapping(
            key='Each branch instruction class\\\'s scope variables '
                'reverting setting',
            value='分岐条件の各クラスのスコープ内変数の復元設定'),
        Mapping(
            key='  - Boolean value to be used for judgment.',
            value='  - 判定に使われるBooleanの真偽値。'),
        Mapping(
            key='  - Current scope\'s global variables. Set '
                'globals() value to this argument. This setting '
                'works the same way as the locals_ argument.',
            value='  - 現在のスコープの各グローバル変数。設定する'
                  '場合にはglobal()関数の値をこの引数に指定して'
                  'ください。この設定はlocals_引数と同じように'
                  '動作します。'),
        Mapping(
            key='Timer class delay setting',
            value='Timer クラスの delay 設定'),
        Mapping(
            key='  - Child\'s index (start from 0).',
            value='  - 対象の子のインデックス（0からスタートします）。'),
        Mapping(
            key='  - Target index child instance.',
            value='  - 対象の子のインスタンス。'),
        Mapping(
            key='**[Interface summary]** Get a rotation value '
                'around the center of this instance.<hr>',
            value='**[インターフェイス概要]** インスタンスの中央座標を'
                  '基準とした回転量を取得します。<hr>'),
        Mapping(
            key='  - Rotation value around the center of this instance.',
            value='  - このインスタンスの中央座標を基準とした回転量。'),
        Mapping(
            key='  - Rotation value around the given coordinates.',
            value='  - 指定された座標基準による回転量。'),
        Mapping(
            key='## set_rotation_around_point API',
            value='## set_rotation_around_point API'),
        Mapping(
            key='## get_rotation_around_point API',
            value='## get_rotation_around_point API'),
        Mapping(
            key='  - Rotation value to set.',
            value='  - 設定する回転量。'),
        Mapping(
            key='**[Interface summary]** Update a rotation value '
                'around the given coordinates.<hr>',
            value='**[インターフェイス概要]** 指定された座標基準の回転量を'
                  '更新します。<hr>'),
        Mapping(
            key='## scale_x_from_center property API',
            value='## scale_x_from_center 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a scale-x value '
                'from the center of this instance.<hr>',
            value='**[インターフェイス概要]** インスタンスの中央座標を'
                  '基準とした水平方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-x value from the center of this instance.',
            value='  - インスタンスの中央座標を基準とした水平方向の拡縮の値。'),
        Mapping(
            key='## scale_y_from_center property API',
            value='## scale_y_from_center 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a scale-y value '
                'from the center of this instance.<hr>',
            value='**[インターフェイス概要]** インスタンスの中央座標を'
                  '基準とした垂直方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-y value from the center of this instance.',
            value='  - インスタンスの中央座標を基準とした垂直方向の拡縮の値。'),
        Mapping(
            key='## get_scale_x_from_point API',
            value='## get_scale_x_from_point API'),
        Mapping(
            key='**[Interface summary]** Get a scale-x value from the given '
                'x-coordinate.<hr>',
            value='**[インターフェイス概要]** 指定されたX座標を'
                  '基準として水平方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-x value from the given x-coordinate.',
            value='  - 指定されたX座標を基準とした水平方向の拡縮値。'),
        Mapping(
            key='## set_scale_x_from_point API',
            value='## set_scale_x_from_point API'),
        Mapping(
            key='**[Interface summary]** Update a scale-x '
                'value from the given '
                'x-coordinate.<hr>',
            value='**[インターフェイス概要]** 指定されたX座病を基準'
                  'とした水平方向の拡縮値を更新します。<hr>'),
        Mapping(
            key='## get_scale_y_from_point API',
            value='## get_scale_y_from_point API'),
        Mapping(
            key='**[Interface summary]** Get a scale-y value '
                'from the given y-coordinate.<hr>',
            value='**[インターフェイス概要]** 指定されたY座標を基準'
                  'とした垂直方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-y value from the given y-coordinate.',
            value='  - 指定されたY座標を基準とした垂直方向の拡縮値。'),
        Mapping(
            key='## set_scale_y_from_point API',
            value='## set_scale_y_from_point API'),
        Mapping(
            key='**[Interface summary]** Update a scale-y value '
                'from the given y-coordinate.<hr>',
            value='**[インターフェイス概要]** 指定されたY座標を基準とした'
                  '垂直方向の拡縮値を更新します。<hr>'),
        Mapping(
            key='  - Scale-y value to set.',
            value='  - 設定すの垂直方向の拡縮値。'),
        Mapping(
            key='  - Scale-x value to set.',
            value='  - 設定する水平方向の拡縮値。'),
        Mapping(
            key='## skew_x property API',
            value='## skew_x property API'),
        Mapping(
            key='**[Interface summary]** Get a current skew x value of '
                'the instance.<hr>',
            value='**[インターフェイス概要]** インスタンスの現在のX軸の'
                  '歪みの値を取得します。<hr>'),
        Mapping(
            key='  - Current skew x value of this instance.',
            value='  - インスタンスの現在のX軸の歪みの値。'),
        Mapping(
            key='## skew_y property API',
            value='## skew_y property API'),
        Mapping(
            key='**[Interface summary]** Get a current skew y '
                'value of the instance.<hr>',
            value='**[インターフェイス概要]** インスタンスの現在のY軸の'
                  '歪みの値を取得します。<hr>'),
        Mapping(
            key='  - Current skew y value of the instance.',
            value='  - インスタンスの現在のY軸の歪みの値。'),
        Mapping(
            key='## Fill color setting',
            value='## 塗りの色の設定'),
        Mapping(
            key='## Fill color alpha (opacity) setting',
            value='## 塗りの色の透明度の設定'),
        Mapping(
            key='## begin_fill API',
            value='## begin_fill API'),
        Mapping(
            key='**[Interface summary]** Set single color value for '
                'fill.<hr>',
            value='**[インターフェイス概要]** 塗りのための単一の色の設定を行います。<hr>'),
        Mapping(
            key='**[Interface summary]** Set single color value for '
                'fill.<hr>',
            value='**[インターフェイス概要]** 塗りのための単一の色の設定を行います。<hr>'),
        Mapping(
            key='  - Hexadecimal color string. e.g., \'#00aaff\'',
            value='  - \'#00aaff\'などの16進数の色の文字列。'),
        Mapping(
            key='  - Color opacity (0.0 to 1.0).',
            value='  - 塗りの透明度（0.0～1.0）。'),
        Mapping(
            key='## fill_color property API',
            value='## fill_color 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current fill color.<hr>',
            value='**[インターフェイス概要]** 現在の塗りの色を取得します。<hr>'),
        Mapping(
            key='  - Current fill color (hexadecimal string, e.g., '
                '\'#00aaff\'). If not be set, this interface returns '
                'a blank string.',
            value='  - 現在の塗りの色（`\'#00aaff\'`などの16進数の文字列）。'
                  'もしも設定されていない場合空文字が返却されます。'),
        Mapping(
            key='## fill_alpha property API',
            value='## fill_alpha 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current fill color opacity.<hr>',
            value='**[インターフェイス概要]** 現在の塗りの透明度を取得します。<hr>'),
        Mapping(
            key='  - Current fill color opacity (0.0 to 1.0). If '
                'not be set, 1.0 will be returned.',
            value='  - 現在の塗りの透明度（0.0～1.0）。もし設定されていない'
                  '場合1.0の値が返却されます。'),
        Mapping(
            key='## Return value',
            value='## 返却値'),
        Mapping(
            key='## draw_circle API',
            value='## draw_circle API'),
        Mapping(
            key='**[Interface summary]** Draw a circle vector graphics.<hr>',
            value='**[インターフェイス概要]** 円のベクターグラフィックスを'
                  '描画します。<hr>'),
        Mapping(
            key='  - X-coordinate of the circle center.',
            value='  - 円の中心のX座標。'),
        Mapping(
            key='  - Y-coordinate of the circle center.',
            value='  - 円の中心のY座標。'),
        Mapping(
            key='  - Circle radius.',
            value='  - 円の半径。'),
        Mapping(
            key='  - Created circle graphics instance.',
            value='  - 生成された円のグラフィックスのインスタンス。'),
        Mapping(
            key='## draw_dash_dotted_line API',
            value='## draw_dash_dotted_line API'),
        Mapping(
            key='**[Interface summary]** Draw a dash-dotted (1-dot chain) '
                'line vector graphics.<hr>',
            value='**[インターフェイス概要]** 一点鎖線のベクターグラフィックスの'
                  '線を描画します。<hr>'),
        Mapping(
            key='  - Line start x-coordinate.',
            value='  - 線の開始位置のX座標。'),
        Mapping(
            key='  - Line start y-coordinate.',
            value='  - 線の開始位置のY座標。'),
        Mapping(
            key='  - Line end x-coordinate.',
            value='  - 線の終了位置のX座標。'),
        Mapping(
            key='  - Line end y-coordinate.',
            value='  - 線の終了位置のY座標。'),
        Mapping(
            key='  - Line end y-coordinate.',
            value='  - 線の終了位置のY座標。'),
        Mapping(
            key='  - Dot size.',
            value='  - ドットのサイズ。'),
        Mapping(
            key='  - Dash size.',
            value='  - 破線部分のサイズ。'),
        Mapping(
            key='  - Blank space size between dots and dashes.',
            value='  - ドット（点線）や破線間の空白スペースのサイズ。'),
        Mapping(
            key='  - Created line graphics instance.',
            value='  - 生成された線のグラフィックスのインスタンス。'),
        Mapping(
            key='## draw_dashed_line API',
            value='## draw_dashed_line API'),
        Mapping(
            key='**[Interface summary]** Draw a dashed line vector '
                'graphics.<hr>',
            value='**[インターフェイス概要]** 破線のベクターグラフィックスを'
                  '描画します。<hr>'),
        Mapping(
            key='  - Blank space size between dashes.',
            value='  - 破線間の空白スペースのサイズ。'),
        Mapping(
            key=' ・This interface ignores line settings, like '
                'the `LineDotSetting`, except `LineDashSetting`.<hr>',
            value=' ・このインターフェイスは`LineDashSetting`'
                  'を除いた`LineDotSetting`などの線のスタイル設定を無視します。<hr>'),
        Mapping(
            key='## draw_dotted_line API',
            value='## draw_dotted_line API'),
        Mapping(
            key='**[Interface summary]** Draw a dotted line vector '
                'graphics.<hr>',
            value='**[インターフェイス概要]** 点線のベクター'
                  'グラフィックスを描画します。<hr>'),
        Mapping(
            key=' ・This interface ignores line settings, like the '
                '`LineDashSetting`, except `LineDotSetting`.<hr>',
            value=' ・このインターフェイスは`LineDotSetting`を'
                  '除いた`LineDashSetting`などの線のスタイル設定を無視します。<hr>'),
        Mapping(
            key='## draw_ellipse API',
            value='## draw_ellipse API'),
        Mapping(
            key='**[Interface summary]** Draw an ellipse vector graphic.<hr>',
            value='**[インターフェイス概要]** 楕円のベクターグラフィックスを'
                  '描画します。<hr>'),
        Mapping(
            key='  - X-coordinate of the ellipse center.',
            value='  - 楕円の中央のX座標。'),
        Mapping(
            key='  - Y-coordinate of the ellipse center.',
            value='  - 楕円の中央のY座標。'),
        Mapping(
            key='  - Ellipse width.',
            value='  - 楕円の幅。'),
        Mapping(
            key='  - Ellipse height.',
            value='  - 楕円の高さ。'),
        Mapping(
            key='  - Created ellipse graphics instance.',
            value='  - 作成された楕円のグラフィックスのインスタンス。'),
        Mapping(
            key='## Ignored line style settings',
            value='## 無視される線のスタイル設定'),
        Mapping(
            key='## Line class instance',
            value='## Line クラスのインスタンス'),
        Mapping(
            key='## draw_line API',
            value='## draw_line API'),
        Mapping(
            key='**[Interface summary]** Draw a normal line vector '
                'graphic.<hr>',
            value='**[インターフェイス概要]** 通常の直線のベクター'
                  'グラフィックスを描画します。<hr>'),
        Mapping(
            key=' ・This interface ignores line settings, '
                'like the `LineDotSetting`, `LineDashSetting`.<hr>',
            value=' ・このインターフェイスは`LineDotSetting`や'
                  '`LineDashSetting`などの設定を無視します。<hr>'),
        Mapping(
            key='## draw_polygon API',
            value='## draw_polygon API'),
        Mapping(
            key='**[Interface summary]** Draw a polygon vector '
                'graphic. This interface is similar to the '
                'Polyline class (created by `move_to` or `line_to`). '
                'But unlike that, this interface connects the '
                'last point and the start point.<hr>',
            value='**[インターフェイス概要]** 多角形のベクター'
                  'グラフィックスを描画します。このインターフェイスはPolyline'
                  'クラス（`move_to`や`line_to`のインターフェイスで作成されます）'
                  'に似ていますが、このインターフェイスは始点と終点が連結される'
                  'という違いがあります。<hr>'),
        Mapping(
            key='  - Polygon vertex points.',
            value='  - 多角形の頂点の各座標。'),
        Mapping(
            key='  - Created polygon graphics instance.',
            value='  - 作成された多角形のグラフィックスのインスタンス。'),
        Mapping(
            key='## draw_rect API',
            value='## draw_rect API'),
        Mapping(
            key='**[Interface summary]** Draw a rectangle vector '
                'graphics.<hr>',
            value='**[インターフェイス概要]** ベクターグラフィックスの四角を'
                  '描画します。<hr>'),
        Mapping(
            key='  - X position to start drawing.',
            value='  - 描画を開始する位置のX座標。'),
        Mapping(
            key='  - Y position to start drawing.',
            value='  - 描画を開始する位置のY座標。'),
        Mapping(
            key='  - Rectangle width.',
            value='  - 四角の幅。'),
        Mapping(
            key='  - Rectangle height.',
            value='  - 四角の高さ。'),
        Mapping(
            key='  - Created rectangle.',
            value='  - 生成された四角。'),
        Mapping(
            key='## draw_round_dotted_line API',
            value='## draw_round_dotted_line API'),
        Mapping(
            key='**[Interface summary]** Draw a round-dotted '
                'line vector graphics.<hr>',
            value='**[インターフェイス概要]** 丸ドットの直線の'
                  'ベクターグラフィックスを描画します。<hr>'),
        Mapping(
            key='  - Dot round size.',
            value='  - 丸ドットのサイズ。'),
        Mapping(
            key='  - Blank space size between dots.',
            value='  - ドット間の空白のスペースのサイズ。'),
        Mapping(
            key='This interface ignores line settings, like '
                'the `LineDotSetting`, except `LineRoundDotSetting`.<hr>',
            value='このインターフェイスは`LineRoundDotSetting`を除いて'
                  '`LineDotSetting`などの設定を無視します。<hr>'),
        Mapping(
            key='## draw_round_rect API',
            value='## draw_round_rect API'),
        Mapping(
            key='**[Interface summary]** Draw a rounded rectangle '
                'vector graphics.<hr>',
            value='**[インターフェイス概要]** 角丸四角のベクターグラフィックスを'
                  '描画します。<hr>'),
        Mapping(
            key='  - X-coordinate to start drawing.',
            value='  - 描画を開始するX座標。'),
        Mapping(
            key='  - Y-coordinate to start drawing.',
            value='  - 描画を開始するY座標。'),
        Mapping(
            key='  - Ellipse width of the rectangle corner.',
            value='  - 四角の角丸の幅。'),
        Mapping(
            key='  - Ellipse height of the rectangle corner.',
            value='  - 四角の角丸の高さ。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s fill '
                'opacity.<hr>',
            value='**[インターフェイス概要]** このインスタンスの塗りの透明度を'
                  '取得します。<hr>'),
        Mapping(
            key='  - Current fill opacity (0.0 to 1.0).',
            value='  - 現在の塗りの透明度（0.0～1.0）。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s fill '
                'color.<hr>',
            value='**[インターフェイス概要]** インスタンスの塗りの色を'
                  '取得します。<hr>'),
        Mapping(
            key='The getter or setter interface value becomes '
                '(or requires) the `Number` value (0.0 to 1.0).',
            value='getterとsetterの両方のインターフェイスの値は`Number`'
                  '型の0.0～1.0の範囲の値となります。'),
        Mapping(
            key='## line_alpha property API',
            value='## line_alpha 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line alpha '
                '(opacity).<hr>',
            value='**[インターフェイス概要]** インスタンスの線の'
                  '透明度を取得します。<hr>'),
        Mapping(
            key='  - Current line alpha (opacity. 0.0 to 1.0).',
            value='  - 現在の線の透明度（0.0～1.0）。'),
        Mapping(
            key='The getter or setter interface value becomes '
                '(or requires) the `String` hex color code value.',
            value='getterとsetterのインターフェイスで扱う値は`String`型の'
                  '16進数のカラーコードの文字列となります。'),
        Mapping(
            key='## line_color property API',
            value='## line_color 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line '
                'color.<hr>',
            value='**[インターフェイス概要]** インスタンスの線の色を'
                  '取得します。<hr>'),
        Mapping(
            key='  - Current line color (hexadecimal string, '
                'e.g., \'#00aaff\'). If not be set, this interface '
                'returns a blank string.',
            value='  - \'#00aaff\'などの16進数の線の色。もし設定'
                  'されていない場合はこの空文字となります。'),
        Mapping(
            key='**[Interface summary]** Get current dash dot (1-dot chain) '
                'setting.<hr>',
            value='**[インターフェイス概要]** 現在の一点鎖線のスタイル設定を'
                  '取得します。<hr>'),
        Mapping(
            key='## line_dash_dot_setting API',
            value='## line_dash_dot_setting API'),
        Mapping(
            key='  - Dash dot (1-dot chain) setting.',
            value='  - 一点鎖線の設定。'),
        Mapping(
            key='## line_dash_setting property API',
            value='## line_dash_setting 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line dash '
                'setting.<hr>',
            value='**[インターフェイス概要]** 現在の線の破線のスタイル設定を'
                  '取得します。<hr>'),
        Mapping(
            key='  - Line dash setting.',
            value='  - 線の破線のスタイル設定。'),
        Mapping(
            key='The getter or setter interface value becomes '
                '(or requires) the `LineDotSetting` instance value.',
            value='getterやsetterのインターフェイスの値は`LineDotSetting`'
                  'クラスのインスタンスの値となります。'),
        Mapping(
            key='## line_dot_setting property API',
            value='## line_dot_setting 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s '
                'line dot setting.<hr>',
            value='**[インターフェイス概要]** このインスタンスの線の点線のスタイル'
                  '設定を取得します。<hr>'),
        Mapping(
            key='  - Lien dot setting.',
            value='  - 線の点線のスタイル設定。'),
        Mapping(
            key='The getter or setter interface value becomes '
                '(or requires) the `LineRoundDotSetting` instance value.',
            value='getterやsetterのインターフェイスの値は`interface`クラスの'
                  'インスタンスの値になります。'),
        Mapping(
            key='## line_round_dot_setting property API',
            value='## line_round_dot_setting 属性のAPI'),
        Mapping(
            key='  - Line round dot setting.',
            value='  - 線の丸ドットのスタイル設定。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line round dot '
                'setting.<hr>',
            value='**[インターフェイス]** インスタンスの線の丸ドットの'
                  'スタイル設定を取得します。<hr>'),
        Mapping(
            key='## Line-color setting',
            value='## 線の色の設定'),
        Mapping(
            key='- Six characters, e.g., `#00aaff`.',
            value='- `#00aaff`などの6文字による指定。'),
        Mapping(
            key='- Three characters, e.g., `#0af` (this becomes '
                '`#00aaff`).',
            value='- `#0af`などの3文字による指定（これは`#00aaff`と同じ'
                  '値として扱われます）。'),
        Mapping(
            key='- Single character, e.g., `#5` (this becomes `#000005`).',
            value='- `#5`などの1文字による指定（これは`000005`と同じ値'
                  'として扱われます）。'),
        Mapping(
            key='- Skipped `#` symbol, e.g., `0af` (this becomes '
                '`#00aaff`).',
            value='- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値'
                  'として扱われます）。'),
        Mapping(
            key='- Blank string, e.g., `\'\'` (this clears line color '
                'setting).',
            value='- `\'\'`などの空文字の指定（これは線の色の削除指定として'
                  '扱われます）。`'),
        Mapping(
            key='## Line thickness setting',
            value='## 線幅の設定'),
        Mapping(
            key='## Line alpha (opacity) setting',
            value='## 線の透明度の設定'),
        Mapping(
            key='## Line cap setting',
            value='## 線端の設定'),
        Mapping(
            key='There are three `LineCaps` options, as follows:',
            value='以下のように`LineCaps`のオプションは3種類存在します:'),
        Mapping(
            key='- BUTT: This is the default value, and it sets no cap.',
            value='- BUTT: デフォルト値であり、端にはなにも設定されません。'),
        Mapping(
            key='- ROUND: This changes the line edge to the rounded one.',
            value='- ROUND: 線の端のスタイルを丸くします。'),
        Mapping(
            key='- SQUARE: This is similar to BUTT, but it increases '
                'the line length by the squared edge.',
            value='- SQUARE: 線の端のスタイルを四角くします。これはBUTTと'
                  '似た表示になりますが、設定される四角の分だけ線が長くなります。'),
        Mapping(
            key='## Line joints setting',
            value='## 線の繋ぎ目の設定'),
        Mapping(
            key='There are three LineJoints enum values, as follows:',
            value='以下のようにLineJointsのenumには3つの値が存在します:'),
        Mapping(
            key='- MITER: This setting sets the style like a picture '
                'frame vertices. This setting is the default style setting.',
            value='- MITER: この設定は頂点が（尖った形での）額縁のような'
                  '形のスタイルが設定されます。この設定がデフォルトのスタイルと'
                  'なります。'),
        Mapping(
            key='- ROUND: This setting sets the rounded vertices style.',
            value='- ROUND: この設定は丸い頂点のスタイルを設定します。'),
        Mapping(
            key='- BEVEL: This setting sets a beveled vertices style.',
            value='- BEVEL: この設定は射角（ベベル）の頂点のスタイルを設定します。'),
        Mapping(
            key='## Line dot setting',
            value='## 線の点線設定'),
        Mapping(
            key='Notes: This setting will be ignored by `draw_line`, '
                '`draw_dotted_line`, `draw_dashed_line`, '
                '`draw_round_dotted_line`, and `draw_dash_dotted_line` '
                'interfaces.',
            value='特記事項: この設定は`draw_line`、`draw_dotted_line`、'
                  '`draw_dashed_line`、`draw_round_dotted_line`、'
                  '`draw_dash_dotted_line`の各インターフェイスで無視されます。'),
        Mapping(
            key='## Line dash setting',
            value='## 線の破線設定'),
        Mapping(
            key='## Line round dot setting',
            value='## 線の丸ドット設定'),
        Mapping(
            key='Notes: Since this setting uses the `cap` setting '
                'internally, this setting ignores the `cap` setting, '
                'increasing the line length by the capsize.',
            value='特記事項: この設定は内部で`cap`設定の値を使用している'
                  'ため、この設定では`cap`引数の設定が無視されます。また、丸の'
                  'サイズに応じた分だけ線の長さが長くなります。'),
        Mapping(
            key='## Line dash-dot setting',
            value='## 線の一点鎖線の設定'),
        Mapping(
            key='## line_style API',
            value='## line_style API'),
        Mapping(
            key='**[Interface summary]** Set line style values.<hr>',
            value='**[インターフェイス概要]** 線のスタイルを設定します。<hr>'),
        Mapping(
            key='  - Line thickness (minimum value is 1).',
            value='  - 線の幅（1以上の値を受け付けます）。'),
        Mapping(
            key='  - Line cap (edge style) setting. The not line-related '
                'graphics (e.g., Rectangle ignores this, conversely used '
                'by Polyline) ignore this setting.',
            value='  - 線の端のスタイル設定。線に関係しないRectangleクラスなどの'
                  'グラフィックスインスタンスはこの設定を無視します。逆に'
                  'Polylineクラスなどの線に関係したインスタンスではこの設定を'
                  '使用します。'),
        Mapping(
            key='  - Line vertices (joints) style setting. The not '
                'polyline-related graphics (e.g., Rectangle ignores '
                'this, conversely used by Polyline) ignore this setting.',
            value='  - 線の頂点（接合部）のスタイル設定。折れ線線に関係しないRectangle'
                  'などのグラフィックスインスタンスはこの設定を無視します。'
                  '逆にPolylineクラスなどの折れ線関係のクラスではこの設定を'
                  '使用します。'),
        Mapping(
            key='  - Dot setting. If this is specified, it makes a '
                'line dotted.',
            value='  - 点線の設定。もしもこの引数が指定された場合、線は点線になります。'),
        Mapping(
            key='  - Dash setting. If this is specified, it makes a '
                'line dashed.',
            value='  - 破線の設定。もしこの引数が指定された場合、線は破線になります。'),
        Mapping(
            key='  - Round dot setting. If this is specified, it makes '
                'a line round dotted. Notes: since this style uses a cap '
                'setting, it overrides cap and line thickness settings. '
                'And it increases the amount of line size. If you want to '
                'adjust to the same width of a normal line when using '
                'move_to and line_to interfaces, add half-round size to '
                'start x-coordinate and subtract from end e-coordinate. '
                'e.g., `this.move_to(x + round_size / 2, y)`, '
                '`this.line_to(x - round_size / 2, y)`',
            value='  - 丸ドットの設定。もしこの引数が指定された場合、線は丸ドット'
                  'になります。特記事項: ごの設定は内部でcapの設定を使用しているため、'
                  'cap（線の端のスタイル設定）と線幅の設定を上書きします。'
                  'また、cap設定を使用している都合、線の長さも長くなります。'
                  'move_toやline_toなどのインターフェイスを使った通常の線の'
                  '長さと合わせたい場合には丸の半分のサイズを線の開始位置のX座標'
                  'へ加算し、さらに丸の半分のサイズを線の終了位置のX座標から減算'
                  'してください（Y座標も同様です）。'
                  '例: `this.move_to(x + round_size / 2, y)`、'
                  '`this.line_to(x - round_size / 2, y)`'),
        Mapping(
            key='  - Dash dot (1-dot chain) setting. If this is '
                'specified, it makes a line 1-dot chained.',
            value='  - 一点鎖線のスタイル設定。もしこの引数が指定された'
                  '場合、線の一点鎖線になります。'),
        Mapping(
            key='**[Interface summary]** Get current line color.<hr>',
            value='**[インターフェイス概要]** 現在の線の色を取得します。<hr>'),
        Mapping(
            key='## line_thickness property API',
            value='## line_thickness 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line thickness.<hr>',
            value='**[インターフェイス概要]** 現在の線の線幅を取得します。<hr>'),
        Mapping(
            key='  - Current line thickness.',
            value='  - 現在の線幅。'),
        Mapping(
            key='**[Interface summary]** Get current line color opacity.<hr>',
            value='**[インターフェイス概要]** 現在の線の透明度を取得します。<hr>'),
        Mapping(
            key='  - Current line opacity (0.0 to 1.0).',
            value='  - 現在の線の透明度（0.0～1.0）。'),
        Mapping(
            key='## line_cap property API',
            value='## line_cap 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line cap '
                '(edge) style setting.<hr>',
            value='**[インターフェイス概要]** 現在の線の端のスタイル設定。<hr>'),
        Mapping(
            key='  - Current line cap (edge) style setting.',
            value='  - 現在の線の端のスタイル設定。'),
        Mapping(
            key='## line_joints property API',
            value='## line_joints 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line joints '
                '(vertices) style setting.<hr>',
            value='**[インターフェイス概要]** 現在の線の接合部（頂点）のスタイル'
                  '設定を取得します。<hr>'),
        Mapping(
            key='  - Current line joints (vertices) style setting.',
            value='  - 現在の線の接合部（頂点）のスタイル設定。'),
        Mapping(
            key='**[Interface summary]** Get current line dot setting.<hr>',
            value='**[インターフェイス概要]** 現在の線の点線設定を取得します。<hr>'),
        Mapping(
            key='  - Current line dot setting.',
            value='  - 現在の点線設定。'),
        Mapping(
            key='  - Current line dash setting.',
            value='  - 現在の破線設定。'),
        Mapping(
            key='  - Current line dash setting.',
            value='  - 現在の破線設定。'),
        Mapping(
            key='**[Interface summary]** Get current line round dot '
                'setting.<hr>',
            value='**[インターフェイス概要]** 現在の線の丸ドットのスタイル設定を'
                  '取得します。<hr>'),
        Mapping(
            key='  - Current line round dot setting.',
            value='  - 現在の線の丸ドットのスタイル設定。'),
        Mapping(
            key='## line_dash_dot_setting property API',
            value='## line_dash_dot_setting 属性のAPI'),
        Mapping(
            key='## line_dash_dot_setting property API',
            value='## line_dash_dot_setting 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line dash dot '
                'setting.<hr>',
            value='**[インターフェイス概要]** 現在の線の一点鎖線のスタイル'
                  '設定を取得します。<hr>'),
        Mapping(
            key='  - Line color opacity (0.0 to 1.0).',
            value='  - 線色の透明度（0.0～1.0）。'),
        Mapping(
            key='  - Line color opacity (0.0 to 1.0).',
            value='  - 線色の透明度（0.0～1.0）。'),
        Mapping(
            key='  - Current line dash dot setting.',
            value='  - 現在の一点鎖線のスタイル設定。'),
        Mapping(
            key='The getter or setter interface value becomes (or requires) '
                'the `Int` value.',
            value='getterもしくはsetterの各インターフェイスの値は`Int`型の値に'
                  'なります。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line '
                'thickness.<hr>',
            value='**[インターフェイス概要]** このインスタンスの線幅を'
                  '取得します。<hr>'),
        Mapping(
            key='## What interfaces are they?',
            value='## 各インターフェイスの概要'),
        Mapping(
            key='If you click the following line, line style will be '
                'updated:',
            value='もし以下の四角をクリックし0た場合、線のスタイルは更新'
                  'されます:'),
        Mapping(
            key='## move_to API',
            value='## move_to API'),
        Mapping(
            key='**[Interface summary]** Move a line position to a '
                'specified point.<hr>',
            value='**[インターフェイス概要]** 指定された座標に線の描画位置を'
                  '移動させます。<hr>'),
        Mapping(
            key='  - X destination point to move.',
            value='  - 移動先となるX座標。'),
        Mapping(
            key='  - Y destination point to move.',
            value='  - 移動先となるY座標。'),
        Mapping(
            key='  - Line graphics instance.',
            value='  - 線のグラフィックスのインスタンス。'),
        Mapping(
            key='  - Line graphics instance.',
            value='  - 線のグラフィックスのインスタンス。'),
        Mapping(
            key='## line_to API',
            value='## line_to API'),
        Mapping(
            key='**[Interface summary]** Draw a line from '
                'previous point to specified point (initial '
                'point is x = 0, y = 0).<hr>',
            value='**[インターフェイス概要]** 直前の位置の座標から'
                  '指定された座標に向けて線を描画します（初期位置は'
                  'x=0, y=0になります）。<hr>'),
        Mapping(
            key='  - X destination point to draw a line.',
            value='  - 線の描画先となる終点のX座標。'),
        Mapping(
            key='  - Y destination point to draw a line.',
            value='  - 線の描画先となる終点のY座標。'),
        Mapping(
            key='## Return values',
            value='## 各返却値について'),
        Mapping(
            key='## If constructor API',
            value='## If クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** A class to append if branch '
                'instruction expression.<hr>',
            value='**[インターフェイス概要]** if文の分岐制御の表現を'
                  '追加するためのクラス。<hr>'),
        Mapping(
            key='  - Current scope\'s local variables. Set locals() '
                'value to this argument. If specified, this '
                'interface reverts all local scope VariableNameInterface '
                'variables (like Int, Sprite) at the end of an `If` '
                'scope. This setting is useful when you don\'t want '
                'to update each variable by implementing the `If` scope.',
            value='  - 現在のスコープの各ローカル変数。指定する場合にはlocals()'
                  '関数の値をごの引数に指定してください。もし指定された場合、'
                  'このインターフェイスは`If`のスコープの終了時に対象の'
                  'VariableNameInterfaceクラスの各ローカル変数のインスタンス'
                  'の値をスコープの開始前の時点に復元します。この設定は`If`の'
                  'スコープ内の処理でPython上の各ローカル変数の値を更新したくない'
                  '場合などに便利なことがあります。'),
        Mapping(
            key='## Project links',
            value='## プロジェクトの関連リンク'),
        Mapping(
            key='- [GitHub](https://github.com/simon-ritchie/apysc)',
            value='- [GitHub](https://github.com/simon-ritchie/apysc)'),
        Mapping(
            key='- [Twitter](https://twitter.com/apysc)',
            value='- [Twitter](https://twitter.com/apysc)'),
        Mapping(
            key='- [PyPI](https://pypi.org/project/apysc/)',
            value='- [PyPI](https://pypi.org/project/apysc/)'),
        Mapping(
            key='What apysc can do in its current implementation',
            value='apyscが現在の実装で出来ることの概要'),
        Mapping(
            key='## Contents',
            value='## コンテンツ'),
        Mapping(
            key='**Quick start guide**',
            value='**クイックスタートガイド**'),
        Mapping(
            key='Quick start guide',
            value='クイックスタートガイド'),
        Mapping(
            key='import conventions',
            value='import の慣習'),
        Mapping(
            key='**Container classes**',
            value='**コンテナーの各クラス**'),
        Mapping(
            key='Stage class',
            value='Stage クラス'),
        Mapping(
            key='Sprite class',
            value='Sprite クラス'),
        Mapping(
            key='**Exporting**',
            value='**出力処理**'),
        Mapping(
            key='save_overall_html interface',
            value='save_overall_html インターフェイス'),
        Mapping(
            key='display_on_jupyter interface',
            value='display_on_jupyter インターフェイス'),
        Mapping(
            key='display_on_google_colaboratory interface',
            value='display_on_google_colaboratory インターフェイス'),
        Mapping(
            key='append_js_expression interface',
            value='append_js_expression インターフェイス'),
        Mapping(
            key='**apysc basic data classes**',
            value='**apyscの基本的な各データクラス**'),
        Mapping(
            key='Int and Number classes',
            value='Int と Number の各クラス'),
        Mapping(
            key='Int and Number classes common arithmetic operations',
            value='Int と Number クラスの共通の計算制御'),
        Mapping(
            key='Int and Number classes common comparison operations',
            value='Int と Number クラスの共通の比較制御'),
        Mapping(
            key='String class',
            value='String クラス'),
        Mapping(
            key='String class comparison operations',
            value='String クラスの比較制御'),
        Mapping(
            key='String class addition and multiplication operations',
            value='String クラスの加算と乗算の制御'),
        Mapping(
            key='Boolean class',
            value='Boolean クラス'),
        Mapping(
            key='Array class',
            value='Array クラス'),
        Mapping(
            key='Dictionary class',
            value='Dictionary クラス'),
        Mapping(
            key='Dictionary class generic type settings',
            value='Dictionary クラスのジェネリックの型設定'),
        Mapping(
            key='Dictionary class get interface',
            value='Dictionary クラスの get インターフェイス'),
        Mapping(
            key='Dictionary class length interface',
            value='Dictionary クラスの length インターフェイス'),
        Mapping(
            key='Point2D class',
            value='Point2D クラス'),
        Mapping(
            key='**DisplayObject and GraphicsBase classes**',
            value='DisplayObject と GraphicsBase の各クラス'),
        Mapping(
            key='DisplayObject and GraphicsBase classes basic '
                'properties abstract',
            value='DisplayObject と GraphicsBase の各クラスの'
                  '基本的な各属性の概要'),
        Mapping(
            key='DisplayObject class get_css and set_css interfaces',
            value='DisplayObject クラスの get_css と set_css '
                  'の各インターフェイス'),
        Mapping(
            key='**Graphics class**',
            value='**Graphics クラス**'),
        Mapping(
            key='Draw interfaces abstract',
            value='描画の各インターフェイスの概要'),
        Mapping(
            key='**Common event interfaces**',
            value='**イベントの共通の各インターフェイス**'),
        Mapping(
            key='About the handler options type',
            value='ハンドラの options パラメーターの型について'),
        Mapping(
            key='Event class prevent_default and stop_propagation interfaces',
            value='Event クラスの prevent_default と stop_propagation '
                  'の各インターフェイス'),
        Mapping(
            key='bind_custom_event and trigger_custom_event interfaces',
            value='bind_custom_event と trigger_custom_event '
                  'の各インターフェイス'),
        Mapping(
            key='**MouseEvent class and mouse event binding**',
            value='**MouseEvent クラスとマウスイベントの設定**'),
        Mapping(
            key='MouseEvent interfaces abstract',
            value='MouseEvent クラスの各インターフェイスの概要'),
        Mapping(
            key='dblclick interface',
            value='dblclick インターフェイス'),
        Mapping(
            key='**Branch instruction**',
            value='**条件分岐の制御**'),
        Mapping(
            key='Each branch instruction class scope variables reverting '
                'setting',
            value='各条件分岐のクラスのスコープ内の変数値の復元設定'),
        Mapping(
            key='Return class',
            value='Return クラス'),
        Mapping(
            key='For loop class',
            value='ループ用の For クラス'),
        Mapping(
            key='Continue class',
            value='Continue クラス'),
        Mapping(
            key='**Loop**',
            value='**ループ**'),
        Mapping(
            key='**Timer**',
            value='**タイマー**'),
        Mapping(
            key='Timer class',
            value='Timer クラス'),
        Mapping(
            key='TimerEvent class',
            value='TimerEvent クラス'),
        Mapping(
            key='Timer class delay setting',
            value='Timer クラスの delay 設定'),
        Mapping(
            key='FPS enum',
            value='FPS の enum'),
        Mapping(
            key='Timer class repeat_count setting',
            value='Timer クラスの repeat_count 設定'),
        Mapping(
            key='Timer class start and stop interfaces',
            value='Timer クラスの start と stop の各インターフェイス'),
        Mapping(
            key='Timer class timer_complete interface',
            value='Timer クラスの timer_complete インターフェイス'),
        Mapping(
            key='Timer class reset interface',
            value='Timer クラスの reset インターフェイス'),
        Mapping(
            key='**Animation**',
            value='**アニメーション**'),
        Mapping(
            key='Animation interfaces abstract',
            value='アニメーションの各インターフェイスの概要'),
        Mapping(
            key='AnimationEvent class',
            value='AnimationEvent クラス'),
        Mapping(
            key='Animation duration setting',
            value='Animation クラスの duration 設定'),
        Mapping(
            key='Animation delay setting',
            value='Animation クラスの delay 設定'),
        Mapping(
            key='Each animation interface return value',
            value='アニメーションの各インターフェイスの返却値について'),
        Mapping(
            key='AnimationBase class start interface',
            value='AnimationBase クラスの start インターフェイス'),
        Mapping(
            key='AnimationBase class animation_complete interface',
            value='AnimationBase クラスの animation_complete '
                  'インターフェイス'),
        Mapping(
            key='AnimationBase class interfaces method chaining',
            value='AnimationBase クラスの各インターフェイスの'
                  'メソッドチェーンについて'),
        Mapping(
            key='AnimationBase class target property',
            value='AnimationBase クラスの target 属性'),
        Mapping(
            key='Animation pause and play interfaces',
            value='アニメーションの pause と play の各インターフェイス'),
        Mapping(
            key='Animation reset interface',
            value='アニメーションの reset インターフェイス'),
        Mapping(
            key='Animation finish interface',
            value='アニメーションの finish インターフェイス'),
        Mapping(
            key='Animation reverse interface',
            value='アニメーションの reverse インターフェイス'),
        Mapping(
            key='animation_time interface',
            value='animation_time インターフェイス'),
        Mapping(
            key='Easing enum',
            value='イージングの enum'),
        Mapping(
            key='Sequential animation setting',
            value='連続したアニメーション設定'),
        Mapping(
            key='animation_parallel interface',
            value='animation_parallel インターフェイス'),
        Mapping(
            key='animation_move interface',
            value='animation_move インターフェイス'),
        Mapping(
            key='animation_x interface',
            value='animation_x インターフェイス'),
        Mapping(
            key='animation_y interface',
            value='animation_y インターフェイス'),
        Mapping(
            key='animation_width and animation_height interfaces',
            value='animation_width と animation_height の各インターフェイス'),
        Mapping(
            key='animation_y interface',
            value='animation_y インターフェイス'),
        Mapping(
            key='animation_fill_color interface',
            value='animation_fill_color インターフェイス'),
        Mapping(
            key='animation_fill_alpha interface',
            value='animation_fill_alpha インターフェイス'),
        Mapping(
            key='animation_line_color interface',
            value='animation_line_color インターフェイス'),
        Mapping(
            key='animation_line_alpha interface',
            value='animation_line_alpha インターフェイス'),
        Mapping(
            key='animation_line_thickness interface',
            value='animation_line_thickness インターフェイス'),
        Mapping(
            key='animation_radius interface',
            value='animation_radius インターフェイス'),
        Mapping(
            key='animation_rotation_around_center interface',
            value='animation_rotation_around_center インターフェイス'),
        Mapping(
            key='animation_rotation_around_point interface',
            value='animation_rotation_around_point インターフェイス'),
        Mapping(
            key='animation_scale_x_from_center and '
                'animation_scale_y_from_center interfaces',
            value='animation_scale_x_from_center と '
                  'animation_scale_y_from_center の各インターフェイス'),
        Mapping(
            key='animation_scale_x_from_point and '
                'animation_scale_y_from_point interfaces',
            value='animation_scale_x_from_point と '
                  'animation_scale_y_from_point の各インターフェイス'),
        Mapping(
            key='animation_skew_x interface',
            value='animation_skew_x インターフェイス'),
        Mapping(
            key='**Debugging**',
            value='**デバッグ**'),
        Mapping(
            key='trace function interface',
            value='trace 関数のインターフェイス'),
        Mapping(
            key='set_debug_mode interface',
            value='set_debug_mode インターフェイス'),
        Mapping(
            key='unset_debug_mode interface',
            value='unset_debug_mode インターフェイス'),
        Mapping(
            key='**Testing**',
            value='**テスト**'),
        Mapping(
            key='assert_equal and assert_not_equal interfaces',
            value='assert_equal と assert_not_equal の各インターフェイス'),
        Mapping(
            key='assert_true and assert_false interfaces',
            value='assert_true と assert_false の各インターフェイス'),
        Mapping(
            key='assert_arrays_equal and assert_arrays_not_equal interfaces',
            value='assert_arrays_equal と assert_arrays_not_equal の'
                  '各インターフェイス'),
        Mapping(
            key='assert_dicts_equal and assert_dicts_not_equal interfaces',
            value='assert_dicts_equal と assert_dicts_not_equal の'
                  '各インターフェイス'),
        Mapping(
            key='assert_defined and assert_undefined interfaces',
            value='assert_defined と assert_undefined の各インターフェイス'),
        Mapping(
            key='**Child-related interfaces**',
            value='**子要素関係の各インターフェイス**'),
        Mapping(
            key='## Common behaviors',
            value='## 共通の挙動'),
        Mapping(
            key='## Addition',
            value='## 加算'),
        Mapping(
            key='## Subtraction',
            value='## 減算'),
        Mapping(
            key='## Multiplication',
            value='## 乗算'),
        Mapping(
            key='## Division',
            value='## 除算'),
        Mapping(
            key='## Floor division',
            value='## 切り捨て除算'),
        Mapping(
            key='## Modulo',
            value='## 剰余'),
        Mapping(
            key='## Equal comparison operator',
            value='## 等値条件の比較のオペレーター'),
        Mapping(
            key='You can use the `==` operator for the equal comparison:',
            value='`==`のオペレーターを使って等値条件の比較を行うことができます。'),
        Mapping(
            key='## Not equal comparison operator',
            value='## 非等値条件の比較のオペレーター'),
        Mapping(
            key='You can use the `!=` operator for the not equal comparison:',
            value='`!=`のオペレーターを使って非等値条件の比較を行うことができます。'),
        Mapping(
            key='## Less than comparison operator',
            value='## 未満条件の比較のオペレーター'),
        Mapping(
            key='You can use the `<` operator for the less than comparison:',
            value='`<`のオペレーターを使って未満条件の比較を行うことができます。'),
        Mapping(
            key='## Less than or equal comparison operator',
            value='## 以下条件の比較のオペレーター'),
        Mapping(
            key='You can use the `<=` operator for the less than or equal '
                'comparison:',
            value='`<=`のオペレーターを使って以下条件の比較を行うことができます。'),
        Mapping(
            key='## Greater than comparison operator',
            value='## 超過条件の比較のオペレーター'),
        Mapping(
            key='You can use the `>` operator for the greater than '
                'comparison:',
            value='`>`のオペレーターを使って超過条件の比較を行うことができます。'),
        Mapping(
            key='## Greater than or equal comparison operator',
            value='## 以上条件の比較のオペレーター'),
        Mapping(
            key='You can use the `>=` operator for the greater than or '
                'equal comparison:',
            value='`>=`のオペレーターを使って以上条件の比較を行うことができます。'),
        Mapping(
            key='## Int class',
            value='## Int クラス'),
        Mapping(
            key='## Number class',
            value='## Number クラス'),
        Mapping(
            key='## Note for the Float class alias',
            value='## Floatクラスのエイリアスの特記事項'),
        Mapping(
            key='## Int and Number classes basic interfaces',
            value='## Int と Number クラスの基本的なインターフェイス'),
        Mapping(
            key='Int and Number classes basic arithmetic operations',
            value='Int と Number クラスの基本的な各計算の制御'),
        Mapping(
            key='Int and Number classes basic comparison operations',
            value='Int と Number クラスの基本的な各比較の制御'),
        Mapping(
            key='## Int class constructor API',
            value='## Int クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** Integer class for apysc '
                'library.<hr>',
            value='**[インターフェイス概要]** apyscライブラリ上の整数のための'
                  'クラスです。<hr>'),
        Mapping(
            key='  - Initial integer value. If the `float` or `Number` '
                'value is specified, this class casts it to an integer.',
            value='  - 整数の初期値。もしも`float`や`Number`の値が指定された'
                  '場合このクラスは値を整数へと変換します。'),
        Mapping(
            key='Int and Number common arithmetic operations document',
            value='Int と Number クラスの共通の各計算制御'),
        Mapping(
            key='Int and Number common comparison operations document',
            value='Int と Number クラスの共通の各比較制御'),
        Mapping(
            key='## Number class constructor API',
            value='## Number クラスのコンストラクタのAPI'),
        Mapping(
            key='  - Initial floating point number value. This class '
                'casts it to float if you specify int or Int value.',
            value='  - 浮動小数点数の初期値。もしもintやIntなどの型の値が指定された'
                  '場合このクラスは値を浮動小数点数へ変換します。'),
        Mapping(
            key='The `Float` class is the alias of the Number, and '
                'it behaves the same as the Number class.<hr>',
            value='`Float`クラスはNumberクラスのエイリアスであり、このエイリアスは'
                  'Numberクラスと同様に動作します。<hr>'),
        Mapping(
            key='**[Interface summary]** Get a current number value.<hr>',
            value='**[インターフェイス概要]** 現在の数値を取得します。<hr>'),
        Mapping(
            key='  - Current number value.',
            value='  - 現在の数値。'),
        Mapping(
            key='**[Interface summary]** Floating point number class for '
                'apysc library.<hr>',
            value='**[インターフェイス概要]** apyscライブラリ用の浮動小数点数の'
                  'クラスです。<hr>'),

    ])
