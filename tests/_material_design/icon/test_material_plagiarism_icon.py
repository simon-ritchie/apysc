from apysc._material_design.icon.material_plagiarism_icon import MaterialplagiarismIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplagiarismIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplagiarismIcon = MaterialplagiarismIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
