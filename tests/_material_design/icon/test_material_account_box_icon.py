from apysc._material_design.icon.material_account_box_icon import MaterialAccountBoxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccountBoxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccountBoxIcon = MaterialAccountBoxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
