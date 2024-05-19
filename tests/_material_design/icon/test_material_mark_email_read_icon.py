from apysc._material_design.icon.material_mark_email_read_icon import MaterialmarkEmailReadIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmarkEmailReadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmarkEmailReadIcon = MaterialmarkEmailReadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
