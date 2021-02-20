from random import randint

from retrying import retry

from apyscript.expression import callable_expression
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__append_args_expression_to_str() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    expression: str
    arg_var_name: str
    expression, arg_var_name = callable_expression.\
        _append_args_expression_to_str(
            expression='',
            args_dict={
                'sprite': sprite,
                'stage': stage,
            })
    expected: str = (
        f'var {callable_expression.ARG_VAR_TYPE_NAME}_1 = {{'
        f'\n  "sprite": {sprite.variable_name}'
        f'\n  "stage": {stage.variable_name}'
        '\n};\n'
    )
    assert expression == expected
    assert arg_var_name == f'{callable_expression.ARG_VAR_TYPE_NAME}_1'


def test__append_func_call_expression_to_str() -> None:

    def _test_func() -> None:
        ...

    expression: str
    return_var_name: str
    expression, return_var_name = callable_expression.\
        _append_func_call_expression_to_str(
            expression='\n',
            arg_var_name='arg_dict_1',
            func=_test_func,
        )
    expected: str = (
        f'\nvar {return_var_name} = _test_func(arg_dict_1);\n'
    )
    assert expected == expression
