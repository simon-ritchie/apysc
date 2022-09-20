<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/dictionary_length.html)の確認をお願いします。</span>

# Dictionary クラスの length インターフェイス

このページでは`Dictionary`クラスの`length`属性のインターフェイスについて説明します。

## インターフェイス概要

`length`属性は辞書のキーの長さ（件数）を返却します。

## 基本的な使い方

`length`属性は`Int`型の整数を返却します。setterのインターフェイスは存在しません。

```py
# runnable
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({"a": 10, "b": 20})
assert dict_1.length == 2
assert isinstance(dict_1.length, ap.Int)
```

## len関数における特記事項

Pythonビルトインの`len`関数はサポートされておらずエラーとなります:

```py
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({"a": 10, "b": 20})
len(dict_1)
```

```
Exception: Dictionary instance can't apply len function. Please use length property instead.
```

## length property API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

辞書の値の長さ（件数）を取得します。<hr>

**[返却値]**

- `length`: Int
  - この辞書の値の長さ。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 1, "b": 2})
>>> dictionary.length
Int(2)
```