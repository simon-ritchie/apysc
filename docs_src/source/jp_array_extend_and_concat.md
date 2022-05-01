<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_extend_and_concat.html)の確認をお願いします。</span>

# Array クラスの extend と concat のインターフェイス

このページでは`Array`クラスの`extend`と`concat`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`extend`と`concat`メソッドの各インターフェイスは2つの配列の連結処理を扱います。

`extend`メソッドは元々の配列自体を更新し返却値は設定されずNoneとなります。`concat`メソッドでは連結結果の配列を返却します。元の配列は変化しません。

## 基本的な使い方

`extend`と`concat`メソッドは以下のコード例のようにそれぞれ第一引数に連結対象の他の配列など（ビルトインのリストやタプル、apyscの`Array`など）のオブジェクトを必要とします:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2])
arr.extend([3, 4])
assert arr == [1, 2, 3, 4]

other_arr: ap.Array[int] = arr.concat([5, 6])
assert other_arr == [1, 2, 3, 4, 5, 6]
assert arr == [1, 2, 3, 4]
```

## extend API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `extend(self, other_arr:Union[List[~T], tuple, _ForwardRef('Array')]) -> None`<hr>

**[インターフェイス概要]** 引数に指定された配列のこの配列へ連結します。このインターフェイスは引数に指定された配列の値をこの配列の値の後に配置します。このメソッドはconcatメソッドと似た挙動をしますが、extendメソッドはこの配列自体を更新するのに対してconcatメソッドは別の配列として値を返却するという違いがあります。<hr>

**[引数]**

- `other_arr`: Array or list or tuple
  - 連結対象となる他の配列の（もしくはそれに近しい）値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.extend([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```

## concat API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `concat(self, other_arr:Union[List[~T], tuple, _ForwardRef('Array')]) -> 'Array'`<hr>

**[インターフェイス概要]** この配列の値と引数に指定された配列の値を連結した配列を作成します。このインターフェイスでは引数に指定された配列の値をこの配列の値の後に配置します。このメソッドはextendメソッドと似ていますが、extendメソッドが配列自体を更新するのに対してconcatメソッドは連結した別の配列の結果を返却するという違いがあります。<hr>

**[引数]**

- `other_arr`: Array or list or tuple
  - 連結対象となる他の配列の（もしくはそれに近しい）値。

<hr>

**[返却値]**

- `concatenated`: Array
  - 連結結果の配列の値。.

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr = arr.concat([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```