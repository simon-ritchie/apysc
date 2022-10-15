# apysc

[![Deploy to PyPI](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml)
[![CodeQL](https://github.com/simon-ritchie/apysc/actions/workflows/codeql_analysis.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/codeql_analysis.yml)
![Dependabot: enabled](https://img.shields.io/badge/Dependabot-enabled-brightgreen)
[![PyPI version](https://badge.fury.io/py/apysc.svg)](https://badge.fury.io/py/apysc)
![](https://img.shields.io/badge/code%20style-black-black?labelColor=gray)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/simon-ritchie/apysc/blob/main/LICENSE)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_unit_test_python_versions)
![](https://byob.yarr.is/simon-ritchie/apysc/unit_tests_coverage)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_unit_tests_num)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_doctests_num)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_lints)


![logo](https://github.com/simon-ritchie/apysc/blob/main/assets/logo_v1/logo_small_v1.png)

Language: | English | [日本語 (Japanese)](https://github.com/simon-ritchie/apysc/blob/main/README_JP.md) |

apysc (pronounced `æpisk`) is a Python frontend library to create HTML and js files with ActionScript 3 (as3)-like interface.

Notes: Currently developing and only works partially.

## Supported Python Version

Python 3.7 or later.

## Installing

pip command is available:

```
$ pip install apysc
```

## What's new

To check the major features updating and destructive changes, please see the Discussions' [Announcements](https://github.com/simon-ritchie/apysc/discussions/categories/announcements) and [Destructive changes](https://github.com/simon-ritchie/apysc/discussions/categories/destructive-changes).

## How to start

Please see [apysc documentation](https://simon-ritchie.github.io/apysc/en/index.html) and [quick start guide](https://simon-ritchie.github.io/apysc/en/quick_start.html) page.

<a href="https://simon-ritchie.github.io/apysc/en/index.html"><img src="https://github.com/simon-ritchie/apysc/blob/main/assets/document_index_screenshot.png"></a>

## What apysc can do in its current implementation

- **Save HTML or use it on the Jupyter notebook, JupyterLab, and Google Colaboratory!**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/jupyterlab_interface.png)

Documents:

- [save_overall_html interface](https://simon-ritchie.github.io/apysc/en/save_overall_html.html)
- [display_on_jupyter interface](https://simon-ritchie.github.io/apysc/en/display_on_jupyter.html)
- [display_on_colaboratory interface](https://simon-ritchie.github.io/apysc/en/display_on_colaboratory.html)

---

- **Draw the many types of vector graphics**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/vector_graphics_samples.png)

Example code fragments:

```py
...
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
...
```

Abstract document: [Draw interfaces abstract](https://simon-ritchie.github.io/apysc/en/draw_interfaces_abstract.html)

---

- **Lots of the vector graphics updating interfaces, such as the x, width, rotation, alpha (opacity), ellipse size, scale**

Example code fragments:

```py
...
rectangle.x = ap.Int(100)
...
```

Abstract document: [DisplayObject and GraphicsBase classes base properties abstract](https://simon-ritchie.github.io/apysc/en/display_object_and_graphics_base_prop_abstract.html)

---

- **Set each mouse event, such as the click, double click, mouse down, mouse up, mouse over, mouse out, mouse move**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/mouse_move.gif)

Example code fragments:

```py
...
def on_click(e: ap.MouseEvent, options: dict) -> None:
    ap.trace("Rectangle is clicked!")


rectangle.click(on_click)
...
```

Abstract document: [MouseEvent interfaces abstract](https://simon-ritchie.github.io/apysc/en/mouse_event_abstract.html)

---

- **Use the timer interface and animation**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/rotation_and_alpha_animation.gif)

Example code fragments:

```py
...
def on_timer(e: ap.TimerEvent, options: dict) -> None:
    ...


ap.Timer(on_timer, delay=1000).start()
...
```

Documents: [Timer class](https://simon-ritchie.github.io/apysc/en/timer.html)

---

- **Lots of tween animations, including easing options**

[![](https://github.com/simon-ritchie/apysc/blob/main/assets/animation_interfaces_abstract.gif)](https://simon-ritchie.github.io/apysc/animation_interfaces_abstract.html)

Example code fragments:

```py
...
rectangle.animation_x(
    x=100, duration=1000, easing=ap.Easing.EASE_IN_QUART,
).start()
...
```

Abstract document: [Animation interfaces abstract (each animation attribute)](https://simon-ritchie.github.io/apysc/en/animation_interfaces_abstract.html)

---

- **Basic control, like the for loop, if branch instruction, and so on**

Documents:

- [If](https://simon-ritchie.github.io/apysc/en/if.html)
- [Elif](https://simon-ritchie.github.io/apysc/en/elif.html)
- [Else](https://simon-ritchie.github.io/apysc/en/else.html)
- [For](https://simon-ritchie.github.io/apysc/en/for.html)

---

For more details, please see the following document:

[What apysc can do in its current implementation](https://simon-ritchie.github.io/apysc/en/what_apysc_can_do.html)

## License

The apysc library is under the MIT License.

The logo image is using followed Creative Commons license font:

- [Pauline Font - by Marcos Boric (2020)](https://www.behance.net/gallery/94972757/Pauline-Font)
- [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.en)

Also, the apysc library depends on the following libraries:

- [jQuery, MIT License](https://github.com/jquery/jquery/blob/main/LICENSE.txt)
- [jQuery Mousewheel](https://github.com/jquery/jquery-mousewheel/blob/main/LICENSE.txt)
- [SVG.js, MIT License](https://github.com/svgdotjs/svg.js/blob/master/LICENSE.txt)
- [Underscore.js, MIT License](https://github.com/jashkenas/underscore/blob/master/LICENSE)
- [Static Typing for Python (Python official backport package)](https://github.com/python/typing)
- [html-minifier, MIT License](https://github.com/Kaumer/html-minifier/blob/master/LICENSE)
