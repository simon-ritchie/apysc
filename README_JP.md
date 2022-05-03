# apysc

[![Deploy to PyPI](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml)
[![CodeQL](https://github.com/simon-ritchie/apysc/actions/workflows/codeql_analysis.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/codeql_analysis.yml)
![Dependabot: enabled](https://img.shields.io/badge/Dependabot-enabled-brightgreen)
[![PyPI version](https://badge.fury.io/py/apysc.svg)](https://badge.fury.io/py/apysc)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/simon-ritchie/apysc/blob/main/LICENSE)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_unit_test_python_versions)
![](https://byob.yarr.is/simon-ritchie/apysc/unit_tests_coverage)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_unit_tests_num)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_doctests_num)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_lints)


![logo](https://github.com/simon-ritchie/apysc/blob/main/assets/logo_v1/logo_small_v1.png)

言語: | [英語 (English)](https://github.com/simon-ritchie/apysc/) | 日本語 |

※日本語版のREADMEが古い場合には英語版のREADMEを参照してください。

apysc (アピスクと読みます)はHTMLやjsのファイルを生成するための、ActionScript3 (as3)風のインターフェイスを持つPythonのフロントエンドライブラリです。

特記事項: 現在開発中であり部分的にのみ動作します。

## サポートしているPythonバージョン

Python 3.7以降のPythonをサポートしています。

## インストール

pipコマンドでインストールすることができます:

```
$ pip install apysc
```

## 新着情報について

主な機能のアップデートや互換性の無いアップデートに関してはDiscussionsのページの[Announcements](https://github.com/simon-ritchie/apysc/discussions/categories/announcements)と[Destructive changes](https://github.com/simon-ritchie/apysc/discussions/categories/destructive-changes)をご確認ください。

## apyscの始め方

[apysc ドキュメント](https://simon-ritchie.github.io/apysc/jp/jp_index.html)や[クイックスタートガイド](https://simon-ritchie.github.io/apysc/jp/jp_quick_start.html)などをご確認ください。

<a href="https://simon-ritchie.github.io/apysc/jp/jp_index.html"><img src="https://github.com/simon-ritchie/apysc/blob/main/assets/document_index_screenshot.png"></a>

## apyscが現在の実装で出来ること

- **HTMLを保存したり、もしくはそれらをJupyter notebookやJupyterLab、Google Colaboratory上などで利用することができます。**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/jupyterlab_interface.png)

ドキュメント:

- [save_overall_html インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_save_overall_html.html)
- [display_on_jupyter インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_display_on_jupyter.html)
- [display_on_colaboratory インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_display_on_colaboratory.html)

---

- **様々な種類のベクターグラフィックスを描画することができます。**


![](https://github.com/simon-ritchie/apysc/blob/main/assets/vector_graphics_samples.png)

部分的なコード例:

```py
...
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
...
```

概要のドキュメント: [各描画のインターフェイスの概要](https://simon-ritchie.github.io/apysc/jp/jp_draw_interfaces_abstract.html)

---

- **多くの各ベクターグラフィックスのXや幅、回転量、透明度、楕円のサイズ、拡縮などの更新のインターフェイスがあります。**

部分的なコード例:

```py
...
rectangle.x = ap.Int(100)
...
```

概要のドキュメント: [DisplayObject と GraphicsBase クラスの基本的な属性の概要](https://simon-ritchie.github.io/apysc/jp/jp_display_object_and_graphics_base_prop_abstract.html)

---

- **クリックやダブルクリック、マウスダウン、マウスアップ、マウスオーバー、マウスアウト、マウスムーブなどの各マウスイベントを設定することができます。**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/mouse_move.gif)

部分的なコード例:

```py
...
def on_click(e: ap.MouseEvent, options: dict) -> None:
    ap.trace('Rectangle is clicked!')


rectangle.click(on_click)
...
```

概要のドキュメント: [マウスイベントのインターフェイスの概要](https://simon-ritchie.github.io/apysc/jp/jp_mouse_event_abstract.html)

---

- **タイマーの各インターフェイスを使ってアニメーションなどを行うことができます。**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/rotation_and_alpha_animation.gif)

部分的なコード例:

```py
...
def on_timer(e: ap.TimerEvent, options: dict) -> None:
    ...


ap.Timer(on_timer, delay=1000).start()
...
```

ドキュメント: [Timer クラス](https://simon-ritchie.github.io/apysc/jp/jp_timer.html)

---

- **イージングの設定も含めた様々なTweenのアニメーション設定を行うことができます。**

[![](https://github.com/simon-ritchie/apysc/blob/main/assets/animation_interfaces_abstract.gif)](https://simon-ritchie.github.io/apysc/animation_interfaces_abstract.html)

部分的なコード例:

```py
...
rectangle.animation_x(
    x=100, duration=1000, easing=ap.Easing.EASE_IN_QUART,
).start()
...
```

概要のドキュメント: [各アニメーションのインターフェイスの概要](https://simon-ritchie.github.io/apysc/jp/jp_animation_interfaces_abstract.html)

---

- **for文のループやif文による分岐などの基本的な制御を扱うことができます。**

ドキュメント:

- [If](https://simon-ritchie.github.io/apysc/jp/jp_if.html)
- [Elif](https://simon-ritchie.github.io/apysc/jp/jp_elif.html)
- [Else](https://simon-ritchie.github.io/apysc/jp/jp_else.html)
- [For](https://simon-ritchie.github.io/apysc/jp/jp_for.html)

---

その他の詳細については以下の資料をご確認ください。

[apyscが現在の実装で出来ること](https://simon-ritchie.github.io/apysc/jp/jp_what_apysc_can_do.html)

## ライセンス

apyscライブラリはMITライセンスにて公開されています。

ログ画素宇は以下のクリエイティブコモンズのライセンスのフォントを利用しています。

- [Pauline Font - by Marcos Boric (2020)](https://www.behance.net/gallery/94972757/Pauline-Font)
- [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.en)

また、apyscは以下のライブラリにも依存しています。

- jQuery, MIT License: https://github.com/jquery/jquery/blob/main/LICENSE.txt
- jQuery Mousewheel: https://github.com/jquery/jquery-mousewheel/blob/main/LICENSE.txt
- SVG.js, MIT License: https://github.com/svgdotjs/svg.js/blob/master/LICENSE.txt
- Underscore.js, MIT License: https://github.com/jashkenas/underscore/blob/master/LICENSE
- Static Typing for Python (Python official backport package): https://github.com/python/typing
- html-minifier, MIT License: https://github.com/Kaumer/html-minifier/blob/master/LICENSE
