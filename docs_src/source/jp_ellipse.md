<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/ellipse.html)の確認をお願いします。</span>

# Ellipse クラス

このページでは`Ellipse`クラスについて説明します。

## クラス概要

`Ellipse`クラスは楕円のベクターグラフィックスのオブジェクトを生成します。

## 基本的な使い方

`Ellipse`クラスのコンストラクタでは`x`（楕円の中央のX座標）、`y`（楕円の中央のY座標）、`width`、`height`の各引数の指定が必要です。

コンストラクタでは他の`fill_color`などのスタイル設定の各引数も受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='ellipse_basic_usage/')
```

<iframe src="static/ellipse_basic_usage/index.html" width="150" height="150"></iframe>

## draw_ellipse インターフェイスについての特記事項

`draw_ellipse`を使う形でも楕円のインスタンスを生成することができます。

関連資料:

- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)

## x属性のインターフェイス例

`x`属性ではX座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=0, y=75, width=100, height=75, fill_color='#0af')
ellipse.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='ellipse_x/')
```

<iframe src="static/ellipse_x/index.html" width="150" height="150"></iframe>

## y属性のインターフェイス例

`y`属性ではY座標の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=0, width=100, height=50, fill_color='#0af')
ellipse.y = ap.Int(125)

ap.save_overall_html(
    dest_dir_path='ellipse_y/')
```

<iframe src="static/ellipse_y/index.html" width="150" height="150"></iframe>

## width属性のインターフェイス例

`width`属性では幅の値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=0, height=75, fill_color='#0af')
ellipse.width = ap.Int(125)

ap.save_overall_html(
    dest_dir_path='ellipse_width/')
```

<iframe src="static/ellipse_width/index.html" width="150" height="150"></iframe>

## height属性のインターフェイス例

`height`属性では高さの値の更新もしくは取得を行えます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=75, height=0, fill_color='#0af')
ellipse.height = ap.Int(125)

ap.save_overall_html(
    dest_dir_path='ellipse_height/')
```

<iframe src="static/ellipse_height/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75)
ellipse.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='ellipse_fill_color/')
```

<iframe src="static/ellipse_fill_color/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, fill_color='#0af')
ellipse.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='ellipse_fill_alpha/')
```

<iframe src="static/ellipse_fill_alpha/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_thickness=5)
ellipse.line_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='ellipse_line_color/')
```

<iframe src="static/ellipse_line_color/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=5)
ellipse.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='ellipse_line_alpha/')
```

<iframe src="static/ellipse_line_alpha/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_color='0af')
ellipse.line_thickness = ap.Int(8)

ap.save_overall_html(
    dest_dir_path='ellipse_line_thickness/')
```

<iframe src="static/ellipse_line_thickness/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=2)
ellipse.line_dot_setting = ap.LineDotSetting(dot_size=2)

ap.save_overall_html(
    dest_dir_path='ellipse_line_dot_setting/')
```

<iframe src="static/ellipse_line_dot_setting/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=2)
ellipse.line_dash_setting = ap.LineDashSetting(
    dash_size=6, space_size=2)

ap.save_overall_html(
    dest_dir_path='ellipse_line_dash_setting/')
```

<iframe src="static/ellipse_line_dash_setting/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_color='0af')
ellipse.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='ellipse_line_round_dot_setting/')
```

<iframe src="static/ellipse_line_round_dot_setting/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=2)
ellipse.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='ellipse_line_dash_dot_setting/')
```

<iframe src="static/ellipse_line_dash_dot_setting/index.html" width="150" height="150"></iframe>