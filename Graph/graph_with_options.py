from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    opts.GraphNode(name="结点1", symbol_size=10),
    opts.GraphNode(name="结点2", symbol_size=20),
    opts.GraphNode(name="结点3", symbol_size=30),
    opts.GraphNode(name="结点4", symbol_size=40),
    opts.GraphNode(name="结点5", symbol_size=50),
]
links = [
    opts.GraphLink(source="结点1", target="结点2"),
    opts.GraphLink(source="结点2", target="结点3"),
    opts.GraphLink(source="结点3", target="结点4"),
    opts.GraphLink(source="结点4", target="结点5"),
    opts.GraphLink(source="结点5", target="结点1"),
]
c = (
    Graph()
    .add("", nodes, links, repulsion=4000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink"))
    .render("graph_with_options.html")
)
