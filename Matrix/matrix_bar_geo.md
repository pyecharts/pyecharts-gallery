
## pyecharts 代码 / 效果

> 注意：此示例需要网络请求地图数据

```python
import math
import requests

from pyecharts import options as opts
from pyecharts.charts import Grid, Bar, Geo


def get_geo_json() -> str:
    response = requests.get(
        "https://echarts.apache.org/examples/data/asset/geo/ch.geo.json"
    )
    return response.content.decode()


def calculate_data_extent_on_col(data_source_list, col_idx):
    min_val = float("inf")
    max_val = float("-inf")

    for data_source in data_source_list:
        for data_row in data_source["data"]:
            val = data_row[col_idx]
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val

    return [min_val, max_val]


_colHeaders = ["Region and Time", "Data A", "Data B", "Location"]
_regionColIdx = 0
_geoColIdx = 3

_dataSourceList = [
    {
        "name": "2021",
        "data": [
            ["Valais", 1212, 2321],
            ["Ticino", 7181, 2114],
            ["Graubünden", 2763, 4212],
            ["Uri", 6122, 2942],
            ["Lucerne", 4221, 3411],
            ["Neuchâtel", 7221, 5121],
            ["Jura", 5121, 4121],
            ["Vaud", 6121, 3121],
            ["Thurgau", 7121, 2121],
            ["Schwyz", 8121, 1121],
        ],
    },
    {
        "name": "2020",
        "data": [
            ["Valais", 1010, 2221],
            ["Ticino", 7040, 1810],
            ["Graubünden", 2313, 4011],
            ["Uri", 6011, 2749],
            ["Lucerne", 3329, 3015],
            ["Neuchâtel", 7116, 4822],
            ["Jura", 4968, 3820],
            ["Vaud", 6027, 2928],
            ["Thurgau", 7011, 1725],
            ["Schwyz", 7311, 825],
        ],
    },
]
_colorList = [
    "#ffd10a", "#0ca8df", "#b6d634", "#3fbe95", "#5070dd",
    "#ff994d", "#505372", "#fb628b", "#785db0",
]

matrix_body_data = [
    opts.MatrixBodyDataOpts(value=item, coord=[0, i])
    for (i, item) in enumerate([d[0] for d in _dataSourceList[0]["data"]])
]


grid = Grid()
grid.add_js_funcs(f"echarts.registerMap('target_map', {get_geo_json()})")
for data_col_idx in range(len(_colHeaders)):
    data_extent_on_col = (
        None
        if data_col_idx == _regionColIdx or data_col_idx == _geoColIdx
        else calculate_data_extent_on_col(_dataSourceList, data_col_idx)
    )

    for data_row_idx in range(len(_dataSourceList[0]["data"])):
        if data_col_idx == _regionColIdx:
            pass
        elif data_col_idx == _geoColIdx:
            region_name = _dataSourceList[0]["data"][data_row_idx][_regionColIdx]
            geo = (
                Geo()
                .add_schema(
                    maptype="target_map",
                    aspect_scale=math.cos((47 * math.pi) / 180),
                    coordinate_system="matrix",
                    coord=[data_col_idx, data_row_idx],
                    is_roam=False,
                    selected_mode=False,
                    tooltip_opts=opts.TooltipOpts(is_show=False),
                    regions_opts=[
                        opts.GeoRegionsOpts(
                            name=region_name,
                            is_selected=True,
                            select_itemstyle_opts=opts.ItemStyleOpts(
                                color="#0a41e6",
                            ),
                        ),
                    ],
                    select_opts=opts.SelectOpts(
                        label_opts=opts.LabelOpts(is_show=False),
                    ),
                    animation=False,
                )
            )
            grid.add(chart=geo, grid_opts={})
        else:
            _id = f"mini-bar-{data_col_idx}-{data_row_idx}"
            bar = (
                Bar(init_opts=opts.InitOpts(animation_opts={}))
                .add_xaxis(xaxis_data=["2021", "2020"])
                .add_yaxis(
                    series_name=_dataSourceList[0]["name"],
                    label_opts=opts.LabelOpts(is_show=True, position="insideLeft"),
                    bar_min_height=2, gap="40%", bar_width="80%",
                    itemstyle_opts=opts.ItemStyleOpts(color=_colorList[0 % len(_colorList)]),
                    encode={"label": 0},
                    y_axis=[_dataSourceList[0]["data"][data_row_idx][data_col_idx], ""],
                )
                .add_yaxis(
                    series_name=_dataSourceList[1]["name"],
                    label_opts=opts.LabelOpts(is_show=True, position="insideLeft"),
                    bar_min_height=2, gap="40%", bar_width="80%",
                    itemstyle_opts=opts.ItemStyleOpts(color=_colorList[1 % len(_colorList)]),
                    encode={"label": 0},
                    y_axis=[_dataSourceList[1]["data"][data_row_idx][data_col_idx], ""],
                )
                .set_global_opts(
                    xaxis_opts=opts.AxisOpts(
                        grid_id=_id, type_="value", min_=0,
                        max_=data_extent_on_col[1] if data_extent_on_col else None,
                        is_scale=False,
                        axisline_opts=opts.AxisLineOpts(is_show=False),
                        axistick_opts=opts.AxisTickOpts(is_show=False),
                        splitline_opts=opts.SplitLineOpts(is_show=False),
                        axislabel_opts=opts.LabelOpts(is_show=False),
                    ),
                    yaxis_opts=opts.AxisOpts(
                        grid_id=_id, type_="category", boundary_gap=False, is_inverse=True,
                        axisline_opts=opts.AxisLineOpts(is_show=False),
                        axistick_opts=opts.AxisTickOpts(is_show=False),
                        splitline_opts=opts.SplitLineOpts(is_show=False),
                        axislabel_opts=opts.LabelOpts(is_show=False),
                    ),
                    matrix_opts=opts.MatrixOpts(
                        x_data=opts.MatrixAxisOpts(
                            data=[
                                {"value": item, "size": ("15%" if col_idx == _geoColIdx else (120 if col_idx == _regionColIdx else None))}
                                for col_idx, item in enumerate(_colHeaders)
                            ],
                            itemstyle_opts=opts.ItemStyleOpts(color="#f0f8ff"),
                            label_opts=opts.LabelOpts(font_weight="bold"),
                        ),
                        y_data=opts.MatrixAxisOpts(
                            data=["_" for _ in _dataSourceList[0]["data"]],
                            is_show=False,
                        ),
                        body_opts=opts.MatrixBodyOrCornerOpts(data=matrix_body_data),
                        pos_top=25,
                    ),
                    tooltip_opts={}, legend_opts={},
                )
            )
            grid.add(
                chart=bar,
                grid_opts=opts.GridOpts(
                    coordinate_system="matrix",
                    coord=[data_col_idx, data_row_idx],
                    pos_top="50%", pos_bottom="10%",
                ),
            )

grid.render("matrix_bar_geo.html")
```

<iframe width="100%" height="800px" src="Matrix/matrix_bar_geo.html"></iframe>
