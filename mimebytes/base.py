class Bytes(bytes):
    """Wrapper class to make repr of bytes better in ipython."""

    def __new__(cls, source: bytes, mimetype: str = None):
        self = super().__new__(cls, source)
        try:
            import magic
        except ImportError:
            pass
        else:
            mimetype = magic.Magic(mime=True).from_buffer(source)
        self._mime_type = mimetype
        return self

    @property
    def mimetype(self):
        return self._mime_type

    def __repr__(self):
        if self.mimetype:
            return f"{self.__class__.__name__}<{len(self)}> ({self.mimetype})"
        return f"{self.__class__.__name__}<{len(self)}> (un-mimed)"


class JSONBytes(Bytes):
    """Wrapper class to make repr of json bytes better in ipython."""

    def _repr_json_(self):
        return self


class HTMLBytes(Bytes):
    """Wrapper class to make repr of html bytes better in ipython."""

    def _repr_html_(self):
        return self
