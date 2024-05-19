from apysc._material_design.icon.material_add_task_outlined_icon import (
    MaterialaddTaskOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddTaskOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddTaskOutlinedIcon = MaterialaddTaskOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
