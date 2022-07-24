<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_skew.html)の確認をお願いします。</span>

# GraphicsBase クラスの skew_x と skew_y インターフェイス

このページでは`GraphicsBase`クラス（`Rectangle`などのグラフィッククラスの基底クラス）の`skew_x`と`skew_y`属性のインターフェイスについて説明します。

## 各インターフェイスの概要

`skew_x`属性はオブジェクトをX軸方向に歪ませます。逆に`skew_y`属性ではY軸方向にオブジェクトを歪ませます。これらのインターフェイスはgetterとsetterの各インターフェイスを持っています。

各インターフェイスの値の型は`Int`型の値となります。

以下のコード例では左側の四角はデフォルトの状態、右側の四角はX軸方向に50pxの歪みを設定しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50
)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50
)
right_rectangle.skew_x = ap.Int(50)

ap.save_overall_html(dest_dir_path="graphics_base_skew_x_basic_usage/")
```

<iframe src="static/graphics_base_skew_x_basic_usage/index.html" width="250" height="150"></iframe>

以下の例ではY軸方向に四角の歪みを加算していく形で設定しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.skew_y += 1


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _RectOptions = {"rectangle": rectangle}
timer: ap.Timer = ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="graphics_base_skew_y_incremental_basic_usage/")
```

<iframe src="static/graphics_base_skew_y_incremental_basic_usage/index.html" width="150" height="150"></iframe>

## skew_x property API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** インスタンスの現在のX軸の歪みの値を取得します。<hr>

**[返却値]**

- `skew_x`: Int
  - インスタンスの現在のX軸の歪みの値。

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
>>> rectangle.skew_x = ap.Int(50)
>>> rectangle.skew_x
Int(50)
```

## skew_y property API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** インスタンスの現在のY軸の歪みの値を取得します。<hr>

**[返却値]**

- `skew_y`: Int
  - インスタンスの現在のY軸の歪みの値。

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
>>> rectangle.skew_y = ap.Int(50)
>>> rectangle.skew_y
Int(50)
```