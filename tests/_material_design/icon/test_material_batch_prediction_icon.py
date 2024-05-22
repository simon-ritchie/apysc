from apysc._material_design.icon.material_batch_prediction_icon import (
    MaterialBatchPredictionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBatchPredictionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBatchPredictionIcon = MaterialBatchPredictionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
