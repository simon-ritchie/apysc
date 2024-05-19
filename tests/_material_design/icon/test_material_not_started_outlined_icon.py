from apysc._material_design.icon.material_not_started_outlined_icon import MaterialnotStartedOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotStartedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotStartedOutlinedIcon = MaterialnotStartedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
