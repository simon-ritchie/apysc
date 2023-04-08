<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/to_string.html)の確認をお願いします。</span>

# to_string インターフェイス

このページでは`to_string`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`to_string`メソッドはそのインスタンス自体の`String`型での表現の値を返却します。

このインターフェイスは`Int`や`Number`、`Boolean`や`Array`などの基本的な各データクラスに存在します。

## 基本的な使い方

`to_string`メソッドは引数の指定を必要としません。

返却値はJavaScriptに準じた値となります。

たとえば、`Boolean`の値であれば`True`や`False`などの値ではなく`true`や`false`といった文字列の値になります。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=0, stage_height=0, stage_elem_id="stage"
)
int_value: ap.Int = ap.Int(100)
string: ap.String = int_value.to_string()
ap.assert_equal(string, "100")

number_value: ap.Number = ap.Number(10.5)
string = number_value.to_string()
ap.assert_equal(string, "10.5")

bool_value: ap.Boolean = ap.Boolean(True)
string = bool_value.to_string()
ap.assert_equal(string, "true")

array_value: ap.Array = ap.Array([10, 20, 30])
string = array_value.to_string()
ap.assert_equal(string, "10,20,30")

ap.save_overall_html(dest_dir_path="to_string_basic_usage_1/")
```

<iframe src="static/to_string_basic_usage_1/index.html" width="0" height="0"></iframe>

このメソッドはその文字列を使ってテキスト関係のインターフェイスを使う際に便利なことがあります。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=300, stage_height=50, stage_elem_id="stage"
)
width: ap.Int = ap.Int(50)
text: ap.SVGText = ap.SVGText(
    text=ap.String("width is: ") + width.to_string(),
    fill_color="#aaa",
    x=20,
    y=30,
)
ap.save_overall_html(dest_dir_path="to_string_basic_usage_2/")
```

<iframe src="static/to_string_basic_usage_2/index.html" width="300" height="50"></iframe>

## to_string メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `to_string(self) -> apysc._type.string.String`<hr>

**[インターフェイス概要]**

このインスタンスを文字列へと変換します。<hr>

**[返却値]**

- `string`: String
  - 変換された文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color="#333", stage_width=200, stage_height=200
... )
>>> int_value: ap.Int = ap.Int(value=100)
>>> string: ap.String = int_value.to_string()
>>> ap.assert_equal(string, "100")
```