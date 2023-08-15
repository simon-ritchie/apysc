<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/range.html)の確認をお願いします。</span>

# range 関数

このページでは`range`関数について説明していきます。

## 関数概要

`range`関数は`ap.Int`型の指定の範囲の配列を作成します（例 : `[0, 1, 2, 3, 4, 5]`）。

## 基本的な使い方

もしも引数を1つだけ指定した場合、範囲の配列は0から指定された引数の値を-1した範囲になります。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
range_arr: ap.Array[ap.Int] = ap.range(5)
ap.assert_equal(range_arr, [0, 1, 2, 3, 4])
ap.save_overall_html(dest_dir_path="range_basics_usage_1/")
```

<iframe src="static/range_basics_usage_1/index.html" width="0" height="0"></iframe>

また、もし2つの引数を指定した場合には範囲の配列は最初の引数の値～2つ目の引数の値を-1した範囲になります。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
range_arr: ap.Array[ap.Int] = ap.range(2, 4)
ap.assert_equal(range_arr, [2, 3])
ap.save_overall_html(dest_dir_path="range_basics_usage_2/")
```

<iframe src="static/range_basics_usage_2/index.html" width="0" height="0"></iframe>

もし3つ引数を指定した場合には範囲の配列は最初の引数の値～2つ目の引数の値を-1した範囲となり、各値は3つ目に指定された引数の値のステップで設定されます。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
range_arr: ap.Array[ap.Int] = ap.range(2, 10, 2)
ap.assert_equal(range_arr, [2, 4, 6, 8])
ap.save_overall_html(dest_dir_path="range_basics_usage_3/")
```

<iframe src="static/range_basics_usage_3/index.html" width="0" height="0"></iframe>

## range 関数のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `range(*args: Any) -> apysc._type.array.Array[apysc._type.int.Int]`<hr>

**[インターフェイス概要]**

整数の指定範囲の配列を生成します。<hr>

**[返却値]**

- `arr`: Array[Int]
  - 生成された配列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> range_arr: ap.Array[ap.Int] = ap.range(5)
>>> ap.assert_equal(range_arr, [0, 1, 2, 3, 4])
>>> range_arr = ap.range(2, 4)
>>> ap.assert_equal(range_arr, [2, 3])
>>> range_arr = ap.range(2, 10, 2)
>>> ap.assert_equal(range_arr, [2, 4, 6, 8])
```