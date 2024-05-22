from apysc._material_design.icon.material_rowing_icon import MaterialRowingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRowingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRowingIcon = MaterialRowingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
