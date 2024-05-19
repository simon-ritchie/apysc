from apysc._material_design.icon.material_event_seat_outlined_icon import (
    MaterialeventSeatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialeventSeatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialeventSeatOutlinedIcon = MaterialeventSeatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
