from apysc._material_design.icon.material_not_started_icon import MaterialnotStartedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotStartedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotStartedIcon = MaterialnotStartedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
