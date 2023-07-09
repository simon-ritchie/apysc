<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/string_length.html)の確認をお願いします。</span>

# String クラスの length 属性

このページでは`String`クラスの`length`属性について説明します。

## 属性の概要

`length`属性は文字数を返却します。

例えば`ABCDEF`という文字列では6が返却され、`あいうえお`という文字列では5が返却されます。

## 基本的な使い方

`length`属性では以下のように`Int`の値を返却します。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

string: ap.String = ap.String("ABCDEF")
length: ap.Int = string.length
ap.assert_equal(length, 6)

ap.save_overall_html(dest_dir_path="string_length_basic_usage_1/")
```

<iframe src="static/string_length_basic_usage_1/index.html" width="0" height="0"></iframe>

## 絵文字に関する特記事項

この属性はUnicodeのコードポイント数をカウントしているため、絵文字を対象とした場合に想定外の文字列を返却することがあります。

大半の絵文字は以下のように想定通りの文字数として振る舞います。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
string: ap.String = ap.String("🎉")
ap.assert_equal(string.length, 1)

string = ap.String("🥳🌟🍻")
ap.assert_equal(string.length, 3)

ap.save_overall_html(dest_dir_path="string_length_notes_1/")
```

<iframe src="static/string_length_notes_1/index.html" width="0" height="0"></iframe>

しかしながら複数のコードポイントを持つ絵文字に関してはこの属性は想定外の文字数を返却します（これはPythonと同じような挙動をします）:

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

assert len("👨‍👩‍👦") == 5

string: ap.String = ap.String("👨‍👩‍👦")
ap.assert_equal(string.length, 5)

ap.save_overall_html(dest_dir_path="string_length_notes_2/")
```

<iframe src="static/string_length_notes_2/index.html" width="0" height="0"></iframe>

## length 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

文字の長さ（文字数）を取得します。<hr>

**[返却値]**

- `characters_length`: Int
  - 文字の長さ（文字数）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("Hello")
>>> string.length
Int(5)
```