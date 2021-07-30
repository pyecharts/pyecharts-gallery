
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Graphic 组件示例"),
        graphic_opts=[
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(
                    rotation=JsCode("Math.PI / 4"),
                    bounding="raw",
                    right=110,
                    bottom=110,
                    z=100,
                ),
                children=[
                    opts.GraphicRect(
                        graphic_item=opts.GraphicItem(
                            left="center", top="center", z=100
                        ),
                        graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                        graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                            fill="rgba(0,0,0,0.3)"
                        ),
                    ),
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(
                            left="center", top="center", z=100
                        ),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text="pyecharts bar chart",
                            font="bold 26px Microsoft YaHei",
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="#fff"
                            ),
                        ),
                    ),
                ],
            )
        ],
    )
    .render("bar_graphic_component.html")
)

```

<iframe width="100%" height="800px" src="Bar/bar_graphic_component.html"></iframe>
