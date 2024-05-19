from apysc._material_design.icon.material_screen_share_outlined_icon import MaterialscreenShareOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialscreenShareOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialscreenShareOutlinedIcon = MaterialscreenShareOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
