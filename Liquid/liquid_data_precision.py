from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.commons.utils import JsCode

c = (
    Liquid()
    .add(
        "lq",
        [0.3254],
        label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
            ),
            position="inside",
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-数据精度"))
    .render("liquid_data_precision.html")
)
