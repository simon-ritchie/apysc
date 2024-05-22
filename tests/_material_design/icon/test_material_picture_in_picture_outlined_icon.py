from apysc._material_design.icon.material_picture_in_picture_outlined_icon import (
    MaterialPictureInPictureOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPictureInPictureOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPictureInPictureOutlinedIcon = (
            MaterialPictureInPictureOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
