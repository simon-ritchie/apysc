from apysc._material_design.icon.material_event_seat_outlined_icon import (
    MaterialEventSeatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEventSeatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEventSeatOutlinedIcon = MaterialEventSeatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
