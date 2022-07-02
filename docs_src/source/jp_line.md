<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/line.html)の確認をお願いします。</span>

# Line クラス

このページでは`Line`クラスについて説明します。

## クラス概要

`Line`クラスは直線のベクターグラフィックスを生成します。

## 基本的な使い方

`Line`クラスのコンストラクタでは`start_point`や`end_point`の引数指定を必要とします。

コンストラクタでは`line_color`などのスタイル設定用の引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)

ap.save_overall_html(
    dest_dir_path='line_basic_usage/')
```

<iframe src="static/line_basic_usage/index.html" width="200" height="100"></iframe>

## draw_line や他の各インターフェイスの特記事項

`draw_line`や`draw_dotted_line`などの他のインターフェイスを使う形でも直線のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)
- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)

- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)
- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)

- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)
line.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='line_x/')
```

<iframe src="static/line_x/index.html" width="200" height="100"></iframe>

特記事項: この属性の値は`start_point`の値と同じになります。

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)
line.y = ap.Int(80)

ap.save_overall_html(
    dest_dir_path='line_y/')
```

<iframe src="static/line_y/index.html" width="200" height="100"></iframe>

特記事項: この属性の値は`start_point`の値と同じになります。

## line_color属性のインターフェイス例

`line_color`属性では線の色の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50), line_thickness=5)
line.line_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='line_line_color/')
```

<iframe src="static/line_line_color/index.html" width="200" height="100"></iframe>

## line_alpha属性のインターフェイス例

`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)
line.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='line_line_alpha/')
```

<iframe src="static/line_line_alpha/index.html" width="200" height="100"></iframe>

## line_thickness属性のインターフェイス例

`line_thickness`属性では線の幅の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af')
line.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='line_line_thickness/')
```

<iframe src="static/line_line_thickness/index.html" width="200" height="100"></iframe>

## line_dot_setting属性のインターフェイス例

`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=3)
line.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='line_line_dot_setting/')
```

<iframe src="static/line_line_dot_setting/index.html" width="200" height="100"></iframe>

## line_dash_setting属性のインターフェイス例

`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=3)
line.line_dash_setting = ap.LineDashSetting(
    dash_size=6, space_size=2)

ap.save_overall_html(
    dest_dir_path='line_line_dash_setting/')
```

<iframe src="static/line_line_dash_setting/index.html" width="200" height="100"></iframe>

## line_round_dot_setting属性のインターフェイス例

`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af')
line.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=3)

ap.save_overall_html(
    dest_dir_path='line_line_round_dot_setting/')
```

<iframe src="static/line_line_round_dot_setting/index.html" width="200" height="100"></iframe>

## line_dash_dot_setting属性のインターフェイス例

`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=3)
line.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=2, dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='line_line_dash_dot_setting/')
```

<iframe src="static/line_line_dash_dot_setting/index.html" width="200" height="100"></iframe>