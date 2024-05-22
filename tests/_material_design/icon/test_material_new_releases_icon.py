from apysc._material_design.icon.material_new_releases_icon import (
    MaterialNewReleasesIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNewReleasesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNewReleasesIcon = MaterialNewReleasesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
