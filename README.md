# mimebytes

- Make repr of `bytes` better in ipython
- Rich outputs in Jupyter using `_repr_png_` and `_repr_jpeg_`

```python
In [1]: from mimebytes import mime

In [2]: with open('image.png', 'rb') as f:
   ...:     content = f.read()

In [3]: mime(content, 'image/png')
Out[3]: PNGBytes<376151> (image/png)
```

![preview](https://raw.githubusercontent.com/banesullivan/mimebytes/main/jupyter.png)

If [`python-magic`](https://pypi.org/project/python-magic/) is installed,
you do not need to specify the mimetype as it will be autodetected.

```python
In [1]: from mimebytes import mime

In [2]: with open('image.png', 'rb') as f:
   ...:     content = f.read()

In [3]: mime(content)
Out[3]: PNGBytes<376151> (image/png)
```

## Why?

Have you ever tried to output a bytes object in ipython and seen a garbled mess
like the following? *If so, then this is for you.*

```ipython
In [1]: with open('image.png', 'rb') as f:
   ...:     content = f.read()
   ...:

In [2]: content
Out[2]: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x00\x00\x00\x01\xd1\x08\x06\x00\x00\x00\x1c\xf2\x01\xed\x00\x00 \x00IDATx\x9c\xec\xbdy\x9cfWU\xef\xfd\xddk\xefs\x9e\xb1\xc6\xee\xeaNO\xe9$\x9d9\x84$\x1d\x08\x19\x84@\x80\x10@\x01\x15d\x14D\x05\x15\x05\x05\xe1\xe2\xf0^\xbdr\xf5\xeau\x06\x04E#*<... continues on forever>
```
