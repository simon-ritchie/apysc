from apysc._material_design.icon.material_playlist_add_outlined_icon import (
    MaterialplaylistAddOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplaylistAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplaylistAddOutlinedIcon = MaterialplaylistAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
