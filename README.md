# apysc

[![Deploy to PyPI](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml/badge.svg)](https://github.com/simon-ritchie/apysc/actions/workflows/deploy_to_pypi.yml)
[![PyPI version](https://badge.fury.io/py/apysc.svg)](https://badge.fury.io/py/apysc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/simon-ritchie/apysc/blob/main/LICENSE)
![](https://byob.yarr.is/simon-ritchie/apysc/pytest_coverage)

![logo](https://github.com/simon-ritchie/apysc/blob/main/assets/logo_v1/logo_small_v1.png)

apysc is the Python frontend library to create HTML and js files, that has ActionScript 3 (as3)-like interface.

Notes: Currently developing and only works partially.

## Why apysc

- In some cases, when you want to do the front-end works yourself, such as customized data visualization on the web in a Python project or UI creation in a Django project, it's potentially easier not to have to write JavaScript or TypeScript.
- If you can write the front end using only Python, no HTML, CSS, JavaScript, and TypeScript, you can reduce the cost of switching languages.
- It simplifies CI since you only need to maintain only the Python lint and tests (e.g., mypy, flake8, and pytest).

## Supported Python Version

Python 3.6 or later.

## Installing

```
$ pip install apysc
```

## What apysc can do in its current implementation

- **Save HTML or use it on the Jupyter notebook, JupyterLab, and Google Colaboratory!**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/jupyterlab_interface.png)

Documents: [save_overall_html interface](https://simon-ritchie.github.io/apysc/save_overall_html.html), [display_on_jupyter interface](https://simon-ritchie.github.io/apysc/display_on_jupyter.html), [display_on_colaboratory interface](https://simon-ritchie.github.io/apysc/display_on_colaboratory.html)

- **Draw the many types of vector graphics**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/vector_graphics_samples.png)

Documents: [begin_fill interface](https://simon-ritchie.github.io/apysc/graphics_begin_fill.html), [line_style interface](https://simon-ritchie.github.io/apysc/graphics_line_style.html), [draw_rect interface](https://simon-ritchie.github.io/apysc/graphics_draw_rect.html), [draw_round_rect interface](https://simon-ritchie.github.io/apysc/graphics_draw_round_rect.html), [draw_circle interface](https://simon-ritchie.github.io/apysc/graphics_draw_circle.html), [draw_ellipse interfac](https://simon-ritchie.github.io/apysc/graphics_draw_ellipse.html), [move_to and line_to interfaces](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html), [draw_line interface](https://simon-ritchie.github.io/apysc/graphics_draw_line.html), [draw_dotted_line interface](https://simon-ritchie.github.io/apysc/graphics_draw_dotted_line.html), [draw_dashed_line interface](https://simon-ritchie.github.io/apysc/graphics_draw_dashed_line.html), [draw_round_dotted_line interface](https://simon-ritchie.github.io/apysc/graphics_draw_round_dotted_line.html), [draw_dash_dotted_line interface](https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html), [draw_dash_dotted_line interface](https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html), [draw_polygon interface](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)


- **Lots of the vector graphics updating interfaces, such as the `x`, `width`, `rotation`, `alpha (opacity)`, `ellipse size`, `scale`**

Document: [x and y interfaces](https://simon-ritchie.github.io/apysc/display_object_x_and_y.html), [visible interface](https://simon-ritchie.github.io/apysc/display_object_visible.html), [get_css and set_css interfaces](https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html), [rotation_around_center interface](https://simon-ritchie.github.io/apysc/graphics_base_rotation_around_center.html), [rotation_around_point interfaces](https://simon-ritchie.github.io/apysc/graphics_base_rotation_around_point.html), [scale_x_from_center and scale_y_from_center interfaces](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_center.html), [get_scale_from_point and set_scale_from_point interfaces](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html), [flip_x and flip_y interfaces](https://simon-ritchie.github.io/apysc/graphics_base_flip_interfaces.html), [skew_x and skew_y interfaces](https://simon-ritchie.github.io/apysc/graphics_base_skew.html)

- **Set each mouse event, such as the click, double click, mouse down, mouse up, mouse over, mouse out, mouse move**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/mouse_move.gif)

Documents: [Click interface](https://simon-ritchie.github.io/apysc/click.html), [Double click interface](https://simon-ritchie.github.io/apysc/dblclick.html), [Mousedown and mouseup interfaces](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html), [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html), [Mousemove interface](https://simon-ritchie.github.io/apysc/mousemove.html)

- **Use the timer interface and animation**

![](https://github.com/simon-ritchie/apysc/blob/main/assets/rotation_and_alpha_animation.gif)

Documents: [Timer](https://simon-ritchie.github.io/apysc/timer.html)

- Basic control, like the for loop, if branch instruction, and so on

Documents: [If](https://simon-ritchie.github.io/apysc/if.html), [Elif](https://simon-ritchie.github.io/apysc/elif.html), [Else](https://simon-ritchie.github.io/apysc/else.html), [For](https://simon-ritchie.github.io/apysc/for.html)

For more details, please see the following document:

[What apysc can do in its current implementation](https://simon-ritchie.github.io/apysc/what_apysc_can_do.html)

## How to start

Please see [apysc documentation](https://simon-ritchie.github.io/apysc/index.html) and [quick start guide](https://simon-ritchie.github.io/apysc/quick_start.html) page.

<a href="https://simon-ritchie.github.io/apysc/index.html"><img src="https://github.com/simon-ritchie/apysc/blob/main/assets/document_index_screenshot.png"></a>

## License

This library is released under the MIT License.

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