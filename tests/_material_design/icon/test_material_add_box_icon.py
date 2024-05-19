from apysc._material_design.icon.material_add_box_icon import MaterialaddBoxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddBoxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddBoxIcon = MaterialaddBoxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
