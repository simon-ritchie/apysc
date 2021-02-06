from apyscript.decorator import update_current_scope


def test__make_scope_name_from_module_and_func_name() -> None:
    scope_name: str = update_current_scope.\
        _make_scope_name_from_module_and_func_name(
            module_name='any.module.package',
            func_name='get_any_value')
    assert scope_name == 'any__module__package__get_any_value'


def test_update_current_scope() -> None:
    update_current_scope.update_current_scope(module=update_current_scope)
