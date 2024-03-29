<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_rstrip.html)の確認をお願いします。</span>

# String クラスの rstrip インターフェイス

このページでは`String`クラスの`rstrip`メソッドインターフェイスについて説明します。

## インターフェイス概要

`rstrip`メソッドのインターフェイスは文字列の右端から空白文字もしくは指定された文字（または文字列）を取り除きます。

## 基本的な使い方

`rstrip`メソッドは省略可能な`string`引数を受け付けます。

もしこの引数の指定を省略した場合、文字列の右端から空白文字や改行などを取り除きます。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String("  aabbccaa  
 ")
string = string.rstrip()
ap.assert_equal(string, "  aabbccaa")

ap.save_overall_html(dest_dir_path="string_rstrip_basic_usage_1/")
```

<iframe src="static/string_rstrip_basic_usage_1/index.html" width="0" height="0"></iframe>

また、もし`string`引数に何らかの値を指定した場合、このインターフェイスは文字列の右端から指定された文字もしくは文字列を取り除きます。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

string: ap.String = ap.String("aabbccaa")
string = string.rstrip(string="a")
ap.assert_equal(string, "aabbcc")

ap.save_overall_html(dest_dir_path="string_rstrip_basic_usage_2/")
```

<iframe src="static/string_rstrip_basic_usage_2/index.html" width="0" height="0"></iframe>

## rstrip API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `rstrip(self, *, string: Union[str, ForwardRef('String'), NoneType] = None, variable_name_suffix: str = '') -> 'String'`<hr>

**[インターフェイス概要]**

この値の右端から指定された文字もしくは文字列を取り除きます。<hr>

**[引数]**

- `string`: Optional[Union[str, "String"]], optional
  - この値の右端から取り除く文字もしくは文字列。もしこの引数に`None`（デフォルト値）を指定した場合、このメソッドはスペースや改行などを取り除きます。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `result`: String
  - 除外処理実行後の文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("  aabbcc   ")
>>> string = string.rstrip()
>>> string
String("  aabbcc")

>>> string = ap.String("aabbccaa")
>>> string = string.rstrip(string="a")
>>> string
String("aabbcc")
```