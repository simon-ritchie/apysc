from apysc._material_design.icon.material_event_seat_icon import MaterialEventSeatIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEventSeatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEventSeatIcon = MaterialEventSeatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
