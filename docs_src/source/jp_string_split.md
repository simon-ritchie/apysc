<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_split.html)の確認をお願いします。</span>

# String クラスの split インターフェイス

このページでは`String`クラスの`split`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`split`メソッドのインターフェイスは文字列を分割して`String`の値を格納した`Array`の配列を作成します。

## 基本的な使い方

`split`メソッドは区切り文字としての`sep`の`String`型の引数を必要とします。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

str_value: ap.String = ap.String("Lorem ipsum dolor sit")
splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))
ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])

ap.save_overall_html(dest_dir_path="string_split_basic_usage/")
```

<iframe src="static/string_split_basic_usage/index.html" width="0" height="0"></iframe>

## split API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `split(self, *, sep: 'String') -> 'Array[String]'`<hr>

**[インターフェイス概要]**

現在の文字列を指定された区切り文字（列）を使って分割します。<hr>

**[引数]**

- `sep`: String
  - 区切り文字（列）。

<hr>

**[返却値]**

- `splitted_strs`: Array[String]
  - 分割された文字列を格納した配列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> str_value: ap.String = ap.String("Lorem ipsum dolor sit")
>>> splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))
>>> ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])
```