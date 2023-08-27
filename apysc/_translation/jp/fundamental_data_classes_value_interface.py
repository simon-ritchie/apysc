"""This module is for the translation mapping data of the
following document:

Document file: fundamental_data_classes_value_interface.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# apysc fundamental data classes value interface": "# apysc の基本的なデータ型の value インターフェイス",  # noqa
    ##################################################
    "This page explains the apysc fundamental data classes (such as the `Int`\\, `Number`\\, `String`) `value` interface.": "このページではapyscの`Int`や`Number`、`String`などの基本的なデータクラスの`value`インターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `value` getter interface returns each data class value, and the setter interface updates these data class values.": "`value`のgetterのインターフェイスは各データクラスの値を返却します。setterのインターフェイスではそれらの値の更新を行います。",  # noqa
    ##################################################
    "A return value of the getter interface becomes a Python built-in value, like the `int`, `float`, `str`, `list`.": "返却値は基本的に`int`や`float`、`str`などのPythonビルトインの値になります。",  # noqa
    ##################################################
    "## Basic usage of the getter interface": "## getterのインターフェイスの基本的な使い方",
    ##################################################
    "The `value` getter interface returns the Python built-in value.": "`value`のgetterインターフェイスではPythonのビルトインの値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nvalue = int_1.value\nassert isinstance(value, int)\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nvalue = int_1.value\nassert isinstance(value, int)\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nnumber_1: ap.Number = ap.Number(10.5)\nvalue = number_1.value\nassert isinstance(value, float)\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nnumber_1: ap.Number = ap.Number(10.5)\nvalue = number_1.value\nassert isinstance(value, float)\n```",  # noqa
    ##################################################
    "## Basic usage of the setter interface": "## setterのインターフェイスの基本的な使い方",
    ##################################################
    "You can update the apysc fundamental data class values with the `value` setter interface. Python built-in values and the same type value is acceptable:": "apyscの基本的なデータクラスにおける`value`のsetterのインターフェイスではそれらの値を更新することができます。Pythonのビルトインの値やapyscの同じ型の値を指定することができます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1.value = 20\nassert int_1 == 20\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1.value = 20\nassert int_1 == 20\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1.value = ap.Int(20)\nassert int_1 == 20\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1.value = ap.Int(20)\nassert int_1 == 20\n```",  # noqa
}
