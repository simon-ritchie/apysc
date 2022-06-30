<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/rectangle.html)の確認をお願いします。</span>

# Rectangle クラス

このページでは`Rectangle`クラスについて説明します。

## クラス概要

`Rectangle`クラスは四角のベクターグラフィックスを生成します。

## 基本的な使い方

`Rectangle`クラスのコンストラクタでは`x`、`y`、`width`、`height`の引数指定が必要になります。

コンストラクタでは他にも`fill_color`などのスタイル設定の引数を受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=100, height=50,
    fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='rectangle_basic_usage/')
```

<iframe src="static/rectangle_basic_usage/index.html" width="200" height="150"></iframe>

## draw_rect インターフェイスに対する特記事項

`draw_rect`インターフェイスを使っても四角のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=0, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_x/')
```

<iframe src="static/rectangle_x/index.html" width="200" height="150"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=0, width=50, height=50,
    fill_color='#0af')
rectangle.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_y/')
```

<iframe src="static/rectangle_y/index.html" width="150" height="200"></iframe>

## width属性のインターフェイス例

`width`属性では幅の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.width = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_width/')
```

<iframe src="static/rectangle_width/index.html" width="200" height="150"></iframe>

## height属性のインターフェイス例

`height`属性では高さの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.height = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_height/')
```

<iframe src="static/rectangle_height/index.html" width="150" height="200"></iframe>

## ellipse_width属性のインターフェイス例

`ellipse_width`属性では四角の角丸の幅の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.ellipse_width = ap.Int(30)
rectangle.ellipse_height = ap.Int(15)

ap.save_overall_html(
    dest_dir_path='rectangle_ellipse_width/')
```

<iframe src="static/rectangle_ellipse_width/index.html" width="150" height="150"></iframe>

## ellipse_height属性のインターフェイス例

`ellipse_height`属性では四角の角丸の高さの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.ellipse_width = ap.Int(15)
rectangle.ellipse_height = ap.Int(30)

ap.save_overall_html(
    dest_dir_path='rectangle_ellipse_height/')
```

<iframe src="static/rectangle_ellipse_height/index.html" width="150" height="150"></iframe>

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='rectangle_fill_color/')
```

<iframe src="static/rectangle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='rectangle_fill_alpha/')
```

<iframe src="static/rectangle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_thickness=5)
rectangle.line_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='rectangle_line_color/')
```

<iframe src="static/rectangle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=5)
rectangle.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_alpha/')
```

<iframe src="static/rectangle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color='#0af')
rectangle.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='rectangle_line_thickness/')
```

<iframe src="static/rectangle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=5)
rectangle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_dot_setting/')
```

<iframe src="static/rectangle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=2)
rectangle.line_dash_setting = ap.LineDashSetting(
    dash_size=7, space_size=2)

ap.save_overall_html(
    dest_dir_path='rectangle_line_dash_setting/')
```

<iframe src="static/rectangle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af')
rectangle.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_round_dot_setting/')
```

<iframe src="static/rectangle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=3)
rectangle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=7, space_size=3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_dash_dot_setting/')
```

<iframe src="static/rectangle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>