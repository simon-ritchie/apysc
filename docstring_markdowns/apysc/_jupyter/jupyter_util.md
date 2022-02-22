# `apysc._jupyter.jupyter_util` docstrings

## Module summary

This module is for each Jupyter interface and definition implementation. Mainly the following interfaces are defined: <br>・display_on_jupyter Save the overall HTML and display it on the Jupyter. <br>・display_on_colaboratory Save the overall HTML and display it on Google Colaboratory.

## `_save_overall_html` function docstring

Save the overall HTML file.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not.

## `display_on_colaboratory` function docstring

Save the overall HTML and display it on Google Colaboratory.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not. False setting is useful when debugging.

<hr>

**[References]**

- [display_on_colaboratory interface document](https://simon-ritchie.github.io/apysc/display_on_colaboratory.html)

## `display_on_jupyter` function docstring

Save the overall HTML and display it on the Jupyter.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not. False setting is useful when debugging.

<hr>

**[Notes]**

Currently, this interface does not support Jupyter on the VS Code. This interface requires the Jupyter library (e.g., `notebook` package).<hr>

**[References]**

- [display_on_jupyter interface document](https://simon-ritchie.github.io/apysc/display_on_jupyter.html)