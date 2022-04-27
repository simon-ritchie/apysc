<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](what_apysc_can_do.md)の確認をお願いします。</span>

# apysc ライブラリが現在の実装でできること

このページでは apysc ライブパリの現在の実装と機能の概要について説明します。

## Pythonを使って書き、それをHTMLへ出力・もしくはJupyter上で利用する

apysc ライブラリではフロントエンドをPythonを使って書くことができ、結果をHTMLに出力したりもしくはJupyter notebookやJupyterLab、Google Colaboratory上などで表示することができます。

参考資料:

- [save_overall_html インターフェイス](jp_save_overall_html.md)
- [display_on_jupyter インターフェイス](jp_display_on_jupyter.md)

- [display_on_colaboratory インターフェイス](jp_display_on_colaboratory.md)

## 様々な種類のベクターグラフィックスの描画

apysc ライブラリでは四角や円、線などの様々な種類のベクターグラフィックスの描画を行うことができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=650, stage_height=210, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.draw_round_rect(
    x=150, y=50, width=50, height=50, ellipse_width=12, ellipse_height=12)

sprite.graphics.draw_circle(x=275, y=75, radius=25)

sprite.graphics.draw_ellipse(x=375, y=75, width=50, height=30)

sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=475, y=50),
        ap.Point2D(x=450, y=100),
        ap.Point2D(x=500, y=100),
    ])

sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(color='#eee', thickness=3)
sprite.graphics.move_to(x=550, y=50)
sprite.graphics.line_to(x=600, y=50)
sprite.graphics.line_to(x=550, y=100)
sprite.graphics.line_to(x=600, y=100)

sprite.graphics.draw_line(x_start=50, y_start=130, x_end=600, y_end=130)
sprite.graphics.draw_dotted_line(
    x_start=50, y_start=130, x_end=600, y_end=130, dot_size=5)
sprite.graphics.draw_round_dotted_line(
    x_start=53, y_start=160, x_end=600, y_end=160, round_size=6, space_size=6)

ap.save_overall_html(
    dest_dir_path='what_apysc_can_do_draw_vector_graphics/')
```

</details>

<iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>

参考資料:

- [Graphics クラス](jp_graphics.md)
- [Graphics クラスの begin_fill (塗りの設定)のインターフェイス](jp_graphics_begin_fill.md)

- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)
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

## 各種マウスイベントの設定

apysc ライブラリではクリックやマウスダウン、マウスオーバー、マウスムーブなどの各種マウスイベントの設定をサポートしています。

クリックイベントの例（以下の四角をクリックしてご確認ください）:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    color: ap.String = e.this.fill_color
    condition: ap.Boolean = color == '#00aaff'
    with ap.If(condition):
        e.this.fill_color = ap.String('#f0a')
    with ap.Else():
        e.this.fill_color = ap.String('#0af')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='what_apysc_can_do_mouse_event_click/')
```

</details>

<iframe src="static/what_apysc_can_do_mouse_event_click/index.html" width="150" height="150"></iframe>

参考資料:

- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)
- [click インターフェイス](jp_click.md)

- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)
- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)

- [mousemove インターフェイス](jp_mousemove.md)

## タイマーのインターフェイスとアニメーション

タイマーに関係したインターフェイスを利用することができ、それを使ってアニメーションを設定することができます。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _Options(TypedDict):
    rectangle: ap.Rectangle
    alpha_direction: ap.Int


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
    alpha_direction: ap.Int = options['alpha_direction']
    current_alpha: ap.Number = rectangle.fill_alpha
    condition_1: ap.Boolean = current_alpha < 0.0
    condition_2: ap.Boolean = current_alpha > 1.0
    with ap.If(condition_1):
        alpha_direction.value = 1
    with ap.Elif(condition_2):
        alpha_direction.value = -1
    rectangle.fill_alpha += alpha_direction * 0.03
    rectangle.rotation_around_center += 1


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
alpha_direction: ap.Int = ap.Int(1)
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _Options = {
    'rectangle': rectangle, 'alpha_direction': alpha_direction}
timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='what_apysc_can_do_timer_animation/')
```

</details>

<iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>

参考資料:

- [Timer クラス](jp_timer.md)
- [TimerEvent クラス](jp_timer_event.md)

- [Timer クラスの delay 設定](jp_timer_delay.md)
- [FPS の enum](jp_fps.md)

- [Timer クラスの repeat_count 設定](jp_timer_repeat_count.md)
- [Timer クラスの start と stop の各インターフェイス](jp_timer_start_and_stop.md)

- [Timer クラスの timer_complete インターフェイス](jp_timer_complete.md)
- [Timer クラスの reset インターフェイス](jp_timer_reset.md)