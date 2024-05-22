from apysc._material_design.icon.material_pending_icon import MaterialPendingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPendingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPendingIcon = MaterialPendingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
