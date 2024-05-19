from apysc._material_design.icon.material_opacity_outlined_icon import MaterialopacityOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialopacityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialopacityOutlinedIcon = MaterialopacityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
