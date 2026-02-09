
## pyecharts 代码 / 效果

```python
import random

from pyecharts import options as opts
from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType

data = [
    [0, 26.7, 32.5],
    [1, 25.3, 32.4],
    [2, 24.6, 32.7],
    [3, 26.8, 35.8],
    [4, 26.2, 33.1],
    [5, 24.9, 31.4],
    [6, 25.3, 32.9],
]

x_data = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


c = (
    Custom()
    .register_echarts_x(chart_type=ChartType.BAR_RANGE)
    .add_xaxis(xaxis_data=x_data)
    .add(
        series_name="bar",
        render_item=ChartType.BAR_RANGE,
        data=data,
        item_payload_opts={
            "barWidth": 10,
            "borderRadius": 5,
        },
        encode={
            "x": 0,
            "y": [1, 2],
            "tooltip": [1, 2],
        }
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(type_="value"),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
)
```

<iframe width="100%" height="800px" src="Custom/custom_bar_range.html"></iframe>
