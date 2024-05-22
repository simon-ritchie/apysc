from apysc._material_design.icon.material_content_cut_outlined_icon import (
    MaterialContentCutOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContentCutOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContentCutOutlinedIcon = MaterialContentCutOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
