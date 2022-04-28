"""This module is for the Japanese fixed-translation mappings
settings.
"""

from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mappings

MAPPINGS: Mappings = Mappings(
    mappings=[
        Mapping(
            key='## See also',
            val='## 関連資料'),
        Mapping(
            key='**[Returns]**',
            val='**[返却値]**'),
        Mapping(
            key='**[Parameters]**',
            val='**[引数]**'),
        Mapping(
            key='**[Examples]**',
            val='**[コードサンプル]**'),
        Mapping(
            key='**[References]**',
            val='**[関連資料]**'),
        Mapping(
            key='<span class="inconspicuous-txt">Note: the document build '
            'script generates and updates this API document section '
            'automatically. Maybe this section is duplicated '
            'compared with previous sections.</span>',
            val='<span class="inconspicuous-txt">特記事項: このAPI'
            'ドキュメントはドキュメントビルド用のスクリプトによって自動で'
            '生成・同期されています。そのためもしかしたらこの節の'
            '内容は前節までの内容と重複している場合があります。</span>'),
        Mapping(
            key='Graphics class',
            val='Graphics クラス'),
        Mapping(
            key='Graphics begin_fill interface',
            val='Graphics クラス begin_fill （塗り設定）の'
            'インターフェイス'),
        Mapping(
            key='Graphics line_style interface',
            val='Graphics クラス line_style （線設定）の'
            'インターフェイス'),
        Mapping(
            key='Graphics draw_rect interface',
            val='Graphics クラス draw_rect （四角描画）の'
            'インターフェイス'),
        Mapping(
            key='Graphics draw_circle interface',
            val='Graphics クラス draw_circle （円描画）の'
            'インターフェイス'),
        Mapping(
            key='add_child and remove_child interfaces',
            val='add_child （子の追加）と remove_child （子の削除）'
            'のインターフェイス'),
        Mapping(
            key='add_child and remove_child interfaces document',
            val='add_child （子の追加）と remove_child （子の削除）'
            'のインターフェイス'),
        Mapping(
            key='contains interface',
            val='contains インターフェイス'),
        Mapping(
            key='contains interface document',
            val='contains インターフェイス'),
        Mapping(
            key='num_children interface',
            val='num_children （子の件数属性）のインターフェイス'),
        Mapping(
            key='num_children interface document',
            val='num_children （子の件数属性）のインターフェイス'),
        Mapping(
            key='get_child_at interface',
            val='get_child_at （特定位置の子の取得処理）の'
            'インターフェイス'),
        Mapping(
            key='get_child_at interface document',
            val='get_child_at （特定位置の子の取得処理）の'
            'インターフェイス'),
        Mapping(
            key='DisplayObject class parent interfaces',
            val='DisplayObjectクラス parent （親要素属性）の'
            'インターフェイス'),
        Mapping(
            key='**[Notes]**',
            val='**[特記事項]**'),
        Mapping(
            key='**[Raises]**',
            val='**[エラー発生条件]**'),
        Mapping(
            key='About the handler options\\\' type document',
            val='ハンドラのoptions引数の型について'),
        Mapping(
            key='## Basic usage',
            val='## 基本的な使い方'),
        Mapping(
            key='## What setting is this?',
            val='## 設定概要'),
        Mapping(
            key='## What class is this?',
            val='## クラス概要'),
        Mapping(
            key='## What interface is this?',
            val='## インターフェイス概要'),
        Mapping(
            key='Animation interfaces duration setting document',
            val='各アニメーションインターフェイスの duration '
            '（アニメーション時間）設定'),
        Mapping(
            key='Each animation interface return value document',
            val='各アニメーションインターフェイスの返却値'),
        Mapping(
            key='Sequential animation setting document',
            val='連続したアニメーション設定'),
        Mapping(
            key='animation_parallel interface document',
            val='animation_parallel （並列アニメーション設定）の'
            'インターフェイス'),
        Mapping(
            key='Easing enum document',
            val='イージングのenum'),
        Mapping(
            key='  - Milliseconds before an animation ends.',
            val='  - アニメーション完了までのミリ秒。'),
        Mapping(
            key='  - Milliseconds before an animation starts.',
            val='  - アニメーション開始までの遅延時間のミリ秒。'),
        Mapping(
            key='  - Easing setting.',
            val='  - イージング設定。'),
        Mapping(
            key='To start this animation, you need to call the '
            '`start` method of the returned instance.<hr>',
            val='アニメーションを開始するには返却されたインスタンスの'
            '`start`メソッドを呼び出す必要があります。<hr>'),
        Mapping(
            key=' ・To start this animation, you need to call the '
            '`start` method of the returned instance. ',
            val=' ・アニメーションを開始するには返却されたインスタンスの'
            '`start`メソッドを呼び出す必要があります。 '),
        Mapping(
            key='Animation interfaces delay setting document',
            val='各アニメーションインターフェイスの delay （遅延時間）設定'),
        Mapping(
            key='  - Created animation setting instance.',
            val='  - 生成されたアニメーションのインスタンス。'),
        Mapping(
            key='<details>\\n<summary>Display the code block:</summary>',
            val='<details>\\n<summary>コードブロックを表示:</summary>'),
        Mapping(
            key='<details>\n<summary>Display the code block:</summary>',
            val='<details>\n<summary>コードブロックを表示:</summary>'),
        Mapping(
            key='animation_x interface document',
            val='animation_x （X座標のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_y interface document',
            val='animation_y （Y座標のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_move interface document',
            val='animation_move （XとY座標のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_width and animation_height interfaces document',
            val='animation_width （幅のアニメーション）と animation_height '
            '（高さのアニメーション）のインターフェイス'),
        Mapping(
            key='animation_fill_color interface document',
            val='animation_fill_color （塗りの色のアニメーション）の'
            'インターフェイス'),
        Mapping(
            key='animation_fill_alpha interface document',
            val='animation_fill_alpha （塗りの透明度のアニメーション）の'
            'インターフェイス'),
        Mapping(
            key='animation_line_color interface document',
            val='animation_line_color （線色のアニメーション）の'
            'インターフェイス'),
        Mapping(
            key='animation_line_alpha interface document',
            val='animation_line_alpha （線の透明度のアニメーション）'
            'のインターフェイス'),
        Mapping(
            key='animation_line_thickness interface document',
            val='animation_line_thickness （線幅のアニメーション）の'
            'インターフェイス'),
        Mapping(
            key='animation_radius interface document',
            val='animation_radius （半径のアニメーション）の'
            'インターフェイス'),
        Mapping(
            key='animation_rotation_around_center interface document',
            val='animation_rotation_around_center （中央座標での'
            '回転のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_rotation_around_point interface document',
            val='animation_rotation_around_point （指定座標に'
            'よる回転のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_scale_x_from_center and '
            'animation_scale_y_from_center interfaces document',
            val='animation_scale_x_from_center （中央座標による水平方向の'
            '拡縮アニメーション）と animation_scale_y_from_center '
            '（中央座標による垂直方向の拡縮アニメーション）のインターフェイス'),
        Mapping(
            key='animation_scale_x_from_point and '
                'animation_scale_y_from_point interfaces document',
            val='animation_scale_x_from_point （指定座標による'
            '水平方向の拡縮アニメーション）と animation_scale_y_from_point '
            '（指定座標による垂直方向のアニメーション）のインターフェイス'),
        Mapping(
            key='animation_skew_x interface document',
            val='animation_skew_x （水平方向の斜め変換の'
            'アニメーション）のインターフェイス'),
        Mapping(
            key='This interface exists on a `GraphicsBase` subclass, '
            'such as the `Rectangle` or `Circle` class.',
            val='このインターフェイスは`Rectangle`や`Circle`'
            'クラスなどの`GraphicsBase`のサブクラスで存在します。'),
        Mapping(
            key='**[Interface summary]** Set the line alpha '
            'animation setting.<hr>',
            val='**[インターフェイス概要]** 線の透明度の'
            'アニメーションを設定します。<hr>'),
        Mapping(
            key='  - The final line alpha of the animation.',
            val='  - 線の透明度のアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Set the line color animation '
            'setting.<hr>',
            val='**[インターフェイス概要]** 線の色のアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='  - The final line color (hex color code) of the animation.',
            val='  - 16進数の線の色のアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Set the line thickness '
            'animation setting.<hr>',
            val='**[インターフェイス概要]** 線幅のアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='  - The final line thickness of the animation.',
            val='  - 線幅のアニメーションの最終値。'),
        Mapping(
            key='This interface exists on a `DisplayObject` subclass '
            'instance, such as the `Sprite` or `Rectangle` class.',
            val='このインターフェイスは`Sprite`や`Rectangle`'
            'などの`DisplayObject`の各サブクラスに存在します。'),
        Mapping(
            key='**[Interface summary]** Set the x and y '
            'coordinates animation settings.<hr>',
            val='**[インターフェイス概要]** XとY座標に対する'
            'アニメーションを設定します。<hr>'),
        Mapping(
            key='  - Destination of the x-coordinate.',
            val='  - 最終的なX座標。'),
        Mapping(
            key='  - Destination of the y-coordinate.',
            val='  - 最終的なY座標。'),
        Mapping(
            key='## What interface are these?',
            val='## 各インターフェイス概要'),
        Mapping(
            key='These interfaces exist in the instances that '
            'have the animation interfaces (such as the '
            '`animation_x`\\, `animation_move`).',
            val='これらのインターフェイスは`animation_x`や'
            '`animation_move`などのアニメーション関係のインターフェイスを'
            '持つクラスのインスタンス上に存在します。'),
        Mapping(
            key='This interface exists on a `GraphicsBase` '
            'subclass, such as the `Circle` class.',
            val='このインターフェイスは`Circle`クラスなどの'
            '`GraphicsBase`の各サブクラス上に存在します。'),
        Mapping(
            key='  - The final radius of the animation.',
            val='  - 半径のアニメーションの最終値。'),
        Mapping(
            key='This interface exists in the instances that '
            'have the animation interfaces (such as the '
            '`animation_x`\\, `animation_move`).',
            val='このインターフェイスは`animation_x`や`animation_move`'
            'などのアニメーション関係のインターフェイスを持つクラスの'
            'インスタンス上に存在します。'),
        Mapping(
            key='## Interface Notes',
            val='## インターフェイスの特記事項'),
        Mapping(
            key='**[Interface summary]** Reverse all running animations.<hr>',
            val='**[インターフェイス概要]** 動いている全ての'
            'アニメーションを反転（逆再生）します。<hr>'),
        Mapping(
            key='**[Interface summary]** Set the rotation around the center '
            'animation setting.<hr>',
            val='**[インターフェイス概要]** 中央座標を使用した'
            '回転のアニメーションの設定を行います。<hr>'),
        Mapping(
            key='  - The final rotation of the animation.',
            val='  - 回転のアニメーションの回転量の最終値。'),
        Mapping(
            key='**[Interface summary]** Set the rotation around '
            'the given point animation setting.<hr>',
            val='**[インターフェイス概要]** 指定された座標を'
            '基準とした回転のアニメーションを設定します。<hr>'),
        Mapping(
            key='  - X-coordinate.',
            val='  - X座標。'),
        Mapping(
            key='  - Y-coordinate.',
            val='  - Y座標。'),
        Mapping(
            key='## What interfaces are these?',
            val='## 各インターフェイスの概要'),
        Mapping(
            key='**[Interface summary]** Set the scale-x from '
            'the center point animation setting.<hr>',
            val='**[インターフェイス概要]** 中央座標を基準とした'
            'X軸の拡縮アニメーションを設定します。<hr>'),
        Mapping(
            key='  - The final scale-x of the animation.',
            val='  - X軸の拡縮のアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Set the scale-y from '
            'the center point animation setting.<hr>',
            val='**[インターフェイス概要]** 中央座標を基準とした'
            'Y軸の拡縮アニメーションを設定します。<hr>'),
        Mapping(
            key='  - The final scale-y of the animation.',
            val='  - Y軸の拡縮のアニメーションの最終値。'),
        Mapping(
            key='This interface exists on a `GraphicsBase` '
            'subclass, such as the `Rectangle` class.',
            val='このインターフェイスは`Rectangle`などの'
            '`GraphicsBase`の各サブクラス上に存在します。'),
        Mapping(
            key='**[Interface summary]** Set the skew-x animation '
            'setting.<hr>',
            val='**[インターフェイス概要]** X軸の傾きのアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='  - The final skew-x of the animation.',
            val='  - X軸の傾きのアニメーションの最終値。'),
        Mapping(
            key='**[Interface summary]** Get an animation elapsed '
            'millisecond.<hr>',
            val='**[インターフェイス概要]** アニメーションの'
            '経過時間のミリ秒を取得します。<hr>'),
        Mapping(
            key='  - An animation elapsed millisecond.',
            val='  - アニメーションの経過時間のミリ秒。'),
        Mapping(
            key='These interfaces exist on some `DisplayObject` '
            'instances, such as the `Rectangle` class.',
            val='これらの各インターフェイスは`Rectangle`クラスなどの'
            '`DisplayObject`の各サブクラス上に存在します。'),
        Mapping(
            key='## Notes for the Ellipse instance',
            val='## Ellipse のインスタンスにおける特記事項'),
        Mapping(
            key='**[Interface summary]** Set the width animation '
            'setting.<hr>',
            val='**[インターフェイス概要]** 幅のアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='**[Interface summary]** Set the height '
            'animation setting.<hr>',
            val='**[インターフェイス概要]** 高さのアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='  - The final width of the animation.',
            val='  - 幅のアニメーションの最終値。'),
        Mapping(
            key='  - The final height of the animation.',
            val='  - 高さのアニメーションの最終値。'),
        Mapping(
            key='## Notes for the Circle and Ellipse classes',
            val='## Circle と Ellipse の各クラスの特記事項'),
        Mapping(
            key='**[Interface summary]** Set the x-coordinate '
            'animation setting.<hr>',
            val='**[インターフェイス概要]** X座標のアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='**[Interface summary]** Set the y-coordinate '
            'animation setting.<hr>',
            val='**[インターフェイス概要]** Y座標のアニメーションを'
            '設定します。<hr>'),
        Mapping(
            key='  - Any value to append.',
            val='  - 追加対象の任意の値。'),
        Mapping(
            key='  - Other array-like values to concatenate.',
            val='  - 連結対象となる他の配列の（もしくはそれに近しい）値。'),
        Mapping(
            key='  - Any value to search.',
            val='  - 検索対象の任意の値。'),
        Mapping(
            key='  - Index to append value.',
            val='  - 値を追加するインデックス。'),
        Mapping(
            key='  - Separator string.',
            val='  - 区切り文字。'),
        Mapping(
            key='  - Joined string.',
            val='  - 連結された文字列。'),
        Mapping(
            key='  - Removed value.',
            val='  - 取り除かれた値。'),
        Mapping(
            key='  - Value to remove.',
            val='  - 取り除く対象の値。'),
        Mapping(
            key='  - Index to remove value.',
            val='  - 取り除く値のインデックス。'),
        Mapping(
            key='Array class sort interface',
            val='Array クラスの sort インターフェイス'),
        Mapping(
            key='An original array is not modified.',
            val='元々の配列の値は変更されません。'),
        Mapping(
            key='  - Slicing start index.',
            val='  - スライス範囲の開始インデックス。'),
        Mapping(
            key='  - Sliced array.',
            val='  - スライスされた配列。'),
        Mapping(
            key='Array class reverse interface',
            val='Array クラスの reverse インターフェイス'),
        Mapping(
            key='Before reading on, maybe it is helpful to '
            'read the following page:',
            val='事前に以下のページを確認しておくと読み進める上で'
            '役に立つかもしれません:'),
        Mapping(
            key='Why the apysc library doesn\\\'t use the Python '
            'built-in data type',
            val='なぜapyscではPythonのビルトインのデータの'
            '型を使用していないのか'),
        Mapping(
            key='Why the apysc library does not use the Python '
            'built-in data type',
            val='なぜapyscではPythonのビルトインのデータの'
            '型を使用していないのか'),
        Mapping(
            key='## Constructor method',
            val='## コンストラクタメソッド'),
        Mapping(
            key='## Generic type annotation',
            val='## ジェネリックの型アノテーション'),
        Mapping(
            key='Funcdamental data classes common value interface',
            val='基本的なデータクラスの共通の value インターフェイス'),
        Mapping(
            key='Array class append and push interfaces',
            val='Array クラスの append と push のインターフェイス'),
        Mapping(
            key='Array class extend and concat interfaces',
            val='Array クラスの extend と concat のインターフェイス'),
        Mapping(
            key='Array class insert and insert_at interfaces',
            val='Array クラスの insert と insert_at のインターフェイス'),
        Mapping(
            key='Array class pop interface',
            val='Array クラスの pop インターフェイス'),
        Mapping(
            key='Array class remove and remove_at interfaces',
            val='Array クラスの remove と remove_at のインターフェイス'),
        Mapping(
            key='Array class slice interface',
            val='Array クラスの slice インターフェイス'),
        Mapping(
            key='Array class length interface',
            val='Array クラスの length (配列の長さ取得) のインターフェイス'),
        Mapping(
            key='Array class join interface',
            val='Array クラスの join (値の連結文字列生成) のインターフェイス'),
        Mapping(
            key='Array class index_of interface',
            val='Array クラスの index_of (値のインデックス取得) のインターフェイス'),
        Mapping(
            key='Array class comparison interfaces',
            val='Array クラスの比較の各インターフェイス'),
        Mapping(
            key='Array class comparison interfaces document',
            val='Array クラスの比較の各インターフェイス'),
        Mapping(
            key='## Array class constructor API',
            val='## Array クラスのコンストラクタのAPI'),
        Mapping(
            key='  - Initial array value.',
            val='  - 配列の初期値。'),
        Mapping(
            key='## value property API',
            val='## value 属性のAPI'),
        Mapping(
            key='  - Current array value.',
            val='  - 現在の配列の値。'),
        Mapping(
            key='apysc fundamental data classes value interface',
            val='apyscの基本的なデータクラスの value インターフェイス'),
        Mapping(
            key='JavaScript assertion interface basic behavior',
            val='JavaScriptの各アサーションのインターフェイスの基本的な挙動'),
        Mapping(
            key='## Notes for the assert_equal and assert_not_equal '
                'interfaces',
            val='## assert_equal と assert_not_equal の各インターフェイスに'
            'おける特記事項'),
        Mapping(
            key='  - Left-side value to compare.',
            val='  - 比較用の左辺の値。'),
        Mapping(
            key='  - Right-side value to compare.',
            val='  - 比較用の右辺の値。'),
        Mapping(
            key='  - Message to display when assertion failed.',
            val='  - チェックに失敗した際に表示するメッセージ。'),
        Mapping(
            key='  - Target value to check.',
            val='  - チェック対象の値。'),
        Mapping(
            key='  - Callable that this instance calls when its '
            'event\'s dispatching.',
            val='  - 対象のイベントが発生（発火）される時に実行される'
            'ハンドラ。'),
        Mapping(
            key='  - Target custom event type.',
            val='  - 対象の独自のイベントの種別値としての文字列。'),
        Mapping(
            key='  - Event instance.',
            val='  - イベントのインスタンス。'),
        Mapping(
            key='  - Optional arguments dictionary to be passed '
            'to a handler.',
            val='  - ハンドラに渡される省略が可能な追加のパラメーター'
            'としての辞書。'),
        Mapping(
            key='  - Handler\'s name.',
            val='  - ハンドラ名。'),
        Mapping(
            key='If class',
            val='If クラス'),
        Mapping(
            key='Elif class',
            val='Elif クラス'),
        Mapping(
            key='Else class',
            val='Else クラス'),
        Mapping(
            key='The following page describes basic mouse event interfaces.',
            val='以下のページでは基本的なマウスイベントの'
            'インターフェイスについて説明しています。'),
        Mapping(
            key='Basic mouse event interfaces',
            val='基本的なマウスイベントの各インターフェイス'),
        Mapping(
            key='  - Unbinding target Callable.',
            val='  - イベント設定を取り除く対象の関数やメソッドなど。'),
        Mapping(
            key='  - Child instance to check.',
            val='  - チェック対象の子のインスタンス。'),
        Mapping(
            key='The following page describes the basic mouse '
            'event interfaces.',
            val='以下のページでは基本的なマウスイベントの'
            '各インターフェイスについて説明しています。'),
        Mapping(
            key='  - Target key.',
            val='  - 対象のキー。'),
        Mapping(
            key='  - Any default value.',
            val='  - 任意のデフォルト値の値。'),
        Mapping(
            key='## Note for the len function',
            val='## len関数における特記事項'),
        Mapping(
            key='The Python built-in `len` function is not '
            'supported and raises an exception:',
            val='Pythonビルトインの`len`関数はサポートされて'
            'おらずエラーとなります:'),
        Mapping(
            key='## Value setter interface',
            val='## 値のsetterのインターフェイス'),
        Mapping(
            key='## Value getter interface',
            val='## 値のgetterのインターフェイス'),
        Mapping(
            key='## Notes of the getter interface',
            val='## getterのインターフェイスの特記事項'),
        Mapping(
            key='## Value deletion interface',
            val='## 値の削除のインターフェイス'),
        Mapping(
            key='  - Initial dictionary value.',
            val='  - 辞書の初期値。'),
        Mapping(
            key='Dictionary class generic type settings document',
            val='Dictionary クラスのジェネリックの型設定'),
        Mapping(
            key='## value attribute API',
            val='## value 属性のAPI'),
        Mapping(
            key='  - Current dict value.',
            val='  - 現在の辞書の値。'),
        Mapping(
            key='## What apysc can do in its properties',
            val='## それらの属性でapyscができること'),
        Mapping(
            key='For more details, please see the following:',
            val='詳細については以下をご確認ください:'),
        Mapping(
            key='DisplayObject class x and y interfaces',
            val='DisplayObject クラスの x と y インターフェイス'),
        Mapping(
            key='## x and y properties',
            val='## x と y 属性'),
        Mapping(
            key='## visible property',
            val='## visible 属性'),
        Mapping(
            key='DisplayObject class visible interface',
            val='DisplayObject クラスの visible (表示・非表示) の'
            'インターフェイス'),
        Mapping(
            key='## rotation interfaces',
            val='## 回転の各インターフェイス'),
        Mapping(
            key='GraphicsBase class rotation_around_center interface',
            val='GraphicsBase クラスの rotation_around_center '
            '(中央座標基準の回転) インターフェイス'),
        Mapping(
            key='GraphicsBase class rotation_around_point interfaces',
            val='GraphicsBase クラスの rotation_around_point '
            '(指定座標基準の回転) の各インターフェイス'),
        Mapping(
            key='## scale interfaces',
            val='## 拡縮の各インターフェイス'),
        Mapping(
            key='GraphicsBase class scale_from_center interfaces',
            val='GraphicsBase クラスの scale_from_center (中央座標基準の拡縮) '
            'の各インターフェイス'),
        Mapping(
            key='GraphicsBase class scale_from_point interfaces',
            val='GraphicsBase クラスの scale_from_point (指定座標基準の拡縮) '
            'の各インターフェイス'),
        Mapping(
            key='## flip properties',
            val='## 反転の各属性'),
        Mapping(
            key='## GraphicsBase class flip_x and flip_y interfaces',
            val='## GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) '
            'のインターフェイス'),
        Mapping(
            key='GraphicsBase class flip_x and flip_y interfaces',
            val='GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) '
            'のインターフェイス'),
        Mapping(
            key='## skew properties',
            val='## 歪みの各属性'),
        Mapping(
            key='GraphicsBase class skew_x and skew_y interfaces',
            val='GraphicsBase クラスの skew_x (X軸の歪み) と skew_y (Y軸の歪み) '
            'のインターフェイス'),
        Mapping(
            key='DisplayObject class',
            val='DisplayObject クラス'),
        Mapping(
            key='  - CSS name (e.g., \'display\').',
            val='  - CSS名（例 : \'display\'）。'),
        Mapping(
            key='For more details, please see the following pages:',
            val='詳細については以下の各ページをご確認ください:'),
        Mapping(
            key='click interface',
            val='click インターフェイス'),
        Mapping(
            key='mousedown and mouseup interfaces',
            val='mousedown と mouseup のインターフェイス'),
        Mapping(
            key='mouseover and mouseout interfaces',
            val='mouseover と mouseout のインターフェイス'),
        Mapping(
            key='mousemove interface',
            val='mousemove インターフェイス'),
        Mapping(
            key='- ValueError: If a parent is None (there is no parent).',
            val='- ValueError: もしも親のインスタンスがNoneの'
            '場合（親の無い状態の場合）。'),
        Mapping(
            key='## visible property API',
            val='## visible 属性のAPI'),
        Mapping(
            key='## Augmented assignment',
            val='## 累算代入演算'),
        Mapping(
            key='## x property API',
            val='## x属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a x-coordinate.<hr>',
            val='**[インターフェイス概要]** X座標を取得します。<hr>'),
        Mapping(
            key='## y property API',
            val='## y属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a y-coordinate.<hr>',
            val='**[インターフェイス概要]** Y座標を取得します。<hr>'),
        Mapping(
            key='DisplayObject class mouse event binding interfaces',
            val='DisplayObject クラスのマウスイベント設定の各インターフェイス'),
        Mapping(
            key='## Requirements',
            val='## 必要とされるインストールなどの対応'),
        Mapping(
            key='  - Boolean value whether minify a HTML or not. '
            'False setting is useful when debugging.',
            val='  - HTMLを最小化（minify）するかどうかの真偽値。'
            'Falseの設定はデバッグ時などに役に立つことがあります。'),
        Mapping(
            key='For more information, please see:',
            val='詳細は以下をご確認ください:'),
        Mapping(
            key='## Notes',
            val='## 特記事項'),
        Mapping(
            key='  - The output HTML file name.',
            val='  - 出力されるHTMLのファイル名。'),
        Mapping(
            key='Graphics class draw_rect interface',
            val='Graphics クラスの draw_rect (四角の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_round_rect interface',
            val='Graphics クラスの draw_round_rect (角丸の四角の描画)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class draw_circle interface',
            val='Graphics クラスの draw_circle (円の描画)のインターフェイス'),
        Mapping(
            key='Graphics class move_to and line_to interfaces',
            val='Graphics クラスの move_to (線の描画位置の変更)と'
            ' line_to (指定座標への線の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_line interface',
            val='Graphics クラスの draw_line (線の描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_dotted_line interface',
            val='Graphics クラスの draw_dotted_line (点線の描画)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class draw_dashed_line interface',
            val='Graphics クラスの draw_dashed_line (破線の描画)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class draw_round_dotted_line interface',
            val='Graphics クラスの draw_round_dotted_line (点線(丸)の'
            '描画)のインターフェイス'),
        Mapping(
            key='Graphics class draw_dash_dotted_line interface',
            val='Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)'
            'のインターフェイス'),
        Mapping(
            key='Graphics class draw_polygon interface',
            val='Graphics クラスの draw_polygon (多角形描画)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class fill_color interface',
            val='Graphics クラスの fill_color (塗り設定)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class fill_alpha interface',
            val='Graphics クラスの fill_alpha (塗りの透明度設定)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class line_color interface',
            val='Graphics クラスの line_color (線の色設定)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class line_alpha interface',
            val='Graphics クラスの line_color (線の透明度設定)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class line_thickness interface',
            val='Graphics クラスの line_color (線幅設定)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class line_dot_setting interface',
            val='Graphics クラスの line_dot_setting (点線設定)'
            'のインターフェイス'),
        Mapping(
            key='Graphics class line_dash_setting interface',
            val='Graphics クラスの line_dash_setting (破線設定)'
            'のインターフェイス'),
        Mapping(
            key='Graphics class line_round_dot_setting interface',
            val='Graphics クラスの line_round_dot_setting (点線(丸)設定)'
            'のインターフェイス'),
        Mapping(
            key='Graphics class line_dash_dot_setting interface',
            val='Graphics クラスの line_dash_dot_setting (一点'
            '鎖線設定)のインターフェイス'),
        Mapping(
            key='For more details, please see:',
            val='詳細は以下をご確認ください:'),
        Mapping(
            key='Graphics class begin_fill interface',
            val='Graphics クラスの begin_fill (塗りの設定)の'
            'インターフェイス'),
        Mapping(
            key='Graphics class line_style interface',
            val='Graphics クラスの line_style (線のスタイル設定)'
            'のインターフェイス'),
        Mapping(
            key='Graphics class draw_ellipse interface',
            val='Graphics クラスの draw_ellipse (楕円描画) の'
            'インターフェイス'),
        Mapping(
            key='Each branch instruction class\\\'s scope variables '
            'reverting setting',
            val='分岐条件の各クラスのスコープ内変数の復元設定'),
        Mapping(
            key='  - Boolean value to be used for judgment.',
            val='  - 判定に使われるBooleanの真偽値。'),
        Mapping(
            key='  - Current scope\'s global variables. Set '
            'globals() value to this argument. This setting '
            'works the same way as the locals_ argument.',
            val='  - 現在のスコープの各グローバル変数。設定する'
            '場合にはglobal()関数の値をこの引数に指定して'
            'ください。この設定はlocals_引数と同じように'
            '動作します。'),
        Mapping(
            key='Timer class delay setting',
            val='Timer クラスの delay 設定'),
        Mapping(
            key='  - Child\'s index (start from 0).',
            val='  - 対象の子のインデックス（0からスタートします）。'),
        Mapping(
            key='  - Target index child instance.',
            val='  - 対象の子のインスタンス。'),
        Mapping(
            key='**[Interface summary]** Get a rotation value '
            'around the center of this instance.<hr>',
            val='**[インターフェイス概要]** インスタンスの中央座標を'
            '基準とした回転量を取得します。<hr>'),
        Mapping(
            key='  - Rotation value around the center of this instance.',
            val='  - このインスタンスの中央座標を基準とした回転量。'),
        Mapping(
            key='  - Rotation value around the given coordinates.',
            val='  - 指定された座標基準による回転量。'),
        Mapping(
            key='## set_rotation_around_point API',
            val='## set_rotation_around_point API'),
        Mapping(
            key='## get_rotation_around_point API',
            val='## get_rotation_around_point API'),
        Mapping(
            key='  - Rotation value to set.',
            val='  - 設定する回転量。'),
        Mapping(
            key='**[Interface summary]** Update a rotation value '
                'around the given coordinates.<hr>',
            val='**[インターフェイス概要]** 指定された座標基準の回転量を'
            '更新します。<hr>'),
        Mapping(
            key='## scale_x_from_center property API',
            val='## scale_x_from_center 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a scale-x value '
            'from the center of this instance.<hr>',
            val='**[インターフェイス概要]** インスタンスの中央座標を'
            '基準とした水平方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-x value from the center of this instance.',
            val='  - インスタンスの中央座標を基準とした水平方向の拡縮の値。'),
        Mapping(
            key='## scale_y_from_center property API',
            val='## scale_y_from_center 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a scale-y value '
                'from the center of this instance.<hr>',
            val='**[インターフェイス概要]** インスタンスの中央座標を'
            '基準とした垂直方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-y value from the center of this instance.',
            val='  - インスタンスの中央座標を基準とした垂直方向の拡縮の値。'),
        Mapping(
            key='## get_scale_x_from_point API',
            val='## get_scale_x_from_point API'),
        Mapping(
            key='**[Interface summary]** Get a scale-x value from the given '
            'x-coordinate.<hr>',
            val='**[インターフェイス概要]** 指定されたX座標を'
            '基準として水平方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-x value from the given x-coordinate.',
            val='  - 指定されたX座標を基準とした水平方向の拡縮値。'),
        Mapping(
            key='## set_scale_x_from_point API',
            val='## set_scale_x_from_point API'),
        Mapping(
            key='**[Interface summary]** Update a scale-x '
            'value from the given '
            'x-coordinate.<hr>',
            val='**[インターフェイス概要]** 指定されたX座病を基準'
            'とした水平方向の拡縮値を更新します。<hr>'),
        Mapping(
            key='## get_scale_y_from_point API',
            val='## get_scale_y_from_point API'),
        Mapping(
            key='**[Interface summary]** Get a scale-y value '
            'from the given y-coordinate.<hr>',
            val='**[インターフェイス概要]** 指定されたY座標を基準'
            'とした垂直方向の拡縮の値を取得します。<hr>'),
        Mapping(
            key='  - Scale-y value from the given y-coordinate.',
            val='  - 指定されたY座標を基準とした垂直方向の拡縮値。'),
        Mapping(
            key='## set_scale_y_from_point API',
            val='## set_scale_y_from_point API'),
        Mapping(
            key='**[Interface summary]** Update a scale-y value '
            'from the given y-coordinate.<hr>',
            val='**[インターフェイス概要]** 指定されたY座標を基準とした'
            '垂直方向の拡縮値を更新します。<hr>'),
        Mapping(
            key='  - Scale-y value to set.',
            val='  - 設定すの垂直方向の拡縮値。'),
        Mapping(
            key='  - Scale-x value to set.',
            val='  - 設定する水平方向の拡縮値。'),
        Mapping(
            key='## skew_x property API',
            val='## skew_x property API'),
        Mapping(
            key='**[Interface summary]** Get a current skew x value of '
            'the instance.<hr>',
            val='**[インターフェイス概要]** インスタンスの現在のX軸の'
            '歪みの値を取得します。<hr>'),
        Mapping(
            key='  - Current skew x value of this instance.',
            val='  - インスタンスの現在のX軸の歪みの値。'),
        Mapping(
            key='## skew_y property API',
            val='## skew_y property API'),
        Mapping(
            key='**[Interface summary]** Get a current skew y '
            'value of the instance.<hr>',
            val='**[インターフェイス概要]** インスタンスの現在のY軸の'
            '歪みの値を取得します。<hr>'),
        Mapping(
            key='  - Current skew y value of the instance.',
            val='  - インスタンスの現在のY軸の歪みの値。'),
        Mapping(
            key='## Fill color setting',
            val='## 塗りの色の設定'),
        Mapping(
            key='## Fill color alpha (opacity) setting',
            val='## 塗りの色の透明度の設定'),
        Mapping(
            key='## begin_fill API',
            val='## begin_fill API'),
        Mapping(
            key='**[Interface summary]** Set single color value for '
            'fill.<hr>',
            val='**[インターフェイス概要]** 塗りのための単一の色の設定を行います。<hr>'),
        Mapping(
            key='  - Hexadecimal color string. e.g., \'#00aaff\'',
            val='  - \'#00aaff\'などの16進数の色の文字列。'),
        Mapping(
            key='  - Color opacity (0.0 to 1.0).',
            val='  - 塗りの透明度（0.0～1.0）。'),
        Mapping(
            key='## fill_color property API',
            val='## fill_color 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current fill color.<hr>',
            val='**[インターフェイス概要]** 現在の塗りの色を取得します。<hr>'),
        Mapping(
            key='  - Current fill color (hexadecimal string, e.g., '
            '\'#00aaff\'). If not be set, this interface returns '
            'a blank string.',
            val='  - 現在の塗りの色（`\'#00aaff\'`などの16進数の文字列）。'
            'もしも設定されていない場合空文字が返却されます。'),
        Mapping(
            key='## fill_alpha property API',
            val='## fill_alpha 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current fill color opacity.<hr>',
            val='**[インターフェイス概要]** 現在の塗りの透明度を取得します。<hr>'),
        Mapping(
            key='  - Current fill color opacity (0.0 to 1.0). If '
            'not be set, 1.0 will be returned.',
            val='  - 現在の塗りの透明度（0.0～1.0）。もし設定されていない'
            '場合1.0の値が返却されます。'),
        Mapping(
            key='## Return value',
            val='## 返却値'),
        Mapping(
            key='## draw_circle API',
            val='## draw_circle API'),
        Mapping(
            key='**[Interface summary]** Draw a circle vector graphics.<hr>',
            val='**[インターフェイス概要]** 円のベクターグラフィックスを'
            '描画します。<hr>'),
        Mapping(
            key='  - X-coordinate of the circle center.',
            val='  - 円の中心のX座標。'),
        Mapping(
            key='  - Y-coordinate of the circle center.',
            val='  - 円の中心のY座標。'),
        Mapping(
            key='  - Circle radius.',
            val='  - 円の半径。'),
        Mapping(
            key='  - Created circle graphics instance.',
            val='  - 生成された円のグラフィックスのインスタンス。'),
        Mapping(
            key='## draw_dash_dotted_line API',
            val='## draw_dash_dotted_line API'),
        Mapping(
            key='**[Interface summary]** Draw a dash-dotted (1-dot chain) '
            'line vector graphics.<hr>',
            val='**[インターフェイス概要]** 一点鎖線のベクターグラフィックスの'
            '線を描画します。<hr>'),
        Mapping(
            key='  - Line start x-coordinate.',
            val='  - 線の開始位置のX座標。'),
        Mapping(
            key='  - Line start y-coordinate.',
            val='  - 線の開始位置のY座標。'),
        Mapping(
            key='  - Line end x-coordinate.',
            val='  - 線の終了位置のX座標。'),
        Mapping(
            key='  - Line end y-coordinate.',
            val='  - 線の終了位置のY座標。'),
        Mapping(
            key='  - Dot size.',
            val='  - ドットのサイズ。'),
        Mapping(
            key='  - Dash size.',
            val='  - 破線部分のサイズ。'),
        Mapping(
            key='  - Blank space size between dots and dashes.',
            val='  - ドット（点線）や破線間の空白スペースのサイズ。'),
        Mapping(
            key='  - Created line graphics instance.',
            val='  - 生成された線のグラフィックスのインスタンス。'),
        Mapping(
            key='## draw_dashed_line API',
            val='## draw_dashed_line API'),
        Mapping(
            key='**[Interface summary]** Draw a dashed line vector '
            'graphics.<hr>',
            val='**[インターフェイス概要]** 破線のベクターグラフィックスを'
            '描画します。<hr>'),
        Mapping(
            key='  - Blank space size between dashes.',
            val='  - 破線間の空白スペースのサイズ。'),
        Mapping(
            key=' ・This interface ignores line settings, like '
            'the `LineDotSetting`, except `LineDashSetting`.<hr>',
            val=' ・このインターフェイスは`LineDashSetting`'
            'を除いた`LineDotSetting`などの線のスタイル設定を無視します。<hr>'),
        Mapping(
            key='## draw_dotted_line API',
            val='## draw_dotted_line API'),
        Mapping(
            key='**[Interface summary]** Draw a dotted line vector '
            'graphics.<hr>',
            val='**[インターフェイス概要]** 点線のベクター'
            'グラフィックスを描画します。<hr>'),
        Mapping(
            key=' ・This interface ignores line settings, like the '
            '`LineDashSetting`, except `LineDotSetting`.<hr>',
            val=' ・このインターフェイスは`LineDotSetting`を'
            '除いた`LineDashSetting`などの線のスタイル設定を無視します。<hr>'),
        Mapping(
            key='## draw_ellipse API',
            val='## draw_ellipse API'),
        Mapping(
            key='**[Interface summary]** Draw an ellipse vector graphic.<hr>',
            val='**[インターフェイス概要]** 楕円のベクターグラフィックスを'
            '描画します。<hr>'),
        Mapping(
            key='  - X-coordinate of the ellipse center.',
            val='  - 楕円の中央のX座標。'),
        Mapping(
            key='  - Y-coordinate of the ellipse center.',
            val='  - 楕円の中央のY座標。'),
        Mapping(
            key='  - Ellipse width.',
            val='  - 楕円の幅。'),
        Mapping(
            key='  - Ellipse height.',
            val='  - 楕円の高さ。'),
        Mapping(
            key='  - Created ellipse graphics instance.',
            val='  - 作成された楕円のグラフィックスのインスタンス。'),
        Mapping(
            key='## Ignored line style settings',
            val='## 無視される線のスタイル設定'),
        Mapping(
            key='## Line class instance',
            val='## Line クラスのインスタンス'),
        Mapping(
            key='## draw_line API',
            val='## draw_line API'),
        Mapping(
            key='**[Interface summary]** Draw a normal line vector '
            'graphic.<hr>',
            val='**[インターフェイス概要]** 通常の直線のベクター'
            'グラフィックスを描画します。<hr>'),
        Mapping(
            key=' ・This interface ignores line settings, '
            'like the `LineDotSetting`, `LineDashSetting`.<hr>',
            val=' ・このインターフェイスは`LineDotSetting`や'
            '`LineDashSetting`などの設定を無視します。<hr>'),
        Mapping(
            key='## draw_polygon API',
            val='## draw_polygon API'),
        Mapping(
            key='**[Interface summary]** Draw a polygon vector '
            'graphic. This interface is similar to the '
            'Polyline class (created by `move_to` or `line_to`). '
            'But unlike that, this interface connects the '
            'last point and the start point.<hr>',
            val='**[インターフェイス概要]** 多角形のベクター'
            'グラフィックスを描画します。このインターフェイスはPolyline'
            'クラス（`move_to`や`line_to`のインターフェイスで作成されます）'
            'に似ていますが、このインターフェイスは始点と終点が連結される'
            'という違いがあります。<hr>'),
        Mapping(
            key='  - Polygon vertex points.',
            val='  - 多角形の頂点の各座標。'),
        Mapping(
            key='  - Created polygon graphics instance.',
            val='  - 作成された多角形のグラフィックスのインスタンス。'),
        Mapping(
            key='## draw_rect API',
            val='## draw_rect API'),
        Mapping(
            key='**[Interface summary]** Draw a rectangle vector '
            'graphics.<hr>',
            val='**[インターフェイス概要]** ベクターグラフィックスの四角を'
            '描画します。<hr>'),
        Mapping(
            key='  - X position to start drawing.',
            val='  - 描画を開始する位置のX座標。'),
        Mapping(
            key='  - Y position to start drawing.',
            val='  - 描画を開始する位置のY座標。'),
        Mapping(
            key='  - Rectangle width.',
            val='  - 四角の幅。'),
        Mapping(
            key='  - Rectangle height.',
            val='  - 四角の高さ。'),
        Mapping(
            key='  - Created rectangle.',
            val='  - 生成された四角。'),
        Mapping(
            key='## draw_round_dotted_line API',
            val='## draw_round_dotted_line API'),
        Mapping(
            key='**[Interface summary]** Draw a round-dotted '
            'line vector graphics.<hr>',
            val='**[インターフェイス概要]** 丸ドットの直線の'
            'ベクターグラフィックスを描画します。<hr>'),
        Mapping(
            key='  - Dot round size.',
            val='  - 丸ドットのサイズ。'),
        Mapping(
            key='  - Blank space size between dots.',
            val='  - ドット間の空白のスペースのサイズ。'),
        Mapping(
            key='This interface ignores line settings, like '
            'the `LineDotSetting`, except `LineRoundDotSetting`.<hr>',
            val='このインターフェイスは`LineRoundDotSetting`を除いて'
            '`LineDotSetting`などの設定を無視します。<hr>'),
        Mapping(
            key='## draw_round_rect API',
            val='## draw_round_rect API'),
        Mapping(
            key='**[Interface summary]** Draw a rounded rectangle '
            'vector graphics.<hr>',
            val='**[インターフェイス概要]** 角丸四角のベクターグラフィックスを'
            '描画します。<hr>'),
        Mapping(
            key='  - X-coordinate to start drawing.',
            val='  - 描画を開始するX座標。'),
        Mapping(
            key='  - Y-coordinate to start drawing.',
            val='  - 描画を開始するY座標。'),
        Mapping(
            key='  - Ellipse width of the rectangle corner.',
            val='  - 四角の角丸の幅。'),
        Mapping(
            key='  - Ellipse height of the rectangle corner.',
            val='  - 四角の角丸の高さ。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s fill '
            'opacity.<hr>',
            val='**[インターフェイス概要]** このインスタンスの塗りの透明度を'
            '取得します。<hr>'),
        Mapping(
            key='  - Current fill opacity (0.0 to 1.0).',
            val='  - 現在の塗りの透明度（0.0～1.0）。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s fill '
            'color.<hr>',
            val='**[インターフェイス概要]** インスタンスの塗りの色を'
            '取得します。<hr>'),
        Mapping(
            key='The getter or setter interface value becomes '
            '(or requires) the `Number` value (0.0 to 1.0).',
            val='getterとsetterの両方のインターフェイスの値は`Number`'
            '型の0.0～1.0の範囲の値となります。'),
        Mapping(
            key='## line_alpha property API',
            val='## line_alpha 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line alpha '
            '(opacity).<hr>',
            val='**[インターフェイス概要]** インスタンスの線の'
            '透明度を取得します。<hr>'),
        Mapping(
            key='  - Current line alpha (opacity. 0.0 to 1.0).',
            val='  - 現在の線の透明度（0.0～1.0）。'),
        Mapping(
            key='The getter or setter interface value becomes '
            '(or requires) the `String` hex color code value.',
            val='getterとsetterのインターフェイスで扱う値は`String`型の'
            '16進数のカラーコードの文字列となります。'),
        Mapping(
            key='## line_color property API',
            val='## line_color 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line '
            'color.<hr>',
            val='**[インターフェイス概要]** インスタンスの線の色を'
            '取得します。<hr>'),
        Mapping(
            key='  - Current line color (hexadecimal string, '
            'e.g., \'#00aaff\'). If not be set, this interface '
            'returns a blank string.',
            val='  - \'#00aaff\'などの16進数の線の色。もし設定'
            'されていない場合はこの空文字となります。'),
        Mapping(
            key='**[Interface summary]** Get current dash dot (1-dot chain) '
            'setting.<hr>',
            val='**[インターフェイス概要]** 現在の一点鎖線のスタイル設定を'
            '取得します。<hr>'),
        Mapping(
            key='## line_dash_dot_setting API',
            val='## line_dash_dot_setting API'),
        Mapping(
            key='  - Dash dot (1-dot chain) setting.',
            val='  - 一点鎖線の設定。'),
        Mapping(
            key='## line_dash_setting property API',
            val='## line_dash_setting 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line dash '
            'setting.<hr>',
            val='**[インターフェイス概要]** 現在の線の破線のスタイル設定を'
            '取得します。<hr>'),
        Mapping(
            key='  - Line dash setting.',
            val='  - 線の破線のスタイル設定。'),
        Mapping(
            key='The getter or setter interface value becomes '
            '(or requires) the `LineDotSetting` instance value.',
            val='getterやsetterのインターフェイスの値は`LineDotSetting`'
            'クラスのインスタンスの値となります。'),
        Mapping(
            key='## line_dot_setting property API',
            val='## line_dot_setting 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s '
            'line dot setting.<hr>',
            val='**[インターフェイス概要]** このインスタンスの線の点線のスタイル'
            '設定を取得します。<hr>'),
        Mapping(
            key='  - Lien dot setting.',
            val='  - 線の点線のスタイル設定。'),
        Mapping(
            key='The getter or setter interface value becomes '
            '(or requires) the `LineRoundDotSetting` instance value.',
            val='getterやsetterのインターフェイスの値は`interface`クラスの'
            'インスタンスの値になります。'),
        Mapping(
            key='## line_round_dot_setting property API',
            val='## line_round_dot_setting 属性のAPI'),
        Mapping(
            key='  - Line round dot setting.',
            val='  - 線の丸ドットのスタイル設定。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line round dot '
            'setting.<hr>',
            val='**[インターフェイス]** インスタンスの線の丸ドットの'
            'スタイル設定を取得します。<hr>'),
        Mapping(
            key='## Line-color setting',
            val='## 線の色の設定'),
        Mapping(
            key='- Six characters, e.g., `#00aaff`.',
            val='- `#00aaff`などの6文字による指定。'),
        Mapping(
            key='- Three characters, e.g., `#0af` (this becomes '
            '`#00aaff`).',
            val='- `#0af`などの3文字による指定（これは`#00aaff`と同じ'
            '値として扱われます）。'),
        Mapping(
            key='- Single character, e.g., `#5` (this becomes `#000005`).',
            val='- `#5`などの1文字による指定（これは`000005`と同じ値'
            'として扱われます）。'),
        Mapping(
            key='- Skipped `#` symbol, e.g., `0af` (this becomes '
            '`#00aaff`).',
            val='- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値'
            'として扱われます）。'),
        Mapping(
            key='- Blank string, e.g., `\'\'` (this clears line color '
            'setting).',
            val='- `\'\'`などの空文字の指定（これは線の色の削除指定として'
            '扱われます）。`'),
        Mapping(
            key='## Line thickness setting',
            val='## 線幅の設定'),
        Mapping(
            key='## Line alpha (opacity) setting',
            val='## 線の透明度の設定'),
        Mapping(
            key='## Line cap setting',
            val='## 線端の設定'),
        Mapping(
            key='There are three `LineCaps` options, as follows:',
            val='以下のように`LineCaps`のオプションは3種類存在します:'),
        Mapping(
            key='- BUTT: This is the default value, and it sets no cap.',
            val='- BUTT: デフォルト値であり、端にはなにも設定されません。'),
        Mapping(
            key='- ROUND: This changes the line edge to the rounded one.',
            val='- ROUND: 線の端のスタイルを丸くします。'),
        Mapping(
            key='- SQUARE: This is similar to BUTT, but it increases '
            'the line length by the squared edge.',
            val='- SQUARE: 線の端のスタイルを四角くします。これはBUTTと'
            '似た表示になりますが、設定される四角の分だけ線が長くなります。'),
        Mapping(
            key='## Line joints setting',
            val='## 線の繋ぎ目の設定'),
        Mapping(
            key='There are three LineJoints enum values, as follows:',
            val='以下のようにLineJointsのenumには3つの値が存在します:'),
        Mapping(
            key='- MITER: This setting sets the style like a picture '
            'frame vertices. This setting is the default style setting.',
            val='- MITER: この設定は頂点が（尖った形での）額縁のような'
            '形のスタイルが設定されます。この設定がデフォルトのスタイルと'
            'なります。'),
        Mapping(
            key='- ROUND: This setting sets the rounded vertices style.',
            val='- ROUND: この設定は丸い頂点のスタイルを設定します。'),
        Mapping(
            key='- BEVEL: This setting sets a beveled vertices style.',
            val='- BEVEL: この設定は射角（ベベル）の頂点のスタイルを設定します。'),
        Mapping(
            key='## Line dot setting',
            val='## 線の点線設定'),
        Mapping(
            key='Notes: This setting will be ignored by `draw_line`, '
            '`draw_dotted_line`, `draw_dashed_line`, '
            '`draw_round_dotted_line`, and `draw_dash_dotted_line` '
            'interfaces.',
            val='特記事項: この設定は`draw_line`、`draw_dotted_line`、'
            '`draw_dashed_line`、`draw_round_dotted_line`、'
            '`draw_dash_dotted_line`の各インターフェイスで無視されます。'),
        Mapping(
            key='## Line dash setting',
            val='## 線の破線設定'),
        Mapping(
            key='## Line round dot setting',
            val='## 線の丸ドット設定'),
        Mapping(
            key='Notes: Since this setting uses the `cap` setting '
            'internally, this setting ignores the `cap` setting, '
            'increasing the line length by the capsize.',
            val='特記事項: この設定は内部で`cap`設定の値を使用している'
            'ため、この設定では`cap`引数の設定が無視されます。また、丸の'
            'サイズに応じた分だけ線の長さが長くなります。'),
        Mapping(
            key='## Line dash-dot setting',
            val='## 線の一点鎖線の設定'),
        Mapping(
            key='## line_style API',
            val='## line_style API'),
        Mapping(
            key='**[Interface summary]** Set line style values.<hr>',
            val='**[インターフェイス概要]** 線のスタイルを設定します。<hr>'),
        Mapping(
            key='  - Line thickness (minimum value is 1).',
            val='  - 線の幅（1以上の値を受け付けます）。'),
        Mapping(
            key='  - Line cap (edge style) setting. The not line-related '
            'graphics (e.g., Rectangle ignores this, conversely used '
            'by Polyline) ignore this setting.',
            val='  - 線の端のスタイル設定。線に関係しないRectangleクラスなどの'
            'グラフィックスインスタンスはこの設定を無視します。逆に'
            'Polylineクラスなどの線に関係したインスタンスではこの設定を'
            '使用します。'),
        Mapping(
            key='  - Line vertices (joints) style setting. The not '
            'polyline-related graphics (e.g., Rectangle ignores '
            'this, conversely used by Polyline) ignore this setting.',
            val='  - 線の頂点（接合部）のスタイル設定。折れ線線に関係しないRectangle'
            'などのグラフィックスインスタンスはこの設定を無視します。'
            '逆にPolylineクラスなどの折れ線関係のクラスではこの設定を'
            '使用します。'),
        Mapping(
            key='  - Dot setting. If this is specified, it makes a '
            'line dotted.',
            val='  - 点線の設定。もしもこの引数が指定された場合、線は点線になります。'),
        Mapping(
            key='  - Dash setting. If this is specified, it makes a '
            'line dashed.',
            val='  - 破線の設定。もしこの引数が指定された場合、線は破線になります。'),
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
            val='  - 丸ドットの設定。もしこの引数が指定された場合、線は丸ドット'
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
            val='  - 一点鎖線のスタイル設定。もしこの引数が指定された'
            '場合、線の一点鎖線になります。'),
        Mapping(
            key='**[Interface summary]** Get current line color.<hr>',
            val='**[インターフェイス概要]** 現在の線の色を取得します。<hr>'),
        Mapping(
            key='## line_thickness property API',
            val='## line_thickness 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line thickness.<hr>',
            val='**[インターフェイス概要]** 現在の線の線幅を取得します。<hr>'),
        Mapping(
            key='  - Current line thickness.',
            val='  - 現在の線幅。'),
        Mapping(
            key='**[Interface summary]** Get current line color opacity.<hr>',
            val='**[インターフェイス概要]** 現在の線の透明度を取得します。<hr>'),
        Mapping(
            key='  - Current line opacity (0.0 to 1.0).',
            val='  - 現在の線の透明度（0.0～1.0）。'),
        Mapping(
            key='## line_cap property API',
            val='## line_cap 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line cap '
            '(edge) style setting.<hr>',
            val='**[インターフェイス概要]** 現在の線の端のスタイル設定。<hr>'),
        Mapping(
            key='  - Current line cap (edge) style setting.',
            val='  - 現在の線の端のスタイル設定。'),
        Mapping(
            key='## line_joints property API',
            val='## line_joints 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line joints '
            '(vertices) style setting.<hr>',
            val='**[インターフェイス概要]** 現在の線の接合部（頂点）のスタイル'
            '設定を取得します。<hr>'),
        Mapping(
            key='  - Current line joints (vertices) style setting.',
            val='  - 現在の線の接合部（頂点）のスタイル設定。'),
        Mapping(
            key='**[Interface summary]** Get current line dot setting.<hr>',
            val='**[インターフェイス概要]** 現在の線の点線設定を取得します。<hr>'),
        Mapping(
            key='  - Current line dot setting.',
            val='  - 現在の点線設定。'),
        Mapping(
            key='  - Current line dash setting.',
            val='  - 現在の破線設定。'),
        Mapping(
            key='**[Interface summary]** Get current line round dot '
            'setting.<hr>',
            val='**[インターフェイス概要]** 現在の線の丸ドットのスタイル設定を'
            '取得します。<hr>'),
        Mapping(
            key='  - Current line round dot setting.',
            val='  - 現在の線の丸ドットのスタイル設定。'),
        Mapping(
            key='## line_dash_dot_setting property API',
            val='## line_dash_dot_setting 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get current line dash dot '
            'setting.<hr>',
            val='**[インターフェイス概要]** 現在の線の一点鎖線のスタイル'
            '設定を取得します。<hr>'),
        Mapping(
            key='  - Line color opacity (0.0 to 1.0).',
            val='  - 線色の透明度（0.0～1.0）。'),
        Mapping(
            key='  - Current line dash dot setting.',
            val='  - 現在の一点鎖線のスタイル設定。'),
        Mapping(
            key='The getter or setter interface value becomes (or requires) '
            'the `Int` value.',
            val='getterもしくはsetterの各インターフェイスの値は`Int`型の値に'
            'なります。'),
        Mapping(
            key='**[Interface summary]** Get this instance\'s line '
            'thickness.<hr>',
            val='**[インターフェイス概要]** このインスタンスの線幅を'
            '取得します。<hr>'),
        Mapping(
            key='## What interfaces are they?',
            val='## 各インターフェイスの概要'),
        Mapping(
            key='If you click the following line, line style will be '
            'updated:',
            val='もし以下の四角をクリックし0た場合、線のスタイルは更新'
            'されます:'),
        Mapping(
            key='## move_to API',
            val='## move_to API'),
        Mapping(
            key='**[Interface summary]** Move a line position to a '
            'specified point.<hr>',
            val='**[インターフェイス概要]** 指定された座標に線の描画位置を'
            '移動させます。<hr>'),
        Mapping(
            key='  - X destination point to move.',
            val='  - 移動先となるX座標。'),
        Mapping(
            key='  - Y destination point to move.',
            val='  - 移動先となるY座標。'),
        Mapping(
            key='  - Line graphics instance.',
            val='  - 線のグラフィックスのインスタンス。'),
        Mapping(
            key='## line_to API',
            val='## line_to API'),
        Mapping(
            key='**[Interface summary]** Draw a line from '
            'previous point to specified point (initial '
            'point is x = 0, y = 0).<hr>',
            val='**[インターフェイス概要]** 直前の位置の座標から'
            '指定された座標に向けて線を描画します（初期位置は'
            'x=0, y=0になります）。<hr>'),
        Mapping(
            key='  - X destination point to draw a line.',
            val='  - 線の描画先となる終点のX座標。'),
        Mapping(
            key='  - Y destination point to draw a line.',
            val='  - 線の描画先となる終点のY座標。'),
        Mapping(
            key='## Return values',
            val='## 各返却値について'),
        Mapping(
            key='## If constructor API',
            val='## If クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** A class to append if branch '
            'instruction expression.<hr>',
            val='**[インターフェイス概要]** if文の分岐制御の表現を'
            '追加するためのクラス。<hr>'),
        Mapping(
            key='  - Current scope\'s local variables. Set locals() '
            'value to this argument. If specified, this '
            'interface reverts all local scope VariableNameInterface '
            'variables (like Int, Sprite) at the end of an `If` '
            'scope. This setting is useful when you don\'t want '
            'to update each variable by implementing the `If` scope.',
            val='  - 現在のスコープの各ローカル変数。指定する場合にはlocals()'
            '関数の値をごの引数に指定してください。もし指定された場合、'
            'このインターフェイスは`If`のスコープの終了時に対象の'
            'VariableNameInterfaceクラスの各ローカル変数のインスタンス'
            'の値をスコープの開始前の時点に復元します。この設定は`If`の'
            'スコープ内の処理でPython上の各ローカル変数の値を更新したくない'
            '場合などに便利なことがあります。'),
        Mapping(
            key='## Project links',
            val='## プロジェクトの関連リンク'),
        Mapping(
            key='- [GitHub](https://github.com/simon-ritchie/apysc)',
            val='- [GitHub](https://github.com/simon-ritchie/apysc)'),
        Mapping(
            key='- [Twitter](https://twitter.com/apysc)',
            val='- [Twitter](https://twitter.com/apysc)'),
        Mapping(
            key='- [PyPI](https://pypi.org/project/apysc/)',
            val='- [PyPI](https://pypi.org/project/apysc/)'),
        Mapping(
            key='What apysc can do in its current implementation',
            val='apyscが現在の実装で出来ることの概要'),
        Mapping(
            key='## Contents',
            val='## コンテンツ'),
        Mapping(
            key='## Quick start guide',
            val='## クイックスタートガイド'),
        Mapping(
            key='Quick start guide',
            val='クイックスタートガイド'),
        Mapping(
            key='import conventions',
            val='import の慣習'),
        Mapping(
            key='## Container classes',
            val='## コンテナーの各クラス'),
        Mapping(
            key='Stage class',
            val='Stage クラス'),
        Mapping(
            key='Sprite class',
            val='Sprite クラス'),
        Mapping(
            key='## Exporting',
            val='## 出力処理'),
        Mapping(
            key='save_overall_html interface',
            val='save_overall_html インターフェイス'),
        Mapping(
            key='display_on_jupyter interface',
            val='display_on_jupyter インターフェイス'),
        Mapping(
            key='display_on_colaboratory interface',
            val='display_on_colaboratory インターフェイス'),
        Mapping(
            key='append_js_expression interface',
            val='append_js_expression インターフェイス'),
        Mapping(
            key='## apysc basic data classes',
            val='## apyscの基本的な各データクラス'),
        Mapping(
            key='Int and Number classes',
            val='Int と Number の各クラス'),
        Mapping(
            key='Int and Number classes common arithmetic operations',
            val='Int と Number クラスの共通の計算制御'),
        Mapping(
            key='Int and Number classes common comparison operations',
            val='Int と Number クラスの共通の比較制御'),
        Mapping(
            key='String class',
            val='String クラス'),
        Mapping(
            key='String class comparison operations',
            val='String クラスの比較制御'),
        Mapping(
            key='String class comparison operations document',
            val='String クラスの比較制御'),
        Mapping(
            key='String class addition and multiplication operations',
            val='String クラスの加算と乗算の制御'),
        Mapping(
            key='String class addition and multiplication operations '
            'document',
            val='String クラスの加算と乗算の制御'),
        Mapping(
            key='Boolean class',
            val='Boolean クラス'),
        Mapping(
            key='Array class',
            val='Array クラス'),
        Mapping(
            key='Dictionary class',
            val='Dictionary クラス'),
        Mapping(
            key='Dictionary class generic type settings',
            val='Dictionary クラスのジェネリックの型設定'),
        Mapping(
            key='Dictionary class get interface',
            val='Dictionary クラスの get インターフェイス'),
        Mapping(
            key='Dictionary class length interface',
            val='Dictionary クラスの length インターフェイス'),
        Mapping(
            key='Point2D class',
            val='Point2D クラス'),
        Mapping(
            key='## DisplayObject and GraphicsBase classes',
            val='## DisplayObject と GraphicsBase の各クラス'),
        Mapping(
            key='DisplayObject and GraphicsBase classes basic '
            'properties abstract',
            val='DisplayObject と GraphicsBase の各クラスの'
            '基本的な各属性の概要'),
        Mapping(
            key='DisplayObject class get_css and set_css interfaces',
            val='DisplayObject クラスの get_css と set_css '
            'の各インターフェイス'),
        Mapping(
            key='## Graphics class',
            val='## Graphics クラス'),
        Mapping(
            key='Draw interfaces abstract',
            val='描画の各インターフェイスの概要'),
        Mapping(
            key='## Common event interfaces',
            val='## イベントの共通の各インターフェイス'),
        Mapping(
            key='About the handler options type',
            val='ハンドラの options パラメーターの型について'),
        Mapping(
            key='Event class prevent_default and stop_propagation interfaces',
            val='Event クラスの prevent_default と stop_propagation '
            'の各インターフェイス'),
        Mapping(
            key='bind_custom_event and trigger_custom_event interfaces',
            val='bind_custom_event と trigger_custom_event '
            'の各インターフェイス'),
        Mapping(
            key='## MouseEvent class and mouse event binding',
            val='## MouseEvent クラスとマウスイベントの設定'),
        Mapping(
            key='MouseEvent interfaces abstract',
            val='MouseEvent クラスの各インターフェイスの概要'),
        Mapping(
            key='dblclick interface',
            val='dblclick インターフェイス'),
        Mapping(
            key='## Branch instruction',
            val='## 条件分岐の制御'),
        Mapping(
            key='Each branch instruction class scope variables reverting '
            'setting',
            val='各条件分岐のクラスのスコープ内の変数値の復元設定'),
        Mapping(
            key='Return class',
            val='Return クラス'),
        Mapping(
            key='For loop class',
            val='ループ用の For クラス'),
        Mapping(
            key='Continue class',
            val='Continue クラス'),
        Mapping(
            key='## Loop',
            val='## ループ'),
        Mapping(
            key='## Timer',
            val='## タイマー'),
        Mapping(
            key='Timer class',
            val='Timer クラス'),
        Mapping(
            key='TimerEvent class',
            val='TimerEvent クラス'),
        Mapping(
            key='FPS enum',
            val='FPS の enum'),
        Mapping(
            key='Timer class repeat_count setting',
            val='Timer クラスの repeat_count 設定'),
        Mapping(
            key='Timer class start and stop interfaces',
            val='Timer クラスの start と stop の各インターフェイス'),
        Mapping(
            key='Timer class timer_complete interface',
            val='Timer クラスの timer_complete インターフェイス'),
        Mapping(
            key='Timer class reset interface',
            val='Timer クラスの reset インターフェイス'),
        Mapping(
            key='## Animation',
            val='## アニメーション'),
        Mapping(
            key='Animation interfaces abstract',
            val='アニメーションの各インターフェイスの概要'),
        Mapping(
            key='AnimationEvent class',
            val='AnimationEvent クラス'),
        Mapping(
            key='Animation duration setting',
            val='Animation クラスの duration 設定'),
        Mapping(
            key='Animation delay setting',
            val='Animation クラスの delay 設定'),
        Mapping(
            key='Each animation interface return value',
            val='アニメーションの各インターフェイスの返却値について'),
        Mapping(
            key='AnimationBase class start interface',
            val='AnimationBase クラスの start インターフェイス'),
        Mapping(
            key='AnimationBase class animation_complete interface',
            val='AnimationBase クラスの animation_complete '
            'インターフェイス'),
        Mapping(
            key='AnimationBase class interfaces method chaining',
            val='AnimationBase クラスの各インターフェイスの'
            'メソッドチェーンについて'),
        Mapping(
            key='AnimationBase class target property',
            val='AnimationBase クラスの target 属性'),
        Mapping(
            key='Animation pause and play interfaces',
            val='アニメーションの pause と play の各インターフェイス'),
        Mapping(
            key='Animation reset interface',
            val='アニメーションの reset インターフェイス'),
        Mapping(
            key='Animation finish interface',
            val='アニメーションの finish インターフェイス'),
        Mapping(
            key='Animation reverse interface',
            val='アニメーションの reverse インターフェイス'),
        Mapping(
            key='animation_time interface',
            val='animation_time インターフェイス'),
        Mapping(
            key='Easing enum',
            val='イージングの enum'),
        Mapping(
            key='Sequential animation setting',
            val='連続したアニメーション設定'),
        Mapping(
            key='animation_parallel interface',
            val='animation_parallel インターフェイス'),
        Mapping(
            key='animation_move interface',
            val='animation_move インターフェイス'),
        Mapping(
            key='animation_x interface',
            val='animation_x インターフェイス'),
        Mapping(
            key='animation_y interface',
            val='animation_y インターフェイス'),
        Mapping(
            key='animation_width and animation_height interfaces',
            val='animation_width と animation_height の各インターフェイス'),
        Mapping(
            key='animation_fill_color interface',
            val='animation_fill_color インターフェイス'),
        Mapping(
            key='animation_fill_alpha interface',
            val='animation_fill_alpha インターフェイス'),
        Mapping(
            key='animation_line_color interface',
            val='animation_line_color インターフェイス'),
        Mapping(
            key='animation_line_alpha interface',
            val='animation_line_alpha インターフェイス'),
        Mapping(
            key='animation_line_thickness interface',
            val='animation_line_thickness インターフェイス'),
        Mapping(
            key='animation_radius interface',
            val='animation_radius インターフェイス'),
        Mapping(
            key='animation_rotation_around_center interface',
            val='animation_rotation_around_center インターフェイス'),
        Mapping(
            key='animation_rotation_around_point interface',
            val='animation_rotation_around_point インターフェイス'),
        Mapping(
            key='animation_scale_x_from_center and '
            'animation_scale_y_from_center interfaces',
            val='animation_scale_x_from_center と '
            'animation_scale_y_from_center の各インターフェイス'),
        Mapping(
            key='animation_scale_x_from_point and '
            'animation_scale_y_from_point interfaces',
            val='animation_scale_x_from_point と '
            'animation_scale_y_from_point の各インターフェイス'),
        Mapping(
            key='animation_skew_x interface',
            val='animation_skew_x インターフェイス'),
        Mapping(
            key='## Debugging',
            val='## デバッグ'),
        Mapping(
            key='trace function interface',
            val='trace 関数のインターフェイス'),
        Mapping(
            key='set_debug_mode interface',
            val='set_debug_mode インターフェイス'),
        Mapping(
            key='unset_debug_mode interface',
            val='unset_debug_mode インターフェイス'),
        Mapping(
            key='## Testing',
            val='## テスト'),
        Mapping(
            key='assert_equal and assert_not_equal interfaces',
            val='assert_equal と assert_not_equal の各インターフェイス'),
        Mapping(
            key='assert_true and assert_false interfaces',
            val='assert_true と assert_false の各インターフェイス'),
        Mapping(
            key='assert_arrays_equal and assert_arrays_not_equal interfaces',
            val='assert_arrays_equal と assert_arrays_not_equal の'
            '各インターフェイス'),
        Mapping(
            key='assert_dicts_equal and assert_dicts_not_equal interfaces',
            val='assert_dicts_equal と assert_dicts_not_equal の'
            '各インターフェイス'),
        Mapping(
            key='assert_defined and assert_undefined interfaces',
            val='assert_defined と assert_undefined の各インターフェイス'),
        Mapping(
            key='## Child-related interfaces',
            val='## 子要素関係の各インターフェイス'),
        Mapping(
            key='## Common behaviors',
            val='## 共通の挙動'),
        Mapping(
            key='## Addition',
            val='## 加算'),
        Mapping(
            key='## Subtraction',
            val='## 減算'),
        Mapping(
            key='## Multiplication',
            val='## 乗算'),
        Mapping(
            key='## Division',
            val='## 除算'),
        Mapping(
            key='## Floor division',
            val='## 切り捨て除算'),
        Mapping(
            key='## Modulo',
            val='## 剰余'),
        Mapping(
            key='## Equal comparison operator',
            val='## 等値条件の比較のオペレーター'),
        Mapping(
            key='You can use the `==` operator for the equal comparison:',
            val='`==`のオペレーターを使って等値条件の比較を行うことができます。'),
        Mapping(
            key='## Not equal comparison operator',
            val='## 非等値条件の比較のオペレーター'),
        Mapping(
            key='You can use the `!=` operator for the not equal comparison:',
            val='`!=`のオペレーターを使って非等値条件の比較を行うことができます。'),
        Mapping(
            key='## Less than comparison operator',
            val='## 未満条件の比較のオペレーター'),
        Mapping(
            key='You can use the `<` operator for the less than comparison:',
            val='`<`のオペレーターを使って未満条件の比較を行うことができます。'),
        Mapping(
            key='## Less than or equal comparison operator',
            val='## 以下条件の比較のオペレーター'),
        Mapping(
            key='You can use the `<=` operator for the less than or equal '
            'comparison:',
            val='`<=`のオペレーターを使って以下条件の比較を行うことができます。'),
        Mapping(
            key='## Greater than comparison operator',
            val='## 超過条件の比較のオペレーター'),
        Mapping(
            key='You can use the `>` operator for the greater than '
            'comparison:',
            val='`>`のオペレーターを使って超過条件の比較を行うことができます。'),
        Mapping(
            key='## Greater than or equal comparison operator',
            val='## 以上条件の比較のオペレーター'),
        Mapping(
            key='You can use the `>=` operator for the greater than or '
            'equal comparison:',
            val='`>=`のオペレーターを使って以上条件の比較を行うことができます。'),
        Mapping(
            key='## Int class',
            val='## Int クラス'),
        Mapping(
            key='## Number class',
            val='## Number クラス'),
        Mapping(
            key='## Note for the Float class alias',
            val='## Floatクラスのエイリアスの特記事項'),
        Mapping(
            key='## Int and Number classes basic interfaces',
            val='## Int と Number クラスの基本的なインターフェイス'),
        Mapping(
            key='Int and Number classes basic arithmetic operations',
            val='Int と Number クラスの基本的な各計算の制御'),
        Mapping(
            key='Int and Number classes basic comparison operations',
            val='Int と Number クラスの基本的な各比較の制御'),
        Mapping(
            key='## Int class constructor API',
            val='## Int クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** Integer class for apysc '
            'library.<hr>',
            val='**[インターフェイス概要]** apyscライブラリ上の整数のための'
            'クラスです。<hr>'),
        Mapping(
            key='  - Initial integer value. If the `float` or `Number` '
            'value is specified, this class casts it to an integer.',
            val='  - 整数の初期値。もしも`float`や`Number`の値が指定された'
            '場合このクラスは値を整数へと変換します。'),
        Mapping(
            key='Int and Number common arithmetic operations document',
            val='Int と Number クラスの共通の各計算制御'),
        Mapping(
            key='Int and Number common comparison operations document',
            val='Int と Number クラスの共通の各比較制御'),
        Mapping(
            key='## Number class constructor API',
            val='## Number クラスのコンストラクタのAPI'),
        Mapping(
            key='  - Initial floating point number value. This class '
            'casts it to float if you specify int or Int value.',
            val='  - 浮動小数点数の初期値。もしもintやIntなどの型の値が指定された'
            '場合このクラスは値を浮動小数点数へ変換します。'),
        Mapping(
            key='The `Float` class is the alias of the Number, and '
            'it behaves the same as the Number class.<hr>',
            val='`Float`クラスはNumberクラスのエイリアスであり、このエイリアスは'
            'Numberクラスと同様に動作します。<hr>'),
        Mapping(
            key='**[Interface summary]** Get a current number value.<hr>',
            val='**[インターフェイス概要]** 現在の数値を取得します。<hr>'),
        Mapping(
            key='  - Current number value.',
            val='  - 現在の数値。'),
        Mapping(
            key='**[Interface summary]** Floating point number class for '
            'apysc library.<hr>',
            val='**[インターフェイス概要]** apyscライブラリ用の浮動小数点数の'
            'クラスです。<hr>'),
        Mapping(
            key='### Table of contents',
            val='### Table of contents'),
        Mapping(
            key='## What apysc can do in its interfaces',
            val='## これらの各インターフェイスでapyscが出来ること'),
        Mapping(
            key='## stage_x property API',
            val='## stage_x 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get the x-coordinate of the stage '
            'reference.<hr>',
            val='**[インターフェイス概要]** ステージ基準のX座標を取得します。<hr>'),
        Mapping(
            key='## stage_y property API',
            val='## stage_y 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get the y-coordinate of the stage '
            'reference.<hr>',
            val='**[インターフェイス概要]** ステージ基準のY座標を取得します。<hr>'),
        Mapping(
            key='  - x-coordinate.',
            val='  - X座標。'),
        Mapping(
            key='  - y-coordinate.',
            val='  - Y座標。'),
        Mapping(
            key='## local_x property API',
            val='## local_x 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a local x-coordinate '
            'event listening instance. For example, this value '
            'becomes x-coordinate from Sprite\'s left-end position '
            'by clicking a Sprite instance.<hr>',
            val='**[インターフェイス概要]** イベントが設定されている'
            'インスタンス内の相対座標のX座標を取得します。例えばSpriteの'
            'インスタンスをクリックした場合にはSpriteの左上の位置を基準'
            'とした座標になります。<hr>'),
        Mapping(
            key='## local_y property API',
            val='## local_y 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get the local y-coordinate '
            'of the event listening instance. For example, this '
            'value becomes y-coordinate from Sprite\'s top-end '
            'position by clicking a Sprite instance.<hr>',
            val='**[インターフェイス概要]** イベントが設定されている'
            'インスタンスないの相対座標のY座標を取得します。例えばSpriteの'
            'インスタンスをクリックした場合にはSpriteの左上の位置を基準'
            'とした座標になります。<hr>'),
        Mapping(
            key='## this property API',
            val='## this 属性のAPI'),
        Mapping(
            key='  - Instance that listening this event.',
            val='  - このイベントが設定されているインスタンス。'),
        Mapping(
            key='**[Interface summary]** Get an instance of listening to '
            'this event.<hr>',
            val='**[インターフェイス概要]** このイベントが設定されている'
            'インスタンスを取得します。<hr>'),
        Mapping(
            key='The following page describes the basic mouse event '
            'interfaces:',
            val='以下のページでは基本的なマウスイベントのインターフェイスに'
            'ついて説明しています:'),
        Mapping(
            key='## Unbind interfaces',
            val='## 解除用のインターフェイス'),
        Mapping(
            key='## mousedown API',
            val='## mousedown API'),
        Mapping(
            key='**[Interface summary]** Add mouse down event listener '
            'setting.<hr>',
            val='**[インターフェイス概要]** マウスのボタンを押した時のイベント'
            '設定を追加します。<hr>'),
        Mapping(
            key='  - Callable that would be called when mouse down on '
            'this instance.',
            val='  - インスタンス上でマウスのボタンを押した時に呼ばれる関数'
            'もしくはメソッド。'),
        Mapping(
            key='## unbind_mousedown API',
            val='## unbind_mousedown API'),
        Mapping(
            key='**[Interface summary]** Unbind a specified handler\'s '
            'mouse down event.<hr>',
            val='**[インターフェイス概要]** マウスのボタンを押した際のイベントの'
            '指定されたハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## unbind_mousedown_all API',
            val='## unbind_mousedown_all API'),
        Mapping(
            key='**[Interface summary]** Unbind all mouse down events.<hr>',
            val='**[インターフェイス概要]** マウスのボタンを押した時のイベントの'
            '全てのハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## mouseup API',
            val='## mouseup API'),
        Mapping(
            key='**[Interface summary]** Add mouse up event listener '
            'setting.<hr>',
            val='**[インターフェイス概要]** マウスのボタンを離した時の'
            'イベント設定を追加します。<hr>'),
        Mapping(
            key='  - Callable that would be called when mouse-up on this '
            'instance.',
            val='  - インスタンス上でマウスのボタンを離した時に呼ばれる'
            '関数もしくはメソッド。'),
        Mapping(
            key='## unbind_mouseup API',
            val='## unbind_mouseup API'),
        Mapping(
            key='**[Interface summary]** Unbind a specified handler\'s '
            'mouse-up event.<hr>',
            val='**[インターフェイス概要]** マウスのボタンを離した際のイベントの'
            '指定されたハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## unbind_mouseup_all API',
            val='## unbind_mouseup_all API'),
        Mapping(
            key='**[Interface summary]** Unbind all mouse up events.<hr>',
            val='**[インターフェイス概要]** マウスのボタンを離したとぎのイベントの'
            '全てのハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## mousemove API',
            val='## mousemove API'),
        Mapping(
            key='**[Interface summary]** Add mouse move event listener '
            'setting.<hr>',
            val='**[インターフェイス概要]** マウスを動かした時のイベント設定を'
            '追加します。<hr>'),
        Mapping(
            key='  - Callable that would be called when mousemove on '
            'this instance.',
            val='  - インスタンス上でマウスを動かした際に呼ばれる関数'
            'もしくはメソッド。'),
        Mapping(
            key='## unbind_mousemove API',
            val='## unbind_mousemove API'),
        Mapping(
            key='**[Interface summary]** Unbind a specified handler\'s '
            'mouse move event.<hr>',
            val='**[インターフェイス概要]** マウスカーソルを動かした際の'
            'イベントで指定されたハンドラの設定を解除します。<hr>'),
        Mapping(
            key='## unbind_mousemove_all API',
            val='## unbind_mousemove_all API'),
        Mapping(
            key='**[Interface summary]** Unbind all mouse move events.<hr>',
            val='**[インターフェイス概要]** マウスカーソルを動かしたときのイベントの'
            '全てのハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## mouseover API',
            val='## mouseover API'),
        Mapping(
            key='**[Interface summary]** Add mouse over event listener '
            'setting.<hr>',
            val='**[インターフェイス概要]** マウスカーソルが乗った時のイベントの'
            'ハンドラ設定を追加します。<hr>'),
        Mapping(
            key='  - Callable that would be called when mouse over on '
            'this instance.',
            val='  - インスタンス上にマウスカーソルが乗った際に呼ばれる関数'
            'もしくはメソッド。'),
        Mapping(
            key='## unbind_mouseover API',
            val='## unbind_mouseover API'),
        Mapping(
            key='**[Interface summary]** Unbind a specified handler\'s '
            'mouseover event.<hr>',
            val='**[インターフェイス概要]** マウスカーソルが乗った際のイベントの'
            '指定されたハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## unbind_mouseover_all API',
            val='## unbind_mouseover_all API'),
        Mapping(
            key='**[Interface summary]** Unbind all mouseover events.<hr>',
            val='**[インターフェイス概要]** マウスカーソルが乗った際のイベントの'
            '全てのハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## mouseout API',
            val='## mouseout API'),
        Mapping(
            key='**[Interface summary]** Add mouse out event listener '
            'setting.<hr>',
            val='**[インターフェイス概要]** マウスカーソルがインスタンス上から'
            '離れた際のイベントのハンドラを設定します。<hr>'),
        Mapping(
            key='  - Callable that would be called when mouse out on '
            'this instance.',
            val='  - インスタンス上からマウスカーソルが離れた際のイベントの'
            '対象のハンドラ設定を解除します。'),
        Mapping(
            key='## unbind_mouseout API',
            val='## unbind_mouseout API'),
        Mapping(
            key='**[Interface summary]** Unbind a specified handler\'s '
            'mouse-out event.<hr>',
            val='**[インターフェイス概要]** インスタンス上からマウスカーソルが'
            '離れた際のイベントの対象のハンドラ設定を解除します。<hr>'),
        Mapping(
            key='## unbind_mouseout_all API',
            val='## unbind_mouseout_all API'),
        Mapping(
            key='**[Interface summary]** Unbind all mouse out events.<hr>',
            val='**[インターフェイス概要]** インスタンス上からマウスカーソルが'
            '離れた際のイベントのハンドラ設定を全て解除します。<hr>'),
        Mapping(
            key='## num_children API',
            val='## num_children API'),
        Mapping(
            key='**[Interface summary]** Get a current children\'s '
            'number.<hr>',
            val='**[インターフェイス概要]** 現在の子の数を取得します。<hr>'),
        Mapping(
            key='  - Current children number.',
            val='  - 現在の子の数。'),
        Mapping(
            key='## Point2D class constructor API',
            val='## Point2D クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** 2-dimensional geometry point.<hr>',
            val='**[インターフェイス概要]** 2次元の座標値を扱うクラスです。<hr>'),
        Mapping(
            key='**[Interface summary]** X-coordinate property.<hr>',
            val='**[インターフェイス概要]** X座標の属性のインターフェイスです。<hr>'),
        Mapping(
            key='**[Interface summary]** Y-coordinate property.<hr>',
            val='**[インターフェイス概要]** Y座標の属性のインターフェイスです。<hr>'),
        Mapping(
            key='## Return API',
            val='## Return API'),
        Mapping(
            key='**[Interface summary]** Class for the return '
            'expression.<hr>',
            val='**[インターフェイス概要]** return のコード表現のためのクラスです。<hr>'),
        Mapping(
            key='This class can be instantiated only in an event '
            'handler scope.<hr>',
            val='このクラスはイベントハンドラのスコープ内でのみインスタンス化'
            'することができます。<hr>'),
        Mapping(
            key='## save_overall_html API',
            val='## save_overall_html API'),
        Mapping(
            key='**[Interface summary]** Save the overall HTML and js '
            'files under the specified directory path.<hr>',
            val='**[インターフェイス概要]** 指定されたディレクトリパス以下に'
            'HTMLとJavaScriptのファイル全体を出力します。<hr>'),
        Mapping(
            key='  - Destination directory path to save each HTML and '
            'js file.',
            val='  - 各HTMLとJavaScriptファイルの保存先となるディレクトリパス。'),
        Mapping(
            key='  - Boolean value indicates whether minify HTML and '
            'js or not. The False setting is helpful when debugging.',
            val='  - HTMLとJavaScriptの内容を最小化（minify）するかどうかの'
            '真偽値。Falseの設定はデバッグ時などに便利な時があります。'),
        Mapping(
            key='  - JavaScript libraries directory path. This setting '
            'applies to a JavaScript source path in HTML. If not '
            'specified, then set the same directory with HTML. This '
            'setting is maybe helpful to set js lib directory, such '
            'as Django\'s static (static_collected) directory. This '
            'interface recommends setting True value to the '
            '`skip_js_lib_exporting` argument if this argument sets.',
            val='  - JavaScriptライブラリのパスの設定。この設定はHTML内の'
            'JavaScriptのコードのパスの指定部分に影響します。指定されていない'
            '場合にはHTMLと同じディレクトリが設定されます。この設定はDjango'
            'のようなライブラリの静的ファイルのディレクトリを指定する場合などに'
            '便利なことがあります。もしこの引数が設定された場合には'
            '`skip_js_lib_exporting`の設定も有効にすることが推奨されます。'),
        Mapping(
            key='  - If True, this interface does not export JavaScript '
            'libraries.',
            val='  - Trueが設定された場合、このインターフェイスはJavaScriptの'
            '各ライブラリを出力しなくなります。'),
        Mapping(
            key='  - Option to embed the JavaScript libraries script '
            'to the output HTML or not. If True, the output HTML becomes '
            'enormous, and be only one HTML file. Occasionally, this '
            'option is useful when sharing the exported file or using the '
            'output file with an iframe tag to avoid the CORS error.',
            val='  - 各JavaScriptライブラリを出力されるHTML内に埋め込むかどうか'
            'の設定です。もしTrueが設定された場合、出力されるHTMLは大きくなり、'
            'そして1つのHTMLファイルのみ出力されるようになります。この設定は'
            '出力されたファイルをiframeタグで使う際にCORSのエラーを回避したい'
            '時などに役立つことがあります。'),
        Mapping(
            key='  - The Logging setting. If 0 is specified, this '
            'interface does not display a logging message. If 1 or the '
            'other value is specified, this interface displays a message '
            'usually.',
            val='  - ロギング（ログ表示）の設定です。0が指定された場合、この'
            'インターフェイスはログのメッセージを表示しなくなります。1もしくは'
            '他の値を指定した場合、このインターフェイスはログのメッセージを'
            '通常通り表示します。'),
        Mapping(
            key='This interface empties a specified directory before '
            'saving.<hr>',
            val='このインターフェイスは指定された出力先のディレクトリを'
            '出力前に空にします。<hr>'),
        Mapping(
            key='animation_complete interface document',
            val='animation_complete インターフェイス'),
        Mapping(
            key='## set_debug_mode API',
            val='## set_debug_mode API'),
        Mapping(
            key='**[Interface summary]** Set the debug mode for the '
            'HTML and JavaScript debugging. If calling this function, '
            'this interface applies the following setting: ',
            val='**[インターフェイス概要]** HTMLとJavaScriptのデバッグ用に'
            'デバッグモードの設定を行います。もしこの関数を呼び出した場合、'
            'のインターフェイスは以下の設定を追加します: '),
        Mapping(
            key='<br> ・Disabling HTML minify setting. ',
            val='<br> ・HTMLの最小化（minify）設定を無効化します。 '),
        Mapping(
            key='<br> ・Changing to append per each interface JavaScript '
            'divider string.<hr>',
            val='<br> ・各インターフェイスごとのJavaScript上での区切りのための'
            '文字列を追加します。<hr>'),
        Mapping(
            key='## Stage class constructor API',
            val='## Stage クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** Create Stage (overall viewport) '
            'instance.<hr>',
            val='**[インターフェイス概要]** ステージ（描画領域全体）の'
            'インスタンスを生成します。<hr>'),
        Mapping(
            key='  - Stage width.',
            val='  - ステージの幅。'),
        Mapping(
            key='  - Stage height',
            val='  - ステージの高さ。'),
        Mapping(
            key='  - Hexadecimal background color string.',
            val='  - 16進数の背景色の文字列。'),
        Mapping(
            key='  - Specification of element to add stage. Unique '
            'tag (e.g., \'body\') or ID selector (e.g., '
            '\'#any-unique-elem\') is acceptable.',
            val='  - ステージの要素を追加先となる要素の指定。一意のタグ'
            '（例 : \'body\'）やIDのセレクタ（例 : \'#any-unique-elem\'）'
            'を受け付けることができます。'),
        Mapping(
            key='  - ID attribute set to stage html element (e.g., '
            '\'line-graph\'). If None is set, random integer will '
            'be applied.',
            val='  - ステージのHTML要素に設定されるIDの属性（例 : '
            '\'line-graph\'）。もしNoneが設定されている場合、乱数などを使った'
            '数値を使った値が設定されます。'),
        Mapping(
            key='## stage_elem_id property API',
            val='## stage_elem_id 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get stage\'s html element id.<hr>',
            val='**[インターフェイス概要]** ステージのHTML要素のIDを取得します。<hr>'),
        Mapping(
            key='  - Stage\'s html element id (not including class or id '
            'symbol). e.g., \'line-graph\'',
            val='  - ステージのHTML要素のID（ID用の#の記号などは含まれません。'
            '例 : \'line-graph\'）。'),
        Mapping(
            key='## add_child API',
            val='## add_child API'),
        Mapping(
            key='**[Interface summary]** Add display object child to this '
            'instance.<hr>',
            val='**[インターフェイス概要]** 表示オブジェクトの子をこの'
            'インスタンスへと追加します。<hr>'),
        Mapping(
            key='  - Child instance to add.',
            val='  - 追加する子のインスタンス。'),
        Mapping(
            key='## remove_child API',
            val='## remove_child API'),
        Mapping(
            key='**[Interface summary]** Remove display object child from '
            'this instance.<hr>',
            val='**[インターフェイス概要]** このインスタンスから指定された'
            '表示オブジェクトの子を取り除きます。<hr>'),
        Mapping(
            key='  - Child instance to remove.',
            val='  - 取り除く対象の子のインスタンス。'),
        Mapping(
            key='## contains API',
            val='## contains API'),
        Mapping(
            key='**[Interface summary]** Get a boolean whether this '
            'instance contains a specified child.<hr>',
            val='**[インターフェイス概要]** 指定された子のインスタンスを'
            '持っているかどうかの真偽値を取得します。<hr>'),
        Mapping(
            key='  - If this instance contains a specified child, this '
            'method returns True.',
            val='  - このインスタンスが指定された子を持つ場合Trueが設定されます。'),
        Mapping(
            key='## get_child_at API',
            val='## get_child_at API'),
        Mapping(
            key='## num_children property API',
            val='## num_children property API'),
        Mapping(
            key='**[Interface summary]** Get child at a specified '
            'index.<hr>',
            val='**[インターフェイス概要]** 指定されたインデックス位置の子を'
            '取得します。<hr>'),
        Mapping(
            key='## Acceptable comparison right-side value types',
            val='## 受け付けられる右側の値の型'),
        Mapping(
            key='## Equal comparison',
            val='## 等値条件の比較'),
        Mapping(
            key='## Not equal comparison',
            val='## 非等値条件の比較'),
        Mapping(
            key='## Less than or greater than comparison',
            val='## 未満もしくは超過条件の比較'),
        Mapping(
            key='## String class constructor API',
            val='## String クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** String class for apysc '
            'library.<hr>',
            val='**[インターフェイス概要]** apyscライブラリにおける'
            '文字列用のクラスです。<hr>'),
        Mapping(
            key='  - Initial string value.',
            val='  - 文字列の値の初期値。'),
        Mapping(
            key='**[Interface summary]** Get a current string value.<hr>',
            val='**[インターフェイス概要]** 現在の文字列の値を取得します。<hr>'),
        Mapping(
            key='  - Current string value.',
            val='  - 現在の文字列の値。'),
        Mapping(
            key='## timer_complete API',
            val='## timer_complete API'),
        Mapping(
            key='**[Interface summary]** Add a timer complete event '
            'listener setting.<hr>',
            val='**[インターフェイス概要]** タイマー終了時のイベントハンドラの'
            '設定を追加します。<hr>'),
        Mapping(
            key='  - A callable that a timer calls when complete.',
            val='  - タイマー終了時に呼ばれる関数もしくはメソッド。'),
        Mapping(
            key='## What argument is this?',
            val='## 引数の概要'),
        Mapping(
            key='## Timer constructor API',
            val='## Timer クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** Timer class to handle function '
            'calling at regular intervals.<hr>',
            val='**[インターフェイス概要]** 一定間隔ごとにハンドラの関数を実行'
            'するためのタイマーのクラスです。<hr>'),
        Mapping(
            key='  - A delay between each `Handler` calling in a '
            'millisecond or FPS value. If an `FPS` value is specified, '
            'this value becomes a millisecond calculated with that FPS '
            'value (e.g., if the `FPS_60` value is specified, then `delay` '
            'becomes 16.6666667).',
            val='  - ハンドラの実行間隔となるミリ秒もしくはFPSのenumの値。もし'
            '`FPS`の値が指定された場合、FPSに応じて計算されたミリ秒が設定'
            'されます（例えば、もし`FPS_60`が指定されていれば`delay`の値は'
            '16.6666667ミリ秒相当になります。）。'),
        Mapping(
            key='  - Max count of a `Handler`\'s calling. A timer '
            'stops if the `Handler`\'s calling count has reached '
            'this value. If 0 is specified, then a timer loops '
            'forever.',
            val='  - ハンドラの実行回数の上限値。ハンドラの実行回数が'
            'この値に到達した場合タイマーは停止します。もし0が指定された'
            '場合にはタイマーは停止しなくなります。'),
        Mapping(
            key='  - Optional arguments dictionary to pass a `Handler` '
            'callable.',
            val='  - ハンドラの関数もしくはメソッドへ渡すオプションとしての'
            '各パラメーターを格納した辞書。'),
        Mapping(
            key='Timer document',
            val='Timer クラス'),
        Mapping(
            key='TimerEvent class document',
            val='TimerEvent クラス'),
        Mapping(
            key='FPS enum document',
            val='FPS の enum'),
        Mapping(
            key='## delay property API',
            val='## delay 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a delay value.<hr>',
            val='**[インターフェイス概要]** 遅延（間隔）値を取得します。<hr>'),
        Mapping(
            key='  - A delay value of each `Handler` calling in '
            'milliseconds.',
            val='  - ハンドラの実行ごとのミリ秒の間隔値。'),
        Mapping(
            key='  - A handler would be called at regular intervals.',
            val='  - 一定間隔ごとに呼ばれる関数もしくはメソッドのハンドラ。'),
        Mapping(
            key='## this attribute',
            val='## this 属性'),
        Mapping(
            key='## TimerEvent constructor API',
            val='## TimerEvent クラスのコンストラクタのAPI'),
        Mapping(
            key='**[Interface summary]** Timer event class.<hr>',
            val='**[インターフェイス概要]** タイマー関係のイベントの'
            'クラスです。<hr>'),
        Mapping(
            key='  - Target timer instance.',
            val='  - 対象のタイマーのインスタンス。'),
        Mapping(
            key='## this attribute API',
            val='## this 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a timer instance of listening to '
            'this event.<hr>',
            val='**[インターフェイス概要]** このイベントのハンドラが設定されている'
            '対象のタイマーのインスタンス。<hr>'),
        Mapping(
            key='  - Instance of listening to this event.',
            val='  - このイベントのハンドラが設定されているインスタンス。'),
        Mapping(
            key='## repeat_count property API',
            val='## repeat_count 属性のAPI'),
        Mapping(
            key='**[Interface summary]** Get a max count value of a '
            'handler\'s calling.<hr>',
            val='**[インターフェイス概要]** ハンドラが呼ばれる最大数を取得します。<hr>'),
        Mapping(
            key='  - Max count of a handler\'s calling. If this value is '
            '0, then a timer loop forever.',
            val='  - ハンドラの呼び出しの上限回数。もし0が指定された場合、'
            'タイマーはずっと実行され続けます（ハンドラを呼び続けます）。'),
        Mapping(
            key='Timer class delay setting document',
            val='Timer クラスの delay 設定'),
        Mapping(
            key='## reset API',
            val='## reset API'),
        Mapping(
            key='**[Interface summary]** Reset the timer count and stop '
            'this timer.<hr>',
            val='**[インターフェイス概要]** タイマーのカウントをリセットし、そして'
            'タイマーの停止を行います。<hr>'),
        Mapping(
            key='## start API',
            val='## start API'),
        Mapping(
            key='**[Interface summary]** Start this timer.<hr>',
            val='**[インターフェイス概要]** タイマーを開始します。<hr>'),
        Mapping(
            key='## stop API',
            val='## stop API'),
        Mapping(
            key='**[Interface summary]** Stop this timer.<hr>',
            val='**[インターフェイス概要]** タイマーを停止します。<hr>'),
        Mapping(
            key='## trace API',
            val='## trace API'),
        Mapping(
            key='**[Interface summary]** Display arguments information '
            'to console. This function saves a JavaScript `console.log` '
            'expression.<hr>',
            val='**[インターフェイス概要]** 引数に指定された値の情報をコンソールへ'
            '表示します。この関数はJavaScriptの`console.log`に該当するコードを'
            '保存します。<hr>'),
        Mapping(
            key='  - Any arguments to display to console.',
            val='  - コンソール上に表示する任意の引数の値。'),
        Mapping(
            key='## unset_debug_mode API',
            val='## unset_debug_mode API'),
        Mapping(
            key='**[Interface summary]** Unset the debug mode for the '
            'HTML and JavaScript debugging.<hr>',
            val='**[インターフェイス概要]** HTMLとJavaScriptのデバッグ用の'
            'デバッグモードの設定を解除します。<hr>'),
        Mapping(
            key='See also:',
            val='参考資料:'),
    ])
