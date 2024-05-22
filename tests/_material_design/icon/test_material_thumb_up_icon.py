from apysc._material_design.icon.material_thumb_up_icon import MaterialThumbUpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialThumbUpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialThumbUpIcon = MaterialThumbUpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
