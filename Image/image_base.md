
## pyecharts 代码 / 效果

```python
from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts


image = Image()

img_src = (
    "https://user-images.githubusercontent.com/19553554/"
    "71825144-2d568180-30d6-11ea-8ee0-63c849cfd934.png"
)
image.add(
    src=img_src,
    style_opts={"width": "200px", "height": "200px", "style": "margin-top: 20px"},
)
image.set_global_opts(
    title_opts=ComponentTitleOpts(title="Image-基本示例", subtitle="我是副标题支持换行哦")
)
image.render("image_base.html")

```

<iframe width="100%" height="800px" src="Image/image_base.html"></iframe>
