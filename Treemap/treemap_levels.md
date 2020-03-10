
## pyecharts 代码 / 效果

```python
import json

from pyecharts import options as opts
from pyecharts.charts import TreeMap


with open("treemap.json", "r", encoding="utf-8") as f:
    data = json.load(f)
c = (
    TreeMap()
    .add(
        series_name="演示数据",
        data=data,
        levels=[
            opts.TreeMapLevelsOpts(
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color="#555", border_width=4, gap_width=4
                )
            ),
            opts.TreeMapLevelsOpts(
                color_saturation=[0.3, 0.6],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0.7, gap_width=2, border_width=2
                ),
            ),
            opts.TreeMapLevelsOpts(
                color_saturation=[0.3, 0.5],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0.6, gap_width=1
                ),
            ),
            opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-Levels-配置"))
    .render("treemap_levels.html")
)

```

<iframe width="100%" height="800px" src="Treemap/treemap_levels.html"></iframe>
