from apysc._material_design.icon.material_subject_outlined_icon import MaterialsubjectOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsubjectOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsubjectOutlinedIcon = MaterialsubjectOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
