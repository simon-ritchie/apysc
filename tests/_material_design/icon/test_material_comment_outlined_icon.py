from apysc._material_design.icon.material_comment_outlined_icon import (
    MaterialcommentOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcommentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcommentOutlinedIcon = MaterialcommentOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
