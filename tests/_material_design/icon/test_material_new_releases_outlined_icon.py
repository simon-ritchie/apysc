from apysc._material_design.icon.material_new_releases_outlined_icon import (
    MaterialNewReleasesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNewReleasesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNewReleasesOutlinedIcon = MaterialNewReleasesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
