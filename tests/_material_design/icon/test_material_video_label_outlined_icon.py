from apysc._material_design.icon.material_video_label_outlined_icon import (
    MaterialvideoLabelOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideoLabelOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideoLabelOutlinedIcon = MaterialvideoLabelOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
