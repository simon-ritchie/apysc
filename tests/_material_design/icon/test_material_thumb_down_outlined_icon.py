from apysc._material_design.icon.material_thumb_down_outlined_icon import (
    MaterialthumbDownOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialthumbDownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialthumbDownOutlinedIcon = MaterialthumbDownOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
