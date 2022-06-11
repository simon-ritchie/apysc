<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/recommended_type_checker_settings.html)の確認をお願いします。</span>

# 推奨される型アノテーションのチェック設定

このページではmypyやPylance（Pyright）の型アノテーションのチェック用のライブラリの設定について説明します。

## 推奨される型チェックのライブラリについて

apyscライブラリではmypyとPylance（Pyright）の型チェックの各ライブラリを使用しています。

そのためapyscを使ったプロジェクトではこれらの2つの（いずれかもしくは両方の）ライブラリの使用が相性が良く向いています。

## mypyで無視設定を行っているエラーコード

apyscライブラリでは`--disable-error-code misc`の引数オプションを使用してmypyのmisc（miscellaneous）のエラーコードのエラーを無視しています。

このエラーコードは多くのエラーをapyscライブラリ上で発生させますが、大半は無害なエラーとなるためapyscライブラリではこれらを無視する形で開発を行っています。

## 関連資料

- [mypy issue: Decorated property not supported #1362](https://github.com/python/mypy/issues/1362)