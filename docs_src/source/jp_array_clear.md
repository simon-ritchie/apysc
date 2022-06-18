<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/array_clear.html)の確認をお願いします。</span>

# Array クラスの clear インターフェイス

このページでは`Array`クラスの`clear`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`clear`メソッドは配列の値を空にします。

## 基本的な使い方

`clear`メソッドは呼び出しに特に引数を必要としません。

```py
# runnable
import apysc as ap

arr: ap.Array = ap.Array([10, 20, 30])
arr.clear()
assert arr == []
```