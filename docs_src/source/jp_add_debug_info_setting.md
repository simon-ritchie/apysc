<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/add_debug_info_setting.html)の確認をお願いします。</span>

# add_debug_info_setting のデコレーターのインターフェイス

## インターフェイス概要

`add_debug_info_setting`のデコレーターのインターフェイスは対象の関数もしくはメソッドへとデバッグ情報の設定を行います。

デコレーターが設定された関数もしくはメソッドでは、デバッグモードを有効にした後の処理では各デバッグ情報を出力するようになります。

## 基本的な使い方

処理の有効にするために最初に`ap.set_debug_mode()`関数でデバッグモードの設定を行っておく必要があります。

その後、任意の各関数やメソッドに`@ap.add_debug_info_setting`のデコレーターの設定を追加することができます。

`@ap.add_debug_info_setting`の関数は`module_name`引数の指定が必要になります（この引数は基本的に`__name__`の値となります）。

```py
# runnable
import apysc as ap


def _main() -> None:
    """The entry point of this project."""
    ap.Stage(
        background_color="#333",
        stage_width=150,
        stage_height=150,
        stage_elem_id="stage",
    )
    ap.set_debug_mode()
    _draw_rectangle(x=50, y=50)
    ap.save_overall_html(dest_dir_path="add_debug_info_setting_basic_usage/")


@ap.add_debug_info_setting(module_name=__name__)
def _draw_rectangle(*, x: float, y: float) -> None:
    """
    Draw a rectangle with the given coordinates and sprite
    container class.

    Parameters
    ----------
    x : float
        X-coordinate of the rectangle.
    y : float
        Y-coordinate of the rectangle.
    """
    _: MySprite = MySprite(x=x, y=y)


class MySprite(ap.Sprite):
    @ap.add_debug_info_setting(module_name=__name__)
    def __init__(self, *, x: int, y: int) -> None:
        """
        My rectangle's sprite container class.

        Parameters
        ----------
        x : float
            X-coordinate of the rectangle.
        y : float
            Y-coordinate of the rectangle.
        """
        super(MySprite, self).__init__()
        self.graphics.begin_fill(color="#0af")
        self.graphics.draw_rect(x=x, y=y, width=50, height=50)


if __name__ == "__main__":
    _main()
```

出力されたHTMLには以下のように関数やメソッドの呼び出しなどのデバッグ情報が含まれるようになります:

```
...
  //////////////////////////////////////////////////////////////////////
  // [_draw_rectangle 1] started.
  // module name: __main__
  // Keyword arguments: {'x': 50, 'y': 50}
    //////////////////////////////////////////////////////////////////////
    // [__init__ 1] started.
    // module name: __main__
    // class: MySprite
    // Positional arguments: [Sprite('')]
    // Keyword arguments: {'x': 50, 'y': 50}
...
```

## mypy設定に対する特記事項

このデコレーター設定は現在mypy上でエラーが発生します。ごのエラーを避けるためには`--disable-error-code misc`オブションの指定の追加を検討してください。

参考資料:

- [推奨される型アノテーションのチェック設定](jp_recommended_type_checker_settings.md)

## 関連資料

- [set_debug_mode インターフェイス](jp_set_debug_mode.md)
- [unset_debug_mode インターフェイス](jp_unset_debug_mode.md)