from apysc._material_design.icon.material_video_label_icon import MaterialvideoLabelIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideoLabelIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideoLabelIcon = MaterialvideoLabelIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
