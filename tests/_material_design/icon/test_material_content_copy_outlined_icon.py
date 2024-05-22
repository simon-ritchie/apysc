from apysc._material_design.icon.material_content_copy_outlined_icon import (
    MaterialContentCopyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContentCopyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContentCopyOutlinedIcon = MaterialContentCopyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
