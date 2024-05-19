from apysc._material_design.icon.material_face_icon import MaterialfaceIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfaceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfaceIcon = MaterialfaceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
