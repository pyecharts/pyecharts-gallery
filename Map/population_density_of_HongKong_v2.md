
## pyecharts 代码 / 效果

```python
import ssl

import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.datasets import register_url

"""
Gallery 使用 pyecharts 1.1.0 和 echarts-china-cities-js
参考地址: https://echarts.apache.org/examples/editor.html?c=map-HK
"""
ssl._create_default_https_context = ssl._create_unverified_context
# 与 pyecharts 注册，当画香港地图的时候，用 echarts-china-cities-js
register_url("https://echarts-maps.github.io/echarts-china-cities-js")

WIKI_LINK = (
    "http://zh.wikipedia.org/wiki/"
    "%E9%A6%99%E6%B8%AF%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83#cite_note-12"
)
MAP_DATA = [
    ["中西区", 20057.34],
    ["湾仔", 15477.48],
    ["东区", 31686.1],
    ["南区", 6992.6],
    ["油尖旺", 44045.49],
    ["深水埗", 40689.64],
    ["九龙城", 37659.78],
    ["黄大仙", 45180.97],
    ["观塘", 55204.26],
    ["葵青", 21900.9],
    ["荃湾", 4918.26],
    ["屯门", 5881.84],
    ["元朗", 4178.01],
    ["北区", 2227.92],
    ["大埔", 2180.98],
    ["沙田", 9172.94],
    ["西贡", 3368],
    ["离岛", 806.98],
]


NAME_MAP_DATA = {
    # "key": "value"
    # "name on the hong kong map": "name in the MAP DATA",
    "中西区": "中西区",
    "东区": "东区",
    "离岛区": "离岛",
    "九龙城区": "九龙城",
    "葵青区": "葵青",
    "观塘区": "观塘",
    "北区": "北区",
    "西贡区": "西贡",
    "沙田区": "沙田",
    "深水埗区": "深水埗",
    "南区": "南区",
    "大埔区": "大埔",
    "荃湾区": "荃湾",
    "屯门区": "屯门",
    "湾仔区": "湾仔",
    "黄大仙区": "黄大仙",
    "油尖旺区": "油尖旺",
    "元朗区": "元朗",
}

(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add(
        series_name="香港18区人口密度",
        maptype="香港",
        data_pair=MAP_DATA,
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="香港18区人口密度 （2011）",
            subtitle="人口密度数据来自Wikipedia",
            subtitle_link=WIKI_LINK,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c} (p / km2)"
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=800,
            max_=50000,
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("population_density_of_HongKong_v2.html")
)

```

<iframe width="100%" height="800px" src="Map/population_density_of_HongKong_v2.html"></iframe>
