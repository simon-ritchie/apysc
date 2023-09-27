<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_lower.html)の確認をお願いします。</span>

# String クラスの lower メソッド

このページでは`String`クラスの`lower`メソッドについて説明します。

## メソッド概要

`lower`メソッドは小文字に変換された文字列のコピーを返却します。

## 基本的な使い方

`lower`メソッドは引数を必要とせず、且つ`ap.String`型の値を返却します。

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
string: ap.String = ap.String("AbC1_")
string = string.lower()
ap.assert_equal(string, "abc1_")

ap.save_overall_html(dest_dir_path="string_lower_basic_usage/")
```

<iframe src="static/string_lower_basic_usage/index.html" width="0" height="0"></iframe>

## lower メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `lower(self) -> 'String'`<hr>

**[インターフェイス概要]**

小文字に変換された文字列のコピーを取得します。<hr>

**[返却値]**

- `string`: String
  - 小文字に変換された文字列のコピー。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("HELLO")
>>> string = string.lower()
>>> string
String("hello")
```