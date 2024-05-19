from apysc._material_design.icon.material_account_circle_outlined_icon import MaterialaccountCircleOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccountCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccountCircleOutlinedIcon = MaterialaccountCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
