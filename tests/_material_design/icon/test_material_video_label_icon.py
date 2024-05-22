from apysc._material_design.icon.material_video_label_icon import MaterialVideoLabelIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideoLabelIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideoLabelIcon = MaterialVideoLabelIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
