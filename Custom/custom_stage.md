
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType


raw_data = [
    ('2024-09-07 06:12', '2024-09-07 06:12', 'Awake'),
    ('2024-09-07 06:15', '2024-09-07 06:18', 'Awake'),
    ('2024-09-07 08:59', '2024-09-07 09:00', 'Awake'),
    ('2024-09-07 05:45', '2024-09-07 06:12', 'REM'),
    ('2024-09-07 07:37', '2024-09-07 07:56', 'REM'),
    ('2024-09-07 08:56', '2024-09-07 08:59', 'REM'),
    ('2024-09-07 09:08', '2024-09-07 09:29', 'REM'),
    ('2024-09-07 05:45', '2024-09-07 06:12', 'REM'),
    ('2024-09-07 03:12', '2024-09-07 03:27', 'Core'),
    ('2024-09-07 04:02', '2024-09-07 04:36', 'Core'),
    ('2024-09-07 04:40', '2024-09-07 04:48', 'Core'),
    ('2024-09-07 04:57', '2024-09-07 05:45', 'Core'),
    ('2024-09-07 06:12', '2024-09-07 06:15', 'Core'),
    ('2024-09-07 06:18', '2024-09-07 07:37', 'Core'),
    ('2024-09-07 07:56', '2024-09-07 08:56', 'Core'),
    ('2024-09-07 09:00', '2024-09-07 09:08', 'Core'),
    ('2024-09-07 09:29', '2024-09-07 10:41', 'Core'),
    ('2024-09-07 03:27', '2024-09-07 04:02', 'Deep'),
    ('2024-09-07 04:36', '2024-09-07 04:40', 'Deep'),
    ('2024-09-07 04:48', '2024-09-07 04:57', 'Deep')
]

data = [
    [
        JsCode(f"new Date('{start}')"),
        JsCode(f"new Date('{end}')"),
        stage,
    ]
    for start, end, stage in raw_data
]

format_time_js_func = """
function formatTime(time) {
    const minutes = time.getMinutes();
    const minStr = minutes < 10 ? '0' + minutes : minutes;
    return time.getHours() + ':' + minStr;
}
"""


c = (
    Custom()
    .register_echarts_x(chart_type=ChartType.STAGE)
    .add_js_funcs(format_time_js_func)
    .add(
        series_name="custom",
        render_item=ChartType.STAGE,
        color_by="data",
        item_payload_opts={
            "envelope": {},
        },
        encode={
            "x": [0, 1],
            "y": 2,
            "tooltip": [0, 1],
        }
    )
    .add_dataset(source=data)
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            value_formatter=JsCode(
                "(params) => {return formatTime(params[0]) + '-' + formatTime(params[1])}",
            ),
        ),
        xaxis_opts=opts.AxisOpts(
            type_="time",
            splitline_opts=opts.SplitLineOpts(
                is_show=True,
                linestyle_opts=opts.LineStyleOpts(type_="dashed", opacity=0.8),
            ),
            min_=JsCode("(value) => {return Math.floor(value.min / (60 * 60 * 1000)) * 60 * 60 * 1000;}"),
            max_=JsCode("(value) => {return Math.ceil(value.max / (60 * 60 * 1000)) * 60 * 60 * 1000;}"),
            axislabel_opts=opts.LabelOpts(color="#c6c6c6"),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="category",
            splitline_opts=opts.SplitLineOpts(is_show=True),
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#ccc"))
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_show=False,
            type_="piecewise",
            is_piecewise=True,
            categories=[0 ,1, 2, 3],
            dimension=2,
            range_color={
              3: '#35349D',
              2: '#3478F6',
              1: '#59AAE1',
              0: '#EF8872',
            },
            series_index=0,
            out_of_range={"color": "#61E6E1"},
        )
    )
)
```

<iframe width="100%" height="800px" src="Custom/custom_stage.html"></iframe>
