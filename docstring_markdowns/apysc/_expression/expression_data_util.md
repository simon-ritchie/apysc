# `apysc._expression.expression_data_util` docstrings

## Module summary

The implementation of manipulating HTL and js expression files. Mainly following interfaces are defined: <br>・empty_expression : Empty the current js expression data. <br>・append_js_expression : Append js expression. <br>・get_current_expression : Get current expression string. <br>・get_current_event_handler_scope_expression : Get a current event handler scope's expression string. <br>・exec_query : Execute a SQLite sql query.

## `_check_connection` function docstring

The decorator function to check a SQLite connection when a specified function calling, and if failed, create a new connection and recall a function.<hr>

**[Parameters]**

- `func`: Callable
  - Target function to decorate.

<hr>

**[Returns]**

- `new_func`: Callable
  - Decorated function.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `_get_current_expression` function docstring

Get a current expression string from a specified table.<hr>

**[Parameters]**

- `table_name`: TableName
  - Target table name.

<hr>

**[Returns]**

- `current_expression`: str
  - Current expression string.

## `_get_expression_table_name` function docstring

Get a expression table name. This value will be switched whether current scope is event handler's one or not.<hr>

**[Returns]**

- `table_name`: str
  - Target expression table name.

## `_make_create_table_query` function docstring

Make a create table sql query.<hr>

**[Parameters]**

- `table_name`: str
  - Target table name.
- `column_ddl`: str
  - Target table columns DDL string. e.g., ' id INTEGER, ...'

<hr>

**[Returns]**

- `query`: str
  - A create table sql query.

## `new_func` function docstring

Function for the decoration.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.
- `**kwargs`: dict
  - Any keyword arguments.

<hr>

**[Returns]**

- `result`: Any
  - Any returned value.

## `_validate_limit_clause` function docstring

Validate whether a LIMIT clause is used in a UPDATE or DELETE sql.<hr>

**[Parameters]**

- `sql`: str
  - Target sql.

<hr>

**[Raises]**

- _LimitClauseCantUseError: If the LIMIT clause used in a DELETE or UPDATE sql.

## `append_js_expression` function docstring

Append js expression.<hr>

**[Parameters]**

- `expression`: str
  - JavaScript Expression string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> ap.append_js_expression(expression='console.log("Hello!")')
```

<hr>

**[References]**

- [append_js_expression interface document](https://simon-ritchie.github.io/apysc/append_js_expression.html)

## `empty_expression` function docstring

Empty the current js expression data.

## `exec_query` function docstring

Execute a SQLite sql query.<hr>

**[Parameters]**

- `sql`: str
  - Target sql.
- `commit`: bool, default True
  - A boolean value whether commit the transaction after the sql query or not.

<hr>

**[Raises]**

- _LimitClauseCantUseError: If the LIMIT clause used in a DELETE or UPDATE sql.

## `get_current_event_handler_scope_expression` function docstring

Get a current event handler scope's expression string.<hr>

**[Returns]**

- `current_expression`: str
  - Current expression's string.

<hr>

**[Notes]**

If it is necessary to get normal scope's expression, then use get_current_expression function instead.

## `get_current_expression` function docstring

Get a current expression's string.<hr>

**[Returns]**

- `current_expression`: str
  - Current expression's string.

<hr>

**[Notes]**

If it is necessary to get event handler scope's expression, then use get_current_event_handler_scope_expression function instead.

## `initialize_sqlite_tables_if_not_initialized` function docstring

Initialize the sqlite tables if they have not been initialized yet.<hr>

**[Returns]**

- `initialized`: bool
  - If initialized, returns True.

## `TableName` class docstring

An enumeration.

## `_LimitClauseCantUseError` class docstring