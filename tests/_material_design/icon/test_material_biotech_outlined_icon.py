from apysc._material_design.icon.material_biotech_outlined_icon import (
    MaterialbiotechOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbiotechOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbiotechOutlinedIcon = MaterialbiotechOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
