from apysc._material_design.icon.material_video_call_icon import MaterialVideoCallIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideoCallIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideoCallIcon = MaterialVideoCallIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
