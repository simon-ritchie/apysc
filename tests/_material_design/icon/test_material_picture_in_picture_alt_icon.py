from apysc._material_design.icon.material_picture_in_picture_alt_icon import (
    MaterialpictureInPictureAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpictureInPictureAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpictureInPictureAltIcon = MaterialpictureInPictureAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
