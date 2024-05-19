from apysc._material_design.icon.material_cached_outlined_icon import MaterialcachedOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcachedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcachedOutlinedIcon = MaterialcachedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
