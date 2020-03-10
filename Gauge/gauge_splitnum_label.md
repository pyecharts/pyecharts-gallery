
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "业务指标",
        [("完成率", 55.5)],
        split_number=5,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
            )
        ),
        detail_label_opts=opts.LabelOpts(formatter="{value}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Gauge-分割段数-Label"),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("gauge_splitnum_label.html")
)

```

<iframe width="100%" height="800px" src="Gauge/gauge_splitnum_label.html"></iframe>
