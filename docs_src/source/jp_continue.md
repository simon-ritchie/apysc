<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/continue.html)の確認をお願いします。</span>

# Continue クラス

このページでは`Continue`クラスについて説明します。

このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscでは`Continue`クラスを同様の利用で使用しています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## Continue クラスの概要

`with For`のブロックではJavaScript上での特定のループをスキップするために`Continue`クラスが使用されます。このインターフェイスはPythonビルトインの`continue`キーワードのように動作します。

## 基本的な使い方

`Continue`クラスは以下のコード例のように`with For`（もしくは他のループクラス）のブロックでのみ使用することができます:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

arr: ap.Array = ap.Array(range(2))
i: ap.Int
with ap.For(arr) as i:
    condition: ap.Boolean = i == 0
    with ap.If(condition):
        sprite.graphics.begin_fill(color="#0af")
        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
        ap.Continue()

    sprite.graphics.begin_fill(color="#f0a")
    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="continue_basic_usage/")
```

<iframe src="static/continue_basic_usage/index.html" width="250" height="150"></iframe>

もし`Continue`クラスを`with For`ブロック外で使用した場合はエラーになります:

```py
import apysc as ap

ap.Continue()
```

```
Exception: The `Continue` class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.
```

## Continue API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self) -> None`<hr>

**[インターフェイス概要]** ループ上のcontinue表現のためのクラスです。<hr>

**[特記事項]**

このクラスはwithステートメントのループ内でのみインスタンス化することができます。例えば`with ap.For(...)ステート内が該当します。`<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     with ap.If(i == 1):
...         _ = ap.Continue()
...
```