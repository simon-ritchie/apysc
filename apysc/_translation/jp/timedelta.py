"""This module is for the translation mapping data of the
following document:

Document file: timedelta.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# TimeDelta class": "# TimeDelta クラス",
    ##################################################
    "This page explains the `TimeDelta` class.": "このページでは`TimeDelta`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `TimeDelta` class treats a time delta between two `DateTime` instances.": "`TimeDelta`クラスは2つの`DateTime`クラスのインスタンス間の時間差を扱います。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Subtraction between two `DateTime` instances returns this class\'s instance.": "2つの`DateTime`クラスのインスタンス間の減算はこのクラスのインスタンスを返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\n```",  # noqa
    ##################################################
    "A `TimeDelta` instance has each interface, such as the `days`\' property or `total_seconds`\' method, as follows:": "`TimeDelta`クラスのインスタンスは以下のように`days`属性や`total_seconds`メソッドなどの各インターフェイスを持っています:",  # noqa
    ##################################################
    "```\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ndays: ap.Int = timedelta_.days\nassert days == 2\ntotal_seconds: ap.Number = timedelta_.total_seconds()\nassert total_seconds == 60 * 60 * 24 * 2\n```": "```\n# runnable\nimport apysc as ap\n\ndatetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)\ndatetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)\ntimedelta_: ap.TimeDelta = datetime_1 - datetime_2\ndays: ap.Int = timedelta_.days\nassert days == 2\ntotal_seconds: ap.Number = timedelta_.total_seconds()\nassert total_seconds == 60 * 60 * 24 * 2\n```",  # noqa
}
