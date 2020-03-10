
## pyecharts 代码 / 效果

```python
import math

from pyecharts import options as opts
from pyecharts.charts import Polar

data = []
for i in range(101):
    theta = i / 100 * 360
    r = 5 * (1 + math.sin(theta / 180 * math.pi))
    data.append([r, theta])
hour = [i for i in range(1, 25)]
c = (
    Polar()
    .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(
            data=hour, type_="value", boundary_gap=False, start_angle=0
        )
    )
    .add("love", data, label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Love"))
    .render("polar_love.html")
)

```

<iframe width="100%" height="800px" src="Polar/polar_love.html"></iframe>
