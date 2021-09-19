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

- Save HTML or use it on the Jupyter notebook, JupyterLab, and Google Colaboratory!

![](https://github.com/simon-ritchie/apysc/blob/main/assets/jupyterlab_interface.png)

- Draw the many types of vector graphics

![](https://github.com/simon-ritchie/apysc/blob/main/assets/vector_graphics_samples.png)

- Set each mouse event
- Use the timer interface and animation

![](https://github.com/simon-ritchie/apysc/blob/main/assets/rotation_and_alpha_animation.gif)

- Basic control, like the for loop, if branch instruction, and so on

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
