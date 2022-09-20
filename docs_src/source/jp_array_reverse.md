<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_reverse.html)の確認をお願いします。</span>

# Array クラスの reverse インターフェイス

このページでは`Array`クラスの`reverse`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`reverse`メソッドは配列の値を直接更新する形で値の順番を逆順にします。

## 基本的な使い方

`reverse`メソッドは引数の指定を必要としません。

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
arr.reverse()
assert arr == [5, 3, 1]
```

## 関連資料

- [Array クラスの sort インターフェイス](jp_array_sort.md)

## reverse API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `reverse(self) -> None`<hr>

**[インターフェイス概要]**

この配列の値を直接逆順にします。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.reverse()
>>> arr
Array([3, 2, 1])
```