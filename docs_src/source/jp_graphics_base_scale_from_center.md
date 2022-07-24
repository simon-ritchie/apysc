<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_center.html)の確認をお願いします。</span>

# GraphicsBase クラスの scale_x_from_center と scale_y_from_center インターフェイス

このページでは`GraphicsBase`クラス（`Rectangle`などの各グラフィッククラスの基底クラス）の`scale_x_from_center`と`scale_y_from_center`属性のインターフェイスについて説明します。

## 各インターフェイスの概要

`scale_x_from_center`属性はオブジェクトの水平方向の拡縮を変更し、`scale_y_from_center`属性は垂直方向の拡縮を変更します。これらの拡縮のインターフェイスはオブジェクトの中央座標を基準に実行されます。

## 基本的な使い方

各属性のgetterのインターフェイスは`Number`型の値を返却します。setterのインターフェイスでは拡縮の更新値として`Number`型の値の指定が必要になります（もしも0.0が指定されればオブジェクトは見えなくなり、1.0でデフォルトの拡縮、2.0で2倍のサイズになります）。

以下のコード例では左の四角ではデフォルトの拡縮値、真ん中の四角では水平方向に半分のサイズ、→の四角では垂直方向に半分のサイズを設定しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50
)
center_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50
)
center_rectangle.scale_x_from_center = ap.Number(0.5)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50
)
right_rectangle.scale_y_from_center = ap.Number(0.5)

ap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_1/")
```

<iframe src="static/graphics_base_scale_from_center_basic_usage_1/index.html" width="350" height="150"></iframe>

これらのインターフェイスでは以下の例のように中央座標を基準に拡縮が実行されます:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af", alpha=0.3)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2.scale_x_from_center = ap.Number(0.5)
rectangle_2.scale_y_from_center = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_3.scale_x_from_center = ap.Number(0.25)
rectangle_3.scale_y_from_center = ap.Number(0.25)

ap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_2/")
```

<iframe src="static/graphics_base_scale_from_center_basic_usage_2/index.html" width="150" height="150"></iframe>

`+=`や`-=`記号のオペレーターによる操作もサポートしています:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectanglesOptions(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options["rectangle_1"]
    rectangle_2: ap.Rectangle = options["rectangle_2"]
    direction: ap.Int = options["direction"]

    current_scale: ap.Number = rectangle_1.scale_x_from_center
    condition_1: ap.Boolean = current_scale >= 2.0
    condition_2: ap.Boolean = current_scale <= 0.05
    with ap.If(condition_1):
        direction.value = -1
    with ap.Elif(condition_2):
        direction.value = 1

    rectangle_1.scale_x_from_center += direction * 0.03
    rectangle_2.scale_y_from_center += direction * 0.03


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color="#0af", alpha=0.5)
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color="#f0a", alpha=0.5)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)


direction: ap.Int = ap.Int(1.0)
options: _RectanglesOptions = {
    "rectangle_1": rectangle_1,
    "rectangle_2": rectangle_2,
    "direction": direction,
}
timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="graphics_base_scale_from_center_basic_usage_3/")
```

<iframe src="static/graphics_base_scale_from_center_basic_usage_3/index.html" width="150" height="150"></iframe>

## scale_x_from_center 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** インスタンスの中央座標を基準とした水平方向の拡縮の値を取得します。<hr>

**[返却値]**

- `scale_x_from_center`: ap.Number
  - インスタンスの中央座標を基準とした水平方向の拡縮の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.scale_x_from_center = ap.Number(1.5)
>>> rectangle.scale_x_from_center
Number(1.5)
```

## scale_y_from_center 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** インスタンスの中央座標を基準とした垂直方向の拡縮の値を取得します。<hr>

**[返却値]**

- `scale_y_from_center`: ap.Number
  - インスタンスの中央座標を基準とした垂直方向の拡縮の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.scale_y_from_center = ap.Number(1.5)
>>> rectangle.scale_y_from_center
Number(1.5)
```