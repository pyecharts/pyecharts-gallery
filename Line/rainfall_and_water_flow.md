## Echarts 代码 / 效果

[echarts](https://www.echartsjs.com/examples/zh/editor.html?c=grid-multiple ':include :type=iframe width=100% height=800px')

## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line, Grid

# 数据量过大，省略数据参数 timeData, water_flowData, rainfallData
# 请移步至代码源文件中

l1 = (
    Line()
    .add_xaxis(xaxis_data=timeData)
    .add_yaxis(
        series_name="流量",
        y_axis=water_flowData,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="雨量流量关系图", subtitle="数据来自西安兰特水电测控技术有限公司", pos_left="center"
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_show=True,
                is_realtime=True,
                start_value=30,
                end_value=70,
                xaxis_index=[0, 1],
            )
        ],
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
        ),
        yaxis_opts=opts.AxisOpts(max_=500, name="流量(m^3/s)"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "dataZoom": {"yAxisIndex": "none"},
                "restore": {},
                "saveAsImage": {},
            },
        ),
    )
)

l2 = (
    Line()
    .add_xaxis(xaxis_data=timeData)
    .add_yaxis(
        series_name="降雨量",
        y_axis=rainfallData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    .set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                start_value=30,
                end_value=70,
                xaxis_index=[0, 1],
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name="降雨量(mm)"),
        legend_opts=opts.LegendOpts(pos_left="7%"),
    )
)

(
    Grid(init_opts=opts.InitOpts(width="1024px", height="768px"))
    .add(chart=l1, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="35%"))
    .add(
        chart=l2,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="55%", height="35%"),
    )
    .render("rainfall_and_water_flow.html")
)
```

<iframe width="100%" height="800px" src="Line/rainfall_and_water_flow.html"></iframe>