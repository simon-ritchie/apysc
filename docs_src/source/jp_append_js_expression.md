<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/append_js_expression.html)の確認をお願いします。</span>

# append_js_expression インターフェイス

このページでは`append_js_expression`関数のインターフェイスについて説明します。

## インターフェイス概要

`append_js_expression`関数は出力先のHTMLの任意の場所にJavaScriptのコードを追加します。このインターフェイスはapyscがサポートしていない特殊な処理などを追加する際などに役に立つことがあります（Djangoなどのライブラリでテンプレートタグなどを独自の出力したい場合など）。

## 基本的な使い方

`append_js_expression`関数は引数にJavaScriptのコードの文字列が必要とします。

以下のコード例では四角をクリックした際のハンドラ内で`console.log`のJavaScriptの関数呼び出しのコードを追加しています。

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.append_js_expression(
        expression='console.log("The rectangle is clicked!");')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='append_js_expression_basic_usage/')
```

四角をクリックすると`The rectangle is clicked!`というメッセージがブラウザのコンソールに表示されます（F12キーを押して確認してください）。

<iframe src="static/append_js_expression_basic_usage/index.html" width="150" height="150"></iframe>

## append_js_expression API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `append_js_expression(expression:str) -> None`<hr>

**[インターフェイス概要]** JavaScriptのコード表現の記述を結果のHTMLへ追加します。<hr>

**[引数]**

- `expression`: str
  - 追加対象のJavaScriptのコードの文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> ap.append_js_expression(expression='console.log("Hello!")')
```