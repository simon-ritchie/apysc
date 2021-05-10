from apysc import LineDashSetting
from tests.testing_helper import assert_raises
from apysc import Int


class TestLineDashSetting:

    def test___init__(self) -> None:
        setting: LineDashSetting = LineDashSetting(
            dash_size=10, space_size=5)
        assert setting._value['dash_size'] == 10
        assert isinstance(setting._value['dash_size'], Int)
        assert setting._value['space_size'] == 5
        assert isinstance(setting._value['space_size'], Int)

        dash_size: Int = Int(15)
        space_size: Int = Int(3)
        setting: LineDashSetting = LineDashSetting(
            dash_size=dash_size, space_size=space_size)
        assert setting._value['dash_size'].variable_name != \
            dash_size.variable_name
        assert setting._value['space_size'].variable_name != \
            space_size.variable_name
