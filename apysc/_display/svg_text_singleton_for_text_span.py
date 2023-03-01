"""The class implementation for the SVG text's singleton instance to make a
text span instance.
"""

from typing import Dict, Optional, TYPE_CHECKING

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
        import apysc as ap

        stage: ap.Stage = ap.get_stage()
        stage_id: int = id(stage)
        if stage_id in cls._stage_id_key_svg_texts:
            return cls._stage_id_key_svg_texts[stage_id]

        svg_text: ap.SVGText = ap.SVGText(text="")
        cls._stage_id_key_svg_texts[stage_id] = svg_text
        return svg_text
