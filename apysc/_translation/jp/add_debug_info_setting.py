"""This module is for the translation mapping data of the
following document:

Document file: add_debug_info_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# add_debug_info_setting decorator interface": "# add_debug_info_setting のデコレーターのインターフェイス",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `add_debug_info_setting` decorator interface sets the debug information settings to a target function or method.": "`add_debug_info_setting`のデコレーターのインターフェイスは対象の関数もしくはメソッドへとデバッグ情報の設定を行います。",  # noqa
    ##################################################
    "A decorated function or method exports debug information when you enable the debug mode setting.": "デコレーターが設定された関数もしくはメソッドでは、デバッグモードを有効にした後の処理では各デバッグ情報を出力するようになります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "It is necessary to set the debug mode setting with the `ap.set_debug_mode()` function at the first position.": "処理の有効にするために最初に`ap.set_debug_mode()`関数でデバッグモードの設定を行っておく必要があります。",  # noqa
    ##################################################
    "After that, You can set the `@ap.add_debug_info_setting` decorator settings to any function or method.": "その後、任意の各関数やメソッドに`@ap.add_debug_info_setting`のデコレーターの設定を追加することができます。",  # noqa
    ##################################################
    "The `@ap.add_debug_info_setting` needs to specify the `module_name` (this value becomes `__name__`).": "`@ap.add_debug_info_setting`の関数は`module_name`引数の指定が必要になります（この引数は基本的に`__name__`の値となります）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef _main() -> None:\n    """The entry point of this project."""\n    ap.Stage(\n        background_color="#333",\n        stage_width=150,\n        stage_height=150,\n        stage_elem_id="stage",\n    )\n    ap.set_debug_mode()\n    _draw_rectangle(x=50, y=50)\n    ap.save_overall_html(dest_dir_path="add_debug_info_setting_basic_usage/")\n\n\n@ap.add_debug_info_setting(module_name=__name__)\ndef _draw_rectangle(*, x: float, y: float) -> None:\n    """\n    Draw a rectangle with the given coordinates and sprite\n    container class.\n\n    Parameters\n    ----------\n    x : float\n        X-coordinate of the rectangle.\n    y : float\n        Y-coordinate of the rectangle.\n    """\n    _: MySprite = MySprite(x=x, y=y)\n\n\nclass MySprite(ap.Sprite):\n    @ap.add_debug_info_setting(module_name=__name__)\n    def __init__(self, *, x: int, y: int) -> None:\n        """\n        My rectangle\'s sprite container class.\n\n        Parameters\n        ----------\n        x : float\n            X-coordinate of the rectangle.\n        y : float\n            Y-coordinate of the rectangle.\n        """\n        super(MySprite, self).__init__()\n        self.graphics.begin_fill(color="#0af")\n        self.graphics.draw_rect(x=x, y=y, width=50, height=50)\n\n\nif __name__ == "__main__":\n    _main()\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef _main() -> None:\n    """The entry point of this project."""\n    ap.Stage(\n        background_color="#333",\n        stage_width=150,\n        stage_height=150,\n        stage_elem_id="stage",\n    )\n    ap.set_debug_mode()\n    _draw_rectangle(x=50, y=50)\n    ap.save_overall_html(dest_dir_path="add_debug_info_setting_basic_usage/")\n\n\n@ap.add_debug_info_setting(module_name=__name__)\ndef _draw_rectangle(*, x: float, y: float) -> None:\n    """\n    Draw a rectangle with the given coordinates and sprite\n    container class.\n\n    Parameters\n    ----------\n    x : float\n        X-coordinate of the rectangle.\n    y : float\n        Y-coordinate of the rectangle.\n    """\n    _: MySprite = MySprite(x=x, y=y)\n\n\nclass MySprite(ap.Sprite):\n    @ap.add_debug_info_setting(module_name=__name__)\n    def __init__(self, *, x: int, y: int) -> None:\n        """\n        My rectangle\'s sprite container class.\n\n        Parameters\n        ----------\n        x : float\n            X-coordinate of the rectangle.\n        y : float\n            Y-coordinate of the rectangle.\n        """\n        super(MySprite, self).__init__()\n        self.graphics.begin_fill(color="#0af")\n        self.graphics.draw_rect(x=x, y=y, width=50, height=50)\n\n\nif __name__ == "__main__":\n    _main()\n```',  # noqa
    ##################################################
    "The exported HTML contains the following debug information (function and method calling information):": "出力されたHTMLには以下のように関数やメソッドの呼び出しなどのデバッグ情報が含まれるようになります:",  # noqa
    ##################################################
    "```\n...\n  //////////////////////////////////////////////////////////////////////\n  // [_draw_rectangle 1] started.\n  // module name: __main__\n  // Keyword arguments: {'x': 50, 'y': 50}\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 1] started.\n    // module name: __main__\n    // class: MySprite\n    // Positional arguments: [Sprite('')]\n    // Keyword arguments: {'x': 50, 'y': 50}\n...\n```": "```\n...\n  //////////////////////////////////////////////////////////////////////\n  // [_draw_rectangle 1] started.\n  // module name: __main__\n  // Keyword arguments: {'x': 50, 'y': 50}\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 1] started.\n    // module name: __main__\n    // class: MySprite\n    // Positional arguments: [Sprite('')]\n    // Keyword arguments: {'x': 50, 'y': 50}\n...\n```",  # noqa
    ##################################################
    "## Notes of the mypy setting": "## mypy設定に対する特記事項",
    ##################################################
    "This decorator settings currently raise a mypy error. To avoid this error, please set the `--disable-error-code misc` option.": "このデコレーター設定は現在mypy上でエラーが発生します。ごのエラーを避けるためには`--disable-error-code misc`オブションの指定の追加を検討してください。",  # noqa
    ##################################################
    "See also:": "参考資料:",
    ##################################################
    "- [Recommended type annotation checker settings](recommended_type_checker_settings.md)": "- [推奨される型アノテーションのチェック設定](jp_recommended_type_checker_settings.md)",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [set_debug_mode interface](set_debug_mode.md)": "- [set_debug_mode インターフェイス](jp_set_debug_mode.md)",  # noqa
    ##################################################
    "- [unset_debug_mode interface](unset_debug_mode.md)": "- [unset_debug_mode インターフェイス](jp_unset_debug_mode.md)",  # noqa
}
