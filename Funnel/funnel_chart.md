## Echarts 代码 / 效果

[echarts](https://echarts.baidu.com/examples/editor.html?c=funnel ':include :type=iframe width=100% height=800px')

## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Funnel

x_data = ["展现", "点击", "访问", "咨询", "订单"]
y_data = [100, 80, 60, 40, 20]

data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

(
    Funnel(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图", subtitle="纯属虚构"))
    .render("funnel_chart.html")
)
```

<iframe width="100%" height="800px" src="Funnel/funnel_chart.html"></iframe>