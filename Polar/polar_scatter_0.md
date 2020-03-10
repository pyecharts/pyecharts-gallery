
## pyecharts 代码 / 效果

```python
import random

from pyecharts import options as opts
from pyecharts.charts import Polar

data = [(i, random.randint(1, 100)) for i in range(101)]
c = (
    Polar()
    .add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter0"))
    .render("polar_scatter_0.html")
)

```

<iframe width="100%" height="800px" src="Polar/polar_scatter_0.html"></iframe>
