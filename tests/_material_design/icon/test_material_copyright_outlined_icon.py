from apysc._material_design.icon.material_copyright_outlined_icon import MaterialcopyrightOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcopyrightOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcopyrightOutlinedIcon = MaterialcopyrightOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
