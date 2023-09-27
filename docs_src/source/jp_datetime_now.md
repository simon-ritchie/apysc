<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/datetime_now.html)の確認をお願いします。</span>

# DateTime クラスの now インターフェイス

このページでは`DateTime`クラスの`now`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`DateTime`クラスの`now`のクラスメソッドは現在の時間での`DateTime`のインスタンスを返却します。

## 基本的な使い方

`DateTime`クラスはクラスメソッドとして定義された`now`メソッドを持っています。

そのインターフェイスでは各値に現在時刻が設定された`DateTime`クラスのインスタンスを返却します。

以下のコード例では、四角をクリックするとブラウザのコンソール上に現在の年月日を表示します。

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent, options: dict) -> None:
    """
    The handler to handle a rectangle's click event.

    Parameters
    ----------
    e : ap.MouseEvent
        An event instance.
    options : dict
        Optional arguments dictionary.
    """
    now_datetime: ap.DateTime = ap.DateTime.now()
    ap.trace("Current year:", now_datetime.year)
    ap.trace("Current month:", now_datetime.month)
    ap.trace("Current day:", now_datetime.day)


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#0af"),
)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="datetime_now_basic_usage/")
```

<iframe src="static/datetime_now_basic_usage/index.html" width="150" height="150"></iframe>

## now のクラスメソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `now(*, variable_name_suffix: str = '') -> 'DateTime'`<hr>

**[インターフェイス概要]**

現在時刻が設定された`DateTime`クラスのインスタンスを取得します。<hr>

**[引数]**

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `dt`: DateTime
  - 生成された`DateTime`クラスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> from datetime import datetime
>>> import apysc as ap
>>> _ = ap.Stage()
>>> py_now: datetime = datetime.now()
>>> ap_now: ap.DateTime = ap.DateTime.now()
>>> ap_now.year == py_now.year
Boolean(True)

>>> ap_now.month == py_now.month
Boolean(True)

>>> ap_now.day == py_now.day
Boolean(True)
```