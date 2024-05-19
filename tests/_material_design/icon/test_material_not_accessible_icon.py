from apysc._material_design.icon.material_not_accessible_icon import MaterialnotAccessibleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotAccessibleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotAccessibleIcon = MaterialnotAccessibleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
