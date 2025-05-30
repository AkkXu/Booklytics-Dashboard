import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("books_all_pages.csv")
# Setup price for Range slider
min_price = df['price'].min() 
max_price = df['price'].max()


# App setup
app = dash.Dash(__name__)
app.title = "Booklytics Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Booklytics Dashboard", style={'textAlign': 'center'}),

    html.Label("Select a Graph:", style={'fontSize': 18}),
    # Dropdown
    dcc.Dropdown(
        id='graph-type',
        options=[
            {'label': 'Price by Rating', 'value': 'price-rating'},
            {'label': 'Price by Series Book', 'value': 'price-series'},
            {'label': 'Rating by Series Book', 'value': 'rating-series'},
            {'label': 'Price by Availability', 'value': 'price-availability'},
        ],
        value='price-rating',
        clearable=False,
        style={'width': '60%'}
    ),

    html.Br(),

    dcc.Graph(id='main-graph'),

    html.Hr(),

    html.H3("Price vs Rating", style={'textAlign': 'center'}),

    html.P("Filter by Price Range:"),
    #Range Slider
    dcc.RangeSlider(
        id='price-slider',
        min=min_price,
        max=max_price,
        value=[min_price, max_price],
        step=1,
        tooltip={"placement": "bottom"},
        marks={
            int(min_price): f"${int(min_price)}",
            int((min_price + max_price) / 2): f"${int((min_price + max_price) / 2)}",
            int(max_price): f"${int(max_price)}"
        }
    ),
    html.Br(),

    dcc.Graph(id='scatter-graph')
])

# Callback for dropdown
@app.callback(
    Output('main-graph', 'figure'),
    Input('graph-type', 'value')
)
def update_main_graph(graph_type):
    color_palette = px.colors.qualitative.Set2
    if graph_type == 'price-rating':
        fig = px.box(df, x='rating', y='price', color='rating', title='Price by Rating',
                     color_discrete_sequence=color_palette)
    elif graph_type == 'price-series':
        fig = px.box(df, x='series_book', y='price', color='series_book', title='Price by Series Book',
                     color_discrete_sequence=color_palette)
    elif graph_type == 'rating-series':
        fig = px.box(df, x='series_book', y='rating', color='series_book', title='Rating by Series Book',
                     color_discrete_sequence=color_palette)
    elif graph_type == 'price-availability':
        fig = px.box(df, x='availability', y='price', color='availability',
                     title='Price by Availability',
                     color_discrete_sequence=color_palette)
    else:
        fig = {}
    return fig

# Callback for scatter
@app.callback(
    Output('scatter-graph', 'figure'),
    Input('price-slider', 'value')
)
def update_scatter(price_range):
    filtered_df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]
    fig = px.scatter(
        filtered_df,
        x='price',
        y='rating',
        color='series_book',
        title=f"Price vs Rating",
        hover_data=['title', 'availability'],
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig

# Run
if __name__ == '__main__':
    app.run(debug=True)
