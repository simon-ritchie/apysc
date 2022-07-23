<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/trace.html)の確認をお願いします。</span>

# trace インターフェイス

このページでは`trace`関数のインターフェイスについて説明します。

## インターフェイス概要

`trace`関数のインターフェイスは任意のメッセージをブラウザのコンソール上に表示します。このインターフェイスはJavaScriptの`console.log`の関数と同じような挙動をします。

## 基本的な使い方

`trace`関数は任意の数の引数を受け付け、そして様々な型の値を指定することができます。

伊賀のコード例では四角を描画し、四角をクリックした際にブラウザのコンソール上にメッセージを表示するようにしています（F12キーを押してコンソールを開いてご確認ください）。

```py
# runnable
import apysc as ap


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Hello apysc!", "Rectangle width:", e.this.width)


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(dest_dir_path="trace_basic_usage/")
```

<iframe src="static/trace_basic_usage/index.html" width="150" height="150"></iframe>

## trace API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `trace(*args: Any) -> None`<hr>

**[インターフェイス概要]** 引数に指定された値の情報をコンソールへ表示します。この関数はJavaScriptの`console.log`に該当するコードを保存します。<hr>

**[引数]**

- `*args`: list
  - コンソール上に表示する任意の引数の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.trace('Int value is:', int_val)
```