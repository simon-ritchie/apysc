from apysc._material_design.icon.material_playlist_add_check_outlined_icon import MaterialplaylistAddCheckOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplaylistAddCheckOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplaylistAddCheckOutlinedIcon = MaterialplaylistAddCheckOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
