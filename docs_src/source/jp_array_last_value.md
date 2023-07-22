<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_last_value.html)の確認をお願いします。</span>

# Array クラスの last_value プロパティ

このページでは`Array`クラスの`last_value`属性について説明します。

## 属性の概要

`last_value`属性は配列の最後の値を返却します。

## 基本的な使い方

以下の例では`last_value`属性が30になっていることを試しています（配列の値は`[10, 20, 30]`となっています）。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
arr: ap.Array[int] = ap.Array([10, 20, 30])
last_value: int = arr.last_value
ap.assert_equal(last_value, 30)

ap.save_overall_html(dest_dir_path="array_last_value_basic_usage_1/")
```

<iframe src="static/array_last_value_basic_usage_1/index.html" width="0" height="0"></iframe>

もしも配列の値が空の場合、この属性の値はJavaScriptのランタイム上では`undefined`になります。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")
arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)
last_value: ap.Int = arr.last_value
ap.assert_undefined(last_value)

ap.save_overall_html(dest_dir_path="array_last_value_basic_usage_2/")
```

<iframe src="static/array_last_value_basic_usage_2/index.html" width="0" height="0"></iframe>

## last_value 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

配列の最後のインデックスの値を取得します。<hr>

**[返却値]**

- `last_value`: _ArrValue
  - 配列の最後のインデックスの値。

<hr>

**[特記事項]**

 ・コンストラクタの`fixed_value_type`設定はこの属性の値の型に影響します。<br> ・もし配列が空の場合、この値はJavaScriptのランタイム上では`undefined`となります。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=100, stage_height=50, background_color="#333",
...     stage_elem_id="stage",
... )
>>> arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)
>>> last_value: ap.Int = arr.last_value
>>> ap.assert_undefined(last_value)
>>> arr.append(ap.Int(10))
>>> last_value = arr.last_value
>>> ap.assert_equal(last_value, 10)
>>> arr.append(ap.Int(20))
>>> last_value = arr.last_value
>>> ap.assert_equal(last_value, 20)
```