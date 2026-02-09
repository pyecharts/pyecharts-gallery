import random
from datetime import datetime, timedelta

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
        data=[
              ['1', '1', '1', 'H', Colors.red],
              ['19', '1', '2', 'He', Colors.red],
              ['1', '2', '3', 'Li', Colors.red],
              ['2', '2', '4', 'Be', Colors.red],
              ['14', '2', '5', 'B', Colors.yellow],
              ['15', '2', '6', 'C', Colors.yellow],
              ['16', '2', '7', 'N', Colors.yellow],
              ['17', '2', '8', 'O', Colors.yellow],
              ['18', '2', '9', 'F', Colors.yellow],
              ['19', '2', '10', 'Ne', Colors.yellow],
              ['1', '3', '11', 'Na', Colors.red],
              ['2', '3', '12', 'Mg', Colors.red],
              ['14', '3', '13', 'Al', Colors.yellow],
              ['15', '3', '14', 'Si', Colors.yellow],
              ['16', '3', '15', 'P', Colors.yellow],
              ['17', '3', '16', 'S', Colors.yellow],
              ['18', '3', '17', 'Cl', Colors.yellow],
              ['19', '3', '18', 'Ar', Colors.yellow],
              ['1', '4', '19', 'K', Colors.red],
              ['2', '4', '20', 'Ca', Colors.red],
              ['4', '4', '21', 'Sc', Colors.blue],
              ['5', '4', '22', 'Ti', Colors.blue],
              ['6', '4', '23', 'V', Colors.blue],
              ['7', '4', '24', 'Cr', Colors.blue],
              ['8', '4', '25', 'Mn', Colors.blue],
              ['9', '4', '26', 'Fe', Colors.blue],
              ['10', '4', '27', 'Co', Colors.blue],
              ['11', '4', '28', 'Ni', Colors.blue],
              ['12', '4', '29', 'Cu', Colors.blue],
              ['13', '4', '30', 'Zn', Colors.blue],
              ['14', '4', '31', 'Ga', Colors.yellow],
              ['15', '4', '32', 'Ge', Colors.yellow],
              ['16', '4', '33', 'As', Colors.yellow],
              ['17', '4', '34', 'Se', Colors.yellow],
              ['18', '4', '35', 'Br', Colors.yellow],
              ['19', '4', '36', 'Kr', Colors.yellow],
              ['1', '5', '37', 'Rb', Colors.red],
              ['2', '5', '38', 'Sr', Colors.red],
              ['4', '5', '39', 'Y', Colors.blue],
              ['5', '5', '40', 'Zr', Colors.blue],
              ['6', '5', '41', 'Nb', Colors.blue],
              ['7', '5', '42', 'Mo', Colors.blue],
              ['8', '5', '43', 'Tc', Colors.blue],
              ['9', '5', '44', 'Ru', Colors.blue],
              ['10', '5', '45', 'Rh', Colors.blue],
              ['11', '5', '46', 'Pd', Colors.blue],
              ['12', '5', '47', 'Ag', Colors.blue],
              ['13', '5', '48', 'Cd', Colors.blue],
              ['14', '5', '49', 'In', Colors.yellow],
              ['15', '5', '50', 'Sn', Colors.yellow],
              ['16', '5', '51', 'Sb', Colors.yellow],
              ['17', '5', '52', 'Te', Colors.yellow],
              ['18', '5', '53', 'I', Colors.yellow],
              ['19', '5', '54', 'Xe', Colors.yellow],
              ['1', '6', '55', 'Cs', Colors.red],
              ['2', '6', '56', 'Ba', Colors.red],
              ['4', '9', '57', 'La', Colors.green],
              ['5', '9', '58', 'Ce', Colors.green],
              ['6', '9', '59', 'Pr', Colors.green],
              ['7', '9', '60', 'Nd', Colors.green],
              ['8', '9', '61', 'Pm', Colors.green],
              ['9', '9', '62', 'Sm', Colors.green],
              ['10', '9', '63', 'Eu', Colors.green],
              ['11', '9', '64', 'Gd', Colors.green],
              ['12', '9', '65', 'Tb', Colors.green],
              ['13', '9', '66', 'Dy', Colors.green],
              ['14', '9', '67', 'Ho', Colors.green],
              ['15', '9', '68', 'Er', Colors.green],
              ['16', '9', '69', 'Tm', Colors.green],
              ['17', '9', '70', 'Yb', Colors.green],
              ['4', '6', '71', 'Lu', Colors.blue],
              ['5', '6', '72', 'Hf', Colors.blue],
              ['6', '6', '73', 'Ta', Colors.blue],
              ['7', '6', '74', 'W', Colors.blue],
              ['8', '6', '75', 'Re', Colors.blue],
              ['9', '6', '76', 'Os', Colors.blue],
              ['10', '6', '77', 'Ir', Colors.blue],
              ['11', '6', '78', 'Pt', Colors.blue],
              ['12', '6', '79', 'Au', Colors.blue],
              ['13', '6', '80', 'Hg', Colors.blue],
              ['14', '6', '81', 'Tl', Colors.yellow],
              ['15', '6', '82', 'Pb', Colors.yellow],
              ['16', '6', '83', 'Bi', Colors.yellow],
              ['17', '6', '84', 'Po', Colors.yellow],
              ['18', '6', '85', 'At', Colors.yellow],
              ['19', '6', '86', 'Rn', Colors.yellow],
              ['1', '7', '87', 'Fr', Colors.red],
              ['2', '7', '88', 'Ra', Colors.red],
              ['4', '10', '89', 'Ac', Colors.green],
              ['5', '10', '90', 'Th', Colors.green],
              ['6', '10', '91', 'Pa', Colors.green],
              ['7', '10', '92', 'U', Colors.green],
              ['8', '10', '93', 'Np', Colors.green],
              ['9', '10', '94', 'Pu', Colors.green],
              ['10', '10', '95', 'Am', Colors.green],
              ['11', '10', '96', 'Cm', Colors.green],
              ['12', '10', '97', 'Bk', Colors.green],
              ['13', '10', '98', 'Cf', Colors.green],
              ['14', '10', '99', 'Es', Colors.green],
              ['15', '10', '100', 'Fm', Colors.green],
              ['16', '10', '101', 'Md', Colors.green],
              ['17', '10', '102', 'No', Colors.green],
              ['4', '7', '103', 'Lr', Colors.blue],
              ['5', '7', '104', 'Rf', Colors.blue],
              ['6', '7', '105', 'Db', Colors.blue],
              ['7', '7', '106', 'Sg', Colors.blue],
              ['8', '7', '107', 'Bh', Colors.blue],
              ['9', '7', '108', 'Hs', Colors.blue],
              ['10', '7', '109', 'Mt', Colors.blue],
              ['11', '7', '110', 'Ds', Colors.blue],
              ['12', '7', '111', 'Rg', Colors.blue],
              ['13', '7', '112', 'Cn', Colors.blue],
              ['14', '7', '113', 'Nh', Colors.yellow],
              ['15', '7', '114', 'Fl', Colors.yellow],
              ['16', '7', '115', 'Mc', Colors.yellow],
              ['17', '7', '116', 'Lv', Colors.yellow],
              ['18', '7', '117', 'Ts', Colors.yellow],
              ['19', '7', '118', 'Og', Colors.yellow],
              ['3', '6', None, 'La~Yb', Colors.green],
              ['3', '7', None, 'Ac~No', Colors.green]
        ],
        label_opts=opts.LabelOpts(
            is_show=True,
            formatter=JsCode("""
            (params) => {
                if (params.value[2] == null) { return '{small|' + params.value[3] + '}';}
                return params.value[2] + '\\n' + params.value[3];
            }
            """),
            rich={"small": {"fontSize": 12, "color": "#777"}},
            text_style_opts=opts.TextStyleOpts(
                font_size=14,
                color="#555",
                align="center",
            ),
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
