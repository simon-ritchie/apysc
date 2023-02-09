# flake8: noqa

"""This module is for the Japanese fixed-translation mappings
settings.
"""

from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mappings

MAPPINGS: Mappings = Mappings(
    mappings=[
        Mapping(key="## See also", val="## 関連資料"),
        Mapping(key="**[Returns]**", val="**[返却値]**"),
        Mapping(key="**[Parameters]**", val="**[引数]**"),
        Mapping(key="**[Examples]**", val="**[コードサンプル]**"),
        Mapping(key="**[References]**", val="**[関連資料]**"),
        Mapping(
            key='<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>',
            val='<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',
        ),
        Mapping(key="Graphics class", val="Graphics クラス"),
        Mapping(
            key="Graphics begin_fill interface",
            val="Graphics クラス begin_fill （塗り設定）のインターフェイス",
        ),
        Mapping(
            key="Graphics line_style interface",
            val="Graphics クラス line_style （線設定）のインターフェイス",
        ),
        Mapping(
            key="Graphics draw_rect interface",
            val="Graphics クラス draw_rect （四角描画）のインターフェイス",
        ),
        Mapping(
            key="Graphics draw_circle interface",
            val="Graphics クラス draw_circle （円描画）のインターフェイス",
        ),
        Mapping(
            key="add_child and remove_child interfaces",
            val="add_child （子の追加）と remove_child （子の削除）のインターフェイス",
        ),
        Mapping(key="contains interface", val="contains インターフェイス"),
        Mapping(key="num_children interface", val="num_children （子の件数属性）のインターフェイス"),
        Mapping(
            key="get_child_at interface",
            val="get_child_at （特定位置の子の取得処理）のインターフェイス",
        ),
        Mapping(
            key="DisplayObject class parent interfaces",
            val="DisplayObjectクラス parent （親要素属性）のインターフェイス",
        ),
        Mapping(key="**[Notes]**", val="**[特記事項]**"),
        Mapping(key="**[Raises]**", val="**[エラー発生条件]**"),
        Mapping(key="About the handler options\\' type", val="ハンドラのoptions引数の型について"),
        Mapping(key="## Basic usage", val="## 基本的な使い方"),
        Mapping(key="## What setting is this?", val="## 設定概要"),
        Mapping(key="## What class is this?", val="## クラス概要"),
        Mapping(key="## What interface is this?", val="## インターフェイス概要"),
        Mapping(
            key="Animation interfaces duration setting",
            val="各アニメーションインターフェイスの duration （アニメーション時間）設定",
        ),
        Mapping(
            key="Each animation interface return value",
            val="各アニメーションインターフェイスの返却値",
        ),
        Mapping(key="Sequential animation setting", val="連続したアニメーション設定"),
        Mapping(key="Easing enum", val="イージングのenum"),
        Mapping(
            key="  - Milliseconds before an animation ends.", val="  - アニメーション完了までのミリ秒。"
        ),
        Mapping(
            key="  - Milliseconds before an animation starts.",
            val="  - アニメーション開始までの遅延時間のミリ秒。",
        ),
        Mapping(key="  - Easing setting.", val="  - イージング設定。"),
        Mapping(
            key="To start this animation, you need to call the `start` method of the returned instance.<hr>",
            val="アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>",
        ),
        Mapping(
            key=" ・To start this animation, you need to call the `start` method of the returned instance. ",
            val=" ・アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。 ",
        ),
        Mapping(
            key="Animation interfaces delay setting",
            val="各アニメーションインターフェイスの delay （遅延時間）設定",
        ),
        Mapping(
            key="  - Created animation setting instance.",
            val="  - 生成されたアニメーションのインスタンス。",
        ),
        Mapping(
            key="<details>\\n<summary>Display the code block:</summary>",
            val="<details>\\n<summary>コードブロックを表示:</summary>",
        ),
        Mapping(
            key="<details>\n<summary>Display the code block:</summary>",
            val="<details>\n<summary>コードブロックを表示:</summary>",
        ),
        Mapping(
            key="animation_x interface",
            val="animation_x （X座標のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_y interface",
            val="animation_y （Y座標のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_move interface",
            val="animation_move （XとY座標のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_width and animation_height interfaces",
            val="animation_width （幅のアニメーション）と animation_height （高さのアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_fill_color interface",
            val="animation_fill_color （塗りの色のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_fill_alpha interface",
            val="animation_fill_alpha （塗りの透明度のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_line_color interface",
            val="animation_line_color （線色のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_line_alpha interface",
            val="animation_line_alpha （線の透明度のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_line_thickness interface",
            val="animation_line_thickness （線幅のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_radius interface",
            val="animation_radius （半径のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_rotation_around_center interface",
            val="animation_rotation_around_center （中央座標での回転のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_rotation_around_point interface",
            val="animation_rotation_around_point （指定座標による回転のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_scale_x_from_center and animation_scale_y_from_center interfaces",
            val="animation_scale_x_from_center （中央座標による水平方向の拡縮アニメーション）と animation_scale_y_from_center （中央座標による垂直方向の拡縮アニメーション）のインターフェイス",
        ),
        Mapping(
            key="animation_scale_x_from_point and animation_scale_y_from_point interfaces",
            val="animation_scale_x_from_point （指定座標による水平方向の拡縮アニメーション）と animation_scale_y_from_point （指定座標による垂直方向のアニメーション）のインターフェイス",
        ),
        Mapping(
            key="This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle` class.",
            val="このインターフェイスは`Rectangle`や`Circle`クラスなどの`GraphicsBase`のサブクラスで存在します。",
        ),
        Mapping(
            key="Set the line alpha animation setting.<hr>",
            val="線の透明度のアニメーションを設定します。<hr>",
        ),
        Mapping(
            key="  - The final line alpha of the animation.",
            val="  - 線の透明度のアニメーションの最終値。",
        ),
        Mapping(
            key="Set the line color animation setting.<hr>",
            val="線の色のアニメーションを設定します。<hr>",
        ),
        Mapping(
            key="  - The final line color (hex color code) of the animation.",
            val="  - 16進数の線の色のアニメーションの最終値。",
        ),
        Mapping(
            key="Set the line thickness animation setting.<hr>",
            val="線幅のアニメーションを設定します。<hr>",
        ),
        Mapping(
            key="  - The final line thickness of the animation.",
            val="  - 線幅のアニメーションの最終値。",
        ),
        Mapping(
            key="This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.",
            val="このインターフェイスは`Sprite`や`Rectangle`などの`DisplayObject`の各サブクラスに存在します。",
        ),
        Mapping(
            key="Set the x and y coordinates animation settings.<hr>",
            val="XとY座標に対するアニメーションを設定します。<hr>",
        ),
        Mapping(key="  - Destination of the x-coordinate.", val="  - 最終的なX座標。"),
        Mapping(key="  - Destination of the y-coordinate.", val="  - 最終的なY座標。"),
        Mapping(key="## What interface are these?", val="## 各インターフェイス概要"),
        Mapping(
            key="These interfaces exist in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).",
            val="これらのインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。",
        ),
        Mapping(
            key="This interface exists on a `GraphicsBase` subclass, such as the `Circle` class.",
            val="このインターフェイスは`Circle`クラスなどの`GraphicsBase`の各サブクラス上に存在します。",
        ),
        Mapping(
            key="  - The final radius of the animation.", val="  - 半径のアニメーションの最終値。"
        ),
        Mapping(
            key="This interface exists in the instances that have the animation interfaces (such as the `animation_x`\\, `animation_move`).",
            val="このインターフェイスは`animation_x`や`animation_move`などのアニメーション関係のインターフェイスを持つクラスのインスタンス上に存在します。",
        ),
        Mapping(key="## Interface Notes", val="## インターフェイスの特記事項"),
        Mapping(
            key="Reverse all running animations.<hr>",
            val="動いている全てのアニメーションを反転（逆再生）します。<hr>",
        ),
        Mapping(
            key="Set the rotation around the center animation setting.<hr>",
            val="中央座標を使用した回転のアニメーションの設定を行います。<hr>",
        ),
        Mapping(
            key="  - The final rotation of the animation.",
            val="  - 回転のアニメーションの回転量の最終値。",
        ),
        Mapping(
            key="Set the rotation around the given point animation setting.<hr>",
            val="指定された座標を基準とした回転のアニメーションを設定します。<hr>",
        ),
        Mapping(key="  - X-coordinate.", val="  - X座標。"),
        Mapping(key="  - Y-coordinate.", val="  - Y座標。"),
        Mapping(key="## What interfaces are these?", val="## 各インターフェイスの概要"),
        Mapping(
            key="Set the scale-x from the center point animation setting.<hr>",
            val="中央座標を基準としたX軸の拡縮アニメーションを設定します。<hr>",
        ),
        Mapping(
            key="  - The final scale-x of the animation.", val="  - X軸の拡縮のアニメーションの最終値。"
        ),
        Mapping(
            key="Set the scale-y from the center point animation setting.<hr>",
            val="中央座標を基準としたY軸の拡縮アニメーションを設定します。<hr>",
        ),
        Mapping(
            key="  - The final scale-y of the animation.", val="  - Y軸の拡縮のアニメーションの最終値。"
        ),
        Mapping(
            key="This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` class.",
            val="このインターフェイスは`Rectangle`などの`GraphicsBase`の各サブクラス上に存在します。",
        ),
        Mapping(
            key="Set the skew-x animation setting.<hr>",
            val="X軸の傾きのアニメーションを設定します。<hr>",
        ),
        Mapping(
            key="  - The final skew-x of the animation.", val="  - X軸の傾きのアニメーションの最終値。"
        ),
        Mapping(
            key="Get an animation elapsed millisecond.<hr>",
            val="アニメーションの経過時間のミリ秒を取得します。<hr>",
        ),
        Mapping(
            key="  - An animation elapsed millisecond.", val="  - アニメーションの経過時間のミリ秒。"
        ),
        Mapping(
            key="These interfaces exist on some `DisplayObject` instances, such as the `Rectangle` class.",
            val="これらの各インターフェイスは`Rectangle`クラスなどの`DisplayObject`の各サブクラス上に存在します。",
        ),
        Mapping(
            key="## Notes for the Ellipse instance", val="## Ellipse のインスタンスにおける特記事項"
        ),
        Mapping(
            key="Set the width animation setting.<hr>",
            val="幅のアニメーションを設定します。<hr>",
        ),
        Mapping(
            key="Set the height animation setting.<hr>",
            val="高さのアニメーションを設定します。<hr>",
        ),
        Mapping(key="  - The final width of the animation.", val="  - 幅のアニメーションの最終値。"),
        Mapping(
            key="  - The final height of the animation.", val="  - 高さのアニメーションの最終値。"
        ),
        Mapping(
            key="## Notes for the Circle and Ellipse classes",
            val="## Circle と Ellipse の各クラスの特記事項",
        ),
        Mapping(
            key="Set the x-coordinate animation setting.<hr>",
            val="X座標のアニメーションを設定します。<hr>",
        ),
        Mapping(
            key="Set the y-coordinate animation setting.<hr>",
            val="Y座標のアニメーションを設定します。<hr>",
        ),
        Mapping(key="  - Any value to append.", val="  - 追加対象の任意の値。"),
        Mapping(
            key="  - Other array-like values to concatenate.",
            val="  - 連結対象となる他の配列の（もしくはそれに近しい）値。",
        ),
        Mapping(key="  - Any value to search.", val="  - 検索対象の任意の値。"),
        Mapping(key="  - Index to append value.", val="  - 値を追加するインデックス。"),
        Mapping(key="  - Separator string.", val="  - 区切り文字。"),
        Mapping(key="  - Joined string.", val="  - 連結された文字列。"),
        Mapping(key="  - Removed value.", val="  - 取り除かれた値。"),
        Mapping(key="  - Value to remove.", val="  - 取り除く対象の値。"),
        Mapping(key="  - Index to remove value.", val="  - 取り除く値のインデックス。"),
        Mapping(key="Array class sort interface", val="Array クラスの sort インターフェイス"),
        Mapping(key="An original array is not modified.", val="元々の配列の値は変更されません。"),
        Mapping(key="  - Slicing start index.", val="  - スライス範囲の開始インデックス。"),
        Mapping(key="  - Sliced array.", val="  - スライスされた配列。"),
        Mapping(key="Array class reverse interface", val="Array クラスの reverse インターフェイス"),
        Mapping(
            key="Before reading on, maybe it is helpful to read the following page:",
            val="事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:",
        ),
        Mapping(
            key="Why the apysc library doesn\\'t use the Python built-in data type",
            val="なぜapyscではPythonのビルトインのデータの型を使用していないのか",
        ),
        Mapping(
            key="Why the apysc library does not use the Python built-in data type",
            val="なぜapyscではPythonのビルトインのデータの型を使用していないのか",
        ),
        Mapping(key="## Constructor method", val="## コンストラクタメソッド"),
        Mapping(key="## Generic type annotation", val="## ジェネリックの型アノテーション"),
        Mapping(
            key="Funcdamental data classes common value interface",
            val="基本的なデータクラスの共通の value インターフェイス",
        ),
        Mapping(
            key="Array class append and push interfaces",
            val="Array クラスの append と push のインターフェイス",
        ),
        Mapping(
            key="Array class extend and concat interfaces",
            val="Array クラスの extend と concat のインターフェイス",
        ),
        Mapping(
            key="Array class insert and insert_at interfaces",
            val="Array クラスの insert と insert_at のインターフェイス",
        ),
        Mapping(key="Array class pop interface", val="Array クラスの pop インターフェイス"),
        Mapping(
            key="Array class remove and remove_at interfaces",
            val="Array クラスの remove と remove_at のインターフェイス",
        ),
        Mapping(key="Array class slice interface", val="Array クラスの slice インターフェイス"),
        Mapping(
            key="Array class length interface",
            val="Array クラスの length (配列の長さ取得) のインターフェイス",
        ),
        Mapping(
            key="Array class join interface",
            val="Array クラスの join (値の連結文字列生成) のインターフェイス",
        ),
        Mapping(
            key="Array class index_of interface",
            val="Array クラスの index_of (値のインデックス取得) のインターフェイス",
        ),
        Mapping(
            key="Array class comparison interfaces",
            val="Array クラスの比較の各インターフェイス",
        ),
        Mapping(key="## Array class constructor API", val="## Array クラスのコンストラクタのAPI"),
        Mapping(key="  - Initial array value.", val="  - 配列の初期値。"),
        Mapping(key="## value property API", val="## value 属性のAPI"),
        Mapping(key="  - Current array value.", val="  - 現在の配列の値。"),
        Mapping(
            key="apysc fundamental data classes value interface",
            val="apyscの基本的なデータクラスの value インターフェイス",
        ),
        Mapping(
            key="JavaScript assertion interface basic behavior",
            val="JavaScriptの各アサーションのインターフェイスの基本的な挙動",
        ),
        Mapping(
            key="## Notes for the assert_equal and assert_not_equal interfaces",
            val="## assert_equal と assert_not_equal の各インターフェイスにおける特記事項",
        ),
        Mapping(key="  - Left-side value to compare.", val="  - 比較用の左辺の値。"),
        Mapping(key="  - Right-side value to compare.", val="  - 比較用の右辺の値。"),
        Mapping(
            key="  - Message to display when assertion failed.",
            val="  - チェックに失敗した際に表示するメッセージ。",
        ),
        Mapping(key="  - Target value to check.", val="  - チェック対象の値。"),
        Mapping(
            key="  - Callable that this instance calls when its event's dispatching.",
            val="  - 対象のイベントが発生（発火）される時に実行されるハンドラ。",
        ),
        Mapping(key="  - Target custom event type.", val="  - 対象の独自のイベントの種別値としての文字列。"),
        Mapping(key="  - Event instance.", val="  - イベントのインスタンス。"),
        Mapping(
            key="  - Optional arguments dictionary to be passed to a handler.",
            val="  - ハンドラに渡される省略が可能な追加のパラメーターとしての辞書。",
        ),
        Mapping(key="  - Handler's name.", val="  - ハンドラ名。"),
        Mapping(key="If class", val="If クラス"),
        Mapping(key="Elif class", val="Elif クラス"),
        Mapping(key="Else class", val="Else クラス"),
        Mapping(
            key="The following page describes basic mouse event interfaces.",
            val="以下のページでは基本的なマウスイベントのインターフェイスについて説明しています。",
        ),
        Mapping(key="Basic mouse event interfaces", val="基本的なマウスイベントの各インターフェイス"),
        Mapping(
            key="  - Unbinding target Callable.", val="  - イベント設定を取り除く対象の関数やメソッドなど。"
        ),
        Mapping(key="  - Child instance to check.", val="  - チェック対象の子のインスタンス。"),
        Mapping(
            key="The following page describes the basic mouse event interfaces.",
            val="以下のページでは基本的なマウスイベントの各インターフェイスについて説明しています。",
        ),
        Mapping(key="  - Target key.", val="  - 対象のキー。"),
        Mapping(key="  - Any default value.", val="  - 任意のデフォルト値の値。"),
        Mapping(key="## Note for the len function", val="## len関数における特記事項"),
        Mapping(
            key="The Python built-in `len` function is not supported and raises an exception:",
            val="Pythonビルトインの`len`関数はサポートされておらずエラーとなります:",
        ),
        Mapping(key="## Value setter interface", val="## 値のsetterのインターフェイス"),
        Mapping(key="## Value getter interface", val="## 値のgetterのインターフェイス"),
        Mapping(key="## Notes of the getter interface", val="## getterのインターフェイスの特記事項"),
        Mapping(key="## Value deletion interface", val="## 値の削除のインターフェイス"),
        Mapping(key="  - Initial dictionary value.", val="  - 辞書の初期値。"),
        Mapping(key="## value attribute API", val="## value 属性のAPI"),
        Mapping(key="  - Current dict value.", val="  - 現在の辞書の値。"),
        Mapping(
            key="## What apysc can do in its properties", val="## それらの属性でapyscができること"
        ),
        Mapping(
            key="For more details, please see the following:", val="詳細については以下をご確認ください:"
        ),
        Mapping(
            key="DisplayObject class x and y interfaces",
            val="DisplayObject クラスの x と y インターフェイス",
        ),
        Mapping(key="## x and y properties", val="## x と y 属性"),
        Mapping(key="## visible property", val="## visible 属性"),
        Mapping(
            key="DisplayObject class visible interface",
            val="DisplayObject クラスの visible (表示・非表示) のインターフェイス",
        ),
        Mapping(key="## rotation interfaces", val="## 回転の各インターフェイス"),
        Mapping(
            key="GraphicsBase class rotation_around_center interface",
            val="GraphicsBase クラスの rotation_around_center (中央座標基準の回転) インターフェイス",
        ),
        Mapping(
            key="GraphicsBase class rotation_around_point interfaces",
            val="GraphicsBase クラスの rotation_around_point (指定座標基準の回転) の各インターフェイス",
        ),
        Mapping(key="## scale interfaces", val="## 拡縮の各インターフェイス"),
        Mapping(
            key="GraphicsBase class scale_from_center interfaces",
            val="GraphicsBase クラスの scale_from_center (中央座標基準の拡縮) の各インターフェイス",
        ),
        Mapping(
            key="GraphicsBase class scale_from_point interfaces",
            val="GraphicsBase クラスの scale_from_point (指定座標基準の拡縮) の各インターフェイス",
        ),
        Mapping(key="## flip properties", val="## 反転の各属性"),
        Mapping(
            key="## GraphicsBase class flip_x and flip_y interfaces",
            val="## GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class flip_x and flip_y interfaces",
            val="GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) のインターフェイス",
        ),
        Mapping(key="## skew properties", val="## 歪みの各属性"),
        Mapping(
            key="GraphicsBase class skew_x and skew_y interfaces",
            val="GraphicsBase クラスの skew_x (X軸の歪み) と skew_y (Y軸の歪み) のインターフェイス",
        ),
        Mapping(key="DisplayObject class", val="DisplayObject クラス"),
        Mapping(key="  - CSS name (e.g., 'display').", val="  - CSS名（例 : 'display'）。"),
        Mapping(
            key="For more details, please see the following pages:",
            val="詳細については以下の各ページをご確認ください:",
        ),
        Mapping(key="click interface", val="click インターフェイス"),
        Mapping(
            key="mousedown and mouseup interfaces", val="mousedown と mouseup のインターフェイス"
        ),
        Mapping(
            key="mouseover and mouseout interfaces",
            val="mouseover と mouseout のインターフェイス",
        ),
        Mapping(key="mousemove interface", val="mousemove インターフェイス"),
        Mapping(
            key="- ValueError: If a parent is None (there is no parent).",
            val="- ValueError: もしも親のインスタンスがNoneの場合（親の無い状態の場合）。",
        ),
        Mapping(key="## visible property API", val="## visible 属性のAPI"),
        Mapping(key="## Augmented assignment", val="## 累算代入演算"),
        Mapping(key="## x property API", val="## x属性のAPI"),
        Mapping(
            key="Get an x-coordinate.<hr>",
            val="X座標を取得します。<hr>",
        ),
        Mapping(key="## y property API", val="## y属性のAPI"),
        Mapping(
            key="Get a y-coordinate.<hr>",
            val="Y座標を取得します。<hr>",
        ),
        Mapping(
            key="DisplayObject class mouse event binding interfaces",
            val="DisplayObject クラスのマウスイベント設定の各インターフェイス",
        ),
        Mapping(key="## Requirements", val="## 必要とされるインストールなどの対応"),
        Mapping(
            key="  - Boolean value whether minify a HTML or not. False setting is useful when debugging.",
            val="  - HTMLを最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに役に立つことがあります。",
        ),
        Mapping(key="For more information, please see:", val="詳細は以下をご確認ください:"),
        Mapping(key="## Notes", val="## 特記事項"),
        Mapping(key="  - The output HTML file name.", val="  - 出力されるHTMLのファイル名。"),
        Mapping(
            key="Graphics class draw_rect interface",
            val="Graphics クラスの draw_rect (四角の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_round_rect interface",
            val="Graphics クラスの draw_round_rect (角丸の四角の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_circle interface",
            val="Graphics クラスの draw_circle (円の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class move_to and line_to interfaces",
            val="Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_line interface",
            val="Graphics クラスの draw_line (線の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_dotted_line interface",
            val="Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_dashed_line interface",
            val="Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_round_dotted_line interface",
            val="Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_dash_dotted_line interface",
            val="Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_polygon interface",
            val="Graphics クラスの draw_polygon (多角形描画)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class fill_color interface",
            val="GraphicsBase クラスの fill_color (塗り設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class fill_alpha interface",
            val="GraphicsBase クラスの fill_alpha (塗りの透明度設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_color interface",
            val="GraphicsBase クラスの line_color (線の色設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_alpha interface",
            val="GraphicsBase クラスの line_color (線の透明度設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_thickness interface",
            val="GraphicsBase クラスの line_color (線幅設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_dot_setting interface",
            val="GraphicsBase クラスの line_dot_setting (点線設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_dash_setting interface",
            val="GraphicsBase クラスの line_dash_setting (破線設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_round_dot_setting interface",
            val="GraphicsBase クラスの line_round_dot_setting (点線(丸)設定)のインターフェイス",
        ),
        Mapping(
            key="GraphicsBase class line_dash_dot_setting interface",
            val="GraphicsBase クラスの line_dash_dot_setting (一点鎖線設定)のインターフェイス",
        ),
        Mapping(key="For more details, please see:", val="詳細は以下をご確認ください:"),
        Mapping(
            key="Graphics class begin_fill interface",
            val="Graphics クラスの begin_fill (塗りの設定)のインターフェイス",
        ),
        Mapping(
            key="Graphics class line_style interface",
            val="Graphics クラスの line_style (線のスタイル設定)のインターフェイス",
        ),
        Mapping(
            key="Graphics class draw_ellipse interface",
            val="Graphics クラスの draw_ellipse (楕円描画) のインターフェイス",
        ),
        Mapping(
            key="Each branch instruction class\\'s scope variables reverting setting",
            val="分岐条件の各クラスのスコープ内変数の復元設定",
        ),
        Mapping(
            key="  - Boolean value to be used for judgment.",
            val="  - 判定に使われるBooleanの真偽値。",
        ),
        Mapping(
            key="  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.",
            val="  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。",
        ),
        Mapping(key="Timer class delay setting", val="Timer クラスの delay 設定"),
        Mapping(
            key="  - Child's index (start from 0).", val="  - 対象の子のインデックス（0からスタートします）。"
        ),
        Mapping(key="  - Target index child instance.", val="  - 対象の子のインスタンス。"),
        Mapping(
            key="Get a rotation value around the center of this instance.<hr>",
            val="インスタンスの中央座標を基準とした回転量を取得します。<hr>",
        ),
        Mapping(
            key="  - Rotation value around the center of this instance.",
            val="  - このインスタンスの中央座標を基準とした回転量。",
        ),
        Mapping(
            key="  - Rotation value around the given coordinates.",
            val="  - 指定された座標基準による回転量。",
        ),
        Mapping(
            key="## set_rotation_around_point API",
            val="## set_rotation_around_point API",
        ),
        Mapping(
            key="## get_rotation_around_point API",
            val="## get_rotation_around_point API",
        ),
        Mapping(key="  - Rotation value to set.", val="  - 設定する回転量。"),
        Mapping(
            key="Update a rotation value around the given coordinates.<hr>",
            val="指定された座標基準の回転量を更新します。<hr>",
        ),
        Mapping(
            key="## scale_x_from_center property API",
            val="## scale_x_from_center 属性のAPI",
        ),
        Mapping(
            key="Get a scale-x value from the center of this instance.<hr>",
            val="インスタンスの中央座標を基準とした水平方向の拡縮の値を取得します。<hr>",
        ),
        Mapping(
            key="  - Scale-x value from the center of this instance.",
            val="  - インスタンスの中央座標を基準とした水平方向の拡縮の値。",
        ),
        Mapping(
            key="## scale_y_from_center property API",
            val="## scale_y_from_center 属性のAPI",
        ),
        Mapping(
            key="Get a scale-y value from the center of this instance.<hr>",
            val="インスタンスの中央座標を基準とした垂直方向の拡縮の値を取得します。<hr>",
        ),
        Mapping(
            key="  - Scale-y value from the center of this instance.",
            val="  - インスタンスの中央座標を基準とした垂直方向の拡縮の値。",
        ),
        Mapping(
            key="## get_scale_x_from_point API", val="## get_scale_x_from_point API"
        ),
        Mapping(
            key="Get a scale-x value from the given x-coordinate.<hr>",
            val="指定されたX座標を基準として水平方向の拡縮の値を取得します。<hr>",
        ),
        Mapping(
            key="  - Scale-x value from the given x-coordinate.",
            val="  - 指定されたX座標を基準とした水平方向の拡縮値。",
        ),
        Mapping(
            key="## set_scale_x_from_point API", val="## set_scale_x_from_point API"
        ),
        Mapping(
            key="Update a scale-x value from the given x-coordinate.<hr>",
            val="指定されたX座病を基準とした水平方向の拡縮値を更新します。<hr>",
        ),
        Mapping(
            key="## get_scale_y_from_point API", val="## get_scale_y_from_point API"
        ),
        Mapping(
            key="Get a scale-y value from the given y-coordinate.<hr>",
            val="指定されたY座標を基準とした垂直方向の拡縮の値を取得します。<hr>",
        ),
        Mapping(
            key="  - Scale-y value from the given y-coordinate.",
            val="  - 指定されたY座標を基準とした垂直方向の拡縮値。",
        ),
        Mapping(
            key="## set_scale_y_from_point API", val="## set_scale_y_from_point API"
        ),
        Mapping(
            key="Update a scale-y value from the given y-coordinate.<hr>",
            val="指定されたY座標を基準とした垂直方向の拡縮値を更新します。<hr>",
        ),
        Mapping(key="  - Scale-y value to set.", val="  - 設定すの垂直方向の拡縮値。"),
        Mapping(key="  - Scale-x value to set.", val="  - 設定する水平方向の拡縮値。"),
        Mapping(key="## skew_x property API", val="## skew_x property API"),
        Mapping(
            key="Get a current skew x value of the instance.<hr>",
            val="インスタンスの現在のX軸の歪みの値を取得します。<hr>",
        ),
        Mapping(
            key="  - Current skew x value of this instance.",
            val="  - インスタンスの現在のX軸の歪みの値。",
        ),
        Mapping(key="## skew_y property API", val="## skew_y property API"),
        Mapping(
            key="Get a current skew y value of the instance.<hr>",
            val="インスタンスの現在のY軸の歪みの値を取得します。<hr>",
        ),
        Mapping(
            key="  - Current skew y value of the instance.",
            val="  - インスタンスの現在のY軸の歪みの値。",
        ),
        Mapping(key="## Fill color setting", val="## 塗りの色の設定"),
        Mapping(key="## Fill color alpha (opacity) setting", val="## 塗りの色の透明度の設定"),
        Mapping(key="## begin_fill API", val="## begin_fill API"),
        Mapping(
            key="Set single color value for fill.<hr>",
            val="塗りのための単一の色の設定を行います。<hr>",
        ),
        Mapping(
            key="  - Hexadecimal color string. e.g., '#00aaff'",
            val="  - '#00aaff'などの16進数の色の文字列。",
        ),
        Mapping(key="  - Color opacity (0.0 to 1.0).", val="  - 塗りの透明度（0.0～1.0）。"),
        Mapping(key="## fill_color property API", val="## fill_color 属性のAPI"),
        Mapping(
            key="Get current fill color.<hr>",
            val="現在の塗りの色を取得します。<hr>",
        ),
        Mapping(
            key="  - Current fill color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.",
            val="  - 現在の塗りの色（`'#00aaff'`などの16進数の文字列）。もしも設定されていない場合空文字が返却されます。",
        ),
        Mapping(key="## fill_alpha property API", val="## fill_alpha 属性のAPI"),
        Mapping(
            key="Get current fill color opacity.<hr>",
            val="現在の塗りの透明度を取得します。<hr>",
        ),
        Mapping(
            key="  - Current fill color opacity (0.0 to 1.0). If not be set, 1.0 will be returned.",
            val="  - 現在の塗りの透明度（0.0～1.0）。もし設定されていない場合1.0の値が返却されます。",
        ),
        Mapping(key="## Return value", val="## 返却値"),
        Mapping(key="## draw_circle API", val="## draw_circle API"),
        Mapping(
            key="Draw a circle vector graphics.<hr>",
            val="円のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(key="  - X-coordinate of the circle center.", val="  - 円の中心のX座標。"),
        Mapping(key="  - Y-coordinate of the circle center.", val="  - 円の中心のY座標。"),
        Mapping(key="  - Circle radius.", val="  - 円の半径。"),
        Mapping(
            key="  - Created circle graphics instance.",
            val="  - 生成された円のグラフィックスのインスタンス。",
        ),
        Mapping(key="## draw_dash_dotted_line API", val="## draw_dash_dotted_line API"),
        Mapping(
            key="Draw a dash-dotted (1-dot chain) line vector graphics.<hr>",
            val="一点鎖線のベクターグラフィックスの線を描画します。<hr>",
        ),
        Mapping(key="  - Line start x-coordinate.", val="  - 線の開始位置のX座標。"),
        Mapping(key="  - Line start y-coordinate.", val="  - 線の開始位置のY座標。"),
        Mapping(key="  - Line end x-coordinate.", val="  - 線の終了位置のX座標。"),
        Mapping(key="  - Line end y-coordinate.", val="  - 線の終了位置のY座標。"),
        Mapping(key="  - Dot size.", val="  - ドットのサイズ。"),
        Mapping(key="  - Dash size.", val="  - 破線部分のサイズ。"),
        Mapping(
            key="  - Blank space size between dots and dashes.",
            val="  - ドット（点線）や破線間の空白スペースのサイズ。",
        ),
        Mapping(
            key="  - Created line graphics instance.", val="  - 生成された線のグラフィックスのインスタンス。"
        ),
        Mapping(key="## draw_dashed_line API", val="## draw_dashed_line API"),
        Mapping(
            key="Draw a dashed line vector graphics.<hr>",
            val="破線のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(key="  - Blank space size between dashes.", val="  - 破線間の空白スペースのサイズ。"),
        Mapping(
            key=" ・This interface ignores line settings, like the `LineDotSetting`, except `LineDashSetting`.<hr>",
            val=" ・このインターフェイスは`LineDashSetting`を除いた`LineDotSetting`などの線のスタイル設定を無視します。<hr>",
        ),
        Mapping(key="## draw_dotted_line API", val="## draw_dotted_line API"),
        Mapping(
            key="Draw a dotted line vector graphics.<hr>",
            val="点線のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(
            key=" ・This interface ignores line settings, like the `LineDashSetting`, except `LineDotSetting`.<hr>",
            val=" ・このインターフェイスは`LineDotSetting`を除いた`LineDashSetting`などの線のスタイル設定を無視します。<hr>",
        ),
        Mapping(key="## draw_ellipse API", val="## draw_ellipse API"),
        Mapping(
            key="Draw an ellipse vector graphic.<hr>",
            val="楕円のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(key="  - X-coordinate of the ellipse center.", val="  - 楕円の中央のX座標。"),
        Mapping(key="  - Y-coordinate of the ellipse center.", val="  - 楕円の中央のY座標。"),
        Mapping(key="  - Ellipse width.", val="  - 楕円の幅。"),
        Mapping(key="  - Ellipse height.", val="  - 楕円の高さ。"),
        Mapping(
            key="  - Created ellipse graphics instance.",
            val="  - 作成された楕円のグラフィックスのインスタンス。",
        ),
        Mapping(key="## Ignored line style settings", val="## 無視される線のスタイル設定"),
        Mapping(key="## Line class instance", val="## Line クラスのインスタンス"),
        Mapping(key="## draw_line API", val="## draw_line API"),
        Mapping(
            key="Draw a normal line vector graphic.<hr>",
            val="通常の直線のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(
            key=" ・This interface ignores line settings, like the `LineDotSetting`, `LineDashSetting`.<hr>",
            val=" ・このインターフェイスは`LineDotSetting`や`LineDashSetting`などの設定を無視します。<hr>",
        ),
        Mapping(key="## draw_polygon API", val="## draw_polygon API"),
        Mapping(
            key="Draw a polygon vector graphic. This interface is similar to the Polyline class (created by `move_to` or `line_to`). But unlike that, this interface connects the last point and the start point.<hr>",
            val="多角形のベクターグラフィックスを描画します。このインターフェイスはPolylineクラス（`move_to`や`line_to`のインターフェイスで作成されます）に似ていますが、このインターフェイスは始点と終点が連結されるという違いがあります。<hr>",
        ),
        Mapping(key="  - Polygon vertex points.", val="  - 多角形の頂点の各座標。"),
        Mapping(
            key="  - Created polygon graphics instance.",
            val="  - 作成された多角形のグラフィックスのインスタンス。",
        ),
        Mapping(key="## draw_rect API", val="## draw_rect API"),
        Mapping(
            key="Draw a rectangle vector graphics.<hr>",
            val="ベクターグラフィックスの四角を描画します。<hr>",
        ),
        Mapping(key="  - X position to start drawing.", val="  - 描画を開始する位置のX座標。"),
        Mapping(key="  - Y position to start drawing.", val="  - 描画を開始する位置のY座標。"),
        Mapping(key="  - Rectangle width.", val="  - 四角の幅。"),
        Mapping(key="  - Rectangle height.", val="  - 四角の高さ。"),
        Mapping(key="  - Created rectangle.", val="  - 生成された四角。"),
        Mapping(
            key="## draw_round_dotted_line API", val="## draw_round_dotted_line API"
        ),
        Mapping(
            key="Draw a round-dotted line vector graphics.<hr>",
            val="丸ドットの直線のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(key="  - Dot round size.", val="  - 丸ドットのサイズ。"),
        Mapping(key="  - Blank space size between dots.", val="  - ドット間の空白のスペースのサイズ。"),
        Mapping(
            key="This interface ignores line settings, like the `LineDotSetting`, except `LineRoundDotSetting`.<hr>",
            val="このインターフェイスは`LineRoundDotSetting`を除いて`LineDotSetting`などの設定を無視します。<hr>",
        ),
        Mapping(key="## draw_round_rect API", val="## draw_round_rect API"),
        Mapping(
            key="Draw a rounded rectangle vector graphics.<hr>",
            val="角丸四角のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(key="  - X-coordinate to start drawing.", val="  - 描画を開始するX座標。"),
        Mapping(key="  - Y-coordinate to start drawing.", val="  - 描画を開始するY座標。"),
        Mapping(key="  - Ellipse width of the rectangle corner.", val="  - 四角の角丸の幅。"),
        Mapping(key="  - Ellipse height of the rectangle corner.", val="  - 四角の角丸の高さ。"),
        Mapping(
            key="Get this instance's fill opacity.<hr>",
            val="このインスタンスの塗りの透明度を取得します。<hr>",
        ),
        Mapping(
            key="  - Current fill opacity (0.0 to 1.0).", val="  - 現在の塗りの透明度（0.0～1.0）。"
        ),
        Mapping(
            key="Get this instance's fill color.<hr>",
            val="インスタンスの塗りの色を取得します。<hr>",
        ),
        Mapping(
            key="The getter or setter interface value becomes (or requires) the `Number` value (0.0 to 1.0).",
            val="getterとsetterの両方のインターフェイスの値は`Number`型の0.0～1.0の範囲の値となります。",
        ),
        Mapping(key="## line_alpha property API", val="## line_alpha 属性のAPI"),
        Mapping(
            key="Get this instance's line alpha (opacity).<hr>",
            val="インスタンスの線の透明度を取得します。<hr>",
        ),
        Mapping(
            key="  - Current line alpha (opacity. 0.0 to 1.0).",
            val="  - 現在の線の透明度（0.0～1.0）。",
        ),
        Mapping(
            key="The getter or setter interface value becomes (or requires) the `String` hex color code value.",
            val="getterとsetterのインターフェイスで扱う値は`String`型の16進数のカラーコードの文字列となります。",
        ),
        Mapping(key="## line_color property API", val="## line_color 属性のAPI"),
        Mapping(
            key="Get this instance's line color.<hr>",
            val="インスタンスの線の色を取得します。<hr>",
        ),
        Mapping(
            key="  - Current line color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.",
            val="  - '#00aaff'などの16進数の線の色。もし設定されていない場合はこの空文字となります。",
        ),
        Mapping(
            key="Get a current dash-dot (1-dot chain) setting.<hr>",
            val="現在の一点鎖線のスタイル設定を取得します。<hr>",
        ),
        Mapping(
            key="## line_dash_dot_setting API", val="## line_dash_dot_setting のAPI"
        ),
        Mapping(key="  - Dash-dot (1-dot chain) setting.", val="  - 一点鎖線の設定。"),
        Mapping(
            key="## line_dash_setting property API", val="## line_dash_setting 属性のAPI"
        ),
        Mapping(
            key="Get a current line dash setting.<hr>",
            val="現在の線の破線のスタイル設定を取得します。<hr>",
        ),
        Mapping(key="  - Line dash setting.", val="  - 線の破線のスタイル設定。"),
        Mapping(
            key="The getter or setter interface value becomes (or requires) the `LineDotSetting` instance value.",
            val="getterやsetterのインターフェイスの値は`LineDotSetting`クラスのインスタンスの値となります。",
        ),
        Mapping(
            key="## line_dot_setting property API", val="## line_dot_setting 属性のAPI"
        ),
        Mapping(
            key="Get this instance's line dot setting.<hr>",
            val="このインスタンスの線の点線のスタイル設定を取得します。<hr>",
        ),
        Mapping(key="  - Lien dot setting.", val="  - 線の点線のスタイル設定。"),
        Mapping(
            key="The getter or setter interface value becomes (or requires) the `LineRoundDotSetting` instance value.",
            val="getterやsetterのインターフェイスの値は`interface`クラスのインスタンスの値になります。",
        ),
        Mapping(
            key="## line_round_dot_setting property API",
            val="## line_round_dot_setting 属性のAPI",
        ),
        Mapping(key="  - Line round dot setting.", val="  - 線の丸ドットのスタイル設定。"),
        Mapping(
            key="Get this instance's line round dot setting.<hr>",
            val="**[インターフェイス]** インスタンスの線の丸ドットのスタイル設定を取得します。<hr>",
        ),
        Mapping(key="## Line-color setting", val="## 線の色の設定"),
        Mapping(
            key="- Six characters, e.g., `#00aaff`.", val="- `#00aaff`などの6文字による指定。"
        ),
        Mapping(
            key="- Three characters, e.g., `#0af` (this becomes `#00aaff`).",
            val="- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。",
        ),
        Mapping(
            key="- Single character, e.g., `#5` (this becomes `#000005`).",
            val="- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。",
        ),
        Mapping(
            key="- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).",
            val="- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。",
        ),
        Mapping(
            key="- Blank string, e.g., `''` (this clears line color setting).",
            val="- `''`などの空文字の指定（これは線の色の削除指定として扱われます）。`",
        ),
        Mapping(key="## Line thickness setting", val="## 線幅の設定"),
        Mapping(key="## Line alpha (opacity) setting", val="## 線の透明度の設定"),
        Mapping(key="## Line cap setting", val="## 線端の設定"),
        Mapping(
            key="There are three `LineCaps` options, as follows:",
            val="以下のように`LineCaps`のオプションは3種類存在します:",
        ),
        Mapping(
            key="- BUTT: This is the default value, and it sets no cap.",
            val="- BUTT: デフォルト値であり、端にはなにも設定されません。",
        ),
        Mapping(
            key="- ROUND: This changes the line edge to the rounded one.",
            val="- ROUND: 線の端のスタイルを丸くします。",
        ),
        Mapping(
            key="- SQUARE: This is similar to BUTT, but it increases the line length by the squared edge.",
            val="- SQUARE: 線の端のスタイルを四角くします。これはBUTTと似た表示になりますが、設定される四角の分だけ線が長くなります。",
        ),
        Mapping(key="## Line joints setting", val="## 線の繋ぎ目の設定"),
        Mapping(
            key="There are three LineJoints enum values, as follows:",
            val="以下のようにLineJointsのenumには3つの値が存在します:",
        ),
        Mapping(
            key="- MITER: This setting sets the style like a picture frame vertices. This setting is the default style setting.",
            val="- MITER: この設定は頂点が（尖った形での）額縁のような形のスタイルが設定されます。この設定がデフォルトのスタイルとなります。",
        ),
        Mapping(
            key="- ROUND: This setting sets the rounded vertices style.",
            val="- ROUND: この設定は丸い頂点のスタイルを設定します。",
        ),
        Mapping(
            key="- BEVEL: This setting sets a beveled vertices style.",
            val="- BEVEL: この設定は射角（ベベル）の頂点のスタイルを設定します。",
        ),
        Mapping(key="## Line dot setting", val="## 線の点線設定"),
        Mapping(
            key="Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.",
            val="特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。",
        ),
        Mapping(key="## Line dash setting", val="## 線の破線設定"),
        Mapping(key="## Line round dot setting", val="## 線の丸ドット設定"),
        Mapping(
            key="Notes: Since this setting uses the `cap` setting internally, this setting ignores the `cap` setting, increasing the line length by the capsize.",
            val="特記事項: この設定は内部で`cap`設定の値を使用しているため、この設定では`cap`引数の設定が無視されます。また、丸のサイズに応じた分だけ線の長さが長くなります。",
        ),
        Mapping(key="## Line dash-dot setting", val="## 線の一点鎖線の設定"),
        Mapping(key="## line_style API", val="## line_style API"),
        Mapping(
            key="Set line style values.<hr>",
            val="線のスタイルを設定します。<hr>",
        ),
        Mapping(
            key="  - Line thickness (minimum value is 1).", val="  - 線の幅（1以上の値を受け付けます）。"
        ),
        Mapping(
            key="  - Line cap (edge style) setting. The not line-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.",
            val="  - 線の端のスタイル設定。線に関係しないRectangleクラスなどのグラフィックスインスタンスはこの設定を無視します。逆にPolylineクラスなどの線に関係したインスタンスではこの設定を使用します。",
        ),
        Mapping(
            key="  - Line vertices (joints) style setting. The not polyline-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.",
            val="  - 線の頂点（接合部）のスタイル設定。折れ線線に関係しないRectangleなどのグラフィックスインスタンスはこの設定を無視します。逆にPolylineクラスなどの折れ線関係のクラスではこの設定を使用します。",
        ),
        Mapping(
            key="  - Dot setting. If this is specified, it makes a line dotted.",
            val="  - 点線の設定。もしもこの引数が指定された場合、線は点線になります。",
        ),
        Mapping(
            key="  - Dash setting. If this is specified, it makes a line dashed.",
            val="  - 破線の設定。もしこの引数が指定された場合、線は破線になります。",
        ),
        Mapping(
            key="  - Round dot setting. If this is specified, it makes a line round dotted. Notes: since this style uses a cap setting, it overrides cap and line thickness settings. And it increases the amount of line size. If you want to adjust to the same width of a normal line when using move_to and line_to interfaces, add half-round size to start x-coordinate and subtract from end e-coordinate. e.g., `this.move_to(x + round_size / 2, y)`, `this.line_to(x - round_size / 2, y)`",
            val="  - 丸ドットの設定。もしこの引数が指定された場合、線は丸ドットになります。特記事項: ごの設定は内部でcapの設定を使用しているため、cap（線の端のスタイル設定）と線幅の設定を上書きします。また、cap設定を使用している都合、線の長さも長くなります。move_toやline_toなどのインターフェイスを使った通常の線の長さと合わせたい場合には丸の半分のサイズを線の開始位置のX座標へ加算し、さらに丸の半分のサイズを線の終了位置のX座標から減算してください（Y座標も同様です）。例: `this.move_to(x + round_size / 2, y)`、`this.line_to(x - round_size / 2, y)`",
        ),
        Mapping(
            key="  - Dash-dot (1-dot chain) setting. If this is specified, it makes a line 1-dot chained.",
            val="  - 一点鎖線のスタイル設定。もしこの引数が指定された場合、線の一点鎖線になります。",
        ),
        Mapping(
            key="Get current line color.<hr>",
            val="現在の線の色を取得します。<hr>",
        ),
        Mapping(key="## line_thickness property API", val="## line_thickness 属性のAPI"),
        Mapping(
            key="Get current line thickness.<hr>",
            val="現在の線の線幅を取得します。<hr>",
        ),
        Mapping(key="  - Current line thickness.", val="  - 現在の線幅。"),
        Mapping(
            key="Get current line color opacity.<hr>",
            val="現在の線の透明度を取得します。<hr>",
        ),
        Mapping(
            key="  - Current line opacity (0.0 to 1.0).", val="  - 現在の線の透明度（0.0～1.0）。"
        ),
        Mapping(key="## line_cap property API", val="## line_cap 属性のAPI"),
        Mapping(
            key="Get current line cap (edge) style setting.<hr>",
            val="現在の線の端のスタイル設定。<hr>",
        ),
        Mapping(
            key="  - Current line cap (edge) style setting.", val="  - 現在の線の端のスタイル設定。"
        ),
        Mapping(key="## line_joints property API", val="## line_joints 属性のAPI"),
        Mapping(
            key="Get current line joints (vertices) style setting.<hr>",
            val="現在の線の接合部（頂点）のスタイル設定を取得します。<hr>",
        ),
        Mapping(
            key="  - Current line joints (vertices) style setting.",
            val="  - 現在の線の接合部（頂点）のスタイル設定。",
        ),
        Mapping(
            key="Get current line dot setting.<hr>",
            val="現在の線の点線設定を取得します。<hr>",
        ),
        Mapping(key="  - Current line dot setting.", val="  - 現在の点線設定。"),
        Mapping(key="  - Current line dash setting.", val="  - 現在の破線設定。"),
        Mapping(
            key="Get current line-round dot setting.<hr>",
            val="現在の線の丸ドットのスタイル設定を取得します。<hr>",
        ),
        Mapping(key="  - Current line round dot setting.", val="  - 現在の線の丸ドットのスタイル設定。"),
        Mapping(
            key="## line_dash_dot_setting property API",
            val="## line_dash_dot_setting 属性のAPI",
        ),
        Mapping(
            key="Get current line dash-dot setting.<hr>",
            val="現在の線の一点鎖線のスタイル設定を取得します。<hr>",
        ),
        Mapping(key="  - Line color opacity (0.0 to 1.0).", val="  - 線色の透明度（0.0～1.0）。"),
        Mapping(key="  - Current line dash-dot setting.", val="  - 現在の一点鎖線のスタイル設定。"),
        Mapping(
            key="The getter or setter interface value becomes (or requires) the `Int` value.",
            val="getterもしくはsetterの各インターフェイスの値は`Int`型の値になります。",
        ),
        Mapping(
            key="Get this instance's line thickness.<hr>",
            val="このインスタンスの線幅を取得します。<hr>",
        ),
        Mapping(key="## What interfaces are they?", val="## 各インターフェイスの概要"),
        Mapping(
            key="If you click the following line, line style will be updated:",
            val="もし以下の四角をクリックし0た場合、線のスタイルは更新されます:",
        ),
        Mapping(key="## move_to API", val="## move_to API"),
        Mapping(
            key="Move a line position to a specified point.<hr>",
            val="指定された座標に線の描画位置を移動させます。<hr>",
        ),
        Mapping(key="  - X destination point to move.", val="  - 移動先となるX座標。"),
        Mapping(key="  - Y destination point to move.", val="  - 移動先となるY座標。"),
        Mapping(key="  - Line graphics instance.", val="  - 線のグラフィックスのインスタンス。"),
        Mapping(key="## line_to API", val="## line_to API"),
        Mapping(
            key="Draw a line from previous point to specified point (initial point is x = 0, y = 0).<hr>",
            val="直前の位置の座標から指定された座標に向けて線を描画します（初期位置はx=0, y=0になります）。<hr>",
        ),
        Mapping(
            key="  - X destination point to draw a line.", val="  - 線の描画先となる終点のX座標。"
        ),
        Mapping(
            key="  - Y destination point to draw a line.", val="  - 線の描画先となる終点のY座標。"
        ),
        Mapping(key="## Return values", val="## 各返却値について"),
        Mapping(key="## If constructor API", val="## If クラスのコンストラクタのAPI"),
        Mapping(
            key="A class to append if branch instruction expression.<hr>",
            val="if文の分岐制御の表現を追加するためのクラス。<hr>",
        ),
        Mapping(
            key="  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of an `If` scope. This setting is useful when you don't want to update each variable by implementing the `If` scope.",
            val="  - 現在のスコープの各ローカル変数。指定する場合にはlocals()関数の値をごの引数に指定してください。もし指定された場合、このインターフェイスは`If`のスコープの終了時に対象のVariableNameMixInクラスの各ローカル変数のインスタンスの値をスコープの開始前の時点に復元します。この設定は`If`のスコープ内の処理でPython上の各ローカル変数の値を更新したくない場合などに便利なことがあります。",
        ),
        Mapping(key="## Project links", val="## プロジェクトの関連リンク"),
        Mapping(
            key="- [GitHub](https://github.com/simon-ritchie/apysc)",
            val="- [GitHub](https://github.com/simon-ritchie/apysc)",
        ),
        Mapping(
            key="- [Twitter](https://twitter.com/apysc)",
            val="- [Twitter](https://twitter.com/apysc)",
        ),
        Mapping(
            key="- [PyPI](https://pypi.org/project/apysc/)",
            val="- [PyPI](https://pypi.org/project/apysc/)",
        ),
        Mapping(
            key="What apysc can do in its current implementation",
            val="apyscが現在の実装で出来ることの概要",
        ),
        Mapping(key="## Contents", val="## コンテンツ"),
        Mapping(key="## Quick start guide", val="## クイックスタートガイド"),
        Mapping(key="Quick start guide", val="クイックスタートガイド"),
        Mapping(key="import conventions", val="import の慣習"),
        Mapping(key="## Container classes", val="## コンテナーの各クラス"),
        Mapping(key="Stage class", val="Stage クラス"),
        Mapping(key="Sprite class", val="Sprite クラス"),
        Mapping(key="## Exporting", val="## 出力処理"),
        Mapping(key="save_overall_html interface", val="save_overall_html インターフェイス"),
        Mapping(key="display_on_jupyter interface", val="display_on_jupyter インターフェイス"),
        Mapping(
            key="display_on_colaboratory interface",
            val="display_on_colaboratory インターフェイス",
        ),
        Mapping(
            key="append_js_expression interface", val="append_js_expression インターフェイス"
        ),
        Mapping(key="## apysc basic data classes", val="## apyscの基本的な各データクラス"),
        Mapping(key="Int and Number classes", val="Int と Number の各クラス"),
        Mapping(
            key="Int and Number classes common arithmetic operations",
            val="Int と Number クラスの共通の計算制御",
        ),
        Mapping(
            key="Int and Number classes common comparison operations",
            val="Int と Number クラスの共通の比較制御",
        ),
        Mapping(key="String class", val="String クラス"),
        Mapping(key="String class comparison operations", val="String クラスの比較制御"),
        Mapping(
            key="String class addition and multiplication operations",
            val="String クラスの加算と乗算の制御",
        ),
        Mapping(key="Boolean class", val="Boolean クラス"),
        Mapping(key="Array class", val="Array クラス"),
        Mapping(key="Dictionary class", val="Dictionary クラス"),
        Mapping(
            key="Dictionary class generic type settings",
            val="Dictionary クラスのジェネリックの型設定",
        ),
        Mapping(
            key="Dictionary class get interface", val="Dictionary クラスの get インターフェイス"
        ),
        Mapping(
            key="Dictionary class length interface",
            val="Dictionary クラスの length インターフェイス",
        ),
        Mapping(key="Point2D class", val="Point2D クラス"),
        Mapping(
            key="## DisplayObject and GraphicsBase classes",
            val="## DisplayObject と GraphicsBase の各クラス",
        ),
        Mapping(
            key="DisplayObject and GraphicsBase classes basic properties abstract",
            val="DisplayObject と GraphicsBase の各クラスの基本的な各属性の概要",
        ),
        Mapping(
            key="DisplayObject class get_css and set_css interfaces",
            val="DisplayObject クラスの get_css と set_css の各インターフェイス",
        ),
        Mapping(key="## Graphics class", val="## Graphics クラス"),
        Mapping(key="Draw interfaces abstract", val="描画の各インターフェイスの概要"),
        Mapping(key="## Common event interfaces", val="## イベントの共通の各インターフェイス"),
        Mapping(key="About the handler options type", val="ハンドラの options パラメーターの型について"),
        Mapping(
            key="Event class prevent_default and stop_propagation interfaces",
            val="Event クラスの prevent_default と stop_propagation の各インターフェイス",
        ),
        Mapping(
            key="bind_custom_event and trigger_custom_event interfaces",
            val="bind_custom_event と trigger_custom_event の各インターフェイス",
        ),
        Mapping(
            key="## MouseEvent class and mouse event binding",
            val="## MouseEvent クラスとマウスイベントの設定",
        ),
        Mapping(
            key="MouseEvent interfaces abstract", val="MouseEvent クラスの各インターフェイスの概要"
        ),
        Mapping(key="dblclick interface", val="dblclick インターフェイス"),
        Mapping(key="## Branch instruction", val="## 条件分岐の制御"),
        Mapping(
            key="Each branch instruction class scope variables reverting setting",
            val="各条件分岐のクラスのスコープ内の変数値の復元設定",
        ),
        Mapping(key="Return class", val="Return クラス"),
        Mapping(key="For loop class", val="ループ用の For クラス"),
        Mapping(key="Continue class", val="Continue クラス"),
        Mapping(key="## Loop", val="## ループ"),
        Mapping(key="## Timer", val="## タイマー"),
        Mapping(key="Timer class", val="Timer クラス"),
        Mapping(key="TimerEvent class", val="TimerEvent クラス"),
        Mapping(key="FPS enum", val="FPS の enum"),
        Mapping(
            key="Timer class repeat_count setting", val="Timer クラスの repeat_count 設定"
        ),
        Mapping(
            key="Timer class start and stop interfaces",
            val="Timer クラスの start と stop の各インターフェイス",
        ),
        Mapping(
            key="Timer class timer_complete interface",
            val="Timer クラスの timer_complete インターフェイス",
        ),
        Mapping(key="Timer class reset interface", val="Timer クラスの reset インターフェイス"),
        Mapping(key="## Animation", val="## アニメーション"),
        Mapping(key="Animation interfaces abstract", val="アニメーションの各インターフェイスの概要"),
        Mapping(key="AnimationEvent class", val="AnimationEvent クラス"),
        Mapping(key="Animation duration setting", val="Animation クラスの duration 設定"),
        Mapping(key="Animation delay setting", val="Animation クラスの delay 設定"),
        Mapping(
            key="AnimationBase class start interface",
            val="AnimationBase クラスの start インターフェイス",
        ),
        Mapping(
            key="AnimationBase class animation_complete interface",
            val="AnimationBase クラスの animation_complete インターフェイス",
        ),
        Mapping(
            key="AnimationBase class interfaces method chaining",
            val="AnimationBase クラスの各インターフェイスのメソッドチェーンについて",
        ),
        Mapping(
            key="AnimationBase class target property",
            val="AnimationBase クラスの target 属性",
        ),
        Mapping(
            key="Animation pause and play interfaces",
            val="アニメーションの pause と play の各インターフェイス",
        ),
        Mapping(key="Animation reset interface", val="アニメーションの reset インターフェイス"),
        Mapping(key="Animation finish interface", val="アニメーションの finish インターフェイス"),
        Mapping(key="Animation reverse interface", val="アニメーションの reverse インターフェイス"),
        Mapping(key="animation_time interface", val="animation_time インターフェイス"),
        Mapping(key="animation_parallel interface", val="animation_parallel インターフェイス"),
        Mapping(key="## Debugging", val="## デバッグ"),
        Mapping(key="trace function interface", val="trace 関数のインターフェイス"),
        Mapping(key="set_debug_mode interface", val="set_debug_mode インターフェイス"),
        Mapping(key="unset_debug_mode interface", val="unset_debug_mode インターフェイス"),
        Mapping(key="## Testing", val="## テスト"),
        Mapping(
            key="assert_equal and assert_not_equal interfaces",
            val="assert_equal と assert_not_equal の各インターフェイス",
        ),
        Mapping(
            key="assert_true and assert_false interfaces",
            val="assert_true と assert_false の各インターフェイス",
        ),
        Mapping(
            key="assert_arrays_equal and assert_arrays_not_equal interfaces",
            val="assert_arrays_equal と assert_arrays_not_equal の各インターフェイス",
        ),
        Mapping(
            key="assert_dicts_equal and assert_dicts_not_equal interfaces",
            val="assert_dicts_equal と assert_dicts_not_equal の各インターフェイス",
        ),
        Mapping(
            key="assert_defined and assert_undefined interfaces",
            val="assert_defined と assert_undefined の各インターフェイス",
        ),
        Mapping(key="## Child-related interfaces", val="## 子要素関係の各インターフェイス"),
        Mapping(key="## Common behaviors", val="## 共通の挙動"),
        Mapping(key="## Addition", val="## 加算"),
        Mapping(key="## Subtraction", val="## 減算"),
        Mapping(key="## Multiplication", val="## 乗算"),
        Mapping(key="## Division", val="## 除算"),
        Mapping(key="## Floor division", val="## 切り捨て除算"),
        Mapping(key="## Modulo", val="## 剰余"),
        Mapping(key="## Equal comparison operator", val="## 等値条件の比較のオペレーター"),
        Mapping(
            key="You can use the `==` operator for the equal comparison:",
            val="`==`のオペレーターを使って等値条件の比較を行うことができます。",
        ),
        Mapping(key="## Not equal comparison operator", val="## 非等値条件の比較のオペレーター"),
        Mapping(
            key="You can use the `!=` operator for the not equal comparison:",
            val="`!=`のオペレーターを使って非等値条件の比較を行うことができます。",
        ),
        Mapping(key="## Less than comparison operator", val="## 未満条件の比較のオペレーター"),
        Mapping(
            key="You can use the `<` operator for the less than comparison:",
            val="`<`のオペレーターを使って未満条件の比較を行うことができます。",
        ),
        Mapping(
            key="## Less than or equal comparison operator", val="## 以下条件の比較のオペレーター"
        ),
        Mapping(
            key="You can use the `<=` operator for the less than or equal comparison:",
            val="`<=`のオペレーターを使って以下条件の比較を行うことができます。",
        ),
        Mapping(key="## Greater than comparison operator", val="## 超過条件の比較のオペレーター"),
        Mapping(
            key="You can use the `>` operator for the greater than comparison:",
            val="`>`のオペレーターを使って超過条件の比較を行うことができます。",
        ),
        Mapping(
            key="## Greater than or equal comparison operator", val="## 以上条件の比較のオペレーター"
        ),
        Mapping(
            key="You can use the `>=` operator for the greater than or equal comparison:",
            val="`>=`のオペレーターを使って以上条件の比較を行うことができます。",
        ),
        Mapping(key="## Int class", val="## Int クラス"),
        Mapping(key="## Number class", val="## Number クラス"),
        Mapping(key="## Note for the Float class alias", val="## Floatクラスのエイリアスの特記事項"),
        Mapping(
            key="## Int and Number classes basic interfaces",
            val="## Int と Number クラスの基本的なインターフェイス",
        ),
        Mapping(
            key="Int and Number classes basic arithmetic operations",
            val="Int と Number クラスの基本的な各計算の制御",
        ),
        Mapping(
            key="Int and Number classes basic comparison operations",
            val="Int と Number クラスの基本的な各比較の制御",
        ),
        Mapping(key="## Int class constructor API", val="## Int クラスのコンストラクタのAPI"),
        Mapping(
            key="Integer class for apysc library.<hr>",
            val="apyscライブラリ上の整数のためのクラスです。<hr>",
        ),
        Mapping(
            key="  - Initial integer value. If the `float` or `Number` value is specified, this class casts it to an integer.",
            val="  - 整数の初期値。もしも`float`や`Number`の値が指定された場合このクラスは値を整数へと変換します。",
        ),
        Mapping(
            key="Int and Number common arithmetic operations",
            val="Int と Number クラスの共通の各計算制御",
        ),
        Mapping(
            key="Int and Number common comparison operations",
            val="Int と Number クラスの共通の各比較制御",
        ),
        Mapping(key="## Number class constructor API", val="## Number クラスのコンストラクタのAPI"),
        Mapping(
            key="  - Initial floating point number value. This class casts it to float if you specify int or Int value.",
            val="  - 浮動小数点数の初期値。もしもintやIntなどの型の値が指定された場合このクラスは値を浮動小数点数へ変換します。",
        ),
        Mapping(
            key="The `Float` class is the alias of the Number, and it behaves the same as the Number class.<hr>",
            val="`Float`クラスはNumberクラスのエイリアスであり、このエイリアスはNumberクラスと同様に動作します。<hr>",
        ),
        Mapping(
            key="Get a current number value.<hr>",
            val="現在の数値を取得します。<hr>",
        ),
        Mapping(key="  - Current number value.", val="  - 現在の数値。"),
        Mapping(
            key="Floating point number class for apysc library.<hr>",
            val="apyscライブラリ用の浮動小数点数のクラスです。<hr>",
        ),
        Mapping(key="### Table of contents", val="### Table of contents"),
        Mapping(
            key="## What apysc can do in its interfaces",
            val="## これらの各インターフェイスでapyscが出来ること",
        ),
        Mapping(key="## stage_x property API", val="## stage_x 属性のAPI"),
        Mapping(
            key="Get the x-coordinate of the stage reference.<hr>",
            val="ステージ基準のX座標を取得します。<hr>",
        ),
        Mapping(key="## stage_y property API", val="## stage_y 属性のAPI"),
        Mapping(
            key="Get the y-coordinate of the stage reference.<hr>",
            val="ステージ基準のY座標を取得します。<hr>",
        ),
        Mapping(key="  - x-coordinate.", val="  - X座標。"),
        Mapping(key="  - y-coordinate.", val="  - Y座標。"),
        Mapping(key="## local_x property API", val="## local_x 属性のAPI"),
        Mapping(
            key="Get a local x-coordinate event listening instance. For example, this value becomes x-coordinate from Sprite's left-end position by clicking a Sprite instance.<hr>",
            val="イベントが設定されているインスタンス内の相対座標のX座標を取得します。例えばSpriteのインスタンスをクリックした場合にはSpriteの左上の位置を基準とした座標になります。<hr>",
        ),
        Mapping(key="## local_y property API", val="## local_y 属性のAPI"),
        Mapping(
            key="Get the local y-coordinate of the event listening instance. For example, this value becomes y-coordinate from Sprite's top-end position by clicking a Sprite instance.<hr>",
            val="イベントが設定されているインスタンスないの相対座標のY座標を取得します。例えばSpriteのインスタンスをクリックした場合にはSpriteの左上の位置を基準とした座標になります。<hr>",
        ),
        Mapping(key="## this property API", val="## this 属性のAPI"),
        Mapping(
            key="  - Instance that listening this event.",
            val="  - このイベントが設定されているインスタンス。",
        ),
        Mapping(
            key="Get an instance of listening to this event.<hr>",
            val="このイベントが設定されているインスタンスを取得します。<hr>",
        ),
        Mapping(
            key="The following page describes the basic mouse event interfaces:",
            val="以下のページでは基本的なマウスイベントのインターフェイスについて説明しています:",
        ),
        Mapping(key="## Unbind interfaces", val="## 解除用のインターフェイス"),
        Mapping(key="## mousedown API", val="## mousedown API"),
        Mapping(
            key="Add mouse down event listener setting.<hr>",
            val="マウスのボタンを押した時のイベント設定を追加します。<hr>",
        ),
        Mapping(
            key="  - Callable that would be called when mouse down on this instance.",
            val="  - インスタンス上でマウスのボタンを押した時に呼ばれる関数もしくはメソッド。",
        ),
        Mapping(key="## unbind_mousedown API", val="## unbind_mousedown API"),
        Mapping(
            key="Unbind a specified handler's mouse down event.<hr>",
            val="マウスのボタンを押した際のイベントの指定されたハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## unbind_mousedown_all API", val="## unbind_mousedown_all API"),
        Mapping(
            key="Unbind all mouse down events.<hr>",
            val="マウスのボタンを押した時のイベントの全てのハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## mouseup API", val="## mouseup API"),
        Mapping(
            key="Add mouse up event listener setting.<hr>",
            val="マウスのボタンを離した時のイベント設定を追加します。<hr>",
        ),
        Mapping(
            key="  - Callable that would be called when mouse-up on this instance.",
            val="  - インスタンス上でマウスのボタンを離した時に呼ばれる関数もしくはメソッド。",
        ),
        Mapping(key="## unbind_mouseup API", val="## unbind_mouseup API"),
        Mapping(
            key="Unbind a specified handler's mouse-up event.<hr>",
            val="マウスのボタンを離した際のイベントの指定されたハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## unbind_mouseup_all API", val="## unbind_mouseup_all API"),
        Mapping(
            key="Unbind all mouse up events.<hr>",
            val="マウスのボタンを離したとぎのイベントの全てのハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## mousemove API", val="## mousemove API"),
        Mapping(
            key="Add mouse move event listener setting.<hr>",
            val="マウスを動かした時のイベント設定を追加します。<hr>",
        ),
        Mapping(
            key="  - Callable that would be called when mousemove on this instance.",
            val="  - インスタンス上でマウスを動かした際に呼ばれる関数もしくはメソッド。",
        ),
        Mapping(key="## unbind_mousemove API", val="## unbind_mousemove API"),
        Mapping(
            key="Unbind a specified handler's mouse move event.<hr>",
            val="マウスカーソルを動かした際のイベントで指定されたハンドラの設定を解除します。<hr>",
        ),
        Mapping(key="## unbind_mousemove_all API", val="## unbind_mousemove_all API"),
        Mapping(
            key="Unbind all mouse move events.<hr>",
            val="マウスカーソルを動かしたときのイベントの全てのハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## mouseover API", val="## mouseover API"),
        Mapping(
            key="Add mouse over event listener setting.<hr>",
            val="マウスカーソルが乗った時のイベントのハンドラ設定を追加します。<hr>",
        ),
        Mapping(
            key="  - Callable that would be called when mouse over on this instance.",
            val="  - インスタンス上にマウスカーソルが乗った際に呼ばれる関数もしくはメソッド。",
        ),
        Mapping(key="## unbind_mouseover API", val="## unbind_mouseover API"),
        Mapping(
            key="Unbind a specified handler's mouseover event.<hr>",
            val="マウスカーソルが乗った際のイベントの指定されたハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## unbind_mouseover_all API", val="## unbind_mouseover_all API"),
        Mapping(
            key="Unbind all mouseover events.<hr>",
            val="マウスカーソルが乗った際のイベントの全てのハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## mouseout API", val="## mouseout API"),
        Mapping(
            key="Add mouse out event listener setting.<hr>",
            val="マウスカーソルがインスタンス上から離れた際のイベントのハンドラを設定します。<hr>",
        ),
        Mapping(
            key="  - Callable that would be called when mouse out on this instance.",
            val="  - インスタンス上からマウスカーソルが離れた際のイベントの対象のハンドラ設定を解除します。",
        ),
        Mapping(key="## unbind_mouseout API", val="## unbind_mouseout API"),
        Mapping(
            key="Unbind a specified handler's mouse-out event.<hr>",
            val="インスタンス上からマウスカーソルが離れた際のイベントの対象のハンドラ設定を解除します。<hr>",
        ),
        Mapping(key="## unbind_mouseout_all API", val="## unbind_mouseout_all API"),
        Mapping(
            key="Unbind all mouse out events.<hr>",
            val="インスタンス上からマウスカーソルが離れた際のイベントのハンドラ設定を全て解除します。<hr>",
        ),
        Mapping(key="## num_children API", val="## num_children API"),
        Mapping(
            key="Get a current children's number.<hr>",
            val="現在の子の数を取得します。<hr>",
        ),
        Mapping(key="  - Current children number.", val="  - 現在の子の数。"),
        Mapping(
            key="## Point2D class constructor API", val="## Point2D クラスのコンストラクタのAPI"
        ),
        Mapping(
            key="2-dimensional geometry point.<hr>",
            val="2次元の座標値を扱うクラスです。<hr>",
        ),
        Mapping(
            key="X-coordinate property.<hr>",
            val="X座標の属性のインターフェイスです。<hr>",
        ),
        Mapping(
            key="Y-coordinate property.<hr>",
            val="Y座標の属性のインターフェイスです。<hr>",
        ),
        Mapping(key="## Return API", val="## Return API"),
        Mapping(
            key="Class for the return expression.<hr>",
            val="return のコード表現のためのクラスです。<hr>",
        ),
        Mapping(
            key="This class can be instantiated only in an event handler scope.<hr>",
            val="このクラスはイベントハンドラのスコープ内でのみインスタンス化することができます。<hr>",
        ),
        Mapping(key="## save_overall_html API", val="## save_overall_html API"),
        Mapping(
            key="Save the overall HTML and js files under the specified directory path.<hr>",
            val="指定されたディレクトリパス以下にHTMLとJavaScriptのファイル全体を出力します。<hr>",
        ),
        Mapping(
            key="  - Destination directory path to save each HTML and js file.",
            val="  - 各HTMLとJavaScriptファイルの保存先となるディレクトリパス。",
        ),
        Mapping(
            key="  - Boolean value indicates whether minify HTML and js or not. The False setting is helpful when debugging.",
            val="  - HTMLとJavaScriptの内容を最小化（minify）するかどうかの真偽値。Falseの設定はデバッグ時などに便利な時があります。",
        ),
        Mapping(
            key="  - JavaScript libraries directory path. This setting applies to a JavaScript source path in HTML. If not specified, then set the same directory with HTML. This setting is maybe helpful to set js lib directory, such as Django's static (static_collected) directory. This interface recommends setting True value to the `skip_js_lib_exporting` argument if this argument sets.",
            val="  - JavaScriptライブラリのパスの設定。この設定はHTML内のJavaScriptのコードのパスの指定部分に影響します。指定されていない場合にはHTMLと同じディレクトリが設定されます。この設定はDjangoのようなライブラリの静的ファイルのディレクトリを指定する場合などに便利なことがあります。もしこの引数が設定された場合には`skip_js_lib_exporting`の設定も有効にすることが推奨されます。",
        ),
        Mapping(
            key="  - If True, this interface does not export JavaScript libraries.",
            val="  - Trueが設定された場合、このインターフェイスはJavaScriptの各ライブラリを出力しなくなります。",
        ),
        Mapping(
            key="  - Option to embed the JavaScript libraries script to the output HTML or not. If True, the output HTML becomes enormous, and be only one HTML file. Occasionally, this option is useful when sharing the exported file or using the output file with an iframe tag to avoid the CORS error.",
            val="  - 各JavaScriptライブラリを出力されるHTML内に埋め込むかどうかの設定です。もしTrueが設定された場合、出力されるHTMLは大きくなり、そして1つのHTMLファイルのみ出力されるようになります。この設定は出力されたファイルをiframeタグで使う際にCORSのエラーを回避したい時などに役立つことがあります。",
        ),
        Mapping(
            key="  - The Logging setting. If 0 is specified, this interface does not display a logging message. If 1 or the other value is specified, this interface displays a message usually.",
            val="  - ロギング（ログ表示）の設定です。0が指定された場合、このインターフェイスはログのメッセージを表示しなくなります。1もしくは他の値を指定した場合、このインターフェイスはログのメッセージを通常通り表示します。",
        ),
        Mapping(
            key="This interface empties a specified directory before saving.<hr>",
            val="このインターフェイスは指定された出力先のディレクトリを出力前に空にします。<hr>",
        ),
        Mapping(
            key="animation_complete interface",
            val="animation_complete インターフェイス",
        ),
        Mapping(key="## set_debug_mode API", val="## set_debug_mode API"),
        Mapping(
            key="Set the debug mode for the HTML and JavaScript debugging. If calling this function, this interface applies the following setting: ",
            val="HTMLとJavaScriptのデバッグ用にデバッグモードの設定を行います。もしこの関数を呼び出した場合、のインターフェイスは以下の設定を追加します: ",
        ),
        Mapping(
            key="<br> ・Disabling HTML minify setting. ",
            val="<br> ・HTMLの最小化（minify）設定を無効化します。 ",
        ),
        Mapping(
            key="<br> ・Changing to append per each interface JavaScript divider string.<hr>",
            val="<br> ・各インターフェイスごとのJavaScript上での区切りのための文字列を追加します。<hr>",
        ),
        Mapping(key="## Stage class constructor API", val="## Stage クラスのコンストラクタのAPI"),
        Mapping(
            key="Create Stage (overall viewport) instance.<hr>",
            val="ステージ（描画領域全体）のインスタンスを生成します。<hr>",
        ),
        Mapping(key="  - Stage width.", val="  - ステージの幅。"),
        Mapping(key="  - Stage height", val="  - ステージの高さ。"),
        Mapping(
            key="  - Hexadecimal background color string.", val="  - 16進数の背景色の文字列。"
        ),
        Mapping(
            key="  - Specification of element to add stage. Unique tag (e.g., 'body') or ID selector (e.g., '#any-unique-elem') is acceptable.",
            val="  - ステージの要素を追加先となる要素の指定。一意のタグ（例 : 'body'）やIDのセレクタ（例 : '#any-unique-elem'）を受け付けることができます。",
        ),
        Mapping(
            key="  - ID attribute set to stage html element (e.g., 'line-graph'). If None is set, random integer will be applied.",
            val="  - ステージのHTML要素に設定されるIDの属性（例 : 'line-graph'）。もしNoneが設定されている場合、乱数などを使った数値を使った値が設定されます。",
        ),
        Mapping(key="## stage_elem_id property API", val="## stage_elem_id 属性のAPI"),
        Mapping(
            key="Get stage's html element id.<hr>",
            val="ステージのHTML要素のIDを取得します。<hr>",
        ),
        Mapping(
            key="  - Stage's html element id (not including class or id symbol). e.g., 'line-graph'",
            val="  - ステージのHTML要素のID（ID用の#の記号などは含まれません。例 : 'line-graph'）。",
        ),
        Mapping(key="## add_child API", val="## add_child API"),
        Mapping(
            key="Add display object child to this instance.<hr>",
            val="表示オブジェクトの子をこのインスタンスへと追加します。<hr>",
        ),
        Mapping(key="  - Child instance to add.", val="  - 追加する子のインスタンス。"),
        Mapping(key="## remove_child API", val="## remove_child API"),
        Mapping(
            key="Remove display object child from this instance.<hr>",
            val="このインスタンスから指定された表示オブジェクトの子を取り除きます。<hr>",
        ),
        Mapping(key="  - Child instance to remove.", val="  - 取り除く対象の子のインスタンス。"),
        Mapping(key="## contains API", val="## contains API"),
        Mapping(
            key="Get a boolean whether this instance contains a specified child.<hr>",
            val="指定された子のインスタンスを持っているかどうかの真偽値を取得します。<hr>",
        ),
        Mapping(
            key="  - If this instance contains a specified child, this method returns True.",
            val="  - このインスタンスが指定された子を持つ場合Trueが設定されます。",
        ),
        Mapping(key="## get_child_at API", val="## get_child_at API"),
        Mapping(key="## num_children property API", val="## num_children property API"),
        Mapping(
            key="Get child at a specified index.<hr>",
            val="指定されたインデックス位置の子を取得します。<hr>",
        ),
        Mapping(
            key="## Acceptable comparison right-side value types",
            val="## 受け付けられる右側の値の型",
        ),
        Mapping(key="## Equal comparison", val="## 等値条件の比較"),
        Mapping(key="## Not equal comparison", val="## 非等値条件の比較"),
        Mapping(key="## Less than or greater than comparison", val="## 未満もしくは超過条件の比較"),
        Mapping(key="## String class constructor API", val="## String クラスのコンストラクタのAPI"),
        Mapping(
            key="String class for apysc library.<hr>",
            val="apyscライブラリにおける文字列用のクラスです。<hr>",
        ),
        Mapping(key="  - Initial string value.", val="  - 文字列の値の初期値。"),
        Mapping(
            key="Get a current string value.<hr>",
            val="現在の文字列の値を取得します。<hr>",
        ),
        Mapping(key="  - Current string value.", val="  - 現在の文字列の値。"),
        Mapping(key="## timer_complete API", val="## timer_complete API"),
        Mapping(
            key="Add a timer complete event listener setting.<hr>",
            val="タイマー終了時のイベントハンドラの設定を追加します。<hr>",
        ),
        Mapping(
            key="  - A callable that a timer calls when complete.",
            val="  - タイマー終了時に呼ばれる関数もしくはメソッド。",
        ),
        Mapping(key="## What argument is this?", val="## 引数の概要"),
        Mapping(key="## Timer constructor API", val="## Timer クラスのコンストラクタのAPI"),
        Mapping(
            key="Timer class to handle function calling at regular intervals.<hr>",
            val="一定間隔ごとにハンドラの関数を実行するためのタイマーのクラスです。<hr>",
        ),
        Mapping(
            key="  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).",
            val="  - ハンドラの実行間隔となるミリ秒もしくはFPSのenumの値。もし`FPS`の値が指定された場合、FPSに応じて計算されたミリ秒が設定されます（例えば、もし`FPS_60`が指定されていれば`delay`の値は16.6666667ミリ秒相当になります。）。",
        ),
        Mapping(
            key="  - Max count of a `Handler`'s calling. A timer stops if the `Handler`'s calling count has reached this value. If 0 is specified, then a timer loops forever.",
            val="  - ハンドラの実行回数の上限値。ハンドラの実行回数がこの値に到達した場合タイマーは停止します。もし0が指定された場合にはタイマーは停止しなくなります。",
        ),
        Mapping(
            key="  - Optional arguments dictionary to pass a `Handler` callable.",
            val="  - ハンドラの関数もしくはメソッドへ渡すオプションとしての各パラメーターを格納した辞書。",
        ),
        Mapping(key="Timer", val="Timer クラス"),
        Mapping(key="## delay property API", val="## delay 属性のAPI"),
        Mapping(
            key="Get a delay value.<hr>",
            val="遅延（間隔）値を取得します。<hr>",
        ),
        Mapping(
            key="  - A delay value of each `Handler` calling in milliseconds.",
            val="  - ハンドラの実行ごとのミリ秒の間隔値。",
        ),
        Mapping(
            key="  - A handler would be called at regular intervals.",
            val="  - 一定間隔ごとに呼ばれる関数もしくはメソッドのハンドラ。",
        ),
        Mapping(key="## this attribute", val="## this 属性"),
        Mapping(
            key="## TimerEvent constructor API", val="## TimerEvent クラスのコンストラクタのAPI"
        ),
        Mapping(
            key="Timer event class.<hr>",
            val="タイマー関係のイベントのクラスです。<hr>",
        ),
        Mapping(key="  - Target timer instance.", val="  - 対象のタイマーのインスタンス。"),
        Mapping(key="## this attribute API", val="## this 属性のAPI"),
        Mapping(
            key="Get a timer instance of listening to this event.<hr>",
            val="このイベントのハンドラが設定されている対象のタイマーのインスタンス。<hr>",
        ),
        Mapping(
            key="  - Instance of listening to this event.",
            val="  - このイベントのハンドラが設定されているインスタンス。",
        ),
        Mapping(key="## repeat_count property API", val="## repeat_count 属性のAPI"),
        Mapping(
            key="Get a max count value of a handler's calling.<hr>",
            val="ハンドラが呼ばれる最大数を取得します。<hr>",
        ),
        Mapping(
            key="  - Max count of a handler's calling. If this value is 0, then a timer loop forever.",
            val="  - ハンドラの呼び出しの上限回数。もし0が指定された場合、タイマーはずっと実行され続けます（ハンドラを呼び続けます）。",
        ),
        Mapping(key="## reset API", val="## reset API"),
        Mapping(
            key="Reset the timer count and stop this timer.<hr>",
            val="タイマーのカウントをリセットし、そしてタイマーの停止を行います。<hr>",
        ),
        Mapping(key="## start API", val="## start API"),
        Mapping(
            key="Start this timer.<hr>",
            val="タイマーを開始します。<hr>",
        ),
        Mapping(key="## stop API", val="## stop API"),
        Mapping(
            key="Stop this timer.<hr>",
            val="タイマーを停止します。<hr>",
        ),
        Mapping(key="## trace API", val="## trace API"),
        Mapping(
            key="Display arguments information to console. This function saves a JavaScript `console.log` expression.<hr>",
            val="引数に指定された値の情報をコンソールへ表示します。この関数はJavaScriptの`console.log`に該当するコードを保存します。<hr>",
        ),
        Mapping(
            key="  - Any arguments to display to console.",
            val="  - コンソール上に表示する任意の引数の値。",
        ),
        Mapping(key="## unset_debug_mode API", val="## unset_debug_mode API"),
        Mapping(
            key="Unset the debug mode for the HTML and JavaScript debugging.<hr>",
            val="HTMLとJavaScriptのデバッグ用のデバッグモードの設定を解除します。<hr>",
        ),
        Mapping(key="See also:", val="参考資料:"),
        Mapping(
            key="Recommended type annotation checker settings",
            val="推奨される型アノテーションのチェック設定",
        ),
        Mapping(
            key="add_debug_info_setting decorator interface",
            val="add_debug_info_setting のデコレーターのインターフェイス",
        ),
        Mapping(key="delete interface", val="delete インターフェイス"),
        Mapping(key="Array class clear interface", val="Array クラスの clear インターフェイス"),
        Mapping(key="remove_children interface", val="remove_children インターフェイス"),
        Mapping(
            key="Graphics class clear interface", val="Graphics クラスの clear インターフェイス"
        ),
        Mapping(
            key="GraphicsBase fill_alpha interface",
            val="GraphicsBase クラスの fill_alpha インターフェイス",
        ),
        Mapping(
            key="GraphicsBase fill_color interface",
            val="GraphicsBase クラスの fill_color インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_alpha interface",
            val="GraphicsBase クラスの line_alpha インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_color interface",
            val="GraphicsBase クラスの line_color インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_thickness interface",
            val="GraphicsBase クラスの line_thickness インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_dot_setting interface",
            val="GraphicsBase クラスの line_dot_setting インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_dash_setting interface",
            val="GraphicsBase クラスの line_dash_setting インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_round_dot_setting interface",
            val="GraphicsBase クラスの line_round_dot_setting インターフェイス",
        ),
        Mapping(
            key="GraphicsBase line_dash_dot_setting interface",
            val="GraphicsBase クラスの line_dash_dot_setting インターフェイス",
        ),
        Mapping(key="Please see also:", val="関連資料:"),
        Mapping(key="## x property interface example", val="## x属性のインターフェイス例"),
        Mapping(
            key="The `x` property updates or gets the instance's x-coordinate:",
            val="`x`属性ではX座標の値の更新もしくは取得を行えます:",
        ),
        Mapping(key="## y property interface example", val="## y属性のインターフェイス例"),
        Mapping(
            key="The `y` property updates or gets the instance's y-coordinate:",
            val="`y`属性ではY座標の値の更新もしくは取得を行えます:",
        ),
        Mapping(key="## width property interface example", val="## width属性のインターフェイス例"),
        Mapping(
            key="The `width` property updates or gets the instance's width:",
            val="`width`属性では幅の値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## height property interface example", val="## height属性のインターフェイス例"
        ),
        Mapping(
            key="The `height` property updates or gets the instance's height:",
            val="`height`属性では高さの値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## fill_color property interface example",
            val="## fill_color属性のインターフェイス例",
        ),
        Mapping(
            key="The `fill_color` property updates or gets the instance's fill color:",
            val="`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## fill_alpha property interface example",
            val="## fill_alpha属性のインターフェイス例",
        ),
        Mapping(
            key="The `fill_alpha` property updates or gets the instance's fill alpha (opacity):",
            val="`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_color property interface example",
            val="## line_color属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_color` property updates or gets the instance's line color:",
            val="`line_color`属性では線の色の値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_alpha property interface example",
            val="## line_alpha属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_alpha` property updates or gets the instance's line alpha (opacity):",
            val="`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_thickness property interface example",
            val="## line_thickness属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_thickness` property updates or gets the instance's line thickness (line width):",
            val="`line_thickness`属性では線の幅の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_dot_setting property interface example",
            val="## line_dot_setting属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_dot_setting` property updates or gets the instance's line dot-style setting:",
            val="`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_dash_setting property interface example",
            val="## line_dash_setting属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_dash_setting` property updates or gets the instance's line dash-style setting:",
            val="`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_round_dot_setting property interface example",
            val="## line_round_dot_setting属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:",
            val="`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## line_dash_dot_setting property interface example",
            val="## line_dash_dot_setting属性のインターフェイス例",
        ),
        Mapping(
            key="The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:",
            val="`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:",
        ),
        Mapping(key="Rectangle class", val="Rectangle クラス"),
        Mapping(
            key="The constructor also accepts each style's argument, such as the `fill_color`.",
            val="コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。",
        ),
        Mapping(key="Circle class", val="Circle クラス"),
        Mapping(key="Ellipse class", val="Ellipse クラス"),
        Mapping(key="Line class", val="Line クラス"),
        Mapping(key="Polyline class", val="Polyline クラス"),
        Mapping(
            key="The constructor also accepts each style's argument, such as the `line_color`.",
            val="コンストラクタは`line_color`などのスタイル設定の引数も受け付けます。",
        ),
        Mapping(
            key="Notes: This attribute's value becomes the same as the arguments' minimum point value.",
            val="特記事項: この属性の値は引数の座標の最小値と同値になります。",
        ),
        Mapping(key="Polygon class", val="Polygon クラス"),
        Mapping(
            key="## Rectangle class constructor API", val="## Rectangle クラスのコンストラクタのAPI"
        ),
        Mapping(
            key="Create a rectangle vector graphic.<hr>",
            val="四角のベクターグラフィックスを作成します。<hr>",
        ),
        Mapping(key="  - A fill-color to set.", val="  - 設定する塗りの色。"),
        Mapping(key="  - A fill-alpha to set.", val="  - 設定する塗りの透明度。"),
        Mapping(key="  - A line-color to set.", val="  - 設定する線の色。"),
        Mapping(key="  - A line-alpha to set.", val="  - 設定する線の透明度。"),
        Mapping(key="  - A line-thickness (line-width) to set.", val="  - 設定の線幅。"),
        Mapping(key="  - A line-cap setting to set.", val="  - 設定する線の端のスタイル設定。"),
        Mapping(key="  - A line-joints setting to set.", val="  - 設定する線の連結部分のスタイル設定。"),
        Mapping(key="  - A dot setting to set.", val="  - 設定する点線のスタイル設定。"),
        Mapping(key="  - A dash setting to set.", val="  - 設定する破線のスタイル設定。"),
        Mapping(key="  - A round-dot setting to set.", val="  - 設定する丸ドットのスタイル設定。"),
        Mapping(
            key="  - A dash-dot (1-dot chain) setting to set.",
            val="  - 設定する一点鎖線のスタイル設定。",
        ),
        Mapping(
            key="  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.",
            val="  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。",
        ),
        Mapping(key="## Circle class constructor API", val="## Circle クラスのコンストラクタのAPI"),
        Mapping(
            key="Create a circle vector graphic.<hr>",
            val="円のベクターグラフィックスを生成します。<hr>",
        ),
        Mapping(
            key="## Ellipse class constructor API", val="## Ellipse クラスのコンストラクタのAPI"
        ),
        Mapping(
            key="Create an ellipse vector graphic.<hr>",
            val="楕円のベクターグラフィックスを生成します。<hr>",
        ),
        Mapping(key="## Line class constructor API", val="## Line クラスのコンストラクタのAPI"),
        Mapping(
            key="Create a line vector graphic.<hr>",
            val="線のベクターグラフィックスを生成します。<hr>",
        ),
        Mapping(key="  - Line start point.", val="  - 線の開始座標。"),
        Mapping(key="  - Line end point.", val="  - 線の終了座標。"),
        Mapping(
            key="## Polygon class constructor API", val="## Polygon クラスのコンストラクタのAPI"
        ),
        Mapping(
            key="Create a polygon vector graphic. This class is similar to the Polyline class, but unlike that, this class connects an end-point and start-point.<hr>",
            val="多角形のベクターグラフィックスを生成します。このクラスはPolylineクラスと似ていますが、Polylineクラスとは異なりこのクラスでは座標の終点と始点が接続される点が異なります。<hr>",
        ),
        Mapping(key="  - List of polygon vertex points.", val="  - 多角形の各頂点の座標のリスト。"),
        Mapping(
            key="## Polyline class constructor API", val="## Polyline クラスのコンストラクタのAPI"
        ),
        Mapping(
            key="Create a polyline vector graphic.<hr>",
            val="折れ線のベクターグラフィックスを生成します。<hr>",
        ),
        Mapping(key="  - List of line points.", val="  - 線の座標のリスト。"),
        Mapping(
            key="## rotation_around_center property interface example",
            val="## rotation_around_center属性のインターフェイス例",
        ),
        Mapping(
            key="The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:",
            val="`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## set_rotation_around_point and get_rotation_around_point methods interfaces example",
            val="## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例",
        ),
        Mapping(
            key="The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.",
            val="`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。",
        ),
        Mapping(
            key="Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:",
            val="同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:",
        ),
        Mapping(
            key="## flip_x property interface example", val="## flip_x属性のインターフェイス例"
        ),
        Mapping(
            key="The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:",
            val="`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## flip_y property interface example", val="## flip_y属性のインターフェイス例"
        ),
        Mapping(
            key="The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:",
            val="`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## skew_x property interface example", val="## skew_x属性のインターフェイス例"
        ),
        Mapping(
            key="## skew_y property interface example", val="## skew_y属性のインターフェイス例"
        ),
        Mapping(
            key="The `skew_x` property updates or gets the instance's skew-x (distortion) value:",
            val="`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.",
            val="特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。",
        ),
        Mapping(
            key="The `skew_y` property updates or gets the instance's skew-y (distortion) value:",
            val="`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.",
            val="  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",
        ),
        Mapping(
            key="The scale's minimum value is almost zero, and it does not become negative.<hr>",
            val="拡縮の最小値はほぼ0となり、その値は負の値にはなりません。<hr>",
        ),
        Mapping(
            key="  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.",
            val="  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。",
        ),
        Mapping(
            key="  - The trace's outer frames index adjustment setting. This function uses this argument to adjust the caller's information. Also, this function only uses this argument in internal logic.",
            val="  - trace関数の関数外の参照するフレームのインデックスの調整値です。この引数は呼び出し元の情報の位置を調整するのに使用されます。また、この引数は内部のロジックでのみ使用されるため通常は設定する必要はありません。",
        ),
        Mapping(
            key="## scale_x_from_center property interface example",
            val="## scale_x_from_center属性のインターフェイス例",
        ),
        Mapping(
            key="The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:",
            val="`scale_x_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## scale_y_from_center property interface example",
            val="## scale_y_from_center属性のインターフェイス例",
        ),
        Mapping(
            key="The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:",
            val="`scale_y_from_center`属性ではインスタンスの中央座標でのX軸の拡縮値の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## set_scale_x_from_point and get_scale_x_from_point methods interfaces example",
            val="## set_scale_x_from_pointとget_scale_x_from_pointメソッドのインターフェイス例",
        ),
        Mapping(
            key="The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.",
            val="`set_scale_x_from_point`メソッドは指定されたX座標を基準としてX軸の拡縮値を更新します。",
        ),
        Mapping(
            key="Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:",
            val="同様に、`get_scale_x_from_point`メソッドでは指定されたX座標を基準としたX軸の拡縮値を取得します:",
        ),
        Mapping(
            key="## set_scale_y_from_point and get_scale_y_from_point methods interfaces example",
            val="## set_scale_y_from_pointとget_scale_y_from_pointメソッドのインターフェイス例",
        ),
        Mapping(
            key="The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.",
            val="`set_scale_y_from_point`メソッドは指定されたY座標を基準としてY軸の拡縮値を更新します。",
        ),
        Mapping(
            key="Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:",
            val="同様に、`get_scale_y_from_point`メソッドでは指定されたY座標を基準としたY軸の拡縮値を取得します。",
        ),
        Mapping(
            key="Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.",
            val="主にこの設定は`Path`クラスのコンストラクタと`draw_path`メソッドのインターフェイスで使用されます。",
        ),
        Mapping(
            key="## Relative position setting",
            val="## 相対座標設定",
        ),
        Mapping(
            key="The constructor's `relative` optional argument changes its behavior.",
            val="コンストラクタの`relative`のオプション引数はその挙動を変更します。",
        ),
        Mapping(
            key="For example, if you set True to its argument, coordinates become relative.",
            val="例として、もしその引数にTrueを指定した場合座標は相対座標として設定されます。",
        ),
        Mapping(
            key="The default setting is False, and it becomes absolute.",
            val="デフォルト値はFalseとなっており、この設定では絶対座標として扱われます。",
        ),
        Mapping(
            key="## PathMoveTo class constructor API",
            val="## PathMoveTo クラスのコンストラクタのAPI",
        ),
        Mapping(
            key="  - A boolean value indicates whether the path coordinates are relative or not (absolute).",
            val="  - パスの座標が相対座標として扱うかもしくは絶対座標として扱うかどうかの真偽値。",
        ),
        Mapping(
            key="The constructor also accepts each style's argument, such as the `fill_color` and `line_color`.",
            val="コンストラクタは`fill_color`や`line_color`などのスタイル設定用の引数も受け付けます。",
        ),
        Mapping(
            key="The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.",
            val="`Path`クラスのコンストラクタもしくは`draw_path`メソッドのインターフェイスの`path_data_list`引数でそのインスタンスが必要とされます。",
        ),
        Mapping(
            key="## PathLineTo class constructor API",
            val="## PathLineTo クラスのコンストラクタのAPI",
        ),
        Mapping(
            key="Path data class for the SVG's `2D bezier curve` (Q).<hr>",
            val="SVGの2次のベジェ曲線（Q）のデータを設定するためのクラスです。<hr>",
        ),
        Mapping(
            key="  - X-coordinate of the bezier's control point.",
            val="  - ベジェ曲線の制御点のX座標。",
        ),
        Mapping(
            key="  - Y-coordinate of the bezier's control point.",
            val="  - ベジェ曲線の制御点のY座標。",
        ),
        Mapping(
            key="  - X-coordinate of the destination point.",
            val="  - 終点のX座標。",
        ),
        Mapping(
            key="  - Y-coordinate of the destination point.",
            val="  - 終点のY座標。",
        ),
        Mapping(
            key="Path data class for the SVG `continual 2D bezier curve` (T).<hr>",
            val="SVGの連続した2次元のベジェ曲線のデータ設定用のクラスです。<hr>",
        ),
        Mapping(
            key="Path data class for the SVG's `3D bezier curve` (C).<hr>",
            val="SVGの3次のベジェ曲線（C）のパスデータのためのクラスです。<hr>",
        ),
        Mapping(
            key="  - X-coordinate of the bezier's first control point.",
            val="  - ベジェ曲線の最初の制御点のX座標。",
        ),
        Mapping(
            key="  - Y-coordinate of the bezier's first control point.",
            val="  - ベジェ曲線の最初の制御点のY座標。",
        ),
        Mapping(
            key="  - X-coordinate of the bezier's second control point.",
            val="  - ベジェ曲線の2つ目の制御点のX座標。",
        ),
        Mapping(
            key="  - Y-coordinate of the bezier's second control point.",
            val="  - ベジェ曲線の2つ目の制御点のY座標。",
        ),
        Mapping(
            key="## PathBezier3D class constructor API",
            val="## PathBezier3D クラスのコンストラクタのAPI",
        ),
        Mapping(
            key="Path class",
            val="Path クラス",
        ),
        Mapping(
            key="PathMoveTo class",
            val="PathMoveTo クラス",
        ),
        Mapping(
            key="PathLineTo class",
            val="PathLineTo クラス",
        ),
        Mapping(
            key="PathHorizontal class",
            val="PathHorizontal クラス",
        ),
        Mapping(
            key="PathVertical class",
            val="PathVertical クラス",
        ),
        Mapping(
            key="PathClose class",
            val="PathClose クラス",
        ),
        Mapping(
            key="PathBezier2D class",
            val="PathBezier2D クラス",
        ),
        Mapping(
            key="PathBezier2DContinual class",
            val="PathBezier2DContinual クラス",
        ),
        Mapping(
            key="PathBezier3DContinual class",
            val="PathBezier3DContinual クラス",
        ),
        Mapping(
            key="## draw_path API",
            val="## draw_path API",
        ),
        Mapping(
            key="Draw a path vector graphics.<hr>",
            val="パスのベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(
            key="  - Target path data settings, such as the ap.PathData.MoveTo.",
            val="  - ap.PathData.MoveToなどの対象のパスデータの設定のリスト。",
        ),
        Mapping(
            key="  - Created path graphics instance.",
            val="  - 作成されたパスのグラフィックスのインスタンス。",
        ),
        Mapping(
            key="PathBezier3D class",
            val="PathBezier3D クラス",
        ),
        Mapping(
            key="Graphics draw_path interface",
            val="Graphics クラスの draw_path インターフェイス",
        ),
        Mapping(
            key="The `PathMoveTo` class is the class to set a new position on a path.",
            val="`PathMoveTo`クラスはパスに新しい座標設定を追加するためのクラスです。",
        ),
        Mapping(
            key="The `PathLineTo` class is the class to set a new line from the current position on a path.",
            val="`PathLineTo`クラスは現在設定されている座標位置から新たな線のパスを描画します。",
        ),
        Mapping(
            key="The `PathHorizontal` class is the class to set a new horizontal line on a path.",
            val="`PathHorizontal`クラスはパス上に水平方向の直線の描画設定を追加するためのクラスです。",
        ),
        Mapping(
            key="The `PathVertical` class is the class to set a new vertical line on a path.",
            val="`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。",
        ),
        Mapping(
            key="The `PathClose` class is the class to close a path.",
            val="`PathVertical`クラスはパス上に新しい垂直の直線の設定を追加するためのクラスです。",
        ),
        Mapping(
            key="The `PathBezier2D` class is the class to set a 2D bezier curve on a path.",
            val="`PathBezier2D`クラスはパスへ2次のベジェ曲線を設定するためのクラスです。",
        ),
        Mapping(
            key="The `PathBezier2DContinual` class is the class to set a continual 2D bezier curve on a path.",
            val="PathBezier2DContinual`クラスはパスに連続した2次元のベジェ曲線を設定するためのクラスです。",
        ),
        Mapping(
            key="The `PathBezier3D` class is the class to set a 3D bezier curve on a path.",
            val="`PathBezier3D`クラスはパス上に3次のベジェ曲線を設定するためのクラスです。",
        ),
        Mapping(
            key="The `path_data_list` argument is a list of each path setting, such as the `PathLineTo` or `PathBezier2D`.",
            val="`path_data_list`引数は`PathLineTo`や`PathBezier2D`などの各パス設定を格納したリストです。",
        ),
        Mapping(
            key="The `Path` class constructor requires the `path_data_list` argument.",
            val="`Path`クラスのコンストラクタは`path_data_list`引数を必要とします。",
        ),
        Mapping(
            key="## PathLineTo class setting",
            val="## PathLineTo クラス設定",
        ),
        Mapping(
            key="## PathHorizontal class setting",
            val="## PathHorizontal クラス設定",
        ),
        Mapping(
            key="## PathVertical class setting",
            val="## PathVertical クラス設定",
        ),
        Mapping(
            key="## PathClose class setting",
            val="## PathClose クラス設定",
        ),
        Mapping(
            key="## PathBezier2D class setting",
            val="## PathBezier2D クラス設定",
        ),
        Mapping(
            key="## PathBezier2DContinual class setting",
            val="## PathBezier2DContinual クラス設定",
        ),
        Mapping(
            key="## PathBezier3D class setting",
            val="## PathBezier3D クラス設定",
        ),
        Mapping(
            key="## PathBezier3DContinual class setting",
            val="## PathBezier3DContinual クラス設定",
        ),
        Mapping(
            key="## Path class constructor API",
            val="## Path クラスのコンストラクタのAPI",
        ),
        Mapping(
            key="Create a path vector graphic.<hr>",
            val="パスのベクターグラフィックスを生成します。<hr>",
        ),
        Mapping(
            key="## PathMoveTo class setting",
            val="## PathMoveTo クラス設定",
        ),
        Mapping(
            key="The `PathBezier3DContinual` class is the class to set a continual 3D bezier curve on a path.",
            val="`PathBezier3DContinual`クラスはパス上に連続した3次ベジェ曲線を設定するためのクラスです。",
        ),
        Mapping(
            key="**[Interface summary]**",
            val="**[インターフェイス概要]**",
        ),
        Mapping(
            key="Start an animation with current settings.<hr>",
            val="現在の設定を使ってアニメーションを開始します。<hr>",
        ),
        Mapping(
            key="Get an animation target instance.<hr>",
            val="アニメーション対象のインスタンスを取得します。<hr>",
        ),
        Mapping(
            key="Add an animation complete event listener setting.<hr>",
            val="アニメーション終了時のイベントリスナーの設定を追加します。<hr>",
        ),
        Mapping(
            key="Animation event class.<hr>",
            val="アニメーションイベント用のクラスです。<hr>",
        ),
        Mapping(
            key="Get an animation setting instance of listening to this event.<hr>",
            val="このイベントのリスナーとしてのアニメーション設定のインスタンスを取得します。<hr>",
        ),
        Mapping(
            key="Set the fill alpha (opacity) animation setting.<hr>",
            val="塗りの透明度のアニメーション設定を行います。<hr>",
        ),
        Mapping(
            key="Set the fill color animation setting.<hr>",
            val="塗りの色のアニメーション設定を行います。<hr>",
        ),
        Mapping(
            key="Finish all animations (set the animation last value to each attribute).<hr>",
            val="全てのアニメーションを終了します（各属性にアニメーション終了時の値を設定します）。<hr>",
        ),
        Mapping(
            key="Set the parallel animation setting.<hr>",
            val="並列実行されるアニメーション設定を行います。<hr>",
        ),
        Mapping(
            key="Stop all animations.<hr>",
            val="全てのアニメーションを停止します。<hr>",
        ),
        Mapping(
            key="Restart all paused animations.<hr>",
            val="停止している全てのアニメーションを再開します。<hr>",
        ),
        Mapping(
            key="Set the radius animation setting.<hr>",
            val="半径のアニメーション設定を行います。<hr>",
        ),
        Mapping(
            key="Stop all animations and reset.<hr>",
            val="全てのアニメーションを停止しアニメーション内容をリセットします。<hr>",
        ),
        Mapping(
            key="Append js expression.<hr>",
            val="JavaScriptのコードの追加を行います。<hr>",
        ),
        Mapping(
            key="Array class for the apysc library.<hr>",
            val="apyscライブラリの配列を扱うためのクラスです。<hr>",
        ),
        Mapping(
            key="Get a current array value.<hr>",
            val="現在の配列の値を取得します。<hr>",
        ),
        Mapping(
            key="Add any value to the end of this array. This method behaves the same `push` method.<hr>",
            val="任意の値をこの配列の末尾に加えます。このメソッドは`push`メソッドと同様に動作します。<hr>",
        ),
        Mapping(
            key="Add any value to the end of this array. This interface behaves the same as the `append` method.<hr>",
            val="任意の値をこの配列の末尾に加えます。このメソッドは`append`メソッドと同様に動作します。<hr>",
        ),
        Mapping(
            key="Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to the concat method. Still, there is a difference in whether updating the same variable (extend) or returning as a different variable (concat).<hr>",
            val="引数に指定された配列をこの配列へ連結します。このインターフェイスは引数の配列の値をこの配列の後に配置します。このメソッドはconcatメソッドと似た挙動をしますが、配列の値を直接更新するか（extend）もしくは別の値として返却するか（concat）の違いがあります。<hr>",
        ),
        Mapping(
            key="Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to extend method, but there is a difference in whether updating the same variable (extend) or returning as a different variable (concat).<hr>",
            val="引数に指定された配列をこの配列へ連結します。このインターフェイスは引数の配列の値をこの配列の後に配置します。このメソッドはextendメソッドと似た挙動をしますが、配列の値を直接更新するか（extend）もしくは別の値として返却するか（concat）の違いがあります。<hr>",
        ),
        Mapping(
            key="Search specified value's index and return it.<hr>",
            val="指定された値のインデックス位置を検索しその値を返却します。<hr>",
        ),
        Mapping(
            key="Insert value to this array at a specified index. This interface behaves in the same `insert_at` method.<hr>",
            val="この配列の指定されたインデックスの位置へ値を挿入します。このインターフェイスは`insert_at`メソッドと同じ挙動をします。<hr>",
        ),
        Mapping(
            key="Insert value to this array at a specified index. This interface behaves in the same `insert` method.<hr>",
            val="この配列の指定されたインデックスの位置へ値を挿入します。このインターフェイスは`insert`メソッドと同じ挙動をします。<hr>",
        ),
        Mapping(
            key="Join this array value with a specified separator string.<hr>",
            val="指定された区切り用の文字列を使って配列の値を連結します。<hr>",
        ),
        Mapping(
            key="Get length of this array.<hr>",
            val="この配列の長さ（値の数）を取得します。<hr>",
        ),
        Mapping(
            key="Remove this array's last value and return it.<hr>",
            val="この配列の末尾の値を取り除き、その値を返却します。<hr>",
        ),
        Mapping(
            key="Remove a specified value from this array.<hr>",
            val="指定された値をこの配列から取り除きます。<hr>",
        ),
        Mapping(
            key="Remove a specified index value from this array.<hr>",
            val="指定されたインデックスの値をこの配列から取り除きます。<hr>",
        ),
        Mapping(
            key="Reverse this array in place.<hr>",
            val="この配列の値を直接逆順にします。<hr>",
        ),
        Mapping(
            key="Slice this array by specified start and end indexes.<hr>",
            val="指定された開始と終了のインデックス範囲でこの配列をスライスします。<hr>",
        ),
        Mapping(
            key="Sort this array in place.<hr>",
            val="この配列の値を直接ソートします。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the Array values equal condition.<hr>",
            val="配列の値の等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the Array values not equal condition.<hr>",
            val="配列の値の非等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the defined (not undefined) value condition.<hr>",
            val="定義済みの値かどうかの条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the undefined value condition.<hr>",
            val="未定義の値かどうかの条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the Dictionary values equal condition.<hr>",
            val="辞書の値の等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the Dictionary values not equal condition.<hr>",
            val="辞書の値の非等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the equal condition.<hr>",
            val="等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the not equal condition.<hr>",
            val="非等値条件のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the true condition.<hr>",
            val="真偽値の真の値のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="JavaScript assertion interface for the false condition.<hr>",
            val="真偽値の偽の値のためのJavaScript上のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="Add a custom event listener setting.<hr>",
            val="カスタムイベントのリスナー設定を追加します。<hr>",
        ),
        Mapping(
            key="Add a custom event trigger setting.<hr>",
            val="カスタムイベントのトリガー設定を追加します。<hr>",
        ),
        Mapping(
            key="Boolean class for apysc library.<hr>",
            val="apyscライブラリのための真偽値のクラスです。<hr>",
        ),
        Mapping(
            key="Get a current boolean value.<hr>",
            val="現在の真偽値の値を取得します。<hr>",
        ),
        Mapping(
            key="Get a not condition Boolean value.<hr>",
            val="否定条件を加えた真偽値の値を取得します。<hr>",
        ),
        Mapping(
            key="Add a click event listener setting.<hr>",
            val="クリックイベントのリスナー設定を追加します。<hr>",
        ),
        Mapping(
            key="Unbind specified handler's click event.<hr>",
            val="指定されたクリックイベントのハンドラー設定を取り除きます。<hr>",
        ),
        Mapping(
            key="Unbind all click events.<hr>",
            val="全てのクリックイベント設定を取り除きます。<hr>",
        ),
        Mapping(
            key="The loop continue expression class.<hr>",
            val="ループのcontinueの表現を扱うためのクラスです。<hr>",
        ),
        Mapping(
            key="Add a double-click event listener setting.<hr>",
            val="ダブルクリックイベントのリスナー設定を追加します。<hr>",
        ),
        Mapping(
            key="Unbind a specified handler's double click event.<hr>",
            val="指定されたダブルクリックイベントのハンドラー設定を取り除きます。<hr>",
        ),
        Mapping(
            key="Unbind all double click events.<hr>",
            val="全てのダブルクリックイベント設定を取り除きます。<hr>",
        ),
        Mapping(
            key="Dictionary class for the apysc library.<hr>",
            val="apyscライブラリのための辞書のクラスです。<hr>",
        ),
        Mapping(
            key="Get a current dict value.<hr>",
            val="現在の辞書の値を取得します。<hr>",
        ),
        Mapping(
            key="Get a specified key dictionary value. If this dictionary hasn't a specified key, this interface returns a default value.<hr>",
            val="指定されたキーの辞書内の値を取得します。もし指定されたキーが辞書に存在しない場合、このインターフェイスはデフォルト値を返却します。<hr>",
        ),
        Mapping(
            key="Get length of this dictionary values.<hr>",
            val="辞書の値の長さ（件数）を取得します。<hr>",
        ),
        Mapping(
            key="Get a CSS value string.<hr>",
            val="CSSの設定値の文字列を取得します。<hr>",
        ),
        Mapping(
            key="Set a specified value string to the CSS.<hr>",
            val="CSSに指定された文字列の値を設定します。<hr>",
        ),
        Mapping(
            key="Get a parent instance that has an add_child and remove_child interfaces.<hr>",
            val="add_childやremove_childなどのインターフェイスを持った親のインスタンスを取得します。<hr>",
        ),
        Mapping(
            key="Remove this instance from a parent.<hr>",
            val="親のインスタンスからこのインスタンスを取り除きます。<hr>",
        ),
        Mapping(
            key="Get a visibility value of this instance.<hr>",
            val="このインスタンスの可視状態かどうかの値を取得します。<hr>",
        ),
        Mapping(
            key="Save the overall HTML and display it on Google Colaboratory.<hr>",
            val="HTML全体を保存し結果をGoogle Colaboratory上で表示します。<hr>",
        ),
        Mapping(
            key="Save the overall HTML and display it on the Jupyter.<hr>",
            val="HTML全体を保存し結果をJupyter上で表示します。<hr>",
        ),
        Mapping(
            key="A class to append the `else if` branch instruction expression.<hr>",
            val="`else if`の分岐条件の表現を追加するためのクラスです。<hr>",
        ),
        Mapping(
            key="A class to append else branch instruction expression.<hr>",
            val="elseの分岐条件の表現を追加するためのクラスです。<hr>",
        ),
        Mapping(
            key="Prevent event's default behavior.<hr>",
            val="イベントのデフォルトの挙動を無効化します。<hr>",
        ),
        Mapping(
            key="Stop event propagation.<hr>",
            val="イベントの伝搬を停止させます。<hr>",
        ),
        Mapping(
            key="A class to append for the (loop) expression.<hr>",
            val="ループのfor文の表現を追加するためのクラスです。<hr>",
        ),
        Mapping(
            key="Get a child at a specified index.<hr>",
            val="指定されたインデックスの子を取得します。<hr>",
        ),
        Mapping(
            key="Get a boolean value whether the x-axis is flipping or not.<hr>",
            val="横軸に対して反転しているかどうかの真偽値を取得します。<hr>",
        ),
        Mapping(
            key="Get a boolean value whether the y-axis is flipping or not.<hr>",
            val="縦軸に対して反転しているかどうかの真偽値を取得します。<hr>",
        ),
        Mapping(
            key="Get a rotation value around the given coordinates.<hr>",
            val="指定された座標を基準とした回転量を取得します。<hr>",
        ),
        Mapping(
            key="Path data class for SVG's `continual 3D bezier curve` (S).<hr>",
            val="SVGの連続した3次ベジェ曲線（S）のためのパスデータのクラスです。<hr>",
        ),
        Mapping(
            key="Path data class for the SVG's `close path` (Z).<hr>",
            val="SVGのパスを閉じる指定（Z）のためのパスデータのクラスです。<hr>",
        ),
        Mapping(
            key="Path data class for the SVG's `horizontal line` (H).<hr>",
            val="SVGの水平方向への線（H）の描画のためのパスデータのクラスです。<hr>",
        ),
        Mapping(
            key="Path data class for the SVG `line to` (L).<hr>",
            val="SVGの特定座標に対する線（L）の描画のためのパスデータのクラスです。<hr>",
        ),
        Mapping(
            key="Path data class for the SVG `move to` (M).<hr>",
            val="SVGの特定座標への移動（M）のためのパスデータのクラスです。<hr>",
        ),
        Mapping(
            key="Path data class for the SVG `vertical line' (V).<hr>",
            val="SVGの垂直方向への線（V）の描画のためのパスデータのクラスです。<hr>",
        ),
        Mapping(
            key="Create a basic display object that can be a parent.<hr>",
            val="親になることの出来る基本的な表示用のオブジェクトを作成します。<hr>",
        ),
        Mapping(
            key="## year property API",
            val="## year 属性のAPI",
        ),
        Mapping(
            key="Get a current year's value.<hr>",
            val="現在の年の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current year value.",
            val="  - 現在の年の値。",
        ),
        Mapping(
            key="## DateTime class",
            val="## DateTime クラス",
        ),
        Mapping(
            key="A `DateTime` instance has its property interface.",
            val="`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",
        ),
        Mapping(
            key="## month property API",
            val="## month 属性のAPI",
        ),
        Mapping(
            key="Get a current month's value.<hr>",
            val="現在の月の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current month value.",
            val="  - 現在の月の値。",
        ),
        Mapping(
            key="## day property API",
            val="## day 属性のAPI",
        ),
        Mapping(
            key="Get a current day's value.<hr>",
            val="現在の日の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current-day value.",
            val="  - 現在の日の値。",
        ),
        Mapping(
            key="## hour property API",
            val="## hour 属性のAPI",
        ),
        Mapping(
            key="Get a current hour's value.<hr>",
            val="現在の時間の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current hour value.",
            val="  - 現在の時間の値。",
        ),
        Mapping(
            key="## minute property API",
            val="## minute 属性のAPI",
        ),
        Mapping(
            key="Get a current minute's value.<hr>",
            val="現在の分の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current minute value.",
            val="  - 現在の分の値。",
        ),
        Mapping(
            key="## second property API",
            val="## second 属性のAPI",
        ),
        Mapping(
            key="Get a current second's value.<hr>",
            val="現在の秒の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current second value.",
            val="  - 現在の秒の値。",
        ),
        Mapping(
            key="## millisecond property API",
            val="## millisecond 属性のAPI",
        ),
        Mapping(
            key="Get a current millisecond value.<hr>",
            val="現在のミリ秒の値を取得します。<hr>",
        ),
        Mapping(
            key="  - A current millisecond value.",
            val="  - 現在のミリ秒の値。",
        ),
        Mapping(
            key="A `DateTime` instance has these properties interfaces.",
            val="`DateTime`クラスのインスタンスがこれらの各属性のインターフェイスを持っています。",
        ),
        Mapping(
            key="## weekday_js property API",
            val="## weekday_js 属性のAPI",
        ),
        Mapping(
            key="Get a current weekday value. This interface sets the weekday "
            "based on the JavaScript value as follows: ",
            val="現在の曜日の値を取得します。このインターフェイスは以下のようにJavaScriptの曜日の値を" "ベースとした値を設定します。",
        ),
        Mapping(
            key="<br> ・0 -> Sunday ",
            val="<br> ・0 -> 日曜 ",
        ),
        Mapping(
            key="<br> ・1 -> Monday ",
            val="<br> ・1 -> 月曜 ",
        ),
        Mapping(
            key="<br> ・2 -> Tuesday ",
            val="<br> ・2 -> 火曜 ",
        ),
        Mapping(
            key="<br> ・3 -> Wednesday ",
            val="<br> ・3 -> 水曜 ",
        ),
        Mapping(
            key="<br> ・4 -> Thursday ",
            val="<br> ・4 -> 木曜 ",
        ),
        Mapping(
            key="<br> ・5 -> Friday ",
            val="<br> ・5 -> 金曜 ",
        ),
        Mapping(
            key="<br> ・6 -> Saturday<hr>",
            val="<br> ・6 -> 土曜<hr>",
        ),
        Mapping(
            key="  - A current weekday value.",
            val="  - 現在の曜日の値。",
        ),
        Mapping(
            key="## weekday_py property API",
            val="## weekday_py 属性のAPI",
        ),
        Mapping(
            key="<br> ・0 -> Monday ",
            val="<br> ・0 -> 月曜 ",
        ),
        Mapping(
            key="<br> ・1 -> Thursday ",
            val="<br> ・1 -> 火曜 ",
        ),
        Mapping(
            key="<br> ・2 -> Wednesday ",
            val="<br> ・2 -> 水曜 ",
        ),
        Mapping(
            key="<br> ・3 -> Thursday ",
            val="<br> ・3 -> 木曜 ",
        ),
        Mapping(
            key="<br> ・4 -> Friday ",
            val="<br> ・4 -> 金曜 ",
        ),
        Mapping(
            key="<br> ・5 -> Saturday ",
            val="<br> ・5 -> 土曜 ",
        ),
        Mapping(
            key="<br> ・6 -> Sunday<hr>",
            val="<br> ・6 -> 日曜<hr>",
        ),
        Mapping(
            key="Get a current weekday value. This interface sets the weekday based on "
            "the Python value as follows: ",
            val="現在の曜日の値を取得します。このインターフェイスは以下のようにPythonの曜日の値を" "ベースとした値を設定します。",
        ),
        Mapping(
            key="## now class method API",
            val="## now のクラスメソッドのAPI",
        ),
        Mapping(
            key="Get a `DateTime` instance of the current time.<hr>",
            val="現在時刻が設定された`DateTime`クラスのインスタンスを取得します。<hr>",
        ),
        Mapping(
            key="  - A created `DateTime` instance.",
            val="  - 生成された`DateTime`クラスのインスタンス。",
        ),
        Mapping(
            key="DateTime class year property",
            val="DateTime クラスの year 属性",
        ),
        Mapping(
            key="DateTime class month property",
            val="DateTime クラスの month 属性",
        ),
        Mapping(
            key="DateTime class day property",
            val="DateTime クラスの day 属性",
        ),
        Mapping(
            key="DateTime class hour property",
            val="DateTime クラスの hour 属性",
        ),
        Mapping(
            key="DateTime class minute property",
            val="DateTime クラスの minute 属性",
        ),
        Mapping(
            key="DateTime class second property",
            val="DateTime クラスの second 属性",
        ),
        Mapping(
            key="DateTime class millisecond property",
            val="DateTime クラスの millisecond 属性",
        ),
        Mapping(
            key="DateTime class weekday_js and weekday_py properties",
            val="DateTime クラスの weekday_js と weekday_py 属性",
        ),
        Mapping(
            key="DateTime class now interface",
            val="DateTime クラスの now インターフェイス",
        ),
        Mapping(
            key="## DateTime class constructor API",
            val="## DateTime クラスのコンストラクタのAPI",
        ),
        Mapping(
            key="The class for datetime-related interfaces.<hr>",
            val="日時に絡んだインターフェイスのためのクラスです。<hr>",
        ),
        Mapping(
            key="  - Four-digit year.",
            val="  - 4桁の数字の年。",
        ),
        Mapping(
            key="  - Two-digit month (1 to 12).",
            val="  - 2桁の月（1～12）。",
        ),
        Mapping(
            key="  - Two-digit day (1 to 31).",
            val="  - 2桁の日（1～31）。",
        ),
        Mapping(
            key="  - Two-digit hour (0 to 23).",
            val="  - 2桁の時（0～23）。",
        ),
        Mapping(
            key="  - Two-digit minute (0 to 59).",
            val="  - 2桁の分（0～59）。",
        ),
        Mapping(
            key="  - Two-digit second (0 to 59).",
            val="  - 2桁の秒（0～59）。",
        ),
        Mapping(
            key="  - Millisecond (0 to 999).",
            val="  - ミリ秒（0～999）",
        ),
        Mapping(
            key="  - A boolean indicates whether to skip an initial "
            "substitution expression or not. The `DateTime` class uses "
            "this option internally.",
            val="  - 初期値の代入表現の追加をスキップするかどうかの真偽値。`DateTime`クラスでは内部でのみこのオプションを使用します。",
        ),
        Mapping(
            key="## assert_less API",
            val="## assert_less のAPI",
        ),
        Mapping(
            key="JavaScript assertion interface for the less than condition.<hr>",
            val="JavaScriptの未満条件のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="  - Left-side (less) value to compare.",
            val="  - 比較用の左辺側の値（小さい側の値）。",
        ),
        Mapping(
            key="  - Right-side (greater) value to compare.",
            val="  - 比較用の右辺側の値（大きい側の値）。",
        ),
        Mapping(
            key="## assert_less_equal API",
            val="## assert_less_equal のAPI",
        ),
        Mapping(
            key="JavaScript assertion interface for the less than or equal "
            "to condition.<hr>",
            val="JavaScriptの以下条件のアサーションのインターフェイスです。<hr>",
        ),
        Mapping(
            key="These arguments only accept numeric values, such as the Python "
            "built-in `int`, `float`, apysc `Int`, or `Number` value.",
            val="これらの引数はPythonビルトインの`int`や`float`、apyscの`Int`や`Number`などの数値の値のみ受け付けます。",
        ),
        Mapping(
            key="The `msg` argument is optional.",
            val="`msg`引数は省略可です。",
        ),
        Mapping(
            key="This interface displays a specified `msg` (message) argument to "
            "the browser console when an assertion fails.",
            val="このインターフェイスはアサーションが失敗した際に`msg`（message）引数の値をブラウザのコンソール上に表示します。",
        ),
        Mapping(
            key="The following example fails an assertion and displays the "
            "`Assertion failed` message on the browser console:",
            val="`以下の例ではアサーションが失敗し、`Assertion failed`というメッセージがブラウザ上のコンソールに表示されます:",
        ),
        Mapping(
            key="## assert_greater API",
            val="## assert_greater のAPI",
        ),
        Mapping(
            key="JavaScript assertion interface for the greater than condition.<hr>",
            val="JavaScriptの超過条件のアサーションのためのインターフェイスです。<hr>",
        ),
        Mapping(
            key="  - Left-side (greater) value to compare.",
            val="  - 比較用の左辺の値（大きい側の値）。",
        ),
        Mapping(
            key="  - Right-side (less) value to compare.",
            val="  - 比較用の右辺の値（小さい側の値）。",
        ),
        Mapping(
            key="## assert_greater_equal API",
            val="## assert_greater_equal のAPI",
        ),
        Mapping(
            key="JavaScript assertion interface for the greater than or equal to "
            "condition.<hr>",
            val="JavaScriptの以上の条件のアサーションのためのインターフェイスです。<hr>",
        ),
        Mapping(
            key="## remove_children API",
            val="## remove_children のAPI",
        ),
        Mapping(
            key="Remove all children from this instance.<hr>",
            val="このインスタンスから全ての子要素を取り除きます。<hr>",
        ),
        Mapping(
            key="This method interface requires no arguments.",
            val="このメソッドでは引数を必要としません。",
        ),
        Mapping(
            key="## TimeDelta class",
            val="## TimeDelta クラス",
        ),
        Mapping(
            key="## days property API",
            val="## days 属性のAPI",
        ),
        Mapping(
            key="Get days in the duration.<hr>",
            val="時間の間隔値の日数を取得します。<hr>",
        ),
        Mapping(
            key="  - Days value. This interface ignores a fraction.",
            val="  - 日数値。小数点数の分は無視されます。",
        ),
        Mapping(
            key="## total_seconds method API",
            val="## total_seconds メソッドのAPI",
        ),
        Mapping(
            key="Get the total seconds in the duration.<hr>",
            val="時間の間隔値の合計秒数を取得します。<hr>",
        ),
        Mapping(
            key="  - Total seconds in the duration.",
            val="  - 時間の間隔値の合計秒数。",
        ),
        Mapping(
            key="TimeDelta class days interface",
            val="TimeDelta クラスの days インターフェイス",
        ),
        Mapping(
            key="TimeDelta class",
            val="TimeDelta クラス",
        ),
        Mapping(
            key="TimeDelta class total_seconds interface",
            val="TimeDelta クラスの total_seconds インターフェイス",
        ),
        Mapping(
            key="The `Str` class is the alias of `String`.<hr>",
            val="`Str`クラスは`String`クラスのエイリアスとなります。<hr>",
        ),
        Mapping(
            key="## enter_frame API",
            val="## enter_frame のAPI",
        ),
        Mapping(
            key="Add an enter frame event listener setting.<hr>",
            val="enter frameのイベントのリスナー設定を追加します。<hr>",
        ),
        Mapping(
            key="  - A handler function to handle the enter frame event.",
            val="  - enter frameイベントを扱うためのハンドラの関数。",
        ),
        Mapping(
            key="  - Frame per second to set.",
            val="  - 設定する1秒辺りのフレーム数（frame per second）。",
        ),
        Mapping(
            key="  - Optional arguments to pass to a handler function.",
            val="  - ハンドラの関数へと渡される追加のパラメーターの引数値。",
        ),
        Mapping(
            key="If this is the second call of this interface and an argument is the same function, this interface ignores `options` argument (it changes only the running status and `fps` setting).<hr>",
            val="もしこのインターフェイスの呼び出しが2回目且つ指定されたハンドラの引数の値が同一の場合、このインターフェイスは`options`引数の指定を無視します（実行中かどうかのステータスと`fps`の設定のみ更新します）。<hr>",
        ),
        Mapping(
            key="## unbind_enter_frame API",
            val="## unbind_enter_frame のAPI",
        ),
        Mapping(
            key="Unbind a specified handler's enter-frame event.<hr>",
            val="指定されたハンドラのenter-frameイベントの設定を解除します。<hr>",
        ),
        Mapping(
            key="  - Unbinding target callable.",
            val="  - 設定を取り除く対象のcallableオブジェクト。",
        ),
        Mapping(
            key="- _EnterFrameEventNotRegistered: If there is no unbinding target of a specified handler.",
            val="- _EnterFrameEventNotRegistered: もし指定されたハンドラの設定削除対象が存在しない場合。",
        ),
        Mapping(
            key="## unbind_enter_frame_all API",
            val="## unbind_enter_frame_all のAPI",
        ),
        Mapping(
            key="Unbind all enter-frame events.<hr>",
            val="すべてのenter-frameイベントの設定を解除します。<hr>",
        ),
        Mapping(
            key="enter_frame interface",
            val="enter_frame インターフェイス",
        ),
        Mapping(
            key="## x1 property interface example",
            val="## x1属性のインターフェイス例",
        ),
        Mapping(
            key="The `x1` property updates or gets the instance's first vertex x-coordinate:",
            val="`x1`属性では1つ目の頂点のX座標の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## y1 property interface example",
            val="## y1属性のインターフェイス例",
        ),
        Mapping(
            key="The `y1` property updates or gets the instance's first vertex y-coordinate:",
            val="`y1`属性では1つ目の頂点のY座標の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## x2 property interface example",
            val="## x2属性のインターフェイス例",
        ),
        Mapping(
            key="The `x2` property updates or gets the instance's second vertex x-coordinate:",
            val="`x2`属性では2つ目の頂点のX座標の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## y2 property interface example",
            val="## y2属性のインターフェイス例",
        ),
        Mapping(
            key="The `y2` property updates or gets the instance's second vertex y-coordinate:",
            val="`y2`属性では2つ目の頂点のY座標の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## x3 property interface example",
            val="## x3属性のインターフェイス例",
        ),
        Mapping(
            key="The `x3` property updates or gets the instance's third vertex x-coordinate:",
            val="`x3`属性では3つ目のX座標の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## y3 property interface example",
            val="## y3属性のインターフェイス例",
        ),
        Mapping(
            key="The `y3` property updates or gets the instance's third vertex y-coordinate:",
            val="`y3`属性では3つ目のY座標の更新もしくは取得を行えます:",
        ),
        Mapping(
            key="## Triangle class constructor API",
            val="## Triangle クラスのコンストラクタのAPI",
        ),
        Mapping(
            key="Create a triangle vector graphics instance.<hr>",
            val="三角形のベクターグラフィックスのインスタンスを生成します。<hr>",
        ),
        Mapping(
            key="  - First vertex's x coordinate.",
            val="  - 1つ目の頂点のX座標。",
        ),
        Mapping(
            key="  - First vertex's y coordinate.",
            val="  - 1つ目の頂点のY座標。",
        ),
        Mapping(
            key="  - Second vertex's x coordinate.",
            val="  - 2つ目の頂点のX座標。",
        ),
        Mapping(
            key="  - Second vertex's y coordinate.",
            val="  - 2つ目の頂点のY座標。",
        ),
        Mapping(
            key="  - Third vertex's x coordinate.",
            val="  - 3つ目の頂点のX座標。",
        ),
        Mapping(
            key="  - Third vertex's y coordinate.",
            val="  - 3つ目の頂点のY座標。",
        ),
        Mapping(
            key="## x1 property API",
            val="## x1 属性のAPI",
        ),
        Mapping(
            key="Get a first x-coordinate.<hr>",
            val="1つ目のX座標を取得します。<hr>",
        ),
        Mapping(
            key="  - A first x-coordinate.",
            val="  - 1つ目のX座標。",
        ),
        Mapping(
            key="## y1 property API",
            val="## y1 属性のAPI",
        ),
        Mapping(
            key="Get a first y-coordinate.<hr>",
            val="1つ目のY座標を取得します。<hr>",
        ),
        Mapping(
            key="  - A first y-coordinate.",
            val="  - 1つ目のY座標。",
        ),
        Mapping(
            key="## x2 property API",
            val="## x2 属性のAPI",
        ),
        Mapping(
            key="Get a second x-coordinate.<hr>",
            val="Get a second x-coordinate.<hr>",
        ),
        Mapping(
            key="  - A second x-coordinate.",
            val="  - 2つ目のX座標。",
        ),
        Mapping(
            key="## y2 property API",
            val="## y2 属性のAPI",
        ),
        Mapping(
            key="Get a second y-coordinate.<hr>",
            val="2つ目のY座標を取得します。<hr>",
        ),
        Mapping(
            key="  - A second y-coordinate.",
            val="  - 2つ目のY座標。",
        ),
        Mapping(
            key="## x3 property API",
            val="## x3 属性のAPI",
        ),
        Mapping(
            key="Get a third x-coordinate.<hr>",
            val="3つ目のX座標を取得します。<hr>",
        ),
        Mapping(
            key="  - A third x-coordinate.",
            val="  - 3つ目のX座標。",
        ),
        Mapping(
            key="## y3 property API",
            val="## y3 属性のAPI",
        ),
        Mapping(
            key="Get a third y-coordinate.<hr>",
            val="3つ目のY座標を取得します。<hr>",
        ),
        Mapping(
            key="  - A third y-coordinate.",
            val="  - 3つ目のY座標。",
        ),
        Mapping(
            key="## Math.min API",
            val="## Math.min のAPI",
        ),
        Mapping(
            key="Get a minimum number from a specified array's values.<hr>",
            val="指定された配列の各値の中から最小値の数値を取得します。<hr>",
        ),
        Mapping(
            key="  - An array of numbers.",
            val="  - 数値を格納した配列。",
        ),
        Mapping(
            key="  - Minimum number in an array.",
            val="  - 配列の中で最小の数値。",
        ),
        Mapping(
            key="## Mathematics",
            val="## 数学",
        ),
        Mapping(
            key="Notes: Regardless of the `Array` values' type, this interface returns a `Number` type value.",
            val="特記事項: `Array`内の各値の型に関わらず、このインターフェイスは`Number`型の値を返却します。",
        ),
        Mapping(
            key="## Math.max API",
            val="## Math.max のAPI",
        ),
        Mapping(
            key="Get a maximum number from a specified array's values.<hr>",
            val="指定された配列の値の中から最大値の数値を取得します。<hr>",
        ),
        Mapping(
            key="  - Maximum number in an array.",
            val="  - 配列の中の数値の最大値。",
        ),
        Mapping(
            key="## Math.trunc API",
            val="## Math.trunc のAPI",
        ),
        Mapping(
            key="Truncate a fraction value from a specified value.<hr>",
            val="指定された値から小数点以下の値を切り落とします。<hr>",
        ),
        Mapping(
            key="  - A value to truncate a fraction value. If a specified value is the `Number`'s, `String`'s, or `Boolean`'s type, the return value becomes an `Int`'s value.",
            val="  - 小数点以下を切り捨てる対象の値。もし指定された値が`Number`、`String`、もしくは`Boolean`型の値の場合、変逆値は`Int`型の値となります。",
        ),
        Mapping(
            key="  - Truncated and converted to `Int`'s value.",
            val="  - 切り捨て処理と`Int`型への変換が反映された値。",
        ),
        Mapping(
            key="## Delete setting",
            val="## 設定の削除",
        ),
        Mapping(
            key="In the following example, if you click the rectangle, the handler deletes the line setting:",
            val="以下の例では四角をクリックするとハンドラ内の処理で線の設定を削除しています:",
        ),
        Mapping(
            key="## delete_line_dot_setting API",
            val="## delete_line_dot_setting のAPI",
        ),
        Mapping(
            key="Delete a current line dot setting.",
            val="現在の点線の設定を削除します。",
        ),
        Mapping(
            key="## delete_line_dash_setting API",
            val="## delete_line_dash_setting のAPI",
        ),
        Mapping(
            key="Delete a current line dash setting.",
            val="現在の破線の設定を削除します。",
        ),
        Mapping(
            key="## delete_line_round_dot_setting API",
            val="## delete_line_round_dot_setting のAPI",
        ),
        Mapping(
            key="Delete a current line-round dot setting.",
            val="現在の線の丸ドット設定を削除します。",
        ),
        Mapping(
            key="## delete_line_dash_dot_setting API",
            val="## delete_line_dash_dot_setting のAPI",
        ),
        Mapping(
            key="Delete a current line dash-dot (1-dot chain) setting.",
            val="現在の線の一点鎖線の設定を削除します。",
        ),
        Mapping(
            key="## draw_triangle API",
            val="## draw_triangle のAPI",
        ),
        Mapping(
            key="Draw a triangle vector graphic.<hr>",
            val="三角形のベクターグラフィックスを描画します。<hr>",
        ),
        Mapping(
            key="  - Created triangle graphics instance.",
            val="  - 生成された三角形のグラフィックスのインスタンス。",
        ),
        Mapping(
            key="Graphics draw_triangle interface",
            val="Graphics クラスの draw_triangle インターフェイス",
        ),
        Mapping(
            key="Triangle class",
            val="Triangle クラス",
        ),
        Mapping(
            key="## get_stage API",
            val="## get_stage のAPI",
        ),
        Mapping(
            key="Get an already instantiated stage instance.<hr>",
            val="既に生成済みのステージのインスタンスを取得します。<hr>",
        ),
        Mapping(
            key="  - Target stage instance.",
            val="  - 対象のステージのインスタンス。",
        ),
        Mapping(
            key="- _StageNotCreatedError: If there is no instantiated stage yet.",
            val="- _StageNotCreatedError: もしもまだ生成済みのステージのインスタンスが存在しない場合。",
        ),
        Mapping(
            key="## unbind_custom_event API",
            val="## unbind_custom_event のAPI",
        ),
        Mapping(
            key="Unbind (remove) a custom event listener setting.<hr>",
            val="単体のカスタムイベントのリスナー設定を解除します。<hr>",
        ),
        Mapping(
            key="  - A handler for when the custom event is triggered.",
            val="  - カスタムイベントが発火された際に呼ばれるハンドラ。",
        ),
        Mapping(
            key="## unbind_custom_event_all API",
            val="## unbind_custom_event_all のAPI",
        ),
        Mapping(
            key="Unbind (remove) custom event listener settings.<hr>",
            val="カスタムイベントのリスナー設定を一通り解除します。<hr>",
        ),
    ]
)
