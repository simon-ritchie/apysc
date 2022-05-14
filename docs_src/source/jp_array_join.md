<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_join.html)の確認をお願いします。</span>

# Array クラスの join インターフェイス

このページでは`Array`クラスの`join`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`join`メソッドは引数に指定された区切り文字で連結された配列の値の`String`クラスの文字列を返却します。

## 基本的な使い方

`join`メソッドは以下のコード例のように区切り文字としての`sep`引数が必要になります。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
joined: ap.String = arr.join(sep=',')
assert joined == '1,2,3'
```

## join API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `join(self, sep: Union[str, apysc._type.string.String]) -> apysc._type.string.String`<hr>

**[インターフェイス概要]** 指定された区切り文字を使ってこの配列の値を連結した文字列を生成します。<hr>

**[引数]**

- `sep`: String or str
  - 区切り文字。

<hr>

**[返却値]**

- `joined`: String
  - 連結された文字列。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.join(sep=', ')
String('1, 2, 3')
```