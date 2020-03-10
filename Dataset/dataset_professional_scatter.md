
## pyecharts 代码 / 效果

```python
import json

from pyecharts import options as opts
from pyecharts.charts import Grid, Scatter

with open("life-expectancy-table.json", "r", encoding="utf-8") as f:
    j = json.load(f)

l1_1 = (
    Scatter()
    .add_dataset(
        dimensions=[
            "Income",
            "Life Expectancy",
            "Population",
            "Country",
            {"name": "Year", "type": "ordinal"},
        ],
        source=j,
    )
    .add_yaxis(
        series_name="",
        y_axis=[],
        symbol_size=2.5,
        xaxis_index=0,
        yaxis_index=0,
        encode={"x": "Income", "y": "Life Expectancy", "tooltip": [0, 1, 2, 3, 4]},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value",
            grid_index=0,
            name="Income",
            axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
        ),
        yaxis_opts=opts.AxisOpts(type_="value", grid_index=0, name="Life Expectancy"),
        title_opts=opts.TitleOpts(title="Encode and Matrix"),
    )
)

l1_2 = (
    Scatter()
    .add_dataset()
    .add_yaxis(
        series_name="",
        y_axis=[],
        symbol_size=2.5,
        xaxis_index=1,
        yaxis_index=1,
        encode={"x": "Country", "y": "Income", "tooltip": [0, 1, 2, 3, 4]},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="category",
            grid_index=1,
            name="Country",
            boundary_gap=False,
            axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
        ),
        yaxis_opts=opts.AxisOpts(type_="value", grid_index=1, name="Income"),
    )
)

l2_1 = (
    Scatter()
    .add_dataset()
    .add_yaxis(
        series_name="",
        y_axis=[],
        symbol_size=2.5,
        xaxis_index=2,
        yaxis_index=2,
        encode={"x": "Income", "y": "Population", "tooltip": [0, 1, 2, 3, 4]},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value",
            grid_index=2,
            name="Income",
            axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
        ),
        yaxis_opts=opts.AxisOpts(type_="value", grid_index=2, name="Population"),
    )
)

l2_2 = (
    Scatter()
    .add_dataset()
    .add_yaxis(
        series_name="",
        y_axis=[],
        symbol_size=2.5,
        xaxis_index=3,
        yaxis_index=3,
        encode={"x": "Life Expectancy", "y": "Population", "tooltip": [0, 1, 2, 3, 4]},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value",
            grid_index=3,
            name="Life Expectancy",
            axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
        ),
        yaxis_opts=opts.AxisOpts(type_="value", grid_index=3, name="Population"),
    )
)

grid = (
    Grid(init_opts=opts.InitOpts(width="1280px", height="960px"))
    .add(
        chart=l1_1,
        grid_opts=opts.GridOpts(pos_right="57%", pos_bottom="57%"),
        grid_index=0,
    )
    .add(
        chart=l1_2,
        grid_opts=opts.GridOpts(pos_left="57%", pos_bottom="57%"),
        grid_index=1,
    )
    .add(
        chart=l2_1,
        grid_opts=opts.GridOpts(pos_right="57%", pos_top="57%"),
        grid_index=2,
    )
    .add(
        chart=l2_2, grid_opts=opts.GridOpts(pos_left="57%", pos_top="57%"), grid_index=3
    )
    .render("dataset_professional_scatter.html")
)

```

<iframe width="100%" height="800px" src="Dataset/dataset_professional_scatter.html"></iframe>
