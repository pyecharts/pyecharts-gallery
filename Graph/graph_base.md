
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "结点1", "symbolSize": 10},
    {"name": "结点2", "symbolSize": 20},
    {"name": "结点3", "symbolSize": 30},
    {"name": "结点4", "symbolSize": 40},
    {"name": "结点5", "symbolSize": 50},
    {"name": "结点6", "symbolSize": 40},
    {"name": "结点7", "symbolSize": 30},
    {"name": "结点8", "symbolSize": 20},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
    .render("graph_base.html")
)

```

<iframe width="100%" height="800px" src="Graph/graph_base.html"></iframe>
