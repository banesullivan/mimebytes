class MimeBytes(bytes):
    """Wrapper class to make repr of bytes better in ipython."""

    def __new__(cls, source: bytes, mimetype: str = None):
        self = super().__new__(cls, source)
        self._mime_type = mimetype
        return self

    @property
    def mimetype(self):
        return self._mime_type

    def __repr__(self):
        if self.mimetype:
            return f"{self.__class__.__name__}<{len(self)}> ({self.mimetype})"
        return f"{self.__class__.__name__}<{len(self)}> (un-mimed)"
