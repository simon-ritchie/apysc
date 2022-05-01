<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_comparison.html)の確認をお願いします。</span>

# Array クラスの比較の各インターフェイス

このページでは`Array`クラスにおける等値と非等値の比較の各インターフェイスについて説明します。

## 基本的な使い方

`Array`クラスの値はPythonビルトインのリスト及び別の`Array`クラスの値と比較を行うことができます。結果は`Boolean`型となります。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
result: ap.Boolean = arr == [1, 3, 5]
assert result
```

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
other_arr: ap.Array[int] = ap.Array([1, 3, 5])
result: ap.Boolean = arr == other_arr
assert result
```

等値の比較記号（`==`）と非等値の比較記号（`!=`）をサポートしています:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
result: ap.Boolean = arr != [2, 4, 6]
assert result
```