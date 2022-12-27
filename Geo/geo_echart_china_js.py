from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

# try:
#     register_url("https://assets.pyecharts.org/assets/v5/maps/")
# except Exception:
#     import ssl
#
#     ssl._create_default_https_context = ssl._create_unverified_context
#     register_url("https://assets.pyecharts.org/assets/v5/maps/")

geo = (
    Geo()
    .add_schema(maptype="海淀区")
    .set_global_opts(title_opts=opts.TitleOpts(title="海淀区"))
    .render("geo_echart_china_js.html")
)
