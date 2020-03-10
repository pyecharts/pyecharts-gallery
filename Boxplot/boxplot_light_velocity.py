import pyecharts.options as opts
from pyecharts.charts import Grid, Boxplot, Scatter


y_data = [
    [
        850,
        740,
        900,
        1070,
        930,
        850,
        950,
        980,
        980,
        880,
        1000,
        980,
        930,
        650,
        760,
        810,
        1000,
        1000,
        960,
        960,
    ],
    [
        960,
        940,
        960,
        940,
        880,
        800,
        850,
        880,
        900,
        840,
        830,
        790,
        810,
        880,
        880,
        830,
        800,
        790,
        760,
        800,
    ],
    [
        880,
        880,
        880,
        860,
        720,
        720,
        620,
        860,
        970,
        950,
        880,
        910,
        850,
        870,
        840,
        840,
        850,
        840,
        840,
        840,
    ],
    [
        890,
        810,
        810,
        820,
        800,
        770,
        760,
        740,
        750,
        760,
        910,
        920,
        890,
        860,
        880,
        720,
        840,
        850,
        850,
        780,
    ],
    [
        890,
        840,
        780,
        810,
        760,
        810,
        790,
        810,
        820,
        850,
        870,
        870,
        810,
        740,
        810,
        940,
        950,
        800,
        810,
        870,
    ],
]
scatter_data = [650, 620, 720, 720, 950, 970]

box_plot = Boxplot()

box_plot = (
    box_plot.add_xaxis(xaxis_data=["expr 0", "expr 1", "expr 2", "expr 3", "expr 4"])
    .add_yaxis(series_name="", y_axis=box_plot.prepare_data(y_data))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            pos_left="center", title="Michelson-Morley Experiment"
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="shadow"),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=True,
            splitarea_opts=opts.SplitAreaOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(formatter="expr {value}"),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="km/s minus 299,000",
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
    )
    .set_series_opts(tooltip_opts=opts.TooltipOpts(formatter="{b}: {c}"))
)

scatter = (
    Scatter()
    .add_xaxis(xaxis_data=["expr 0", "expr 1", "expr 2", "expr 3", "expr 4"])
    .add_yaxis(series_name="", y_axis=scatter_data)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            pos_left="10%",
            pos_top="90%",
            title="upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR",
            title_textstyle_opts=opts.TextStyleOpts(
                border_color="#999", border_width=1, font_size=14
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=False),
        ),
    )
)

grid = (
    Grid()
    .add(
        box_plot,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
    )
    .add(
        scatter,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
    )
    .render("boxplot_light_velocity.html")
)
