from apysc._material_design.icon.material_account_box_icon import MaterialaccountBoxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccountBoxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccountBoxIcon = MaterialaccountBoxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
