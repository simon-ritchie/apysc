<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_apply_max_num_of_decimal_places.html)の確認をお願いします。</span>

# String クラスの apply_max_num_of_decimal_places インターフェイス

このページでは`String`クラスの`apply_max_num_of_decimal_places`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`apply_max_num_of_decimal_places`メソッドは文字列に対して浮動小数点数の最大桁数の条件を反映します。

例えば、もし文字列が`123.45678`で小数点数の最大桁数が`3`だった場合、このインターフェイスは`123.456`の文字列を返却します。

もしも文字列が浮動小数点数のフォーマットではない場合、このインターフェイスは元の文字列をそのまま返却します。

## 基本的な使い方

`apply_max_num_of_decimal_places`は`max_num_of_decimal_places`（浮動小数点数の最大桁数、`int`もしくは`Int`型）引数の指定を必要とします。

また、このインターフェイスは`String`型の新しいインスタンスを返却します。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string = ap.String("123.456")
string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
ap.assert_equal(string, "123.4")

# If a string is not a `float` value, this interface returns
# the original string.
string = ap.String("abc")
string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
ap.assert_equal(string, "abc")

ap.save_overall_html(
    dest_dir_path="string_apply_max_num_of_decimal_places_basic_usage_1/"
)
```

<iframe src="static/string_apply_max_num_of_decimal_places_basic_usage_1/index.html" width="0" height="0"></iframe>

## apply_max_num_of_decimal_places API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `apply_max_num_of_decimal_places(self, *, max_num_of_decimal_places: Union[int, ForwardRef('Int')], variable_name_suffix: str = '') -> 'String'`<hr>

**[インターフェイス概要]**

この文字列に浮動小数点数の最大桁数の設定を反映します。<hr>

**[引数]**

- `max_num_of_decimal_places`: Union[int, Int]
  - 浮動小数点数の最大桁数。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `string`: String
  - 反映後の文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> string = ap.String("123.456")
>>> string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
>>> ap.assert_equal(string, "123.4")
```