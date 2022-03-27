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
            value='クリックインターフェイス'),
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
    ])
