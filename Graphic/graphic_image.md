
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Graphic Image 组件示例"),
        graphic_opts=[
            opts.GraphicImage(
                graphic_item=opts.GraphicItem(
                    id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]
                ),
                graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                    image="https://www.echartsjs.com/zh/images/favicon.png",
                    width=150,
                    height=150,
                    opacity=0.4,
                ),
            )
        ],
    )
    .render("graphic_image.html")
)

```

<iframe width="100%" height="800px" src="Graphic/graphic_image.html"></iframe>
