from apysc._material_design.icon.material_picture_in_picture_alt_outlined_icon import (
    MaterialPictureInPictureAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPictureInPictureAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPictureInPictureAltOutlinedIcon = (
            MaterialPictureInPictureAltOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
