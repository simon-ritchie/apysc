from apysc._material_design.icon.material_view_stream_outlined_icon import MaterialviewStreamOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewStreamOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewStreamOutlinedIcon = MaterialviewStreamOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
