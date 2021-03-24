from random import randint

from retrying import retry

from apysc.display.begin_fill_interface import BeginFillInterface
from apysc.type import Number
from apysc.type import String


class TestBeginFillInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_begin_fill(self) -> None:
        begin_fill_interface: BeginFillInterface = BeginFillInterface()
        begin_fill_interface._fill_color = String('')
        begin_fill_interface._fill_alpha = Number(1.0)
        begin_fill_interface.begin_fill(color='#333')
        assert begin_fill_interface.fill_color == String('#333333')
        assert begin_fill_interface.fill_alpha == 1.0

        begin_fill_interface.begin_fill(color='#333', alpha=0.5)
        assert begin_fill_interface.fill_alpha == 0.5

        begin_fill_interface.begin_fill(
            color=String('#333'), alpha=Number(value=0.3))
        assert begin_fill_interface.fill_color == String('#333333')
        assert begin_fill_interface.fill_alpha == 0.3

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_fill_color(self) -> None:
        begin_fill_interface: BeginFillInterface = BeginFillInterface()
        begin_fill_interface._fill_color = String('')
        begin_fill_interface._fill_alpha = Number(1.0)
        begin_fill_interface.begin_fill(color='#333')
        assert begin_fill_interface.fill_color == '#333333'

        fill_color_1: String = begin_fill_interface.fill_color
        assert (fill_color_1.variable_name
                != begin_fill_interface.fill_color.variable_name)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_fill_alpha(self) -> None:
        begin_fill_interface: BeginFillInterface = BeginFillInterface()
        begin_fill_interface._fill_color = String('')
        begin_fill_interface._fill_alpha = Number(1.0)
        begin_fill_interface.begin_fill(color='#333', alpha=0.2)
        assert begin_fill_interface.fill_alpha == 0.2

        fill_alpha_1: Number = begin_fill_interface.fill_alpha
        assert (fill_alpha_1.variable_name
                != begin_fill_interface.fill_alpha.variable_name)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_fill_color_if_not_initialized(self) -> None:
        begin_fill_interface: BeginFillInterface = BeginFillInterface()
        begin_fill_interface._initialize_fill_color_if_not_initialized()
        assert begin_fill_interface.fill_color == ''

        begin_fill_interface._fill_color = String('#333333')
        begin_fill_interface._initialize_fill_color_if_not_initialized()
        assert begin_fill_interface.fill_color == '#333333'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_fill_alpha_if_not_initialized(self) -> None:
        begin_fill_interface: BeginFillInterface = BeginFillInterface()
        begin_fill_interface._initialize_fill_alpha_if_not_initialized()
        assert begin_fill_interface.fill_alpha == 1.0

        begin_fill_interface._fill_alpha = Number(0.5)
        begin_fill_interface._initialize_fill_alpha_if_not_initialized()
        assert begin_fill_interface.fill_alpha == 0.5
