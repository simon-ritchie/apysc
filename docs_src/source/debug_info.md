# DebugInfo class

This page explains the `DebugInfo` class.

## What class is this?

The `DebugInfo` class append the debug mode information exporting setting. The apysc uses this class with the `with` statement. It covers the entire implementation of any callable (function or method) that needs to export the debug information.

## Basic usage for a function call

The `DebugInfo` class constructor requires the `callable_`, `locals_`, and `module_name` arguments.

The `callable_` argument needs to specify the target function (or method), and the `locals_` needs to specify the `locals()` built-in function return value. This interface uses these arguments to inspect the function arguments. Also, the module name must specify the `__name__` fixed value.

```py
# runnable
import apysc as ap


def add_two(int_val: ap.Int) -> ap.Int:
    """
    Add 2 to a specified integer.

    Parameters
    ----------
    int_val : ap.Int
        Target integer value.

    Returns
    -------
    int_val : ap.Int
        An added integer value.
    """
    with ap.DebugInfo(
            callable_=add_two, locals_=locals(), module_name=__name__):
        int_val += 10
        return int_val


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
int_val: ap.Int = ap.Int(10)
ap.set_debug_mode()
int_val = add_two(int_val=int_val)

ap.save_overall_html(
    minify=False, dest_dir_path='debug_info_basic_usage_for_function/')
```

This code exports the HTML with the debug info for the `add_two` function, as follows:

```js
...
//////////////////////////////////////////////////////////////////////
  // [add_two 1] started.
  // module name: __main__
  // arguments and variables:
  //    int_val = 10(i_11)
    //////////////////////////////////////////////////////////////////////
    // [__iadd__ 1] started.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    // arguments and variables:
    //    other = 10
    //    self = 10(i_11)
...
        //////////////////////////////////////////////////////////////////////
        // [_append_addition_expression 1] started.
        // module name: apysc._type.number_value_interface
        // class: NumberValueInterface
        // arguments and variables:
        //    other = 10
        //    result = 20(i_12)
        //    self = 10(i_11)
          var i_12 = i_11 + 10;
        // [_append_addition_expression 1] ended.
        // module name: apysc._type.number_value_interface
        // class: NumberValueInterface
        //////////////////////////////////////////////////////////////////////
...
    // [__iadd__ 1] ended.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    //////////////////////////////////////////////////////////////////////
  // [add_two 1] ended.
  // module name: __main__
  //////////////////////////////////////////////////////////////////////
```

## Notes about the debug mode setting

If the debug mode isn't enabled, the apysc ignores the `DebugInfo` class setting, so you don't need to drop that setting when debugging ends.

## Basic usage for a method call

Suppose the `callable_` argument value is a method. In that case, this interface also requires the `class_` argument to export class information, as follows:

```py
# runnable
import apysc as ap


class Calc:

    def add_two(self, int_val: ap.Int) -> ap.Int:
        """
        Add 2 to a specified integer.

        Parameters
        ----------
        int_val : ap.Int
            Target integer value.

        Returns
        -------
        int_val : ap.Int
            An added integer value.
        """
        with ap.DebugInfo(
                callable_=self.add_two, locals_=locals(),
                module_name=__name__, class_=Calc):
            int_val += 10
            return int_val

    def __repr__(self) -> str:
        """
        Get a representation string of this object.

        Returns
        -------
        repr_str : str
            Representation string.
        """
        return 'Calc()'


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
int_val: ap.Int = ap.Int(10)
calc: Calc = Calc()
ap.set_debug_mode()
int_val = calc.add_two(int_val=int_val)

ap.save_overall_html(
    minify=False, dest_dir_path='debug_info_basic_usage_for_method/')
```

This setting appends the class information to the exported HTML:

```js
...
  //////////////////////////////////////////////////////////////////////
  // [add_two 1] started.
  // module name: __main__
  // class: Calc
  // arguments and variables:
  //    int_val = 10(i_11)
  //    self = Calc()
    //////////////////////////////////////////////////////////////////////
    // [__iadd__ 1] started.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    // arguments and variables:
    //    other = 10
    //    self = 10(i_11)
...
```

## Notes for the property and dunder method

The class property can't specify as the `callable_` argument value, so it is acceptable to specify a callable name to the `callable_` argument, as follows:

```py
# runnable
import apysc as ap


class Coordinates:

    @property
    def x(self) -> ap.Int:
        """
        X-coordinate property.

        Returns
        -------
        x_val : ap.Int
            Current X-coordinate value.
        """
        with ap.DebugInfo(
                callable_='x', locals_=locals(), module_name=__name__,
                class_=Coordinates):
            x_val: ap.Int = ap.Int(10)
            return x_val

    def __repr__(self) -> str:
        """
        Get a representation string of this object.

        Returns
        -------
        repr_str : str
            Representation string.
        """
        return 'Coordinates()'


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
coordinates: Coordinates = Coordinates()
ap.set_debug_mode()
x: ap.Int = coordinates.x
x += 10

ap.save_overall_html(
    minify=False, dest_dir_path='debug_info_notes_for_property/')
```

Also, the direct referring of the dunder method (e.g., `__init__`)  raises the mypy type check error, so these methods name string specification is also acceptable:

```py
# runnable
import apysc as ap


class Coordinates:

    _x: ap.Int
    _y: ap.Int

    def __init__(self, x: ap.Int, y: ap.Int) -> None:
        """
        The x and y coordinates class.

        Parameters
        ----------
        x : ap.Int
            X-coordinate.
        y : ap.Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Coordinates):
            self._x = x
            self._y = y

    def __repr__(self) -> str:
        """
        Get a representation string of this object.

        Returns
        -------
        repr_str : str
            Representation string.
        """
        if hasattr(self, '_x'):
            x: ap.Int = self._x
        else:
            x = ap.Int(0)
        if hasattr(self, '_y'):
            y: ap.Int = self._y
        else:
            y = ap.Int(0)
        return f'Coordinates({x}, {y})'


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
x: ap.Int = ap.Int(10)
y: ap.Int = ap.Int(20)
ap.set_debug_mode()
coordinates: Coordinates = Coordinates(x=x, y=y)


ap.save_overall_html(
    minify=False, dest_dir_path='debug_info_notes_for_dunder_method/')
```

## See also

- [Set debug mode interface](set_debug_mode.md)
- [Unset debug mode interface](unset_debug_mode.md)


## DebugInfo constructor API

<!-- Docstring: apysc._html.debug_mode.DebugInfo.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, callable_:Union[Callable, str], locals_:Dict[str, Any], module_name:str, *, class_:Union[Type, str, NoneType]=None) -> None`<hr>

**[Interface summary]** Save debug information (append callable interface name comment and arguments information) to the JavaScript expression file. This class needs to use the `with` statement when instantiating.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `locals_`: dict
  - Local variables. This value requires a `locals()` function's value.
- `module_name`: str
  - Module name. This value requires the `__name__` value.
- `class_`: Type or str None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this interface ignores this argument.

<hr>

**[Notes]**

If the debug mode setting is not enabled, this interface skips the saving.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> def any_func(a: int, b: str) -> None:
...     with ap.DebugInfo(
...             callable_=any_func, locals_=locals(),
...             module_name=__name__):
...         int_val: ap.Int = ap.Int(10)
```