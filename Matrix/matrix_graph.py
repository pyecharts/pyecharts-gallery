import math

from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.commons.utils import JsCode

width = 942
height = 492
margin = [150, 80]

c = (
    Graph()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Course Prerequisites"),
        matrix_opts=opts.MatrixOpts(
            x_data=opts.MatrixAxisOpts(data=['Data Analysis', 'Programming', 'Algorithms']),
            y_data=opts.MatrixAxisOpts(data=['1st Year', '2nd Year', '3rd Year', '4th Year']),
            pos_left=80,
            pos_right=80,
            pos_top=150,
            pos_bottom=150,
        ),
        graphic_opts=[
            opts.GraphicText(
                graphic_item={
                    "x": (width /4) * 2.5 + margin[1],
                    "y": margin[0] - 15,
                },
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    text="Course Categories",
                    text_align="center",
                    text_vertical_align="bottom",
                    font_size=18,
                    font_weight="bold",
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#333"),
                )
            ),
            opts.GraphicText(
                graphic_item={
                    "x": margin[1] - 15,
                    "y": (height / 5) * 3 + margin[0],
                    "rotation": math.pi / 2,
                },
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    text="Course Categories",
                    text_align="center",
                    text_vertical_align="bottom",
                    font_size=18,
                    font_weight="bold",
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#333"),
                )
            ),
        ]
    )
    .add(
        series_name="course",
        coordinate_system="matrix",
        edge_symbol=["none", "arrow"],
        symbol_size=15,
        links=[
            opts.GraphLink(source=1, target=0),
            opts.GraphLink(source=2, target=0),
            opts.GraphLink(source=3, target=0),
            opts.GraphLink(source=4, target=3),
            opts.GraphLink(source=4, target=2),
            opts.GraphLink(source=5, target=1),
            opts.GraphLink(source=6, target=3),
        ],
        nodes=[
            ['Programming', '1st Year', 1, 'Intro to Computer Science'],
            ['Data Analysis', '2nd Year', 1, 'Intro to Data Analysis'],
            ['Algorithms', '2nd Year', 1, 'Intro to Algorithms'],
            ['Programming', '2nd Year', 1, 'Advanced Programming'],
            ['Algorithms', '4th Year', 1, 'Data Structures\nand Algorithms'],
            ['Data Analysis', '3rd Year', 1, 'Statistics for Data Analysis'],
            ['Programming', '3rd Year', 1, 'Software Development']
        ],
        label_opts=opts.LabelOpts(
            is_show=True,
            formatter=JsCode("(params) => { return params.data[3];}"),
            color="#555",
            border_width=0,
            font_size=15,
            font_weight="bold",
            offset=[0, -15],
            vertical_align="bottom",
        ),
        linestyle_opts=opts.LineStyleOpts(
            color="#9af",
            width=2,
            opacity=1,
        ),
    )
)
c.render("matrix_graph.html")
