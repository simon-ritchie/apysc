<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](return.md)の確認をお願いします。</span>

# Return クラス

このページでは`Return`クラスについて説明します。

このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscライブラリでは`Return`クラスを各データクラスと同じような理由で使用しています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Return クラスの概要

`Return`クラスはJavaScriptの`return;`のコードのように振る舞います。従って、このクラスはイベントハンドラの関数もしくはメソッド内のスコープでのみ使用することができます。

## 基本的な使い方

`Return`クラスのコンストラクタは引数を必要としません。このクラスは`ap.If`などの条件分岐の記述内などで使うことができます。

以下のコード例では四角をクリックするたびに塗りの色を変更しています。各`ap.If`での分岐内では`Return`クラスを使用しているため、1回のクリックでは1回の色変更のみ行われます:

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    fill_color: ap.String = rectangle.fill_color
    with ap.If(fill_color == '#00aaff'):
        rectangle.fill_color = ap.String('#ff00aa')
        ap.Return()
    with ap.If(fill_color == '#ff00aa'):
        rectangle.fill_color = ap.String('#00ffaa')
        ap.Return()
    with ap.If(fill_color == '#00ffaa'):
        rectangle.fill_color = ap.String('#00aaff')
        ap.Return()


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='return_basic_usage/')
```

<iframe src="static/return_basic_usage/index.html" width="150" height="150"></iframe>

## Return API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self) -> None`<hr>

**[インターフェイス概要]** return のコード表現のためのクラスです。<hr>

**[特記事項]**

このクラスはイベントハンドラのスコープ内でのみインスタンス化することができます。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     """
...     The handler that the timer calls.
...
```