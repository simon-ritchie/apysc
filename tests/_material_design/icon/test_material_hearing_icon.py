from apysc._material_design.icon.material_hearing_icon import MaterialHearingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHearingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHearingIcon = MaterialHearingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
