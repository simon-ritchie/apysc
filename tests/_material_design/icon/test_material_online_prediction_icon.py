from apysc._material_design.icon.material_online_prediction_icon import (
    MaterialonlinePredictionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialonlinePredictionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialonlinePredictionIcon = MaterialonlinePredictionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
