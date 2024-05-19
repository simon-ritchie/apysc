from apysc._material_design.icon.material_new_releases_outlined_icon import MaterialnewReleasesOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnewReleasesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnewReleasesOutlinedIcon = MaterialnewReleasesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
