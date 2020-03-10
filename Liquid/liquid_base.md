
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Liquid

c = (
    Liquid()
    .add("lq", [0.6, 0.7])
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    .render("liquid_base.html")
)

```

<iframe width="100%" height="800px" src="Liquid/liquid_base.html"></iframe>
