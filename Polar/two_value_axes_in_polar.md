
## pyecharts 代码 / 效果

```python
import math
import pyecharts.options as opts
from pyecharts.charts import Polar

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-polar

目前无法实现的功能:

1、赞无
"""

data = []

for i in range(0, 101):
    theta = i / 100 * 360
    r = 5 * (1 + math.sin(theta / 180 * math.pi))
    data.append([r, theta])

(
    Polar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(series_name="line", data=data, label_opts=opts.LabelOpts(is_show=False))
    .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(
            start_angle=0, type_="value", is_clockwise=True
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        title_opts=opts.TitleOpts(title="极坐标双数值轴"),
    )
    .render("two_value_axes_in_polar.html")
)

```

<iframe width="100%" height="800px" src="Polar/two_value_axes_in_polar.html"></iframe>
