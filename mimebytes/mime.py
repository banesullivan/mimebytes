from mimebytes.base import Bytes, HTMLBytes, JSONBytes
from mimebytes.image import JPEGBytes, PNGBytes, SVGBytes

MIME_MAPPING = {
    "image/png": PNGBytes,
    "image/jpeg": JPEGBytes,
    "image/svg+xml": SVGBytes,
    "application/json": JSONBytes,
    "text/html": HTMLBytes,
}


def mime(source, mimetype=None):
    """Wrapper class to make repr of bytes better in ipython."""
    if mimetype is None:
        try:
            import magic
        except ImportError:
            pass
        else:
            mimetype = magic.Magic(mime=True).from_buffer(source)
    if mimetype in MIME_MAPPING:
        return MIME_MAPPING[mimetype](source, mimetype)
    return Bytes(source, mimetype)
