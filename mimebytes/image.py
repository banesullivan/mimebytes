from mimebytes.base import Bytes


class PNGBytes(Bytes):
    """Wrapper class to make repr of image bytes better in ipython."""

    def _repr_png_(self):
        return self


class JPEGBytes(Bytes):
    """Wrapper class to make repr of jpeg bytes better in ipython."""

    def _repr_jpeg_(self):
        return self


class SVGBytes(Bytes):
    """Wrapper class to make repr of svg bytes better in ipython."""

    def _repr_svg_(self):
        return self
