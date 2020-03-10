
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import MapGlobe
from pyecharts.faker import POPULATION

data = [x for _, x in POPULATION[1:]]
low, high = min(data), max(data)

c = (
    MapGlobe()
    .add_schema()
    .add(
        maptype="world",
        series_name="World Population",
        data_pair=POPULATION[1:],
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_=low,
            max_=high,
            range_text=["max", "min"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        )
    )
    .render("map_globe_base.html")
)

```

<iframe width="100%" height="800px" src="MapGlobe/map_globe_base.html"></iframe>
