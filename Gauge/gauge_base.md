
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add("", [("完成率", 66.6)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    .render("gauge_base.html")
)

```

<iframe width="100%" height="800px" src="Gauge/gauge_base.html"></iframe>
