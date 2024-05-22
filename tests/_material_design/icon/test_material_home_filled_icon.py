from apysc._material_design.icon.material_home_filled_icon import MaterialHomeFilledIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHomeFilledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHomeFilledIcon = MaterialHomeFilledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
