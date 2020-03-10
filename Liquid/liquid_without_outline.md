
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Liquid

c = (
    Liquid()
    .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-无边框"))
    .render("liquid_without_outline.html")
)

```

<iframe width="100%" height="800px" src="Liquid/liquid_without_outline.html"></iframe>
