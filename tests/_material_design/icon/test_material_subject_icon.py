from apysc._material_design.icon.material_subject_icon import MaterialSubjectIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubjectIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubjectIcon = MaterialSubjectIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
