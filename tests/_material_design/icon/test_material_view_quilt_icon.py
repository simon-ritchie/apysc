from apysc._material_design.icon.material_view_quilt_icon import MaterialViewQuiltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewQuiltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewQuiltIcon = MaterialViewQuiltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
