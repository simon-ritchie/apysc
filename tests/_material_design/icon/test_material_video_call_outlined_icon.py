from apysc._material_design.icon.material_video_call_outlined_icon import (
    MaterialvideoCallOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideoCallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideoCallOutlinedIcon = MaterialvideoCallOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
