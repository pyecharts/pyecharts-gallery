## Echarts 代码 / 效果

[echarts](https://www.echartsjs.com/examples/zh/editor.html?c=area-rainfall ':include :type=iframe width=100% height=800px')

## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line

# 数据量过大，省略数据参数 x_data, y_data_flow_amount, y_data_rain_fall_amount
# 请移步至代码源文件中

(
    Line(init_opts=opts.InitOpts(width="1680px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="流量",
        y_axis=y_data_flow_amount,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        linestyle_opts=opts.LineStyleOpts(),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="降雨量",
        y_axis=y_data_rain_fall_amount,
        yaxis_index=1,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        linestyle_opts=opts.LineStyleOpts(),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="降雨量(mm)",
            name_location="start",
            type_="value",
            max_=5,
            is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="雨量流量关系图",
            subtitle="数据来自西安兰特水电测控技术有限公司",
            pos_left="center",
            pos_top="top",
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100),
            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
        ],
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="流量(m^3/s)", type_="value", max_=500),
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
            data=[
                opts.MarkAreaItem(
                    name="流量",
                    x=("2009/9/12-7:00", "2009/9/22-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#DCA3A2", opacity=0.5),
                ),
                opts.MarkAreaItem(
                    name="降雨量",
                    x=("2009/9/10-7:00", "2009/9/20-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#A1A9AF", opacity=0.5),
                ),
            ],
        ),
        axisline_opts=opts.AxisLineOpts(),
    )
    .render("rainfall.html")
)
```

<iframe width="100%" height="800px" src="Line/rainfall.html"></iframe>