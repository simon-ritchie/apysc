from apysc._material_design.icon.material_outbond_outlined_icon import MaterialoutbondOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialoutbondOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialoutbondOutlinedIcon = MaterialoutbondOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
