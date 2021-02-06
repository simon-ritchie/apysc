from apyscript.display.graphics import Graphics
from tests import testing_helper


class TestGraphics:

    def test_begin_fill(self) -> None:
        graphics: Graphics = Graphics()
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=graphics.begin_fill,
            kwargs={'color': 'red'})

        graphics.begin_fill(color='#0af')
        assert graphics._fill_color == '#00aaff'
