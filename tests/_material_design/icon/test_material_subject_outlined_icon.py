from apysc._material_design.icon.material_subject_outlined_icon import (
    MaterialSubjectOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubjectOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubjectOutlinedIcon = MaterialSubjectOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
