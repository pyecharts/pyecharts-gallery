from pyecharts import options as opts
from pyecharts.charts import HeatMap, Scatter
from pyecharts.commons.utils import JsCode

mbti = [
  'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
  'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP'
]
mbti_data = [
  ['ENFJ', 'ENFJ', 0.86], ['ENFJ', 'ENFP', 0.91], ['ENFJ', 'ENTJ', 0.42],
  ['ENFJ', 'ENTP', 0.73], ['ENFJ', 'ESFJ', 0.64], ['ENFJ', 'ESFP', 0.8],
  ['ENFJ', 'ESTJ', 0.22], ['ENFJ', 'ESTP', 0.41], ['ENFJ', 'INFJ', 0.74],
  ['ENFJ', 'INFP', 0.73], ['ENFJ', 'INTJ', 0.16], ['ENFJ', 'INTP', 0.35],
  ['ENFJ', 'ISFJ', 0.3], ['ENFJ', 'ISFP', 0.4], ['ENFJ', 'ISTJ', 0.18],
  ['ENFJ', 'ISTP', 0.09], ['ENFP', 'ENFJ', 0.91], ['ENFP', 'ENFP', 0.97],
  ['ENFP', 'ENTJ', 0.37], ['ENFP', 'ENTP', 0.85], ['ENFP', 'ESFJ', 0.42],
  ['ENFP', 'ESFP', 0.93], ['ENFP', 'ESTJ', 0.27], ['ENFP', 'ESTP', 0.76],
  ['ENFP', 'INFJ', 0.51], ['ENFP', 'INFP', 0.73], ['ENFP', 'INTJ', 0.13],
  ['ENFP', 'INTP', 0.36], ['ENFP', 'ISFJ', 0.11], ['ENFP', 'ISFP', 0.49],
  ['ENFP', 'ISTJ', 0.04], ['ENFP', 'ISTP', 0.14], ['ENTJ', 'ENFJ', 0.42],
  ['ENTJ', 'ENFP', 0.37], ['ENTJ', 'ENTJ', 0.91], ['ENTJ', 'ENTP', 0.81],
  ['ENTJ', 'ESFJ', 0.53], ['ENTJ', 'ESFP', 0.51], ['ENTJ', 'ESTJ', 0.87],
  ['ENTJ', 'ESTP', 0.74], ['ENTJ', 'INFJ', 0.25], ['ENTJ', 'INFP', 0.13],
  ['ENTJ', 'INTJ', 0.46], ['ENTJ', 'INTP', 0.47], ['ENTJ', 'ISFJ', 0.29],
  ['ENTJ', 'ISFP', 0.06], ['ENTJ', 'ISTJ', 0.66], ['ENTJ', 'ISTP', 0.41],
  ['ENTP', 'ENFJ', 0.73], ['ENTP', 'ENFP', 0.64], ['ENTP', 'ENTJ', 0.81],
  ['ENTP', 'ENTP', 0.94], ['ENTP', 'ESFJ', 0.32], ['ENTP', 'ESFP', 0.87],
  ['ENTP', 'ESTJ', 0.7], ['ENTP', 'ESTP', 0.92], ['ENTP', 'INFJ', 0.11],
  ['ENTP', 'INFP', 0.35], ['ENTP', 'INTJ', 0.22], ['ENTP', 'INTP', 0.51],
  ['ENTP', 'ISFJ', 0.05], ['ENTP', 'ISFP', 0.14], ['ENTP', 'ISTJ', 0.11],
  ['ENTP', 'ISTP', 0.35], ['ESFJ', 'ESFJ', 0.94], ['ESFJ', 'ESFP', 0.4],
  ['ESFJ', 'ESTJ', 0.77], ['ESFJ', 'ESTP', 0.37], ['ESFJ', 'INFJ', 0.74],
  ['ESFJ', 'INFP', 0.17], ['ESFJ', 'INTJ', 0.32], ['ESFJ', 'INTP', 0.05],
  ['ESFJ', 'ISFJ', 0.79], ['ESFJ', 'ISFP', 0.57], ['ESFJ', 'ISTJ', 0.71],
  ['ESFJ', 'ISTP', 0.19], ['ESFP', 'ESFP', 0.7], ['ESFP', 'ESTJ', 0.39],
  ['ESFP', 'ESTP', 0.75], ['ESFP', 'INFJ', 0.43], ['ESFP', 'INFP', 0.58],
  ['ESFP', 'INTJ', 0.22], ['ESFP', 'INTP', 0.39], ['ESFP', 'ISFJ', 0.12],
  ['ESFP', 'ISFP', 0.58], ['ESFP', 'ISTJ', 0.08], ['ESFP', 'ISTP', 0.26],
  ['ESTJ', 'ESTJ', 0.96], ['ESTJ', 'ESTP', 0.78], ['ESTJ', 'INFJ', 0.14],
  ['ESTJ', 'INFP', 0.03], ['ESTJ', 'INTJ', 0.33], ['ESTJ', 'INTP', 0.22],
  ['ESTJ', 'ISFJ', 0.48], ['ESTJ', 'ISFP', 0.22], ['ESTJ', 'ISTJ', 0.79],
  ['ESTJ', 'ISTP', 0.55], ['ESTP', 'ESTP', 0.95], ['ESTP', 'INFJ', 0.05],
  ['ESTP', 'INFP', 0.24], ['ESTP', 'INTJ', 0.17], ['ESTP', 'INTP', 0.39],
  ['ESTP', 'ISFJ', 0.12], ['ESTP', 'ISFP', 0.43], ['ESTP', 'ISTJ', 0.2],
  ['ESTP', 'ISTP', 0.62], ['INFJ', 'INFJ', 0.95], ['INFJ', 'INFP', 0.85],
  ['INFJ', 'INTJ', 0.65], ['INFJ', 'INTP', 0.5], ['INFJ', 'ISFJ', 0.85],
  ['INFJ', 'ISFP', 0.58], ['INFJ', 'ISTJ', 0.53], ['INFJ', 'ISTP', 0.23],
  ['INFP', 'INFP', 0.97], ['INFP', 'INTJ', 0.7], ['INFP', 'INTP', 0.84],
  ['INFP', 'ISFJ', 0.46], ['INFP', 'ISFP', 0.78], ['INFP', 'ISTJ', 0.21],
  ['INFP', 'ISTP', 0.49], ['INTJ', 'INTJ', 0.86], ['INTJ', 'INTP', 0.89],
  ['INTJ', 'ISFJ', 0.79], ['INTJ', 'ISFP', 0.45], ['INTJ', 'ISTJ', 0.85],
  ['INTJ', 'ISTP', 0.78], ['INTP', 'INTP', 0.96], ['INTP', 'ISFJ', 0.38],
  ['INTP', 'ISFP', 0.43], ['INTP', 'ISTJ', 0.51], ['INTP', 'ISTP', 0.81],
  ['ISFJ', 'ISFJ', 0.95], ['ISFJ', 'ISFP', 0.76], ['ISFJ', 'ISTJ', 0.93],
  ['ISFJ', 'ISTP', 0.62], ['ISFP', 'ISFP', 0.97], ['ISFP', 'ISTJ', 0.47],
  ['ISFP', 'ISTP', 0.76], ['ISTJ', 'ISTJ', 0.96], ['ISTJ', 'ISTP', 0.78],
  ['ISTP', 'ISTP', 0.96]
]
mbti_dict = {f"{k}-{v}": data for k, v, data in mbti_data}

color = {
    "green": "#2D9A69", "purple": "#7D568F", "blue": "#3A8DAB", "yellow": "#E0A433",
    "greenLighter": "#10CA77", "purpleLighter": "#9253AF",
    "blueLighter": "#26A9D9", "yellowLighter": "#F4AC24",
    "greenDarker": "#0FB369", "purpleDarker": "#854AA0",
    "blueDarker": "#2298C3", "yellowDarker": "#F2A30D"
}
font_size = {"group": 24, "item": 13, "value": 15}

def get_color(mbti_: str, lightness: int = 0) -> str:
    if "NF" in mbti_:
        if lightness < 0: return color["greenLighter"]
        elif lightness > 0: return color["greenDarker"]
        else: return color["green"]
    if "NT" in mbti_:
        if lightness < 0: return color["purpleLighter"]
        elif lightness > 0: return color["purpleDarker"]
        else: return color["purple"]
    if "S" in mbti_ and "J" in mbti_:
        if lightness < 0: return color["blueLighter"]
        elif lightness > 0: return color["blueDarker"]
        else: return color["blue"]
    if "S" in mbti_ and "P" in mbti_:
        if lightness < 0: return color["yellowLighter"]
        elif lightness > 0: return color["yellowDarker"]
        else: return color["yellow"]
    return None

def generate_group(group_name: str) -> dict:
    color_map = {"NF": color["green"], "NT": color["purple"], "SJ": color["blue"], "SP": color["yellow"]}
    group_members = {
        "NF": ['INFJ', 'INFP', 'ENFJ', 'ENFP'],
        "NT": ['INTJ', 'INTP', 'ENTJ', 'ENTP'],
        "SJ": ['ISFJ', 'ISTJ', 'ESFJ', 'ESTJ'],
        "SP": ['ISFP', 'ISTP', 'ESFP', 'ESTP']
    }
    return {
        "value": group_name,
        "label": {"color": color_map[group_name], "fontSize": font_size["group"], "fontWeight": "bolder", "padding": 0},
        "children": [{"value": mbti, "label": {"color": color_map[group_name], "fontSize": font_size["item"], "fontWeight": "bold"}} for mbti in group_members[group_name]]
    }

xData = [generate_group("NF"), generate_group("NT"), generate_group("SJ"), generate_group("SP")]
yData = [generate_group("NF"), generate_group("NT"), generate_group("SJ"), generate_group("SP")]

heatmap_data = []
scatter_data = []
for x in mbti:
    for y in mbti:
        key = f"{x}-{y}"
        alt_key = f"{y}-{x}"

        if key in mbti_dict:
            value = [x, y, mbti_dict.get(key)]
        elif alt_key in mbti_dict:
            value = [x, y, mbti_dict.get(alt_key)]
        else:
            value = [x, y, 0]

        heatmap_data.append({
            "value": value,
            "itemStyle": {
                "decal": {
                    "shape": "circle", "symbolSize": 1,
                    "color": get_color(x, 1), "backgroundColor": get_color(y, 1),
                    "dashArrayX": [[1, 1], [0, 1, 1, 0]], "dashArrayY": [1, 0],
                },
                "borderColor": get_color(y), "borderWidth": 0,
            }
        })

        scatter_data.append(opts.ScatterItem(
            value=value,
            label_opts=opts.LabelOpts(
                color=get_color(y) if value[2] < 0.2 else "#fff",
                opacity=0.6 if value[2] < 0.15 else 1,
            )
        ))


s = (
    Scatter()
    .add_xaxis(xaxis_data=[item.opts["value"][0] for item in scatter_data])
    .add_yaxis(
        series_name="scatter",
        coordinate_system="matrix",
        symbol_size=0,
        y_axis=scatter_data,
        color="#fff",
        label_opts=opts.LabelOpts(
            is_show=True,
            formatter=JsCode("(params) => Math.round(params.value[2] * 100) + '%'"),
            font_weight="bold",
            color="inherit",
        ),
        is_silent=True,
    )
)

h = (
    HeatMap(
        init_opts=opts.InitOpts(
            bg_color="#F0F7F9",
            aria_opts=opts.AriaOpts(is_enable=True, aria_decal_opts=opts.AriaDecalOpts(is_show=True)),
        ),
    )
    .add_yaxis(series_name="heatmap", yaxis_data=[], value=heatmap_data, coordinate_system="matrix",
               label_opts=opts.LabelOpts(is_show=False),
               emphasis_opts=opts.EmphasisOpts(itemstyle_opts=opts.ItemStyleOpts(border_width=5)))
    .overlap(chart=s)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="MBTI Partner Compatibility",
            subtitle="Data from: https://www.personalitydata.org/16-types/enfj-relationships#partner-matrix",
            subtitle_link="https://www.personalitydata.org/16-types/enfj-relationships#partner-matrix",
            pos_left="center", pos_top=5,
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="#57576A"),
            item_gap=5,
        ),
        tooltip_opts=opts.TooltipOpts(
            formatter=JsCode("""(params) => { return `<span style="color:${getColor(params.value[1])};font-weight:bold">${params.value[1]}</span> / <span style="color:${getColor(params.value[0])};font-weight:bold">${params.value[0]}</span> : ${Math.round(params.value[2] * 100)}%`; }"""),
            border_color="#eee", padding=[2, 8],
        ),
        matrix_opts=opts.MatrixOpts(
            x_data=opts.MatrixAxisOpts(
                data=xData,
                itemstyle_opts=opts.ItemStyleOpts(border_color="transparent", border_width=0),
                divider_line_style_opts=opts.MatrixDividerLineStyleOpts(width=0),
                label_opts=opts.LabelOpts(font_family="Ubuntu Condensed, sans-serif"),
                levels=[{"levelSize": 25}, {"levelSize": 30}]
            ),
            y_data=opts.MatrixAxisOpts(
                data=yData,
                itemstyle_opts=opts.ItemStyleOpts(border_color="transparent", border_width=0),
                divider_line_style_opts=opts.MatrixDividerLineStyleOpts(width=0),
                label_opts=opts.LabelOpts(font_family="Ubuntu Condensed, sans-serif"),
            ),
            body_opts=opts.MatrixBodyOrCornerOpts(
                itemstyle_opts=opts.ItemStyleOpts(border_width=0),
                label_opts=opts.LabelOpts(font_family="Ubuntu Condensed, sans-serif"),
            ),
            pos_left="50",
            background_style=opts.MatrixBackgroundStyleOpts(color="transparent", border_color="transparent", border_width=0),
        ),
        visualmap_opts=[opts.VisualMapOpts(
            type_="continuous", min_=0, max_=1, dimension=2, is_calculable=True,
            orient="horizontal", pos_top=5, pos_left="center",
            range_opacity=[0, 1], series_index=[0, 2], is_show=False,
        )],
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(is_show=False),
        legend_opts=opts.LegendOpts(is_show=False),
    )
)

h.render("matrix_heatmap_mbti.html")
