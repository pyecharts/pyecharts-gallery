
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Gauge

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://gallery.echartsjs.com/editor.html?c=xH1vxib94f

目前无法实现的功能:

1、暂无
"""

(
    Gauge(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(series_name="业务指标", data_pair=[["完成率", 55.5]])
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    .set_series_opts(
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=30
            )
        )
    )
    .render("gauge_change_color.html")
)

```

<iframe width="100%" height="800px" src="Gauge/gauge_change_color.html"></iframe>
