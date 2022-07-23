<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/easing_enum.html)の確認をお願いします。</span>

# イージングのenum

このページでは`Easing`のenumのクラスについて説明します。

## クラス概要

`Easing`のenumのクラスは各イージング関数について定義しています。これらは`animation_move`などのアニメーションのインターフェイスで使用します。

## 基本的な使い方

`animation_move`や`animation_x`などの各アニメーションのメソッドのインターフェイスでは`easing`引数を持っており、以下のコード例のようにその引数に`Easing`のenumの値を指定することができます:

```py
# runnable
import apysc as ap


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=50, y=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_move.animation_complete(on_animation_complete_2)
    animation_move.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=100, y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_move.animation_complete(on_animation_complete_1)
    animation_move.start()


ap.Stage(
    stage_width=200, stage_height=200, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
)
animation_move.animation_complete(on_animation_complete_1)
animation_move.start()

ap.save_overall_html(dest_dir_path="./easing_enum_basic_usage/")
```

<iframe src="static/easing_enum_basic_usage/index.html" width="200" height="200"></iframe>

もしも`easing`引数の指定を省略した場合、アニメーションは線形（スタートから終了まで一定の変動）のアニメーションとなります。

```py
# runnable
import apysc as ap


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=50, y=50, duration=1000
    )
    animation_move.animation_complete(on_animation_complete_2)
    animation_move.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=100, y=100, duration=1000
    )
    animation_move.animation_complete(on_animation_complete_1)
    animation_move.start()


ap.Stage(
    stage_width=200, stage_height=200, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)
animation_move.animation_complete(on_animation_complete_1)
animation_move.start()

ap.save_overall_html(dest_dir_path="./easing_enum_default_setting/")
```

<iframe src="static/easing_enum_default_setting/index.html" width="200" height="200"></iframe>

## イーズイン（ease-in）、イーズアウト（ease-out）、イーズインアウト（ease-in-out）の違い

- イーズイン（ease-in）は最初は遅くスタートし、最後の方で速いアニメーションになります。
- イーズアウト（ease-out）は最初は速いスピードでスタートし、最後の方で遅いアニメーションになります。

- イーズインアウト（ease-in-out）は最初と最後の両方が遅いスピードとなり、中間で一番速いアニメーションとなります。

以下のコード例では差が分かるように`EASE_IN_QUINT`、`EASE_OUT_QUINT`、`EASE_IN_OUT_QUINT`のそれぞれを表示しています。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_QUINT
EASING_2: ap.Easing = ap.Easing.EASE_OUT_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_IN_OUT_QUINT


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_difference/")
```

</details>

<iframe src="static/easing_enum_ease_difference/index.html" width="200" height="350"></iframe>

## イーズインの例

この節ではX座標のアニメーションにおける各イーズインの設定による例を表示しています。

以下のコード例では`EASE_IN_SINE`、`EASE_IN_QUAD`、`EASE_IN_CUBIC`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_SINE
EASING_2: ap.Easing = ap.Easing.EASE_IN_QUAD
EASING_3: ap.Easing = ap.Easing.EASE_IN_CUBIC


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_1/")
```

</details>

<iframe src="static/easing_enum_ease_in_1/index.html" width="200" height="350"></iframe>

以下のコード例では`EASE_IN_QUART`、`EASE_IN_QUINT`、`EASE_IN_EXPO`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_QUART
EASING_2: ap.Easing = ap.Easing.EASE_IN_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_IN_EXPO


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_2/")
```

</details>

<iframe src="static/easing_enum_ease_in_2/index.html" width="200" height="350"></iframe>

以下のコード例では`EASE_IN_CIRC`と`EASE_IN_BACK`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_CIRC
EASING_2: ap.Easing = ap.Easing.EASE_IN_BACK


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=250, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_3/")
```

</details>

<iframe src="static/easing_enum_ease_in_3/index.html" width="200" height="250"></iframe>

以下のコード例では`EASE_IN_ELASTIC`と`EASE_IN_BOUNCE`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_ELASTIC
EASING_2: ap.Easing = ap.Easing.EASE_IN_BOUNCE


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=250, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_4/")
```

</details>

<iframe src="static/easing_enum_ease_in_4/index.html" width="200" height="250"></iframe>

## イーズアウトの例

この節ではX座標のアニメーションにおける各イーズアウトの設定による例を表示しています。

以下のコード例では`EASE_OUT_SINE`、`EASE_OUT_QUAD`、`EASE_OUT_CUBIC`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_SINE
EASING_2: ap.Easing = ap.Easing.EASE_OUT_QUAD
EASING_3: ap.Easing = ap.Easing.EASE_OUT_CUBIC


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_out_1/")
```

</details>

<iframe src="static/easing_enum_ease_out_1/index.html" width="200" height="350"></iframe>

以下のコード例では`EASE_OUT_QUART`, `EASE_OUT_QUINT`, `EASE_OUT_EXPO`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_QUART
EASING_2: ap.Easing = ap.Easing.EASE_OUT_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_OUT_EXPO


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_out_2/")
```

</details>

<iframe src="static/easing_enum_ease_out_2/index.html" width="200" height="350"></iframe>

以下のコード例では`EASE_OUT_CIRC`と`EASE_OUT_BACK`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_CIRC
EASING_2: ap.Easing = ap.Easing.EASE_OUT_BACK


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=250, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_out_3/")
```

</details>

<iframe src="static/easing_enum_ease_out_3/index.html" width="200" height="250"></iframe>

以下のコード例では`EASE_OUT_ELASTIC`と`EASE_OUT_BOUNCE`の各値を設定しています。

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_OUT_ELASTIC
EASING_2: ap.Easing = ap.Easing.EASE_OUT_BOUNCE


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=250, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_out_4/")
```

</details>

<iframe src="static/easing_enum_ease_out_4/index.html" width="200" height="250"></iframe>

## イーズインアウトの例

この節ではX座標のアニメーションにおける各イーズインアウトの設定による例を表示しています。

以下の例では`EASE_IN_OUT_SINE`, `EASE_IN_OUT_QUAD`, `EASE_IN_OUT_CUBIC`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_OUT_SINE
EASING_2: ap.Easing = ap.Easing.EASE_IN_OUT_QUAD
EASING_3: ap.Easing = ap.Easing.EASE_IN_OUT_CUBIC


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_out_1/")
```

</details>

<iframe src="static/easing_enum_ease_in_out_1/index.html" width="200" height="350"></iframe>

以下のコード例では`EASE_IN_OUT_QUART`, `EASE_IN_OUT_QUINT`, `EASE_IN_OUT_EXPO`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_OUT_QUART
EASING_2: ap.Easing = ap.Easing.EASE_IN_OUT_QUINT
EASING_3: ap.Easing = ap.Easing.EASE_IN_OUT_EXPO


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=350, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_3.animation_x(x=x, duration=DURATION, easing=EASING_3)
options = {"easing": EASING_3}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_out_2/")
```

</details>

<iframe src="static/easing_enum_ease_in_out_2/index.html" width="200" height="350"></iframe>

以下のコード例では`EASE_IN_OUT_CIRC`と`EASE_IN_OUT_BACK`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_OUT_CIRC
EASING_2: ap.Easing = ap.Easing.EASE_IN_OUT_BACK


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=250, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_out_3/")
```

</details>

<iframe src="static/easing_enum_ease_in_out_3/index.html" width="200" height="250"></iframe>

以下のコード例では`EASE_IN_OUT_ELASTIC`と`EASE_IN_OUT_BOUNCE`の各値を設定しています:

<details>
<summary>コードブロックを表示:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _EasingOptions(TypedDict):
    easing: ap.Easing


DURATION: int = 1000
EASING_1: ap.Easing = ap.Easing.EASE_IN_OUT_ELASTIC
EASING_2: ap.Easing = ap.Easing.EASE_IN_OUT_BOUNCE


def on_animation_complete_1(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=50, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_2, options=options)
    animation_x.start()


def on_animation_complete_2(
    e: ap.AnimationEvent[ap.Rectangle], options: _EasingOptions
) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_x: ap.AnimationX = e.this.target.animation_x(
        x=100, duration=DURATION, easing=options["easing"]
    )
    animation_x.animation_complete(on_animation_complete_1, options=options)
    animation_x.start()


ap.Stage(
    stage_width=200, stage_height=250, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

x: int = 100
animation_x: ap.AnimationX = rectangle_1.animation_x(
    x=x, duration=DURATION, easing=EASING_1
)
options: _EasingOptions = {"easing": EASING_1}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

animation_x = rectangle_2.animation_x(x=x, duration=DURATION, easing=EASING_2)
options = {"easing": EASING_2}
animation_x.animation_complete(on_animation_complete_1, options=options)
animation_x.start()

ap.save_overall_html(dest_dir_path="./easing_enum_ease_in_out_4/")
```

</details>

<iframe src="static/easing_enum_ease_in_out_4/index.html" width="200" height="250"></iframe>