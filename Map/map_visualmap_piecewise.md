
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
    )
    .render("map_visualmap_piecewise.html")
)

```

<iframe width="100%" height="800px" src="Map/map_visualmap_piecewise.html"></iframe>
