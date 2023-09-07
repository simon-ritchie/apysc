"""This module is for the translation mapping data of the
following document:

Document file: display_object_get_and_set_css.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject class get_css and set_css interfaces": "# DisplayObject クラスの get_css と set_css メソッドのインターフェイス",  # noqa
    ##################################################
    "This page will explain the `DisplayObject` class `get_css` and `set_css` method interfaces.": "このページでは`DisplayObject`クラスの`get_css`と`set_css`の各インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interfaces are these?": "## 各インターフェイスの概要",
    ##################################################
    "The `get_css` method will return a CSS string, and the `set_css` method will set the CSS setting to a `DisplayObject` instance.": "`get_css`メソッドは`DisplayObject`のインスタンスに設定されている特定のCSSの文字列を返却し、`set_css`メソッドは特定のCSSの値を設定します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each interface requires the `name` argument as the CSS name. In addition, the `set_css` method interface also requires the `value` argument as the CSS value string.": "各インターフェイスはCSS名としての`name`引数の指定を必要とします。加えて、`set_css`メソッドではCSSの値の文字列としての`value`引数が必要になります。",  # noqa
    ##################################################
    "The following example sets the `none` value to the `display` CSS if the current CSS value is the default (blank string, `''`). Otherwise, revert the value to default (`Else` case) by the timer event (ticks every second).": "以下のコード例では1秒ごとのタイマーでCSSの`display`の値がもしデフォルトの空文字になっていれば`none`の値を設定しています。デフォルト値以外の値になっていればデフォルトの値へと戻しています。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _SpriteOptions(TypedDict):\n    sprite: ap.Sprite\n\n\ndef on_timer(e: ap.TimerEvent, options: _SpriteOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = options["sprite"]\n    display_css_val: ap.String = sprite.get_css(name="display")\n    condition: ap.Boolean = display_css_val == "none"\n    with ap.If(condition):\n        sprite.set_css(name="display", value="")\n    with ap.Else():\n        sprite.set_css(name="display", value="none")\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _SpriteOptions = {"sprite": sprite}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="display_object_get_and_set_css_basic_usage/")\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _SpriteOptions(TypedDict):\n    sprite: ap.Sprite\n\n\ndef on_timer(e: ap.TimerEvent, options: _SpriteOptions) -> None:\n    """\n    The handler that the timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    sprite: ap.Sprite = options["sprite"]\n    display_css_val: ap.String = sprite.get_css(name="display")\n    condition: ap.Boolean = display_css_val == "none"\n    with ap.If(condition):\n        sprite.set_css(name="display", value="")\n    with ap.Else():\n        sprite.set_css(name="display", value="none")\n\n\nap.Stage(\n    stage_width=150,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\noptions: _SpriteOptions = {"sprite": sprite}\ntimer: ap.Timer = ap.Timer(handler=on_timer, delay=1000, options=options)\ntimer.start()\n\nap.save_overall_html(dest_dir_path="display_object_get_and_set_css_basic_usage/")\n```',  # noqa
    ##################################################
    "## get_css API": "## get_css API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a CSS value string.<hr>": "CSSの設定値の文字列を取得します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `name`: str or String": "- `name`: str or String",
    ##################################################
    "  - CSS name (e.g., 'display').": "  - CSS名（例 : 'display'）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `css`: ap.String": "- `css`: ap.String",
    ##################################################
    "  - CSS value.": "  - CSSの値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> sprite.set_css(name="display", value="none")\n>>> sprite.get_css(name="display")\nString("none")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> sprite.set_css(name="display", value="none")\n>>> sprite.get_css(name="display")\nString("none")\n```',  # noqa
    ##################################################
    "## set_css API": "## set_css API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set a specified value string to the CSS.<hr>": "CSSに指定された文字列の値を設定します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `name`: str or String": "- `name`: str or String",
    ##################################################
    "  - CSS name (e.g., 'display').": "  - CSS名（例 : 'display'）。",
    ##################################################
    "- `value`: str or String": "- `value`: str or String",
    ##################################################
    "  - A CSS value string (e.g., 'none').": "  - CSSの値の文字列（例 : 'none'）",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> sprite.set_css(name="display", value="none")\n>>> sprite.get_css(name="display")\nString("none")\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)\n>>> sprite.set_css(name="display", value="none")\n>>> sprite.get_css(name="display")\nString("none")\n```',  # noqa
}
