<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/int_and_number_to_hex.html)の確認をお願いします。</span>

# Int と Number クラスの to_hex メソッド

このページでは`Int`と`Number`クラスの`to_hex`メソッドについて説明します。

## メソッド概要

`to_hex`メソッドは`ap.Int`や`ap.Number`型の値から16進数の文字列（例 : "1f"）を返却します。

## `ap.Number`型の値における特記事項

`ap.Number`の値でこのメソッドを使った場合浮動小数点数の値は無視されます。

## 基本的な使い方

`to_hex`メソッドは引数の指定を必要としません。

このメソッドは16進数の文字列（`ap.String`型の値）を返却します。

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
int_value: ap.Int = ap.Int(28)
hex_str: ap.String = int_value.to_hex()
ap.assert_equal(hex_str, "1c")

number: ap.Number = ap.Number(28.5)
hex_str = int_value.to_hex()
ap.assert_equal(hex_str, "1c")

ap.save_overall_html(dest_dir_path="int_and_number_to_hex_basic_usage/")
```

<iframe src="static/to_fixed_basics_usage/index.html" width="0" height="0"></iframe>

## to_hex メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `to_hex(self, *, variable_name_suffix: str = '') -> apysc._type.string.String`<hr>

**[インターフェイス概要]**

16進数の文字列（例 : "1f"）を取得します。<hr>

**[引数]**

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `hex_str`: String
  - 16進数の文字列（例 : "1f"）

<hr>

**[特記事項]**

このメソッドは浮動小数点数を無視します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> int_value: ap.Int = ap.Int(28)
>>> hex_str: ap.String = int_value.to_hex()
>>> hex_str
String("1c")

>>> number: ap.Number = ap.Number(28.5)
>>> hex_str = int_value.to_hex()
>>> hex_str
String("1c")
```