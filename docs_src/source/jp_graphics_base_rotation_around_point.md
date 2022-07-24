<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html)の確認をお願いします。</span>

# GraphicsBase クラスの rotation_around_point インターフェイス

このページでは`GraphicsBase`クラス（`Rectangle`などの各グラフィックスクラスの基底クラス）の`get_rotation_around_point`と`set_rotation_around_point`の各メソッドのインターフェイスについて説明します。

## 各インターフェイスの概要

`get_rotation_around_point`メソッドは指定された座標基準の回転量を取得し、`set_rotation_around_point`メソッドは指定された座標を基準とした回転量を更新します。

これらの回転量は相対値であり、各回転量は座標ごとに異なる値が保持されます。例えばx=50, y=50の座標とx=100, y=100の座標の回転量の値はそれぞれ別の値になります。

## 基本的な使い方

`get_rotation_around_point`メソッドは`x`と`y`の引数の指定を必要とし、指定された座標での回転量を返却します。`set_rotation_around_point`メソッドは`x`と`y`、そして`rotation`の引数の指定を必要とします。全ての引数と返却値は`Int`型になります。

以下の例では二つの四角を作成し、各四角をタイマーのハンドラ内で回転させています。1つ目の四角は左上の座標（`x=50, y=50`）で回転させていて、2つ目の四角は右下の座標（`x=100, y=100`）で回転させています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectanglesOptions(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle


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
    x: ap.Int = ap.Int(50)
    y: ap.Int = ap.Int(50)
    rectangle_1: ap.Rectangle = options["rectangle_1"]
    rotation: ap.Int = rectangle_1.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_1.set_rotation_around_point(rotation=rotation, x=x, y=y)

    rectangle_2: ap.Rectangle = options["rectangle_2"]
    x = ap.Int(100)
    y = ap.Int(100)
    rotation = rectangle_2.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_2.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af", alpha=0.5)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

options: _RectanglesOptions = {"rectangle_1": rectangle_1, "rectangle_2": rectangle_2}
timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="graphics_base_rotation_around_point_basic_usage/")
```

<iframe src="static/graphics_base_rotation_around_point_basic_usage/index.html" width="150" height="150"></iframe>

## get_rotation_around_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_rotation_around_point(self, *, x: apysc._type.int.Int, y: apysc._type.int.Int) -> apysc._type.int.Int`<hr>

**[インターフェイス概要]** Get a rotation value around the given coordinates.<hr>

**[引数]**

- `x`: Int
  - X座標。

- `y`: Int
  - Y座標。

<hr>

**[返却値]**

- `rotation`: Int
  - 指定された座標基準による回転量。

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
>>> x: ap.Int = ap.Int(100)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_rotation_around_point(rotation=ap.Int(45), x=x, y=y)
>>> rectangle.get_rotation_around_point(x=x, y=y)
Int(45)
```

## set_rotation_around_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `set_rotation_around_point(self, *, rotation: apysc._type.int.Int, x: apysc._type.int.Int, y: apysc._type.int.Int) -> None`<hr>

**[インターフェイス概要]** 指定された座標基準の回転量を更新します。<hr>

**[引数]**

- `rotation`: Int
  - 設定する回転量。

- `x`: Int
  - X座標。

- `y`: Int
  - Y座標。