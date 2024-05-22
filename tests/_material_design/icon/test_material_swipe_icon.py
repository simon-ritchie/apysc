from apysc._material_design.icon.material_swipe_icon import MaterialSwipeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwipeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwipeIcon = MaterialSwipeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
