from apysc._material_design.icon.material_new_releases_icon import MaterialnewReleasesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnewReleasesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnewReleasesIcon = MaterialnewReleasesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
