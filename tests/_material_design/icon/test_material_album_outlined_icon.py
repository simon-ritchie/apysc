from apysc._material_design.icon.material_album_outlined_icon import MaterialalbumOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalbumOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalbumOutlinedIcon = MaterialalbumOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
