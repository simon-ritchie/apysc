from apysc._material_design.icon.material_person_add_disabled_icon import MaterialpersonAddDisabledIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpersonAddDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpersonAddDisabledIcon = MaterialpersonAddDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
