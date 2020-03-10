
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

l1 = (
    Liquid()
    .add("lq", [0.6, 0.7], center=["60%", "50%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="多个 Liquid 显示"))
)

l2 = Liquid().add(
    "lq",
    [0.3254],
    center=["25%", "50%"],
    label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),
)

grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
grid.render("multiple_liquid.html")

```

<iframe width="100%" height="800px" src="Liquid/multiple_liquid.html"></iframe>
