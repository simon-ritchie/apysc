"""This module is for the translation mapping data of the
following document:

Document file: display_object.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DisplayObject class": "# DisplayObject クラス",
    ##################################################
    "This page explains the `DisplayObject` class.": "このページでは`DisplayObject`クラスについて説明します。",  # noqa
    ##################################################
    "## What is the DisplayObject?": "## DisplayObject クラスの概要",
    ##################################################
    "The `DisplayObject` is the apysc base class for each display class, such as  `Sprite`, `Rectangle`, `Circle`, or something else.": "`DisplayObject`クラスは`Sprite`や`Rectangle`などのapyscの表示オブジェクトの基底クラスとなります。",  # noqa
    ##################################################
    "You can verify the `DisplayObject` inheritance with each instance by the `isinstance` function.": "各インスタンスが`DisplayObject`を継承していることを`isinstance`関数を使って確認することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\n\n# Verify each instance type.\nassert isinstance(sprite, ap.DisplayObject)\nassert isinstance(circle, ap.DisplayObject)\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id="stage",\n)\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=ap.Color("#0af"))\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\n\n# Verify each instance type.\nassert isinstance(sprite, ap.DisplayObject)\nassert isinstance(circle, ap.DisplayObject)\n```',  # noqa
    ##################################################
    "The apysc uses this class for basic interfaces or creates a new `DisplayObject` instance with the `DisplayObject` inheritance.": "apyscはこのクラスを基本的な共通のインターフェイスで使用したり、もしくは別の`DisplayObject`を継承したインスタンスの作成処理などで使用しています。",  # noqa
    ##################################################
    "The `DisplayObject` class has the basic interfaces, like `x`, `y`, `visible`, each mouse event binding, or others. The following page explains these interfaces one by one.": "`DisplayObject`クラスは`x`や`y`、`visible`属性、各マウスイベントの設定などの基本的なインターフェイスを持っています。以下のページではそれぞれのインターフェイスについて1つ1つ詳しく触れています。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [DisplayObject class x and y interfaces](display_object_x_and_y.md)": "- [DisplayObject クラスの x と y インターフェイス](jp_display_object_x_and_y.md)",  # noqa
    ##################################################
    "- [DisplayObject class parent interfaces](display_object_parent.md)": "- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)",  # noqa
    ##################################################
    "- [DisplayObject class visible interface](display_object_visible.md)": "- [DisplayObject クラスの visible (表示・非表示) のインターフェイス](jp_display_object_visible.md)",  # noqa
    ##################################################
    "- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)": "- [DisplayObject クラスのマウスイベント設定の各インターフェイス](jp_display_object_mouse_event.md)",  # noqa
}
