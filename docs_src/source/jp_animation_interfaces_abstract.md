<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](animation_interfaces_abstract.md)の確認をお願いします。</span>

# 各アニメーションインターフェイス概要

このページでは各アニメーションの概要について説明します。

## apyscの各アニメーションのインターフェイスで出来ること

- 座標値や回転量、色や透明度、拡縮値などの各属性に対してアニメーションを行うことができます。
- 何ミリ秒かけてアニメーションするかを設定することができます。

- アニメーション開始前の遅延時間をミリ秒単位で設定することができます。

`EASE_IN_CUBIC`や`EASE_OUT_QUINT`、`EASE_IN_OUT_BOUNCE`などのイージングの設定を行うことができます。

一時停止、再生、リセット、終了、逆再生、経過時間取得などのアニメーション関係の制御を行うことができます。

アニメーションの並列実行や直列実行を設定することができます。

- アニメーション終了時のイベント設定をサポートしています。

## 各属性のアニメーション設定例

この節では各属性のアニメーション設定例を表示します。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=550, stage_height=550, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.line_style(color='#fff', thickness=1)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_x_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the x-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_x_animation_complete_2).start()


def on_x_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the x-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_x_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_x_animation_complete_1).start()


def on_y_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the y-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_y_animation_complete_2).start()


def on_y_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the y-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_y_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50,
).animation_y(
    y=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_y_animation_complete_1).start()


def on_cx_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=275, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cx_animation_complete_2).start()


def on_cx_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=325, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cx_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=275, y=75, radius=25,
).animation_x(
    x=325, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_cx_animation_complete_1).start()


def on_cy_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-y animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=75, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cy_animation_complete_2).start()


def on_cy_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-y animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=25, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cy_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=375, y=75, radius=25,
).animation_y(
    y=25, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_cy_animation_complete_1).start()


def on_move_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that move-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=450, y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_move_animation_complete_2).start()


def on_move_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that move-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=500, y=0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_move_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=450, y=50, width=50, height=50,
).animation_move(
    x=500, y=0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_move_animation_complete_1).start()


def on_width_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_width_animation_complete_2).start()


def on_width_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_width_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50,
).animation_width(
    width=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_width_animation_complete_1).start()


def on_height_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_height_animation_complete_2).start()


def on_height_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_height_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=150, y=150, width=50, height=50,
).animation_height(
    height=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_height_animation_complete_1).start()


def on_ellipse_width_animation_complete_1(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_width_animation_complete_2).start()


def on_ellipse_width_animation_complete_2(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_width_animation_complete_1).start()


sprite.graphics.draw_ellipse(
    x=275, y=175, width=50, height=50,
).animation_width(
    width=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_ellipse_width_animation_complete_1).start()


def on_ellipse_height_animation_complete_1(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_height_animation_complete_2).start()


def on_ellipse_height_animation_complete_2(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_height_animation_complete_1).start()


sprite.graphics.draw_ellipse(
    x=375, y=175, width=50, height=50,
).animation_height(
    height=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_ellipse_height_animation_complete_1).start()


def on_fill_color_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#0af', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_color_animation_complete_2).start()


def on_fill_color_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_color_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=450, y=150, width=50, height=50,
).animation_fill_color(
    fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_fill_color_animation_complete_1).start()


def on_fill_alpha_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_alpha_animation_complete_2).start()


def on_fill_alpha_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_alpha_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50,
).animation_fill_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_fill_alpha_animation_complete_1).start()


def on_line_color_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#fff', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_color_animation_complete_2).start()


def on_line_color_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#666', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_color_animation_complete_1).start()


sprite.graphics.line_style(color='#fff', thickness=5)
sprite.graphics.draw_rect(
    x=150, y=250, width=50, height=50,
).animation_line_color(
    line_color='#666', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_line_color_animation_complete_1).start()


def on_line_alpha_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_alpha_animation_complete_2).start()


def on_line_alpha_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_alpha_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=250, y=250, width=50, height=50,
).animation_line_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_line_alpha_animation_complete_1).start()
sprite.graphics.line_style(color='#fff', thickness=1)


def on_line_thickness_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-thickness animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=1, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_thickness_animation_complete_2).start()


def on_line_thickness_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-thickness animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_thickness_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=350, y=250, width=50, height=50,
).animation_line_thickness(
    thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_line_thickness_animation_complete_1).start()


def on_radius_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the radius-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=25, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_radius_animation_complete_2).start()


def on_radius_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the radius-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_radius_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=475, y=275, radius=25,
).animation_radius(
    radius=50, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_radius_animation_complete_1).start()


def on_rotation_around_center_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(
        on_rotation_around_center_animation_complete_2,
    ).start()


def on_rotation_around_center_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=90, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(
        on_rotation_around_center_animation_complete_1,
    ).start()


sprite.graphics.draw_rect(
    x=50, y=350, width=50, height=50,
).animation_rotation_around_center(
    rotation_around_center=90, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_rotation_around_center_animation_complete_1).start()


def on_rotation_around_point_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=0,
        x=200, y=400, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(
        on_rotation_around_point_animation_complete_2,
    ).start()


def on_rotation_around_point_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=90,
        x=200, y=400, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(
        on_rotation_around_point_animation_complete_1,
    ).start()


sprite.graphics.draw_rect(
    x=150, y=350, width=50, height=50,
).animation_rotation_around_point(
    rotation_around_point=90,
    x=200, y=400, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_rotation_around_point_animation_complete_1).start()


def on_scale_x_from_center_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_center_animation_complete_2).start()


def on_scale_x_from_center_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_center_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=250, y=350, width=50, height=50,
).animation_scale_x_from_center(
    scale_x_from_center=0.5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_scale_x_from_center_animation_complete_1).start()


def on_scale_y_from_center_animation_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the center point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_center_animation_2).start()


def on_scale_y_from_center_animation_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the center point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_center_animation_1).start()


sprite.graphics.draw_rect(
    x=350, y=350, width=50, height=50,
).animation_scale_y_from_center(
    scale_y_from_center=0.5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_scale_y_from_center_animation_1).start()


def on_scale_x_from_point_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=1.0, x=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_point_animation_complete_2).start()


def on_scale_x_from_point_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=0.5, x=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_point_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=450, y=350, width=50, height=50,
).animation_scale_x_from_point(
    scale_x_from_point=0.5, x=500, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_scale_x_from_point_animation_complete_1).start()


def on_scale_y_from_point_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=1.0, y=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_point_animation_complete_2).start()


def on_scale_y_from_point_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=0.5, y=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_point_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=450, width=50, height=50,
).animation_scale_y_from_point(
    scale_y_from_point=0.5, y=500, duration=DURATION, delay=DELAY,
).animation_complete(on_scale_y_from_point_animation_complete_1).start()


def on_skew_x_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the skew-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_skew_x_animation_complete_2).start()


def on_skew_x_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the skew-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=30, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_skew_x_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=150, y=450, width=50, height=50,
).animation_skew_x(
    skew_x=30, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_skew_x_animation_complete_1).start()


ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_each_attr/')
```

</details>

<iframe src="static/animation_interfaces_abstract_each_attr/index.html" width="550" height="550"></iframe>

## イージング

イージング設定は各インターフェイスの`easing`引数で設定することができます。詳細は以下を参照してください:

- [イージングのenum](jp_easing_enum.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500


class EasingOptions(TypedDict):
    easing: ap.Easing


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: EasingOptions) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=50, duration=DURATION, delay=DELAY,
        easing=options['easing'],
    ).animation_complete(
        on_animation_complete_2, options=options,
    ).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: EasingOptions) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=100, duration=DURATION, delay=DELAY,
        easing=options['easing'],
    ).animation_complete(
        on_animation_complete_1, options=options,
    ).start()


options: EasingOptions = {'easing': ap.Easing.EASE_IN_QUINT}
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY,
    easing=options['easing'],
).animation_complete(
    on_animation_complete_1, options=options,
).start()

options = {'easing': ap.Easing.EASE_OUT_QUINT}
sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY,
    easing=options['easing'],
).animation_complete(
    on_animation_complete_1, options=options,
).start()

options = {'easing': ap.Easing.EASE_IN_OUT_QUINT}
sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY,
    easing=options['easing'],
).animation_complete(
    on_animation_complete_1, options=options,
).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_easing/')
```

</details>

<iframe src="static/animation_interfaces_abstract_easing/index.html" width="200" height="350"></iframe>

## X座標のアニメーション

`animation_x`のインターフェイスではX座標のアニメーションを設定します。詳細は以下を参照してください:

- [animation_x （X座標のアニメーション）のインターフェイス](jp_animation_x.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_x/')
```

</details>

<iframe src="static/animation_interfaces_abstract_x/index.html" width="200" height="150"></iframe>

## Y座標のアニメーション

`animation_y`インターフェイスではY座標のアニメーションを設定します。詳細は以下を参照してください:

- [animation_y （Y座標のアニメーション）のインターフェイス](jp_animation_y.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_y(
    y=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_y/')
```

</details>

<iframe src="static/animation_interfaces_abstract_y/index.html" width="150" height="200"></iframe>

## X座標とY座標のアニメーション

`animation_move`のインターフェイスはX座標とY座標両方のアニメーションを設定します。詳細は以下を参照してください:

- [animation_move （XとY座標のアニメーション）のインターフェイス](jp_animation_move.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=50, y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=100, y=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_move(
    x=100, y=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_move/')
```

</details>

<iframe src="static/animation_interfaces_abstract_move/index.html" width="200" height="200"></iframe>

## 幅のアニメーション

`animation_width`インターフェイスは幅のアニメーションを設定します。詳細は以下を参照してください:

- [animation_width （幅のアニメーション）と animation_height （高さのアニメーション）のインターフェイス](jp_animation_width_and_height.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_width(
    width=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_width/')
```

</details>

<iframe src="static/animation_interfaces_abstract_width/index.html" width="200" height="150"></iframe>

## 高さのアニメーション

`animation_height`インターフェイスは高さのアニメーションを設定します。詳細は以下を参照してください:

- [animation_width （幅のアニメーション）と animation_height （高さのアニメーション）のインターフェイス](jp_animation_width_and_height.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_height(
    height=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_height/')
```

</details>

<iframe src="static/animation_interfaces_abstract_height/index.html" width="150" height="200"></iframe>

## 塗りの色のアニメーション

`animation_fill_color`インターフェイスは塗りの色のアニメーションを設定します。詳細は以下を参照してください:

- [animation_fill_color （塗りの色のアニメーション）のインターフェイス](jp_animation_fill_color.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#0af', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_fill_color(
    fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_fill_color/')
```

</details>

<iframe src="static/animation_interfaces_abstract_fill_color/index.html" width="150" height="150"></iframe>

## 塗りの透明度のアニメーション

`animation_fill_alpha`インターフェイスは塗りの透明度のアニメーションを設定します。詳細は以下を参照してください:

- [animation_fill_alpha （塗りの透明度のアニメーション）のインターフェイス](jp_animation_fill_alpha.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_fill_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_fill_alpha/')
```

</details>

<iframe src="static/animation_interfaces_abstract_fill_alpha/index.html" width="150" height="150"></iframe>

## 線色のアニメーション

`animation_line_color`インターフェイスは線色のアニメーションを設定します。詳細は以下を参照してください:

- [animation_line_color （線色のアニメーション）のインターフェイス](jp_animation_line_color.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=5)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#0af', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_line_color(
    line_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_line_color/')
```

</details>

<iframe src="static/animation_interfaces_abstract_line_color/index.html" width="150" height="150"></iframe>

## 線の透明度のアニメーション

`animation_line_alpha`インターフェイスは線の透明度のアニメーションを設定します。詳細は以下を参照してください:

- [animation_line_alpha （線の透明度のアニメーション）のインターフェイス](jp_animation_line_alpha.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=5)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_line_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_line_alpha/')
```

</details>

<iframe src="static/animation_interfaces_abstract_line_alpha/index.html" width="150" height="150"></iframe>

## 線幅のアニメーション

`animation_line_thickness`インターフェイスは線幅のアニメーションを設定します。詳細は以下を参照してください:

- [animation_line_thickness （線幅のアニメーション）のインターフェイス](jp_animation_line_thickness.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=1)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=1, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_line_thickness(
    thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_line_thickness/')
```

</details>

<iframe src="static/animation_interfaces_abstract_line_thickness/index.html" width="150" height="150"></iframe>

## 半径のアニメーション

`animation_radius`インターフェイスは円のインスタンスなどの半径のアニメーションを設定します。詳細は以下を参照してください:

- [animation_radius （半径のアニメーション）のインターフェイス](jp_animation_radius.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=25, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=75, y=75, radius=25,
).animation_radius(
    radius=50, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_radius/')
```

</details>

<iframe src="static/animation_interfaces_abstract_radius/index.html" width="150" height="150"></iframe>

## 中央座標による回転のアニメーション

`animation_rotation_around_center`インターフェイスは中央座標による回転のアニメーションを設定します。詳細は以下を参照してください:

- [animation_rotation_around_center （中央座標での回転のアニメーション）のインターフェイス](jp_animation_rotation_around_center.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=90, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_rotation_around_center(
    rotation_around_center=90, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_rotation_around_center/')
```

</details>

<iframe src="static/animation_interfaces_abstract_rotation_around_center/index.html" width="150" height="150"></iframe>

## 指定座標による回転のアニメーション

`animation_rotation_around_point`

- [animation_rotation_around_point （指定座標による回転のアニメーション）のインターフェイス](jp_animation_rotation_around_point.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=0, x=100, y=100, duration=DURATION,
        delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=90, x=100, y=100, duration=DURATION,
        delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_rotation_around_point(
    rotation_around_point=90, x=100, y=100, duration=DURATION,
    delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_rotation_around_point/')
```

</details>

<iframe src="static/animation_interfaces_abstract_rotation_around_point/index.html" width="200" height="150"></iframe>

## 中央座標による水平方向の拡縮のアニメーション

`animation_scale_x_from_center`インターフェイスは中央座標による水平方向の拡縮のアニメーションを設定します。詳細は以下を参照してください:

- [animation_scale_x_from_center （中央座標による水平方向の拡縮アニメーション）と animation_scale_y_from_center （中央座標による垂直方向の拡縮アニメーション）のインターフェイス](jp_animation_scale_x_and_y_from_center.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_x_from_center(
    scale_x_from_center=0.5, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_x_from_center/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_x_from_center/index.html" width="150" height="150"></iframe>

## 中央座標による垂直方向の拡縮のアニメーション

`animation_scale_y_from_center`インターフェイスは中央座標による垂直方向のアニメーションを設定します。詳細は以下を参照してください:

- [animation_scale_x_from_center （中央座標による水平方向の拡縮アニメーション）と animation_scale_y_from_center （中央座標による垂直方向の拡縮アニメーション）のインターフェイス](jp_animation_scale_x_and_y_from_center.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_y_from_center(
    scale_y_from_center=0.5, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_y_from_center/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_y_from_center/index.html" width="150" height="150"></iframe>

## 指定座標による水平方向の拡縮アニメーション

`animation_scale_x_from_point`インターフェイスは指定座標による水平方向の拡縮のアニメーションを設定します。詳細は以下を参照してください:

- [animation_scale_x_from_point （指定座標による水平方向の拡縮アニメーション）と animation_scale_y_from_point （指定座標による垂直方向のアニメーション）のインターフェイス](jp_animation_scale_x_and_y_from_point.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=1.0, x=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=0.5, x=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_x_from_point(
    scale_x_from_point=0.5, x=100, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_x_from_point/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_x_from_point/index.html" width="150" height="150"></iframe>

## 指定座標による垂直方向の拡縮アニメーション

`animation_scale_y_from_point`インターフェイスは指定座標による垂直方向の拡縮アニメーションを設定します。詳細は以下を参照してください:

- [animation_scale_x_from_point （指定座標による水平方向の拡縮アニメーション）と animation_scale_y_from_point （指定座標による垂直方向のアニメーション）のインターフェイス](jp_animation_scale_x_and_y_from_point.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=1.0, y=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=0.5, y=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_y_from_point(
    scale_y_from_point=0.5, y=100, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_y_from_point/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_y_from_point/index.html" width="150" height="150"></iframe>

## 水平方向の斜め変換のアニメーション

`animation_skew_x`インターフェイスは水平方向の斜め変換のアニメーションを設定します。詳細は以下を参照してください:

- [animation_skew_x （水平方向の斜め変換のアニメーション）のインターフェイス](jp_animation_skew_x.md)

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=50, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_skew_x(
    skew_x=50, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_skew_x/')
```

</details>

<iframe src="static/animation_interfaces_abstract_skew_x/index.html" width="150" height="150"></iframe>