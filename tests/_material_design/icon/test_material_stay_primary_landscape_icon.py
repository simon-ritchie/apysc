from apysc._material_design.icon.material_stay_primary_landscape_icon import MaterialstayPrimaryLandscapeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstayPrimaryLandscapeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstayPrimaryLandscapeIcon = MaterialstayPrimaryLandscapeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
