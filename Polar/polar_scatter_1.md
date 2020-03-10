
## pyecharts 代码 / 效果

```python
import random

from pyecharts import options as opts
from pyecharts.charts import Polar

c = (
    Polar()
    .add("", [(10, random.randint(1, 100)) for i in range(300)], type_="scatter")
    .add("", [(11, random.randint(1, 100)) for i in range(300)], type_="scatter")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter1"))
    .render("polar_scatter_1.html")
)

```

<iframe width="100%" height="800px" src="Polar/polar_scatter_1.html"></iframe>
