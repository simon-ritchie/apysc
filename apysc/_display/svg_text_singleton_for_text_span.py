"""The class implementation for the SVG text's singleton instance to make a
text span instance.
"""

from typing import TYPE_CHECKING
from typing import Dict

if TYPE_CHECKING:
    from apysc._display.svg_text import SVGText


class SVGTextSingletonForTextSpan:
    _stage_id_key_svg_texts: Dict[int, "SVGText"] = {}

    @classmethod
    def get_instance(cls) -> "SVGText":
        """
        Get a text instance.

        Returns
        -------
        svg_text : SVGText
            A target text instance.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._display.svg_text import SVGText
        from apysc._type.boolean import Boolean

        stage: Stage = get_stage()
        stage_id: int = id(stage)
        if stage_id in cls._stage_id_key_svg_texts:
            return cls._stage_id_key_svg_texts[stage_id]

        svg_text: SVGText = SVGText(text="")
        svg_text.visible = Boolean(False)
        cls._stage_id_key_svg_texts[stage_id] = svg_text
        return svg_text
