from apysc._material_design.icon.material_anchor_icon import MaterialanchorIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialanchorIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialanchorIcon = MaterialanchorIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
