<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/math_clamp.html)の確認をお願いします。</span>

# Math クラスの clamp インターフェイス

このページでは`Math`クラスの`clamp`メソッドについて説明します。

## インターフェイス概要

`clamp`メソッドは指定された最小値と最大値の範囲内で値を設定します。

例えば、もし値が`20`で最小値が`25`の場合、結果の値は`25`になります。

同様に、もし値が`20`で最大値が`15`であれば、結果の値は`15`になります。

もし値が`20`で最小値と最大値が`15`と`25`であれば、このメソッドはそのまま`20`の値を返却します。

## 基本的な使い方

`clamp`メソッドは`value`、`min_`、`max_`の引数を必要とします。

各引数と返却値は`ap.Int`もしくは`ap.Number`型となります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=1,
    stage_height=1,
    stage_elem_id="stage",
)
value: ap.Int = ap.Int(20)
result: ap.Int = ap.Math.clamp(value=value, min_=ap.Int(25), max_=ap.Int(50))
ap.assert_equal(result, ap.Int(25))

result = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(15))
ap.assert_equal(result, ap.Int(15))

result = ap.Math.clamp(value=value, min_=ap.Int(15), max_=ap.Int(25))
ap.assert_equal(result, ap.Int(20))

ap.save_overall_html(dest_dir_path="math_clamp_basic_usage/")
```

<iframe src="static/math_clamp_basic_usage/index.html" width="1" height="1"></iframe>

## clamp メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `clamp(*, value: ~_ValueType, min_: ~_ValueType, max_: ~_ValueType) -> ~_ValueType`<hr>

**[インターフェイス概要]**

指定された最小値と最大値の範囲内で値を設定します。もし値が最小値未満であればこのメソッドは最小値を返却します。もし値が最大値よりも大きければこのメソッドは最大値を返却します。<hr>

**[引数]**

- `value`: _ValueType
  - 対象の`Int`もしくは`Number`型の値。

- `min_`: _ValueType
  - 最小値。

- `max_`: _ValueType
  - 最大値。

<hr>

**[返却値]**

- `result`: _ValueType
  - 最小値と最大値範囲の反映後の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> value: ap.Int = ap.Int(5)
>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))
>>> value
Int(10)

>>> value = ap.Int(25)
>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))
>>> value
Int(20)
```