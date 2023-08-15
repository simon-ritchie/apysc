<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/int_and_number_to_fixed.html)の確認をお願いします。</span>

# Int と Number クラスの to_fixed インターフェイス

このページでは`Int`と`Number`クラスの`to_fixed`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`to_fixed`メソッドは数値を固定の桁数の浮動小数点数を持った文字列へと変換します。

## 基本的な使い方

`to_fixed`メソッドは`digits`引数の指定を必要とします。

その引数は0～100の範囲の値を受け付けます。

もし`digits`引数に0を指定した場合、結果の文字列は整数の形式の文字列になります。

また、`digits`引数に2を指定した場合には結果の文字列は小数点以下が2桁の数値の文字列になります（例 : 10.34）。

このインターフェイスは切り捨てられた浮動小数点数に偶数丸めの処理を反映します。

例えばもし数値が10.678であり`digits`引数がに2が指定されたばあぽ、結果の文字列は10.68になります。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
num: ap.Number = ap.Number(10.789)
fixed_float_str: ap.String = num.to_fixed(digits=2)
ap.assert_equal(fixed_float_str, "10.79")

fixed_float_str = num.to_fixed(digits=5)
ap.assert_equal(fixed_float_str, "10.78900")

fixed_float_str = num.to_fixed(digits=0)
ap.assert_equal(fixed_float_str, "11")

ap.save_overall_html(dest_dir_path="to_fixed_basics_usage/")
```

<iframe src="static/to_fixed_basics_usage/index.html" width="0" height="0"></iframe>

## to_fixed API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `to_fixed(self, *, digits: Union[int, ForwardRef('Int')], variable_name_suffix: str = '') -> apysc._type.string.String`<hr>

**[インターフェイス概要]**

値を固定の小数点以下の桁数の文字列へと変換します。<hr>

**[引数]**

- `digits`: int or Int
  - 浮動小数点数の桁数（0～100の範囲の値を受け付けることができます）。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `result_str`: String
  - 変換された文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> num: ap.Number = ap.Number(10.789)
>>> fixed_float_str: ap.String = num.to_fixed(digits=2)
>>> fixed_float_str
String("10.79")

>>> fixed_float_str = num.to_fixed(digits=5)
>>> fixed_float_str
String("10.78900")

>>> fixed_float_str = num.to_fixed(digits=0)
>>> fixed_float_str
String("11")
```