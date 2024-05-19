from apysc._material_design.icon.material_turned_in_not_outlined_icon import (
    MaterialturnedInNotOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialturnedInNotOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialturnedInNotOutlinedIcon = MaterialturnedInNotOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
