from apysc._material_design.icon.material_turned_in_outlined_icon import (
    MaterialTurnedInOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTurnedInOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTurnedInOutlinedIcon = MaterialTurnedInOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
