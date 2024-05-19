from apysc._material_design.icon.material_music_video_outlined_icon import (
    MaterialmusicVideoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmusicVideoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmusicVideoOutlinedIcon = MaterialmusicVideoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
