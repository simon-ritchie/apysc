from apysc._material_design.icon.material_report_problem_icon import (
    MaterialreportProblemIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreportProblemIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreportProblemIcon = MaterialreportProblemIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
