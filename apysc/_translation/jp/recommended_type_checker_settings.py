"""This module is for the translation mapping data of the
following document:

Document file: recommended_type_checker_settings.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Recommended type-annotation checker settings": "# 推奨される型アノテーションのチェック設定",
    ##################################################
    "This page explains the type-annotation checker libraries settings, such as the mypy and Pylance (Pyright).": "このページではmypyやPylance（Pyright）の型アノテーションのチェック用のライブラリの設定について説明します。",  # noqa
    ##################################################
    "## Recommended type-annotation checker libraries": "## 推奨される型チェックのライブラリについて",
    ##################################################
    "The apysc library uses the mypy and Pylance (Pyright) checker libraries.": "apyscライブラリではmypyとPylance（Pyright）の型チェックの各ライブラリを使用しています。",  # noqa
    ##################################################
    "So if you want to use the type-annotation checker libraries on the apysc-using project, these two libraries probably become comfortable.": "そのためapyscを使ったプロジェクトではこれらの2つの（いずれかもしくは両方の）ライブラリの使用が相性が良く向いています。",  # noqa
    ##################################################
    "## The ignoring error code of the mypy": "## mypyで無視設定を行っているエラーコード",
    ##################################################
    "The apysc library ignores the mypy misc (miscellaneous) errors with the `--disable-error-code misc` option.": "apyscライブラリでは`--disable-error-code misc`の引数オプションを使用してmypyのmisc（miscellaneous）のエラーコードのエラーを無視しています。",  # noqa
    ##################################################
    "This error code causes many mypy errors on the apysc library, but most are harmless, so the apysc ignores them.": "このエラーコードは多くのエラーをapyscライブラリ上で発生させますが、大半は無害なエラーとなるためapyscライブラリではこれらを無視する形で開発を行っています。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [mypy issue: Decorated property not supported #1362](https://github.com/python/mypy/issues/1362)": "- [mypy issue: Decorated property not supported #1362](https://github.com/python/mypy/issues/1362)",  # noqa
}
