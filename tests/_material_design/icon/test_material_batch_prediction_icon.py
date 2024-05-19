from apysc._material_design.icon.material_batch_prediction_icon import (
    MaterialbatchPredictionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbatchPredictionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbatchPredictionIcon = MaterialbatchPredictionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
