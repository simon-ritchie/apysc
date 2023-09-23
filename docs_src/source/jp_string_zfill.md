<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_zfill.html)の確認をお願いします。</span>

# String クラスの zfill メソッド

このページでは`String`クラスの`zfill`メソッドについて説明します。

## メソッド概要

`zfill`メソッドは指定された文字数でゼロ埋めされた文字列を返却します。

## 基本的な使い方

`zfill`メソッドは`width`引数を必要とします（`int`もしくは`ap.Int`型となります）。

その設定によって合計の文字数が決定します。

返却値はコピーされた`ap.String`型の値となります。

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String(value="1")
string = string.zfill(width=1)
ap.assert_equal(string, "1")

string = string.zfill(width=3)
ap.assert_equal(string, "001")

string = string.zfill(width=5)
ap.assert_equal(string, "00001")

ap.save_overall_html(dest_dir_path="string_zfill_basic_usage/")
```

<iframe src="static/string_zfill_basic_usage/index.html" width="0" height="0"></iframe>

## zfill メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `zfill(self, *, width: Union[int, ForwardRef('Int')]) -> 'String'`<hr>

**[インターフェイス概要]**

文字列の左側を0で埋めた文字列を返却します。<hr>

**[引数]**

- `width`: Union[int, "Int"]
  - 文字列の幅（長さ）。

<hr>

**[返却値]**

- `result`: String
  - 結果の文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _: ap.Stage = ap.Stage()
>>> string: ap.String = ap.String("1")
>>> string = string.zfill(width=1)
>>> string
String("1")

>>> string = string.zfill(width=3)
>>> string
String("001")

>>> string = string.zfill(width=5)
>>> string
String("00001")
```