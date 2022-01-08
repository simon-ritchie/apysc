# apysc

[![Deploy to PyPI](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml)
[![CodeQL](https://github.com/simon-ritchie/apysc/actions/workflows/codeql_analysis.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/codeql_analysis.yml)
[![PyPI version](https://badge.fury.io/py/apysc.svg)](https://badge.fury.io/py/apysc)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/simon-ritchie/apysc/blob/main/LICENSE)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_on_py3.6.15)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_on_py3.7.12)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_on_py3.8.12)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_on_py3.9.9)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_on_py3.10.0)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_coverage)
![](https://byob.yarr.is/simon-ritchie/apysc/passing_tests_num)
![](https://byob.yarr.is/simon-ritchie/apysc/flake8_checking)
![](https://byob.yarr.is/simon-ritchie/apysc/mypy_checking)
![](https://byob.yarr.is/simon-ritchie/apysc/pyright_checking)
![](https://byob.yarr.is/simon-ritchie/apysc/numdoclint_checking)

![logo](https://github.com/simon-ritchie/apysc/blob/main/assets/logo_v1/logo_small_v1.png)

apysc (pronounced `æpisk`) is the Python frontend library to create HTML and js files with ActionScript 3 (as3)-like interface.

Notes: Currently developing and only works partially.

## Supported Python Version

Python 3.6 or later.

## Installing

```
$ pip install apysc
```

## How to start

Please see [apysc documentation](https://simon-ritchie.github.io/apysc/index.html) and [quick start guide](https://simon-ritchie.github.io/apysc/quick_start.html) page.

<a href="https://simon-ritchie.github.io/apysc/index.html"><img src="https://github.com/simon-ritchie/apysc/blob/main/assets/document_index_screenshot.png"></a>

## What apysc can do in its current implementation

- **Save HTML or use it on the Jupyter notebook, JupyterLab, and Google Colaboratory!**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/jupyterlab_interface.png)

Documents:

- [save_overall_html interface](https://simon-ritchie.github.io/apysc/save_overall_html.html)
- [display_on_jupyter interface](https://simon-ritchie.github.io/apysc/display_on_jupyter.html)
- [display_on_colaboratory interface](https://simon-ritchie.github.io/apysc/display_on_colaboratory.html)

- **Draw the many types of vector graphics**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/vector_graphics_samples.png)

Example code fragments:

```py
...
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
...
```

Abstract document: [Draw interfaces abstract](https://simon-ritchie.github.io/apysc/draw_interfaces_abstract.html)


- **Lots of the vector graphics updating interfaces, such as the x, width, rotation, alpha (opacity), ellipse size, scale**

Example code fragments:

```py
...
rectangle.x = ap.Int(100)
...
```

Abstract document: [DisplayObject and GraphicsBase classes base properties abstract](https://simon-ritchie.github.io/apysc/display_object_and_graphics_base_prop_abstract.html)

- **Set each mouse event, such as the click, double click, mouse down, mouse up, mouse over, mouse out, mouse move**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/mouse_move.gif)

Example code fragments:

```py
...
def on_click(e: ap.MouseEvent, options: dict) -> None:
    ap.trace('Rectangle is clicked!')


rectangle.click(on_click)
...
```

Abstract document: [MouseEvent interfaces abstract](https://simon-ritchie.github.io/apysc/mouse_event_abstract.html)

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

Documents: [Timer](https://simon-ritchie.github.io/apysc/timer.html)

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

Abstract document: [Animation interfaces abstract (each animation attribute)](https://simon-ritchie.github.io/apysc/animation_interfaces_abstract.html)


- **Basic control, like the for loop, if branch instruction, and so on**

Documents:

- [If](https://simon-ritchie.github.io/apysc/if.html)
- [Elif](https://simon-ritchie.github.io/apysc/elif.html)
- [Else](https://simon-ritchie.github.io/apysc/else.html)
- [For](https://simon-ritchie.github.io/apysc/for.html)

For more details, please see the following document:

[What apysc can do in its current implementation](https://simon-ritchie.github.io/apysc/what_apysc_can_do.html)

## License

The apysc library is under the MIT License.

The logo image is using followed Creative Commons license font:

- [Pauline Font - by Marcos Boric (2020)](https://www.behance.net/gallery/94972757/Pauline-Font)
- [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.en)

Also, the apysc library depends on the following libraries:

- jQuery, MIT License: https://github.com/jquery/jquery/blob/main/LICENSE.txt
- jQuery Mousewheel: https://github.com/jquery/jquery-mousewheel/blob/main/LICENSE.txt
- SVG.js, MIT License: https://github.com/svgdotjs/svg.js/blob/master/LICENSE.txt
- Underscore.js, MIT License: https://github.com/jashkenas/underscore/blob/master/LICENSE
- Static Typing for Python (Python official backport package): https://github.com/python/typing
- html-minifier, MIT License: https://github.com/Kaumer/html-minifier/blob/master/LICENSE
