"""This module is for the translation mapping data of the
following document:

Document file: datetime_set_month_end.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class set_month_end interface": "# DateTime クラスの set_month_end インターフェイス",  # noqa
    ##################################################
    "This page explains the `DateTime` class's `set_month_end` method interface.": "このページでは`DateTime`クラスの`set_month_end`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `set_month_end` method interface sets the current month's end date.": "`set_month_end`メソッドのインターフェイスでは現在の月の月末の日付を設定します。",  # noqa
    ##################################################
    "For instance, if the current date is 05/12/2022, this method sets 31/12/2022.": "例えば、もし現在の日付が2022-12-05であればこのメソッドによって2022-12-31が設定されます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "This method interface requires no arguments.": "このメソッドでは引数を必要としません。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\ndatetime_.set_month_end()\nassert datetime_.day == 31\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\ndatetime_.set_month_end()\nassert datetime_.day == 31\n```",  # noqa
}
