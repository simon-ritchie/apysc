<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/svg_mask.html)の確認をお願いします。</span>

# SvgMask クラスと関連インターフェース

このページでは`SvgMask`クラスとそれに関連した`add_svg_masking_object`メソッドや`svg_mask`属性などのインターフェイスについて説明します。

## クラス概要

`SvgMask`クラスはSVGグラフィックのマスク設定を扱います。

重なりあった領域のみを表示する形でSVGの`DisplayObject`（例 : `ap.Rectangle`）に別のSVGの`DisplayObject`を設定することができます。

## 基本的な使い方

以下のステップでマスク設定を適用することができます。

1. `SvgMask`インスタンスを作成します。

2. `add_svg_masking_object`メソッドを使って作成した`SvgMask`のインスタンスに`DisplayObject`を追加します。

マスクのインスタンスを対象の`DisplayObject`の`svg_mask`属性に設定します。