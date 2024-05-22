from apysc._material_design.icon.material_class_icon import MaterialClassIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClassIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClassIcon = MaterialClassIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
