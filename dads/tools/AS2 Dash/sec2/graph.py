#Reference: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash%20Components/Graph/dash-graph.py

from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()
print(df.head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)


# map country to a color
c = dict(zip(df["country"].unique(), px.colors.qualitative.T10))


app.layout = html.Div([
    html.H2(children='Gross Domestic Product (GDP) per capita'),
    #value=['Germany','Brazil'] >> default
    dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True, options=[{'label': x, 'value': x} for x in df.country.unique()]),
    html.Div([
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, selectedData=None,
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': True,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns',   style={'flex': '2'}
                  ),
        dcc.Graph(id='pie-graph', figure={}, className='six columns', style={'flex': '1', 'margin-left': '5px'}),
    ],style={'display': 'flex', 'flex-wrap': 'wrap'}),
    html.Div([
        dcc.Graph(id='bar-graph', figure={}, style={'width': '65%'})
    ])
])



@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff = df[df.country.isin(country_chosen)]
    #print(dff)
    fig = px.line(data_frame=dff, x='year', y='gdpPercap', color='country', hover_data=["lifeExp", "pop", "iso_alpha"], 
                  color_discrete_map=c)
    fig.update_traces(mode='lines+markers')
       
    return fig

        

# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')                     #input เริ่มต้นจาก dpdn2 (drop down 2)
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == 1952]
        #print(dff2)
        fig2 = px.pie(data_frame=dff2, values='pop', names='country', 
                      title='Population for 1952', color='country', color_discrete_map=c)
        return fig2
    
    
    else:
        dff2 = df[df.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']          
        dff2 = dff2[dff2.year == hov_year]

        fig2 = px.pie(data_frame=dff2, values='pop', names='country', 
                      title=f'Population for: {hov_year}', color='country', color_discrete_map=c) 
        return fig2


# add bar chart

@app.callback(
    Output(component_id='bar-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)

def update_bar_chart(slct_data, country_chosen):
    if slct_data:
        slct_year = [point['x'] for point in slct_data['points']]
        dff3 = df[df.country.isin(country_chosen) & df.year.isin(slct_year)]
        fig3 = px.bar(data_frame=dff3, x='year', y='gdpPercap',
            title='GDP Per Capita', color='country', barmode='group',
            color_discrete_map=c
        )
        return fig3
    else:
        dff3 = df[df.country.isin(country_chosen)]
        fig3 = px.bar(data_frame=dff3, x='year', y='gdpPercap',
            color='country',  title='GDP Per Capita',
            barmode='group', color_discrete_map=c
        )
        return fig3

        
    



if __name__ == '__main__':
    app.run_server(debug=True)

'''
GDP Per Capita คือ ผลิตภัณฑ์มวลรวมในประเทศต่อหัว หรือ GDP ต่อหัว 
เป็นตัวเลขที่บอกว่าค่าเฉลี่ยของ GDP เมื่อเทียบกับคนในประเทศแล้ว โดยเฉลี่ยคนหนึ่งคนสามารถสร้างมูลค่า GDP ขึ้นมาเท่าไหร่ 
และแน่นอนว่า GDP per capita คือ ตัวเลขที่คำนวณมาจาก ค่า GDP ÷ จำนวนประชากร

iso_alpha
The 3-letter ISO 3166-1 alpha-3 code.

iso_num
The 3-digit ISO 3166-1 numeric-3 code.

อายุคาดเฉลี่ย (Life Expectancy) : LE หรือ Life Expectancy หมายถึง
การคาดประมาณจำนวนปีโดยเฉลี่ยของการมีชีวิตอยู่ของประชากร
'''

