
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    .render("map_base.html")
)

```

<iframe width="100%" height="800px" src="Map/map_base.html"></iframe>
