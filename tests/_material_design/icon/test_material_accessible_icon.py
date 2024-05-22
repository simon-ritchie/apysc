from apysc._material_design.icon.material_accessible_icon import MaterialAccessibleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccessibleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccessibleIcon = MaterialAccessibleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
