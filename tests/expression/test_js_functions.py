from typing import List
from apysc.expression import js_functions


def test_get_js_functions() -> None:
    setattr(js_functions, 'FUNC_TEST', 100)
    js_function_strs: List[str] = js_functions.get_js_functions()
    for js_function_str in js_function_strs:
        assert isinstance(js_function_str, str)
        assert 'function' in js_function_str
    assert js_functions.FUNC_COPY in js_function_strs
