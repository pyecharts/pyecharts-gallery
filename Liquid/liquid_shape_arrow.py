from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType

c = (
    Liquid()
    .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-arrow"))
    .render("liquid_shape_arrow.html")
)
