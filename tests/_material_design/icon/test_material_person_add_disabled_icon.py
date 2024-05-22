from apysc._material_design.icon.material_person_add_disabled_icon import (
    MaterialPersonAddDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPersonAddDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPersonAddDisabledIcon = MaterialPersonAddDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
