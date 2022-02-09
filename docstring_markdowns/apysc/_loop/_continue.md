# apysc._loop._continue docstrings

## Module summary

Class implementation for the continue.

## Continue class docstring

The loop continue expression class.<hr>

**[Notes]**

This class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     with ap.If(i == 1):
...         _ = ap.Continue()
```

<hr>

**[References]**

- [Continue document](https://simon-ritchie.github.io/apysc/continue.html)

### __init__ method docstring

The loop continue expression class.<hr>

**[Notes]**

This class can be instantiated in the with loop statement, for example, after the `with ap.For(...):` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     with ap.If(i == 1):
...         _ = ap.Continue()
```

<hr>

**[References]**

- [Continue document](https://simon-ritchie.github.io/apysc/continue.html)