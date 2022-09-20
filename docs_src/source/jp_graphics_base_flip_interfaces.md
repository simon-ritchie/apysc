<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_flip_interfaces.html)の確認をお願いします。</span>

# GraphicsBase クラスの flip_x と flip_y インターフェイス

このページでは`GraphicsBase`クラス（`Rectangle`などの各グラフィッククラスの基底クラス）の`flip_x`と`flip_y`属性のインターフェイスについて説明します。

## 各インターフェイスの概要

`flip_x`属性はオブジェクトを横方向に反転し、`flip_y`属性はオブジェクトを縦方向に反転します。

## 基本的な使い方

`flip_x`と`flip_y`には`Boolean`型の値を設定できます。もし`True`を指定すれば反転した状態になり、`False`を設定すれ反転がリセットされます。

getterのインターフェイスでは現在の反転設定の`Boolean`型の値を返却します。

以下のコード例では1秒ごとに三角形の反転とリセットを行っています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _PolygonOptions(TypedDict):
    polygon: ap.Polygon


def on_timer(e: ap.TimerEvent, options: _PolygonOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    polygon: ap.Polygon = options["polygon"]
    flip_x: ap.Boolean = polygon.flip_x
    flip_x = flip_x.not_
    polygon.flip_x = flip_x


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

polygon: ap.Polygon = sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=75),
    ]
)
options: _PolygonOptions = {"polygon": polygon}
timer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="graphics_base_flip_x_basic_usage/")
```

<iframe src="static/graphics_base_flip_x_basic_usage/index.html" width="150" height="150"></iframe>

`flip_y`インターフェイスは軸の方向の違いを除いて`flip_x`の員スターフェイスと同様に動作します。

## flip_x 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

横軸に対して反転しているかどうかの真偽値を取得します。<hr>

**[返却値]**

- `flip_x`: Boolean
  - 横方向に反転しているかどうかのBooleanの真偽値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ]
... )
>>> polygon.flip_x = ap.Boolean(True)
>>> polygon.flip_x
Boolean(True)
```

## flip_y 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

縦軸に対して反転しているかどうかの真偽値を取得します。<hr>

**[返却値]**

- `flip_y`: Boolean
  - 縦方向に反転しているかどうかのBooleanの真偽値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=50, y=0),
...         ap.Point2D(x=25, y=50),
...     ]
... )
>>> polygon.flip_y = ap.Boolean(True)
>>> polygon.flip_y
Boolean(True)
```