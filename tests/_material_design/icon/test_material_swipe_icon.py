from apysc._material_design.icon.material_swipe_icon import MaterialswipeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswipeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswipeIcon = MaterialswipeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
