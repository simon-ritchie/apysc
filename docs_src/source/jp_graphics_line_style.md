<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)の確認をお願いします。</span>

# Graphics クラスの line_style インターフェイス

このページでは`Graphics`クラスの`line_style`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`line_style`インターフェイスは線の色や線の透明度、線幅、点線などの線の各スタイルの設定を行います。このインターフェイスは再度インターフェイスを実行したり`clear`メソッドなどを呼ぶまでスタイル設定を保持し続けます（`begin_fill`インターフェイスと同じような挙動をします）。

## 基本的な使い方

`draw_rect`や`line_to`などのベクターグラフィックスの描画系の各インターフェイスはこのインターフェイスのスタイル設定を各グラフィックスインスタンス作成時に参照します。従って線の設定が必要な場合には各描画系のインターフェイスを呼ぶ前にこのインターフェイスで設定を行っておく必要があります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=162, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Draw a white line with 3px line thickness.
sprite.graphics.line_style(color="#ccc", thickness=8)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=150, y=50)

# Line style setting will be maintained.
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=150, y=80)

# Change line color and thickness.
sprite.graphics.line_style(color="#0af", thickness=3)
sprite.graphics.move_to(x=50, y=110)
sprite.graphics.line_to(x=150, y=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_basics/")
```

<iframe src="static/graphics_line_style_basics/index.html" width="200" height="162"></iframe>

## 線の色の設定

指定が必須な`color`引数は線の色を設定します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=102, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set a cyan line color and draw the line.
sprite.graphics.line_style(color="#0af", thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_color/")
```

<iframe src="static/graphics_line_style_line_color/index.html" width="200" height="102"></iframe>

もしも線の色設定を削除したい場合にはこの引数に空文字を指定してください。

例えば以下のコード例では線の色設定を削除しているので線は見えなくなっています。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=102, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set a cyan line color.
sprite.graphics.line_style(color="#0af", thickness=4)

# Clear the line color by specifying a blank string.
sprite.graphics.line_style(color="", thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_line_style_clear_line_color/")
```

<iframe src="static/graphics_line_style_clear_line_color/index.html" width="200" height="102"></iframe>

以下のリストようなのカラーコードの文字列を指定することができます（`begin_fill`インターフェイスの`color`引数と同じ挙動になります）。

- `#00aaff`などの6文字による指定。
- `#0af`などの3文字による指定（これは`#00aaff`と同じ値として扱われます）。

- `#5`などの1文字による指定（これは`000005`と同じ値として扱われます）。
- `0af`などの`#`記号を省略した指定（これは`#00aaff`と同じ値として扱われます）。

- `''`などの空文字の指定（これは線の色の削除指定として扱われます）。`

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=162, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# The six characters line color setting (a cyan color).
sprite.graphics.line_style(color="#00aaff", thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# The three characters line color setting (a magenta color).
sprite.graphics.line_style(color="#f0a", thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)

# The one character line color setting (a black color).
sprite.graphics.line_style(color="#5", thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_color_color_code/")
```

<iframe src="static/graphics_line_style_line_color_color_code/index.html" width="200" height="162"></iframe>

## 線幅の設定

`thickness`引数は線の幅を設定します。1以上の値を受け付けることができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=165, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set 1-pixel line thickness.
sprite.graphics.line_style(color="#0af", thickness=1)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# Set 4-pixel line thickness.
sprite.graphics.line_style(color="#0af", thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)

# Set 10-pixel line thickness.
sprite.graphics.line_style(color="#0af", thickness=10)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_thickness/")
```

<iframe src="static/graphics_line_style_thickness/index.html" width="200" height="165"></iframe>

## 線の透明度の設定

`alpha`引数で線の透明度を設定することができます。0.0（透明）～1.0（不透明）の範囲の値を受け付けることができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Draw the cyan line from upper-left to lower-right.
sprite.graphics.line_style(color="#0af", thickness=15, alpha=0.3)
sprite.graphics.draw_line(x_start=50, x_end=100, y_start=50, y_end=100)

# Draw the magenta line from upper-right to lower-left.
sprite.graphics.line_style(color="#f0a", thickness=15, alpha=0.3)
sprite.graphics.draw_line(x_start=100, x_end=50, y_start=50, y_end=100)

ap.save_overall_html(dest_dir_path="graphics_line_style_alpha/")
```

<iframe src="static/graphics_line_style_alpha/index.html" width="150" height="150"></iframe>

## 線端の設定

線の端のスタイルは`cap`引数で設定することができます。`LineCaps`クラスのenumの値を受け付けます。

以下のように`LineCaps`のオプションは3種類存在します:

- BUTT: デフォルト値であり、端にはなにも設定されません。
- ROUND: 線の端のスタイルを丸くします。

- SQUARE: 線の端のスタイルを四角くします。これはBUTTと似た表示になりますが、設定される四角の分だけ線が長くなります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=180, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# BUTT caps setting (default).
sprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.BUTT)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# ROUND caps setting.
sprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.ROUND)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=90, y_end=90)

# SQUARE caps setting (same line length setting as BUTT line,
# but this will be longer for the caps).
sprite.graphics.line_style(color="#0af", thickness=20, cap=ap.LineCaps.SQUARE)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=130, y_end=130)

ap.save_overall_html(dest_dir_path="graphics_line_style_caps/")
```

<iframe src="static/graphics_line_style_caps/index.html" width="200" height="180"></iframe>

## 線の繋ぎ目の設定

`joints`引数では線の繋ぎ目（頂点部分）のスタイルを変更します。この引数には`LineJoints`のenumの各値を受け付けます。主に`move_to`や`line_to`などのインターフェイスで生成される`Polyline`クラスのインスタンスでこの引数は使用されます。

以下のようにLineJointsのenumには3つの値が存在します:

- MITER: この設定は頂点が（尖った形での）額縁のような形のスタイルが設定されます。この設定がデフォルトのスタイルとなります。
- ROUND: この設定は丸い頂点のスタイルを設定します。

- BEVEL: この設定は射角（ベベル）の頂点のスタイルを設定します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=350, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set MITER joints setting and draw the polyline.
sprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.MITER)
sprite.graphics.move_to(x=50, y=100)
sprite.graphics.line_to(x=75, y=50)
sprite.graphics.line_to(x=100, y=100)

# Set ROUND joints setting and draw the polyline.
sprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.ROUND)
sprite.graphics.move_to(x=150, y=100)
sprite.graphics.line_to(x=175, y=50)
sprite.graphics.line_to(x=200, y=100)

# Set BEVEL joints setting and draw the polyline.
sprite.graphics.line_style(color="#0af", thickness=10, joints=ap.LineJoints.BEVEL)
sprite.graphics.move_to(x=250, y=100)
sprite.graphics.line_to(x=275, y=50)
sprite.graphics.line_to(x=300, y=100)

ap.save_overall_html(dest_dir_path="graphics_line_style_joints/")
```

<iframe src="static/graphics_line_style_joints/index.html" width="350" height="150"></iframe>

## 線の点線設定

`dot_setting`引数は線を点線へと変更する設定です。この引数は`LineDotSetting`クラスの設定を受け付けます。点線のサイズは`dot_size`引数で変更することができます（1以上の値を受け付けます）。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=300, stage_height=160, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set the line dot settings with 2-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=2)
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set the line dot settings with 5-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

# Set the line dot settings with 10-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=10)
)
sprite.graphics.move_to(x=50, y=110)
sprite.graphics.line_to(x=250, y=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting/")
```

<iframe src="static/graphics_line_style_line_dot_setting/index.html" width="300" height="160"></iframe>

この設定や類似の設定は線のグラフィックスだけでなく`Rectangle`など他のグラフィックスクラスの表示も変更します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set the line dot setting with 2-pixel dot size and draw the rectangle.
# Fill color setting is skipped.
sprite.graphics.line_style(
    color="#0af", thickness=5, dot_setting=ap.LineDotSetting(dot_size=2)
)
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Draw the rectangle with the dotted line setting and the fill color.
sprite.graphics.begin_fill(color="#038")
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting_rectangle/")
```

<iframe src="static/graphics_line_style_line_dot_setting_rectangle/index.html" width="250" height="150"></iframe>

特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。

## 線の破線設定

`dash_setting`引数は線の破線のスタイル設定を変更します。ごの引数は`LineDashSetting`クラスの設定を受け付けます。この設定では破線のサイズを`dash_size`引数で、空白のスペースのサイズを`space_size`引数で変更することができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set 10-pixel dash size and 3-pixel space size and draw the line.
sprite.graphics.line_style(
    color="#0af",
    thickness=3,
    dash_setting=ap.LineDashSetting(dash_size=10, space_size=3),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 15-pixel dash size and 5-pixel space size and draw the line.
sprite.graphics.line_style(
    color="#0af",
    thickness=3,
    dash_setting=ap.LineDashSetting(dash_size=15, space_size=5),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_setting/")
```

<iframe src="static/graphics_line_style_line_dash_setting/index.html" width="300" height="130"></iframe>

特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。

## 線の丸ドット設定

`round_dot_setting`引数は線の丸ドットのスタイルを設定します。この引数は`LineRoundDotSetting`クラスの値を受け付けます。この設定では円のサイズを`round_size`、円の間のスペースのサイズを`space_size`引数で変更することができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(
    color="#0af",
    thickness=5,
    round_dot_setting=ap.LineRoundDotSetting(round_size=5, space_size=5),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 10-pixel round size and draw the line.
sprite.graphics.line_style(
    color="#0af",
    thickness=5,
    round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_round_dot_setting/")
```

<iframe src="static/graphics_line_style_line_round_dot_setting/index.html" width="300" height="130"></iframe>

特記事項: この設定は内部で`cap`設定の値を使用しているため、この設定では`cap`引数の設定が無視されます。また、丸のサイズに応じた分だけ線の長さが長くなります。

特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。

## 線の一点鎖線の設定

`dash_dot_setting`引数は線に一点鎖線のスタイルを設定します。この引数は`LineDashDotSetting`クラスのインスタンスを受け付けます。この設定は短い点線のサイズを`dot_size`、長い破線のサイズを`dash_size`、そして空白のスペースのサイズを`space_size`引数で設定できます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=300, stage_height=130, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# Set 3-pixel dot size and 10-pixel dash size and draw the line.
sprite.graphics.line_style(
    color="#0af",
    thickness=3,
    dash_dot_setting=ap.LineDashDotSetting(dot_size=3, dash_size=10, space_size=3),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 5-pixel dot size and 15-pixel dash size and draw the line.
sprite.graphics.line_style(
    color="#0af",
    thickness=3,
    dash_dot_setting=ap.LineDashDotSetting(dot_size=5, dash_size=15, space_size=3),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_dot_setting/")
```

<iframe src="static/graphics_line_style_line_dash_dot_setting/index.html" width="300" height="130"></iframe>

特記事項: この設定は`draw_line`、`draw_dotted_line`、`draw_dashed_line`、`draw_round_dotted_line`、`draw_dash_dotted_line`の各インターフェイスで無視されます。

## line_style API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `line_style(self, *, color: ~StrOrString, thickness: Union[int, apysc._type.int.Int] = 1, alpha: Union[float, apysc._type.number.Number] = 1.0, cap: Union[apysc._display.line_caps.LineCaps, NoneType] = None, joints: Union[apysc._display.line_joints.LineJoints, NoneType] = None, dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None) -> None`<hr>

**[インターフェイス概要]**

線のスタイルを設定します。<hr>

**[引数]**

- `color`: String or str
  - '#00aaff'などの16進数の色の文字列。

- `thickness`: Int or int, default 1
  - 線の幅（1以上の値を受け付けます）。

- `alpha`: float or Number, default 1.0
  - 線色の透明度（0.0～1.0）。

- `cap`: LineCaps or None, default None
  - 線の端のスタイル設定。線に関係しないRectangleクラスなどのグラフィックスインスタンスはこの設定を無視します。逆にPolylineクラスなどの線に関係したインスタンスではこの設定を使用します。

- `joints`: LineJoints or None, default None
  - 線の頂点（接合部）のスタイル設定。折れ線線に関係しないRectangleなどのグラフィックスインスタンスはこの設定を無視します。逆にPolylineクラスなどの折れ線関係のクラスではこの設定を使用します。

- `dot_setting`: LineDotSetting or None, default None
  - 点線の設定。もしもこの引数が指定された場合、線は点線になります。

- `dash_setting`: LineDashSetting or None, default None
  - 破線の設定。もしこの引数が指定された場合、線は破線になります。

- `round_dot_setting`: LineRoundDotSetting or None, default None
  - 丸ドットの設定。もしこの引数が指定された場合、線は丸ドットになります。特記事項: ごの設定は内部でcapの設定を使用しているため、cap（線の端のスタイル設定）と線幅の設定を上書きします。また、cap設定を使用している都合、線の長さも長くなります。move_toやline_toなどのインターフェイスを使った通常の線の長さと合わせたい場合には丸の半分のサイズを線の開始位置のX座標へ加算し、さらに丸の半分のサイズを線の終了位置のX座標から減算してください（Y座標も同様です）。例: `this.move_to(x + round_size / 2, y)`、`this.line_to(x - round_size / 2, y)`
- `dash_dot_setting`: LineDashDotSetting or None, default None

  - 一点鎖線のスタイル設定。もしこの引数が指定された場合、線の一点鎖線になります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)

>>> line.line_alpha
Number(0.5)

>>> line.line_cap
String('round')
```

## line_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の色を取得します。<hr>

**[返却値]**

- `line_color`: String
  - '#00aaff'などの16進数の線の色。もし設定されていない場合はこの空文字となります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> sprite.graphics.line_color
String('#ffffff')
```

## line_thickness 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の線幅を取得します。<hr>

**[返却値]**

- `line_thickness`: Int
  - 現在の線幅。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)
>>> sprite.graphics.line_thickness
Int(5)
```

## line_alpha 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の透明度を取得します。<hr>

**[返却値]**

- `line_alpha`: Number
  - 現在の線の透明度（0.0～1.0）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> sprite.graphics.line_alpha
Number(0.5)
```

## line_cap 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の端のスタイル設定。<hr>

**[返却値]**

- `line_cap`: String
  - 現在の線の端のスタイル設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> sprite.graphics.line_cap
String('round')
```

## line_joints 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の接合部（頂点）のスタイル設定を取得します。<hr>

**[返却値]**

- `line_joints`: String
  - 現在の線の接合部（頂点）のスタイル設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff", thickness=5, joints=ap.LineJoints.ROUND
... )
>>> sprite.graphics.line_joints
String('round')
```

## line_dot_setting 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の点線設定を取得します。<hr>

**[返却値]**

- `line_dot_setting`: LineDotSetting or None
  - 現在の点線設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)
... )
>>> sprite.graphics.line_dot_setting.dot_size
Int(5)
```

## line_dash_setting 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の破線のスタイル設定を取得します。<hr>

**[返却値]**

- `line_dash_setting`: LineDashSetting or None
  - 現在の破線設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff",
...     thickness=5,
...     dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
... )
>>> sprite.graphics.line_dash_setting.dash_size
Int(10)

>>> sprite.graphics.line_dash_setting.space_size
Int(5)
```

## line_round_dot_setting 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の丸ドットのスタイル設定を取得します。<hr>

**[返却値]**

- `line_round_dot_setting`: LineRoundDotSetting or None
  - 現在の線の丸ドットのスタイル設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff",
...     thickness=5,
...     round_dot_setting=ap.LineRoundDotSetting(round_size=6, space_size=3),
... )
>>> sprite.graphics.line_round_dot_setting.round_size
Int(6)

>>> sprite.graphics.line_round_dot_setting.space_size
Int(3)
```

## line_dash_dot_setting 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

現在の線の一点鎖線のスタイル設定を取得します。<hr>

**[返却値]**

- `line_dash_dot_setting`: LineDashDotSetting or None
  - 現在の一点鎖線のスタイル設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color="#fff",
...     thickness=5,
...     dash_dot_setting=ap.LineDashDotSetting(
...         dot_size=2, dash_size=5, space_size=3
...     ),
... )
>>> sprite.graphics.line_dash_dot_setting.dot_size
Int(2)

>>> sprite.graphics.line_dash_dot_setting.dash_size
Int(5)

>>> sprite.graphics.line_dash_dot_setting.space_size
Int(3)
```