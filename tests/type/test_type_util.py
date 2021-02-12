from apyscript.type import type_util


def test_is_same_class_instance() -> None:
    result: bool = type_util.is_same_class_instance(class_=bool, instance=1)
    assert not result

    result = type_util.is_same_class_instance(class_=int, instance=1)
    assert result
