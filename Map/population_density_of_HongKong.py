import asyncio
from aiohttp import TCPConnector, ClientSession

import pyecharts.options as opts
from pyecharts.charts import Map

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=map-HK
"""

WIKI_LINK = (
    "http://zh.wikipedia.org/wiki/"
    "%E9%A6%99%E6%B8%AF%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83#cite_note-12"
)


async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()


# 下载香港地图
data = asyncio.run(
    get_json_data(url="https://echarts.apache.org/examples/data/asset/geo/HK.json")
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
    "Central and Western": "中西区",
    "Eastern": "东区",
    "Islands": "离岛",
    "Kowloon City": "九龙城",
    "Kwai Tsing": "葵青",
    "Kwun Tong": "观塘",
    "North": "北区",
    "Sai Kung": "西贡",
    "Sha Tin": "沙田",
    "Sham Shui Po": "深水埗",
    "Southern": "南区",
    "Tai Po": "大埔",
    "Tsuen Wan": "荃湾",
    "Tuen Mun": "屯门",
    "Wan Chai": "湾仔",
    "Wong Tai Sin": "黄大仙",
    "Yau Tsim Mong": "油尖旺",
    "Yuen Long": "元朗",
}

(
    Map()
    .add_js_funcs("echarts.registerMap('HK', {});".format(data))
    .add(
        series_name="香港18区人口密度",
        maptype="HK",
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
    .render("population_density_of_HongKong.html")
)
