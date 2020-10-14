import re
import asyncio
from aiohttp import TCPConnector, ClientSession

import pyecharts.options as opts
from pyecharts.charts import TreeMap

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=treemap-drill-down

目前无法实现的功能:

1、层级的样式配置
"""


async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()


# 获取官方的数据
data = asyncio.run(
    get_json_data(
        url="https://echarts.apache.org/examples/data/asset/data/"
        "ec-option-doc-statistics-201604.json"
    )
)

tree_map_data: dict = {"children": []}


def convert(source, target, base_path: str):
    for key in source:
        if base_path != "":
            path = base_path + "." + key
        else:
            path = key
        if re.match(r"/^\$/", key):
            pass
        else:
            child = {"name": path, "children": []}
            target["children"].append(child)
            if isinstance(source[key], dict):
                convert(source[key], child, path)
            else:
                target["value"] = source["$count"]


convert(source=data, target=tree_map_data, base_path="")


(
    TreeMap(init_opts=opts.InitOpts(width="1200px", height="720px"))
    .add(
        series_name="option",
        data=tree_map_data["children"],
        visual_min=300,
        leaf_depth=1,
        # 标签居中为 position = "inside"
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title="Echarts 配置项查询分布", subtitle="2016/04", pos_left="leafDepth"
        ),
    )
    .render("echarts_option_query.html")
)
