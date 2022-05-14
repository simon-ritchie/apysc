<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html)の確認をお願いします。</span>

# GraphicsBase クラスの get_scale_from_point と set_scale_from_point のインターフェイス

このページでは`GraphicsBase`クラス（`Rectangle`などのグラフィッククラスの基底クラス）の`get_scale_x_from_point`、`get_scale_y_from_point`、`set_scale_x_from_point`、`set_scale_y_from_point`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`set_scale_x_from_point`メソッドは指定された座標を基準にオブジェクトの水平方向の拡縮を変更します。同様に`set_scale_y_from_point`メソッドは指定された座標を基準にオブジェクトの垂直方向の拡縮を変更します。

`scale_x_from_center`や`scale_y_from_center`のインターフェイスは属性になっていますが、`set_scale_x_from_point`や`set_scale_y_from_point`のインターフェイスは座標の指定が必要なためメソッドのインターフェイスになっています。

同様に`get_scale_x_from_point`と`get_scale_y_from_point`のメソッドは指定された座標における拡縮値を返却します。これらのインターフェイスも引数に座標の指定が必要になります。

返却値は各座標ごとに設定されます。例えば水平方向の拡縮を50pxのX座標の位置で設定した場合、100pxのX座標の位置における拡縮値には影響しません。

## 基本的な使い方

`get_scale_x_from_point`メソッドは`Int`型の`x`引数の指定を必要とし、`set_scale_x_from_point`メソッドは`Number`型の`scale_x`と`x`の各引く数の指定が必要になります。

以下のコード例では3つの四角を生成し水平方向の拡縮を増減させています。上の四角は左端を基準に拡縮を、真ん中の四角は中央を基準に拡縮を、そして下の四角では右右端を基準に拡縮を行っています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _Options(TypedDict):
    rectangle: ap.Rectangle
    x: ap.Int
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _Options) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    x: ap.Int = options['x']
    direction: ap.Int = options['direction']
    current_scale_x: ap.Number = rectangle.get_scale_x_from_point(x=x)
    current_scale_x += direction * 0.03
    rectangle.set_scale_x_from_point(scale_x=current_scale_x, x=x)
    with ap.If(current_scale_x >= 2.0):
        direction *= -1
    with ap.If(current_scale_x <= 0.0):
        direction *= -1


ap.Stage(
    stage_width=150, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

top_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
middle_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50)
bottom_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50)

top_rect_direction: ap.Int = ap.Int(1)
options: _Options = {
    'rectangle': top_rect, 'x': ap.Int(50),
    'direction': top_rect_direction}
top_rect_timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60,
    options=options)
top_rect_timer.start()

middle_rect_direction: ap.Int = ap.Int(1)
options = {
    'rectangle': middle_rect, 'x': ap.Int(75),
    'direction': middle_rect_direction}
middle_rect_timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60,
    options=options)
middle_rect_timer.start()

bottom_rect_direction: ap.Int = ap.Int(1)
options = {
    'rectangle': bottom_rect, 'x': ap.Int(100),
    'direction': bottom_rect_direction}
bottom_rect_timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60,
    options=options)
bottom_rect_timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_scale_from_point_basic_usage_x/')
```

<iframe src="static/graphics_base_scale_from_point_basic_usage_x/index.html" width="150" height="350"></iframe>

似たような形で`get_scale_y_from_point`と`set_scale_y_from_point`のメソッドは`scale_y`と`y`の引数を必要とします。これらは拡縮の方向が垂直方向になっている以外は水平方向のインターフェイスと同じように動作します。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _Options(TypedDict):
    rectangle: ap.Rectangle
    y: ap.Int
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _Options) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    y: ap.Int = options['y']
    direction: ap.Int = options['direction']
    current_scale_y: ap.Number = rectangle.get_scale_y_from_point(y=y)
    current_scale_y += direction * 0.03
    rectangle.set_scale_y_from_point(scale_y=current_scale_y, y=y)
    with ap.If(current_scale_y >= 2.0):
        direction *= -1
    with ap.If(current_scale_y <= 0.0):
        direction *= -1


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
direction: ap.Int = ap.Int(1)
options: _Options = {
    'rectangle': rectangle, 'y': ap.Int(50), 'direction': direction}
timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60,
    options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_scale_from_point_basic_usage_y/')
```

<iframe src="static/graphics_base_scale_from_point_basic_usage_y/index.html" width="150" height="150"></iframe>

## get_scale_x_from_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_scale_x_from_point(self, *, x: apysc._type.int.Int) -> apysc._type.number.Number`<hr>

**[インターフェイス概要]** 指定されたX座標を基準として水平方向の拡縮の値を取得します。<hr>

**[引数]**

- `x`: Int
  - X座標。

<hr>

**[返却値]**

- `scale_x`: Number
  - 指定されたX座標を基準とした水平方向の拡縮値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

## set_scale_x_from_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `set_scale_x_from_point(self, *, scale_x: apysc._type.number.Number, x: apysc._type.int.Int) -> None`<hr>

**[インターフェイス概要]** 指定されたX座病を基準とした水平方向の拡縮値を更新します。<hr>

**[引数]**

- `scale_x`: Number
  - 設定する水平方向の拡縮値。

- `x`: Int
  - X座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

## get_scale_y_from_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_scale_y_from_point(self, *, y: apysc._type.int.Int) -> apysc._type.number.Number`<hr>

**[インターフェイス概要]** 指定されたY座標を基準とした垂直方向の拡縮の値を取得します。<hr>

**[引数]**

- `y`: Int
  - Y座標。

<hr>

**[返却値]**

- `scale_y`: ap.Number
  - 指定されたY座標を基準とした垂直方向の拡縮値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```

## set_scale_y_from_point API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `set_scale_y_from_point(self, *, scale_y: apysc._type.number.Number, y: apysc._type.int.Int) -> None`<hr>

**[インターフェイス概要]** 指定されたY座標を基準とした垂直方向の拡縮値を更新します。<hr>

**[引数]**

- `scale_y`: Number
  - 設定すの垂直方向の拡縮値。

- `y`: Int
  - Y座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```