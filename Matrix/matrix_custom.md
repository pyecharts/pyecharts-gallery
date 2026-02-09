
## pyecharts 代码 / 效果

> 元素周期表 - 自定义渲染示例

```python
from pyecharts import options as opts
from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode

class Colors:
    red = "#f88"
    green = "#8f8"
    blue = "#8bf"
    yellow = "#ff8"

c = (
    Custom()
    .set_global_opts(
        matrix_opts=opts.MatrixOpts(
            x_data=opts.MatrixAxisOpts(
                data=JsCode("Array.from({ length: 19 }, (_, i) => i + 1 + '')"),
                label_opts=opts.LabelOpts(is_show=False),
                itemstyle_opts=opts.ItemStyleOpts(border_width=0),
                divider_line_style_opts=opts.MatrixDividerLineStyleOpts(width=0),
            ),
            y_data=opts.MatrixAxisOpts(
                data=JsCode("Array.from({ length: 10 }, (_, i) => i + 1 + '')"),
                label_opts=opts.LabelOpts(is_show=False),
                itemstyle_opts=opts.ItemStyleOpts(border_width=0),
                divider_line_style_opts=opts.MatrixDividerLineStyleOpts(width=0),
            ),
            pos_left="center",
            width=900,
            background_style=opts.MatrixBackgroundStyleOpts(border_width=0),
            body_opts=opts.MatrixBodyOrCornerOpts(
                itemstyle_opts=opts.ItemStyleOpts(border_width=0),
            )
        ),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .add(
        series_name="0",
        coordinate_system="matrix",
        data=[...],  # 元素数据
        label_opts=opts.LabelOpts(
            is_show=True,
            formatter=JsCode("""
            (params) => {
                if (params.value[2] == null) { return '{small|' + params.value[3] + '}';}
                return params.value[2] + '\\n' + params.value[3];
            }
            """),
            rich={"small": {"fontSize": 12, "color": "#777"}},
            text_style_opts=opts.TextStyleOpts(font_size=14, color="#555", align="center"),
        ),
        render_item=JsCode("""
        function (params, api) {
          const x = api.value(0);
          const y = api.value(1);
          const rect = api.layout([x, y]).rect;
          const isElement = !isNaN(api.value(2));
          const margin = 2;
          return {
            type: 'rect',
            shape: {
              x: rect.x + margin,
              y: rect.y + margin,
              width: rect.width - margin * 2,
              height: rect.height - margin * 2
            },
            style: api.style({
              fill: api.value(4),
              stroke: '#aaa',
              lineWidth: isElement ? 1 : 0,
              opacity: isElement ? 1 : 0.5
            })
          };
        }
        """)
    )
)
c.render("matrix_custom.html")
```

<iframe width="100%" height="800px" src="Matrix/matrix_custom.html"></iframe>
