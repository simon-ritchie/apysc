from apysc._material_design.icon.material_pending_icon import MaterialpendingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpendingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpendingIcon = MaterialpendingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
