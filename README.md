# mimebytes

A thin wrapper of `bytes` to make the repr better in ipython.

```py
from mimebytes import ImageBytes
with open('image.png', 'rb') as f:
    content = f.read()

ImageBytes(content, 'image/png')
```

![preview](https://raw.githubusercontent.com/banesullivan/mimebytes/main/jupyter.png)
