from apysc._material_design.icon.material_remove_icon import MaterialRemoveIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRemoveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRemoveIcon = MaterialRemoveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
