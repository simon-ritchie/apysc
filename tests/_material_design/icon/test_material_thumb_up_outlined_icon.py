from apysc._material_design.icon.material_thumb_up_outlined_icon import (
    MaterialthumbUpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialthumbUpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialthumbUpOutlinedIcon = MaterialthumbUpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
