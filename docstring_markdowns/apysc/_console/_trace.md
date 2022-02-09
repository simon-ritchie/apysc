# apysc._console._trace docstrings

## Module summary

`trace` (console.log expression) interface implementations

## trace function docstring

Display arguments information to console. This function will save js `console.log` expression.<hr>

**[Parameters]**

- `*args`: list
  - Any arguments to display to console.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.trace('Int value is:', int_val)
```

<hr>

**[References]**

- [Trace interface document](https://simon-ritchie.github.io/apysc/trace.html)