from apysc._material_design.icon.material_view_stream_icon import MaterialviewStreamIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewStreamIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewStreamIcon = MaterialviewStreamIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
