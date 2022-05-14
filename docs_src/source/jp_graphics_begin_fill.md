<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_begin_fill.html)の確認をお願いします。</span>

# Graphics クラスの begin_fill インターフェイス

このページでは`Graphics`クラスの`begin_fill`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`begin_fill`インターフェイスは塗りの色と塗りの透明度を設定します。この設定は再度`begin_fill`のインターフェイスを呼び出すか、もしくは`clear`メソッドを呼ぶまで保持されます。

## 基本的な使い方

ベクターグラフィックスの描画系の各インターフェイス（例 : `draw_rect`など）はグラフィックス生成時にこの塗りの設定を参照します。そのため描画系のインターフェイスを実行する前にこの`begin_fill`のインターフェイスを呼び出しておく必要があります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set blue fill color and draw the first rectangle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Draw the second rectangle (fill color setting will be maintained).
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

# Set the other fill color and draw the third rectangle.
sprite.graphics.begin_fill(color='#f0a')
sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_basic_usage/')
```

<iframe src="static/graphics_begin_fill_basic_usage/index.html" width="350" height="150"></iframe>

## 塗りの色の設定

`color`引数は塗りの色を設定します。`begin_fill`インターフェイスではこの引数は必須になっています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set a cyan fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_fill_color/')
```

<iframe src="static/graphics_begin_fill_fill_color/index.html" width="150" height="150"></iframe>

もしも塗りの色の設定を削除したい場合、空の文字列をこの引数に指定してください。

以下のコード例では塗りの色の設定を削除しているため、四角のグラフィックは見えなくなります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')

# Clear fill color by specifying blank string.
sprite.graphics.begin_fill(color='')

# Since fill color is not set, the rectangle is invisible.
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_color_setting_clear/')
```

<iframe src="static/graphics_begin_fill_color_setting_clear/index.html" width="150" height="150"></iframe>

カラーコードは以下の形の指定を受け付けています。

- `#00aaff`などの6文字による指定。
- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。

- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。
- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。

- ``などの空文字（この指定は塗りの色の設定を削除します）。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=450,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Six characters fill color setting (a cyan color).
sprite.graphics.begin_fill(color='#00aaff')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Three characters fill color setting (a magenta color).
sprite.graphics.begin_fill(color='#f0a')
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

# Single characters fill color setting (a black color).
sprite.graphics.begin_fill(color='#0')
sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)

# Fill color that Skipped `#` symbol is also acceptable.
sprite.graphics.begin_fill(color='999')
sprite.graphics.draw_rect(
    x=350, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_acceptable_color_settings/')
```

<iframe src="static/graphics_begin_fill_acceptable_color_settings/index.html" width="450" height="150"></iframe>

## 塗りの色の透明度の設定

塗りの透明度は`alpha`引数で設定できます。0.0（透明）～1.0（不透明）の範囲の値を受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#00aaff', alpha=0.2)
sprite.graphics.draw_rect(
    x=50, y=75, width=50, height=50)
sprite.graphics.draw_rect(
    x=75, y=50, width=50, height=50)
sprite.graphics.draw_rect(
    x=75, y=75, width=50, height=50)
sprite.graphics.draw_rect(
    x=75, y=100, width=50, height=50)
sprite.graphics.draw_rect(
    x=100, y=75, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_alpha_setting/')
```

<iframe src="static/graphics_begin_fill_alpha_setting/index.html" width="200" height="200"></iframe>

## begin_fill API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `begin_fill(self, *, color: ~StrOrString, alpha: Union[float, apysc._type.number.Number] = 1.0) -> None`<hr>

**[インターフェイス概要]** 塗りのための単一の色の設定を行います。<hr>

**[引数]**

- `color`: str or String
  - '#00aaff'などの16進数の色の文字列。

- `alpha`: float or Number, default 1.0
  - 塗りの透明度（0.0～1.0）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color
String('#00aaff')
```

## fill_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の塗りの色を取得します。<hr>

**[返却値]**

- `fill_color`: String
  - 現在の塗りの色（`'#00aaff'`などの16進数の文字列）。もしも設定されていない場合空文字が返却されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color
String('#00aaff')
```

## fill_alpha 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の塗りの透明度を取得します。<hr>

**[返却値]**

- `fill_alpha`: Number
  - 現在の塗りの透明度（0.0～1.0）。もし設定されていない場合1.0の値が返却されます。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_alpha
Number(0.5)
```