from mimebytes.mime import MimeBytes


class ImageBytes(MimeBytes):
    """Wrapper class to make repr of image bytes better in ipython."""

    def _repr_png_(self):
        if self.mimetype == "image/png":
            return self

    def _repr_jpeg_(self):
        if self.mimetype == "image/jpeg":
            return self
