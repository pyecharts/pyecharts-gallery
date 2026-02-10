from pyecharts import options as opts
from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType


c = (
    Custom()
    .register_echarts_x(chart_type=ChartType.DOUGHNUT)
    .add(
        series_name="A",
        render_item=ChartType.DOUGHNUT,
        coordinate_system="none",
        item_payload_opts={
            "center": ["25%", "50%"],
            "radius": ["50%", "65%"],
            "segmentCount": 8,
            "label": {
                "show": True,
                "formatter": "{c}/{b}",
                "fontSize": 35,
                "color": "#555",
            }
        },
        data=[5],
        itemstyle_opts={},
        emphasis_opts=opts.EmphasisOpts(
            itemstyle_opts={
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.2)",
            },
        )
    )
    .add(
        series_name="B",
        render_item=ChartType.DOUGHNUT,
        coordinate_system="none",
        item_payload_opts={
            "center": ["75%", "50%"],
            "radius": ["50%", "65%"],
            "segmentCount": 6,
            "label": {
                "show": True,
                "formatter": "{d} 🎉",
                "fontSize": 35,
                "color": "#555",
            }
        },
        data=[6],
        itemstyle_opts={},
        emphasis_opts=opts.EmphasisOpts(
            itemstyle_opts={
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.2)",
            },
        )
    )
    .render("custom_doughnut.html")
)
