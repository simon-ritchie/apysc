from apysc._material_design.icon.material_duo_outlined_icon import (
    MaterialDuoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDuoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDuoOutlinedIcon = MaterialDuoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
