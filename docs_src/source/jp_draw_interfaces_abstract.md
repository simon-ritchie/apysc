<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/draw_interfaces_abstract.html)の確認をお願いします。</span>

# 描画の各インターフェイスの概要

このページでは描画の各インターフェイスについて説明します。

## apyscの描画の各インターフェイスでできること

- これらのインターフェイスを使って塗りの色、塗りの透明度、線の色、線の透明度、線幅などを設定することができます。
- 四角や丸、楕円、多角形、線、折れ線、パスなどの描画をサポートしています。

## 塗りの設定

`begin_fill`のインターフェイスは塗りの色と塗りの透明度を設定します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af', alpha=0.5)
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='draw_interfaces_abstract_begin_fill/')
```

<iframe src="static/draw_interfaces_abstract_begin_fill/index.html" width="150" height="150"></iframe>

詳細は以下をご確認ください:

- [Graphics クラスの begin_fill (塗りの設定)のインターフェイス](jp_graphics_begin_fill.md)

## 線のスタイル設定

`line_style`インターフェイスは線の色と線の透明度、線幅などを設定することができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=5, alpha=0.5)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

ap.save_overall_html(
    dest_dir_path='draw_interfaces_abstract_line_style/')
```

<iframe src="static/draw_interfaces_abstract_line_style/index.html" width="200" height="100"></iframe>

詳細は以下をご確認ください:

- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)

## 描画の各インターフェイス

各描画のインターフェイスは`draw_`のプレフィックスを持っており、SVGのグラフィックを描画します（例 : draw_rect や draw_circle など）。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_circle(x=175, y=75, radius=25)

ap.save_overall_html(
    dest_dir_path='draw_interfaces_abstract_each_drawing_interface/')
```

<iframe src="static/draw_interfaces_abstract_each_drawing_interface/index.html" width="250" height="150"></iframe>

詳細については以下をご確認ください:

- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)
- [Graphics クラスの draw_round_rect (角丸の四角の描画)のインターフェイス](jp_graphics_draw_round_rect.md)

- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)
- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)

- [Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス](jp_graphics_move_to_and_line_to.md)
- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)

- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)
- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)

- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)
- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)

- [Graphics クラスの draw_polygon (多角形描画)のインターフェイス](jp_graphics_draw_polygon.md)

## 関連資料

- [Graphics クラス](jp_graphics.md)
- [Graphics クラスの fill_color (塗り設定)のインターフェイス](jp_graphics_fill_color.md)

- [Graphics クラスの fill_alpha (塗りの透明度設定)のインターフェイス](jp_graphics_fill_alpha.md)
- [Graphics クラスの line_color (線の色設定)のインターフェイス](jp_graphics_line_color.md)

- [Graphics クラスの line_color (線の透明度設定)のインターフェイス](jp_graphics_line_alpha.md)
- [Graphics クラスの line_color (線幅設定)のインターフェイス](jp_graphics_line_thickness.md)

- [Graphics クラスの line_dot_setting (点線設定)のインターフェイス](jp_graphics_line_dot_setting.md)
- [Graphics クラスの line_dash_setting (破線設定)のインターフェイス](jp_graphics_line_dash_setting.md)

- [Graphics クラスの line_round_dot_setting (点線(丸)設定)のインターフェイス](jp_graphics_line_round_dot_setting.md)
- [Graphics クラスの line_dash_dot_setting (一点鎖線設定)のインターフェイス](jp_graphics_line_dash_dot_setting.md)