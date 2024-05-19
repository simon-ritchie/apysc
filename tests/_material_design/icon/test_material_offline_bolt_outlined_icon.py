from apysc._material_design.icon.material_offline_bolt_outlined_icon import MaterialofflineBoltOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialofflineBoltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialofflineBoltOutlinedIcon = MaterialofflineBoltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
