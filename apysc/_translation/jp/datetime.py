"""This module is for the translation mapping data of the
following document:

Document file: datetime.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class": "# DateTime クラス",
    ##################################################
    "This page explains the `DateTime` class.": "このページでは`DateTime`クラスについて説明します。",
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `DateTime` class is a class to handle each date- and time-related interface.": "`DateTime`クラスは日付と時間かんけぽの各インターフェイスを扱うためのクラスです。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The constructor requires the `year`, `month`, and `day` arguments, as follows:": "コンストラクタの引数では`year`、`month`、`day`の各引数の指定を必要とします。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\n```": "```py\n# runnable\nimport apysc as ap\n\ndt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\n```",  # noqa
    ##################################################
    "Also, it has the optional `hour`, `minute`, `second`, and `millisecond` arguments:": "また、省略可能な引数として`hour`、`minute`、`second`の引数を指定することもできます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndt: ap.DateTime = ap.DateTime(\n    year=2022, month=12, day=5, hour=10, minute=30, second=50, millisecond=500\n)\n```": "```py\n# runnable\nimport apysc as ap\n\ndt: ap.DateTime = ap.DateTime(\n    year=2022, month=12, day=5, hour=10, minute=30, second=50, millisecond=500\n)\n```",  # noqa
    ##################################################
    "Each value has a getter and setter interface.": "各値はgetterとsetterのインターフェイスを持っています。",  # noqa
    ##################################################
    "For instance, the `month` value can get or set via the properties:": "例えば`month`属性であれば以下のように属性経由で値の取得や更新を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\nassert dt.month == 12\ndt.month = ap.Int(10)\nassert dt.month == 10\n```": "```py\n# runnable\nimport apysc as ap\n\ndt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)\nassert dt.month == 12\ndt.month = ap.Int(10)\nassert dt.month == 10\n```",  # noqa
    ##################################################
    "Notes: the `weekday_py` and `weekday_js` properties only have a getter interface.": "特記事項: `weekday_py`と`weekday_js`属性はgetterのインターフェイスのみ存在します。",  # noqa
    ##################################################
    "For more information about the other properties, please see the followings:": "他の属性の詳細に関しては以下のを参照してください:",  # noqa
    ##################################################
    "- [DateTime class year property](datetime_year.md)": "- [DateTime クラスの year 属性](jp_datetime_year.md)",  # noqa
    ##################################################
    "- [DateTime class month property](datetime_month.md)": "- [DateTime クラスの month 属性](jp_datetime_month.md)",  # noqa
    ##################################################
    "- [DateTime class day property](datetime_day.md)": "- [DateTime クラスの day 属性](jp_datetime_day.md)",  # noqa
    ##################################################
    "- [DateTime class hour property](datetime_hour.md)": "- [DateTime クラスの hour 属性](jp_datetime_hour.md)",  # noqa
    ##################################################
    "- [DateTime class minute property](datetime_minute.md)": "- [DateTime クラスの minute 属性](jp_datetime_minute.md)",  # noqa
    ##################################################
    "- [DateTime class second property](datetime_second.md)": "- [DateTime クラスの second 属性](jp_datetime_second.md)",  # noqa
    ##################################################
    "- [DateTime class millisecond property](datetime_millisecond.md)": "- [DateTime クラスの millisecond 属性](jp_datetime_millisecond.md)",  # noqa
    ##################################################
    "- [DateTime class weekday_js and weekday_py properties](datetime_weekday_js_and_weekday_py.md)": "- [DateTime クラスの weekday_js と weekday_py 属性](jp_datetime_weekday_js_and_weekday_py.md)",  # noqa
    ##################################################
    "Also, the `DateTime` class has each method interface, such as the `now` class method.": "また、`DateTime`クラスは`now`のクラスメソッドのような各メソッドのインターフェイスを持っています。",  # noqa
    ##################################################
    "For more information about the methods interfaces, please see the following:": "メソッドの各インターフェイスの詳細は以下を参照してください。",  # noqa
    ##################################################
    "- [DateTime class now interface](datetime_now.md)": "- [DateTime クラスの now インターフェイス](jp_datetime_now.md)",  # noqa
    ##################################################
    "## DateTime class constructor API": "## DateTime クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The class for datetime-related interfaces.<hr>": "日時に絡んだインターフェイスのためのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `year`: Union[int, Int]": "- `year`: Union[int, Int]",
    ##################################################
    "  - Four-digit year.": "  - 4桁の数字の年。",
    ##################################################
    "- `month`: Union[int, Int]": "- `month`: Union[int, Int]",
    ##################################################
    "  - Two-digit month (1 to 12).": "  - 2桁の月（1～12）。",
    ##################################################
    "- `day`: Union[int, Int]": "- `day`: Union[int, Int]",
    ##################################################
    "  - Two-digit day (1 to 31).": "  - 2桁の日（1～31）。",
    ##################################################
    "- `hour`: Optional[Union[int, Int]], optional": "- `hour`: Optional[Union[int, Int]], optional",  # noqa
    ##################################################
    "  - Two-digit hour (0 to 23).": "  - 2桁の時（0～23）。",
    ##################################################
    "- `minute`: Optional[Union[int, Int]], optional": "- `minute`: Optional[Union[int, Int]], optional",  # noqa
    ##################################################
    "  - Two-digit minute (0 to 59).": "  - 2桁の分（0～59）。",
    ##################################################
    "- `second`: Optional[Union[int, Int]], optional": "- `second`: Optional[Union[int, Int]], optional",  # noqa
    ##################################################
    "  - Two-digit second (0 to 59).": "  - 2桁の秒（0～59）。",
    ##################################################
    "- `millisecond`: Optional[Union[int, Int]], optional": "- `millisecond`: Optional[Union[int, Int]], optional",  # noqa
    ##################################################
    "  - Millisecond (0 to 999).": "  - ミリ秒（0～999）",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "- `skip_init_substitution_expression_appending`: bool, default False": "- `skip_init_substitution_expression_appending`: bool, default False",  # noqa
    ##################################################
    "  - A boolean indicates whether to skip an initial substitution expression or not. The `DateTime` class uses this option internally.": "  - 初期値の代入表現の追加をスキップするかどうかの真偽値。`DateTime`クラスでは内部でのみこのオプションを使用します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(\n...     year=2022,\n...     month=12,\n...     day=5,\n...     hour=10,\n...     minute=30,\n...     second=50,\n...     millisecond=500,\n... )\n>>> datetime_.year\nInt(2022)\n\n>>> datetime_.month\nInt(12)\n\n>>> datetime_.day\nInt(5)\n\n>>> datetime_.hour\nInt(10)\n\n>>> datetime_.minute\nInt(30)\n\n>>> datetime_.millisecond\nInt(500)\n\n>>> datetime_.weekday_py\nInt(0)\n\n>>> datetime_.weekday_js\nInt(1)\n```": "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(\n...     year=2022,\n...     month=12,\n...     day=5,\n...     hour=10,\n...     minute=30,\n...     second=50,\n...     millisecond=500,\n... )\n>>> datetime_.year\nInt(2022)\n\n>>> datetime_.month\nInt(12)\n\n>>> datetime_.day\nInt(5)\n\n>>> datetime_.hour\nInt(10)\n\n>>> datetime_.minute\nInt(30)\n\n>>> datetime_.millisecond\nInt(500)\n\n>>> datetime_.weekday_py\nInt(0)\n\n>>> datetime_.weekday_js\nInt(1)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [DateTime class year property](https://simon-ritchie.github.io/apysc/en/datetime_year.html)": "- [DateTime クラスの year 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_year.html)",  # noqa
    ##################################################
    "- [DateTime class month property](https://simon-ritchie.github.io/apysc/en/datetime_month.html)": "- [DateTime クラスの month 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_month.html)",  # noqa
    ##################################################
    "- [DateTime class day property](https://simon-ritchie.github.io/apysc/en/datetime_day.html)": "- [DateTime クラスの day 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_day.html)",  # noqa
    ##################################################
    "- [DateTime class hour property](https://simon-ritchie.github.io/apysc/en/datetime_hour.html)": "- [DateTime クラスの hour 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_hour.html)",  # noqa
    ##################################################
    "- [DateTime class minute property](https://simon-ritchie.github.io/apysc/en/datetime_minute.html)": "- [DateTime クラスの minute 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_minute.html)",  # noqa
    ##################################################
    "- [DateTime class second property](https://simon-ritchie.github.io/apysc/en/datetime_second.html)": "- [DateTime クラスの second 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_second.html)",  # noqa
    ##################################################
    "- [DateTime class millisecond property](https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html)": "- [DateTime クラスの millisecond 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_millisecond.html)",  # noqa
    ##################################################
    "- [DateTime class weekday_js and weekday_py properties](https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html)": "- [DateTime クラスの weekday_js と weekday_py 属性](https://simon-ritchie.github.io/apysc/jp/jp_datetime_weekday_js_and_weekday_py.html)",  # noqa
    ##################################################
    "- [DateTime class now interface](https://simon-ritchie.github.io/apysc/en/datetime_now.html)": "- [DateTime クラスの now インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_datetime_now.html)",  # noqa
}
