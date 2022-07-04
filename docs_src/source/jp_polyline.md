<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/polyline.html)の確認をお願いします。</span>

# Polyline クラス

このページでは`Polyline`クラスについて説明します。

## クラス概要

`Polyline`クラスは折れ線のベクターグラフィックスを生成します。

## 基本的な使い方

`Polyline`クラスはコンストラクタに`points`のリストの引数を必要とします。

コンストラクタは`line_color`などのスタイル設定の引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)

ap.save_overall_html(
    dest_dir_path='polyline_basic_usage/')
```

<iframe src="static/polyline_basic_usage/index.html" width="200" height="150"></iframe>

## move_to と line_to インターフェイスの特記事項

`move_to`と`line_to`の各インターフェイスを使う形でも折れ線のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス](jp_graphics_move_to_and_line_to.md)

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
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)
polyline.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='polyline_x/')
```

<iframe src="static/polyline_x/index.html" width="200" height="150"></iframe>

特記事項: この属性の値は引数の座標の最小値と同値になります。

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)
polyline.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='polyline_y/')
```

<iframe src="static/polyline_y/index.html" width="200" height="150"></iframe>

特記事項: この属性の値は引数の座標の最小値と同値になります。

## fill_color属性のインターフェイス例

`fill_color`属性は塗りの色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#fff',
    line_thickness=3)
polyline.fill_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='polyline_fill_color/')
```

<iframe src="static/polyline_fill_color/index.html" width="200" height="150"></iframe>

## fill_alpha属性のインターフェイス例

`fill_alpha`属性は塗りの透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    fill_color='#0af',
    line_color='#fff',
    line_thickness=3)
polyline.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='polyline_fill_alpha/')
```

<iframe src="static/polyline_fill_alpha/index.html" width="200" height="150"></iframe>

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_thickness=3)
polyline.line_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='polyline_line_color/')
```

<iframe src="static/polyline_line_color/index.html" width="200" height="150"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)
polyline.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='polyline_line_alpha/')
```

<iframe src="static/polyline_line_alpha/index.html" width="200" height="150"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af')
polyline.line_thickness = ap.Int(6)

ap.save_overall_html(
    dest_dir_path='polyline_line_thickness/')
```

<iframe src="static/polyline_line_thickness/index.html" width="200" height="150"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)
polyline.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='polyline_line_dot_setting/')
```

<iframe src="static/polyline_line_dot_setting/index.html" width="200" height="150"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)
polyline.line_dash_setting = ap.LineDashSetting(
    dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='polyline_line_dash_setting/')
```

<iframe src="static/polyline_line_dash_setting/index.html" width="200" height="150"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af')
polyline.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='polyline_line_round_dot_setting/')
```

<iframe src="static/polyline_line_round_dot_setting/index.html" width="200" height="150"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color='#0af',
    line_thickness=3)
polyline.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=2, dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='polyline_line_dash_dot_setting/')
```

<iframe src="static/polyline_line_dash_dot_setting/index.html" width="200" height="150"></iframe>