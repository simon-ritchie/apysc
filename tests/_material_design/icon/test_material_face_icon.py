from apysc._material_design.icon.material_face_icon import MaterialFaceIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFaceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFaceIcon = MaterialFaceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
