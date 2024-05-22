from apysc._material_design.icon.material_plagiarism_icon import MaterialPlagiarismIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlagiarismIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlagiarismIcon = MaterialPlagiarismIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
