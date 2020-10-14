import pyecharts.options as opts
from pyecharts.charts import Line

# 将在 v1.1.0 中更改
from pyecharts.commons.utils import JsCode

"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://echarts.apache.org/examples/editor.html?c=multiple-x-axis

目前无法实现的功能:

1、暂无
"""

js_formatter = """function (params) {
        console.log(params);
        return '降水量  ' + params.value + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
    }"""

(
    Line()
    .add_xaxis(
        xaxis_data=[
            "2016-1",
            "2016-2",
            "2016-3",
            "2016-4",
            "2016-5",
            "2016-6",
            "2016-7",
            "2016-8",
            "2016-9",
            "2016-10",
            "2016-11",
            "2016-12",
        ]
    )
    .extend_axis(
        xaxis_data=[
            "2015-1",
            "2015-2",
            "2015-3",
            "2015-4",
            "2015-5",
            "2015-6",
            "2015-7",
            "2015-8",
            "2015-9",
            "2015-10",
            "2015-11",
            "2015-12",
        ],
        xaxis=opts.AxisOpts(
            type_="category",
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#6e9ef1")
            ),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
            ),
        ),
    )
    .add_yaxis(
        series_name="2015 降水量",
        is_smooth=True,
        symbol="emptyCircle",
        is_symbol_show=False,
        # xaxis_index=1,
        color="#d14a61",
        y_axis=[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .add_yaxis(
        series_name="2016 降水量",
        is_smooth=True,
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#6e9ef1",
        y_axis=[3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7],
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(),
        tooltip_opts=opts.TooltipOpts(trigger="none", axis_pointer_type="cross"),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        ),
    )
    .render("multiple_x_axes.html")
)
