from apysc._material_design.icon.material_skip_next_outlined_icon import MaterialskipNextOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialskipNextOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialskipNextOutlinedIcon = MaterialskipNextOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
