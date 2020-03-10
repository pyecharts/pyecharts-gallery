
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
        title_opts=opts.TitleOpts(title="Bar-Graphic Rect+Text 2 组件示例"),
        graphic_opts=[
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(left="50%", top="15%"),
                children=[
                    opts.GraphicRect(
                        graphic_item=opts.GraphicItem(
                            z=100, left="center", top="middle"
                        ),
                        graphic_shape_opts=opts.GraphicShapeOpts(width=190, height=90),
                        graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                            fill="#fff",
                            stroke="#555",
                            line_width=2,
                            shadow_blur=8,
                            shadow_offset_x=3,
                            shadow_offset_y=3,
                            shadow_color="rgba(0,0,0,0.3)",
                        ),
                    ),
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(
                            left="center", top="middle", z=100
                        ),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text=JsCode(
                                "['横轴表示数据类别',"
                                "'纵轴表示数值的值',"
                                "'这个文本块可以放在图中各',"
                                "'种位置'].join('\\n')"
                            ),
                            font="14px Microsoft YaHei",
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="#333"
                            ),
                        ),
                    ),
                ],
            )
        ],
    )
    .render("graphic_rect_bar1.html")
)

```

<iframe width="100%" height="800px" src="Graphic/graphic_rect_bar1.html"></iframe>
