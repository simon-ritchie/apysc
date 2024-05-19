from apysc._material_design.icon.material_picture_in_picture_icon import MaterialpictureInPictureIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpictureInPictureIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpictureInPictureIcon = MaterialpictureInPictureIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
