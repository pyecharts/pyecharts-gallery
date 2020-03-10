from pyecharts import options as opts
from pyecharts.charts import Pie

c = (
    Pie()
    .add_dataset(
        source=[
            ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
            ["Matcha Latte", 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
            ["Milk Tea", 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
            ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
            ["Walnut Brownie", 55.2, 67.1, 69.2, 72.4, 53.9, 39.1],
        ]
    )
    .add(
        series_name="Matcha Latte",
        data_pair=[],
        radius=60,
        center=["25%", "30%"],
        encode={"itemName": "product", "value": "2012"},
    )
    .add(
        series_name="Milk Tea",
        data_pair=[],
        radius=60,
        center=["75%", "30%"],
        encode={"itemName": "product", "value": "2013"},
    )
    .add(
        series_name="Cheese Cocoa",
        data_pair=[],
        radius=60,
        center=["25%", "75%"],
        encode={"itemName": "product", "value": "2014"},
    )
    .add(
        series_name="Walnut Brownie",
        data_pair=[],
        radius=60,
        center=["75%", "75%"],
        encode={"itemName": "product", "value": "2015"},
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Dataset simple pie example"),
        legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
    )
    .render("dataset_pie.html")
)
