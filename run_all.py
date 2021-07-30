import hashlib
import json
import os
import subprocess
import operator
import random
import time
from typing import Dict, List, Optional

from jinja2 import Template

# 清理的命令
ClearCmd: str = (
    'find ./ -mindepth 2 -type f ! -name "*.py" ! -name "*.json" ! '
    '-path ".//.idea/*" ! -path ".//.mypy_cache/*" ! -path ".//.git/*" '
    "| xargs rm -f"
)

# 需要跳过的文件名
SKIP_FILE: List = [
    ".git",
    ".mypy_cache",
    ".idea",
    "run_all.py",
    "README.md",
    "README_EN.md",
    "LICENSE",
    "index.html",
    "CNAME",
    "favicon.ico",
    "_sidebar.md",
    "_navbar.md",
    "_coverpage.md",
    ".nojekyll",
    ".DS_Store",
    "file_checker.json",
]

# 当前 Demo 的模块
ChartModelDict: Dict = {
    "Bar": "柱状图",
    "Bar3D": "3D 柱状图",
    "BMap": "百度地图",
    "Boxplot": "箱形图",
    "Calendar": "日历图",
    "Candlestick": "K 线图",
    "Dataset": "数据集",
    "EffectScatter": "涟漪散点图",
    "Funnel": "漏斗图",
    "Gauge": "仪表盘",
    "Geo": "地理坐标",
    "Graph": "关系图",
    "Graphic": "图形组件",
    "Grid": "组合组件",
    "Heatmap": "热力图",
    "Image": "图片",
    "Line": "折线图",
    "Line3D": "3D 折线图",
    "Liquid": "水球图",
    "Map": "地图",
    "Map3D": "3D 地图",
    "MapGlobe": "Globe 地图",
    "Overlap": "层叠组件",
    "Page": "页面组件",
    "Parallel": "平行坐标系",
    "PictorialBar": "象型柱图",
    "Pie": "饼状图",
    "Polar": "极坐标系",
    "Radar": "雷达图",
    "Sankey": "桑基图",
    "Scatter": "散点图",
    "Scatter3D": "3D 散点图",
    "Sunburst": "旭日图",
    "Surface3D": "3D 曲面",
    "Tab": "分页组件",
    "Table": "表格组件",
    "Theme": "主题组件",
    "ThemeRiver": "主题河流图",
    "Timeline": "时间轴组件",
    "Tree": "树图",
    "Treemap": "矩形树图",
    "WordCloud": "词云图",
}

# Markdown 模版
ChartMarkdownModel: str = """
## pyecharts 代码 / 效果

```python
{code}
```

<iframe width="100%" height="800px" src="{html}"></iframe>
"""

# 每个图的 README 的模版
ChartREADMEModel: str = "- [{chart_name}]({path} ':type=code')"

# 侧边栏模版
SidebarModel: str = """
- 概览
    - [中文简介](README.md)
    - [英文简介](README_EN.md)
- 示例
    {% for chart in charts -%}
        - [**{{ chart.name }} {{ chart.type }}**]({{ chart.type }}/README.md)
        {% for info in chart.info -%}
            {{ info }}
        {% endfor %}
    {% endfor %}
"""


def get_md5_of_file(filename: str) -> Optional[str]:
    """
    获取文件的 MD5
    :param filename: 文件名
    :return: None or md5 string
    """
    if not os.path.isfile(filename):
        return None
    md5_obj = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            md5_obj.update(b)
    return md5_obj.hexdigest()


def save_md5_to_json(md5_json: dict):
    """
    保存所有的文件 md5 到 json 文件中
    :param md5_json: md5 dict
    """
    with open("file_checker.json", "a") as md5_f:
        md5_f.write(json.dumps(md5_json))


# 清理删除命令
# 命令解释：搜索当前目录下除根目录外的子文件夹中后缀不为 .py 和 .json 的文件，且忽略 .idea, .mypy_cache, .git 文件夹
# find ./ -mindepth 2 -type f ! -name "*.py" ! -name "*.json" !
# -path ".//.idea/*" ! -path ".//.mypy_cache/*" ! -path ".//.git/*"
# {上面的命令} | xargs rm -f
# {上面的命令} -exec rm -f {} \;
def clear_all():
    print("正在清理...")
    try:
        print(ClearCmd)
        os.system(ClearCmd)
        time.sleep(3)
        print("清理成功!")
    except Exception as err:
        raise err


def write_chart_markdown_and_html(
    chart_script: str, chart_script_name: str, folder: str
):
    """
    保存各图的 markdown 和 html
    :param chart_script: 路径
    :param chart_script_name: 脚本名称
    :param folder: 文件夹名字
    """
    chart_model = ChartMarkdownModel
    with open(f"{chart_script_name}.md", "w") as md:
        with open(chart_script, "r") as f:
            chart_model = chart_model.replace("{code}", f.read())
        subprocess.check_call(["python3", chart_script], stdout=subprocess.PIPE)

        chart_model = chart_model.replace(
            "{html}", f"{folder}/{chart_script_name}.html"
        )
        md.write(chart_model)


def update_chart_readme_markdown(chart_script_name: str, folder: str):
    """
    更新各图的 README.md
    :param chart_script_name: 脚本名称
    :param folder: 文件夹名字
    """
    readme_model = ChartREADMEModel
    with open(f"README.md", "a") as readme:
        readme_model = readme_model.replace(
            "{chart_name}", f"{folder.capitalize()} - {chart_script_name.capitalize()}"
        )
        readme_model = readme_model.replace(
            "{path}", f"{folder}/{chart_script_name}.md"
        )
        readme.write(readme_model + "\n")


def run_all() -> List[Dict]:
    charts = []
    for folder in os.listdir():
        if folder in SKIP_FILE:
            continue
        print(f"当前图的类型: {folder}")
        os.chdir(folder)
        for chart_script in os.listdir():
            if ".py" not in chart_script:
                continue
            else:
                print(f"当前图的类型对应的示例: {folder}/{chart_script}")
                # TODO 后续进行开发(新增图后局部更新)
                # file_md5 = get_md5_of_file(filename=f"{chart_script}")
                chart_script_name = chart_script.replace(".py", "")
                # 更新各板块图的 md 和对应的 html
                write_chart_markdown_and_html(chart_script, chart_script_name, folder)
                # 更新各板块图的 README.md
                update_chart_readme_markdown(chart_script_name, folder)
        # 封装数据
        with open(f"README.md", "r") as f:
            charts.append(
                {
                    "name": ChartModelDict[folder],
                    "type": folder,
                    "info": [d.replace("\n", "") for d in f.readlines()],
                }
            )

        # 返回上一级
        os.chdir("../")
    return charts


def format_code():
    os.system("black .")
    os.system("flake8 --max-line-length 89 --ignore=F401,E501")


def write_sidebar_markdown(charts: Dict):
    """
    更新项目侧边栏的 Markdown
    :param charts: 图的数据
    """
    with open("_sidebar.md", "w") as sidebar_f:
        template = Template(SidebarModel)
        result = template.render(charts)
        sidebar_f.write(result)


if __name__ == "__main__":
    # 清理所有旧版数据
    clear_all()
    # 格式化代码
    format_code()
    # 运行
    all_charts = run_all()
    all_charts.sort(key=operator.itemgetter("type"))
    # 更新 SideBar
    write_sidebar_markdown(charts={"charts": all_charts})
