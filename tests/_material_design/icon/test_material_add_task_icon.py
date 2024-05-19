from apysc._material_design.icon.material_add_task_icon import MaterialaddTaskIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddTaskIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddTaskIcon = MaterialaddTaskIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
