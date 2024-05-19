from apysc._material_design.icon.material_pending_outlined_icon import MaterialpendingOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpendingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpendingOutlinedIcon = MaterialpendingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
