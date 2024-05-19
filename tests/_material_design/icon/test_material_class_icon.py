from apysc._material_design.icon.material_class_icon import MaterialclassIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclassIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclassIcon = MaterialclassIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
