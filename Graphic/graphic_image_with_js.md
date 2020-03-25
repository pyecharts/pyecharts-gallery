
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid
from pyecharts.faker import Faker

bar = (
    Bar(init_opts=opts.InitOpts(chart_id="1234"))
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Graphic Image（旋转功能）组件示例"),
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
)
c = (
    Grid(init_opts=opts.InitOpts(chart_id="1234"))
    .add(
        chart=bar,
        grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"),
    )
    .add_js_funcs(
        """
        var rotation = 0;
        setInterval(function () {
            chart_1234.setOption({
                graphic: {
                    id: 'logo',
                    rotation: (rotation += Math.PI / 360) % (Math.PI * 2)
                }
            });
        }, 30);
    """
    )
    .render("graphic_image_with_js.html")
)

```

<iframe width="100%" height="800px" src="Graphic/graphic_image_with_js.html"></iframe>
