<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_append_and_push.html)の確認をお願いします。</span>

# Array クラスの append と push のインターフェイス

このページでは`Array`クラスの`append`と`push`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`append`と`push`メソッドの各インターフェイスは配列の末端に任意の値を追加します。これらの各インターフェイスはお互いに同じ挙動をします（`append`はPython寄りな名前であり、`push`はJavaScript寄りな名前でエイリアスとして設けてあります）。

## 基本的な使い方

`append`と`push`の各メソッドは第一引数に`value`という引数名で追加する値の指定が必要になります。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2])
arr.append(value=3)
assert arr == [1, 2, 3]

arr.push(value=4)
assert arr == [1, 2, 3, 4]
```

## append API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `append(self, value: ~T) -> None`<hr>

**[インターフェイス概要]**

任意の値をこの配列の末尾に加えます。このメソッドは`push`メソッドと同様に動作します。<hr>

**[引数]**

- `value`: *
  - 追加対象の任意の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.append(4)
>>> arr
Array([1, 2, 3, 4])
```

## push API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `push(self, value: ~T) -> None`<hr>

**[インターフェイス概要]**

任意の値をこの配列の末尾に加えます。このメソッドは`append`メソッドと同様に動作します。<hr>

**[引数]**

- `value`: *
  - 追加対象の任意の値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.push(4)
>>> arr
Array([1, 2, 3, 4])
```