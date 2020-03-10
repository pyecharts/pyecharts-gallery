from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType

c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("", Faker.values(), symbol=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-不同Symbol"))
    .render("effectscatter_symbol.html")
)
