## Echarts 代码 / 效果

[echarts](https://www.echartsjs.com/examples/zh/editor.html?c=pie-doughnut ':include :type=iframe width=100% height=800px')

## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Pie

x_data = ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
y_data = [335, 310, 234, 135, 1548]

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add(
        series_name="访问来源",
        data_pair=[list(z) for z in zip(x_data, y_data)],
        radius=["50%", "70%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        # label_opts=opts.LabelOpts(formatter="{b}: {c}")
    )
    .render("doughnut_chart.html")
)
```

<iframe width="100%" height="800px" src="Pie/doughnut_chart.html"></iframe>