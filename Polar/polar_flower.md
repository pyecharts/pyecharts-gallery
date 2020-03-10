
## pyecharts 代码 / 效果

```python
import math

from pyecharts import options as opts
from pyecharts.charts import Polar

data = []
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
c = (
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(start_angle=0, min_=0))
    .add("flower", data, label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Flower"))
    .render("polar_flower.html")
)

```

<iframe width="100%" height="800px" src="Polar/polar_flower.html"></iframe>
