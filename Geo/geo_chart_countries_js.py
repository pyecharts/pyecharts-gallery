from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

# try:
#     register_url("https://assets.pyecharts.org/assets/maps/")
# except Exception:
#     import ssl
#
#     ssl._create_default_https_context = ssl._create_unverified_context
#     register_url("https://assets.pyecharts.org/assets/maps/")

geo = (
    Geo()
    .add_schema(maptype="瑞士")
    .set_global_opts(title_opts=opts.TitleOpts(title="瑞士"))
    .render("geo_chart_countries_js.html")
)
