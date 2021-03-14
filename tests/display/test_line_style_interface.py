from apyscript.display.line_style_interface import LineStyleInterface
from apyscript.type import Number
from apyscript.type import String
from tests import testing_helper


class TestLineStyleInterface:

    def test_line_style(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._line_color = String('')
        line_style_interface._line_alpha = Number(1.0)
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        testing_helper.assert_attrs(
            expected_attrs={
                '_line_color': '#333333',
                '_line_thickness': 3,
                '_line_alpha': 0.5,
            },
            any_obj=line_style_interface)

        line_style_interface.line_style(color=String('222'))
        assert line_style_interface.line_color == '#222222'

    def test_line_color(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._line_color = String('')
        line_style_interface._line_alpha = Number(1.0)
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_color == '#333333'

    def test_line_thickness(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._line_color = String('')
        line_style_interface._line_alpha = Number(1.0)
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_thickness == 3

    def test_line_alpha(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._line_color = String('')
        line_style_interface._line_alpha = Number(1.0)
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_alpha == 0.5
