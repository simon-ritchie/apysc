<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/circle.html)の確認をお願いします。</span>

# Circle クラス

このページでは`Circle`クラスについて説明します。

## クラス概要

`Circle`クラスは円のベクターグラフィックスを生成します。

## 基本的な使い方

`Circle`クラスのコンストラクタでは`x`（円の中央のX座標）、`y`（円の中央のY座標）、そして半径としての`radius`引数が必要となります。

コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='circle_basic_usage/')
```

<iframe src="static/circle_basic_usage/index.html" width="150" height="150"></iframe>

## draw_circle インターフェイスに対する特記事項

`draw_circle`インターフェイスを使って円を作成することもできます。

関連資料:

- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)

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
circle: ap.Circle = ap.Circle(
    x=0, y=75, radius=50, fill_color='#0af')
circle.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='circle_x/')
```

<iframe src="static/circle_x/index.html" width="200" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=0, radius=50, fill_color='#0af')
circle.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='circle_y/')
```

<iframe src="static/circle_y/index.html" width="150" height="200"></iframe>

## radius属性のインターフェイス例

`radius`属性では円の半径の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=0, fill_color='#0af')
circle.radius = ap.Int(30)

ap.save_overall_html(
    dest_dir_path='circle_radius/')
```

<iframe src="static/circle_radius/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50)
circle.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='circle_fill_color/')
```

<iframe src="static/circle_fill_color/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='circle_fill_alpha/')
```

<iframe src="static/circle_fill_alpha/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_thickness=5)
circle.line_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='circle_line_color/')
```

<iframe src="static/circle_line_color/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=5)
circle.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='circle_line_alpha/')
```

<iframe src="static/circle_line_alpha/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af')
circle.line_thickness = ap.Int(8)

ap.save_overall_html(
    dest_dir_path='circle_line_thickness/')
```

<iframe src="static/circle_line_thickness/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_dot_setting/')
```

<iframe src="static/circle_line_dot_setting/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dash_setting = ap.LineDashSetting(
    dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='circle_line_dash_setting/')
```

<iframe src="static/circle_line_dash_setting/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af')
circle.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_round_dot_setting/')
```

<iframe src="static/circle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

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
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_dash_dot_setting/')
```

<iframe src="static/circle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>