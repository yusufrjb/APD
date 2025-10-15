import dash
from dash import html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import os

# ----- Load Data -----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "aqi_surabaya.csv")

df = pd.read_csv(file_path)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# ----- App Initialization -----
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Surabaya Air Quality Dashboard"

# ----- Sidebar (Offcanvas) -----
sidebar = dbc.Offcanvas(
    [
        html.H5("🔍 Filter Data", className="fw-bold text-primary"),
        html.Hr(),
        html.Label("Pilih Rentang Tanggal:", className="fw-bold"),
        dcc.DatePickerRange(
            id="date-range",
            start_date=df["timestamp"].min(),
            end_date=df["timestamp"].max(),
            display_format="YYYY-MM-DD",
            className="mt-2"
        ),
        html.Br(), html.Br(),
        html.P("Gunakan panel ini untuk memfilter data dashboard.", className="text-muted fs-6"),
    ],
    id="sidebar",
    title="Filter Panel",
    is_open=False,
    placement="start",  # posisi kiri
    style={"width": "320px"}
)

# ----- Navbar with toggle button -----
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.Button("⚙️ Filter", id="open-sidebar", color="primary", className="me-2"),
                width="auto"
            ),
            dbc.Col(html.H4("🌤️ Dashboard Kualitas Udara Surabaya", className="text-white mb-0")),
        ], align="center", className="g-0")
    ]),
    color="primary",
    dark=True,
    className="shadow-sm mb-4"
)

# ----- Layout utama -----
app.layout = html.Div([
    navbar,
    sidebar,  # sidebar filter

    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📈 Tren AQI (Air Quality Index)", className="fw-bold text-primary"),
                    dbc.CardBody([dcc.Graph(id="aqi-chart")])
                ], className="shadow-sm mb-4 rounded-3")
            ], md=6),

            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🌡️ Suhu dan Kelembapan", className="fw-bold text-primary"),
                    dbc.CardBody([dcc.Graph(id="weather-chart")])
                ], className="shadow-sm mb-4 rounded-3")
            ], md=6)
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📊 Tabel Data Kualitas Udara", className="fw-bold text-primary"),
                    dbc.CardBody([
                        dash_table.DataTable(
                            id="data-table",
                            columns=[{"name": i, "id": i} for i in df.columns],
                            page_size=10,
                            filter_action="native",
                            sort_action="native",
                            style_table={"overflowX": "auto"},
                            style_header={
                                "backgroundColor": "#f8f9fa",
                                "fontWeight": "bold",
                                "border": "1px solid lightgray"
                            },
                            style_cell={
                                "textAlign": "center",
                                "padding": "8px",
                                "whiteSpace": "normal",
                                "border": "1px solid #dee2e6"
                            }
                        )
                    ])
                ], className="shadow-sm border mb-5 rounded-3")
            ])
        ])
    ], fluid=True)
])

# ----- Callback untuk toggle sidebar -----
@app.callback(
    Output("sidebar", "is_open"),
    Input("open-sidebar", "n_clicks"),
    State("sidebar", "is_open")
)
def toggle_sidebar(n, is_open):
    if n:
        return not is_open
    return is_open

# ----- Callback untuk update grafik -----
@app.callback(
    [Output("aqi-chart", "figure"),
     Output("weather-chart", "figure"),
     Output("data-table", "data")],
    [Input("date-range", "start_date"),
     Input("date-range", "end_date")]
)
def update_dashboard(start_date, end_date):
    dff = df[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)]

    fig_aqi = px.line(
        dff, x="timestamp", y="aqius",
        markers=True,
        color_discrete_sequence=["#007bff"]
    )
    fig_aqi.update_layout(
        title="Tren AQI (Air Quality Index)",
        xaxis_title="Waktu",
        yaxis_title="AQI",
        template="plotly_white"
    )

    fig_weather = px.line(
        dff, x="timestamp", y=["temp", "humidity"],
        markers=True
    )
    fig_weather.update_layout(
        title="Suhu dan Kelembapan dari Waktu ke Waktu",
        xaxis_title="Waktu",
        yaxis_title="Nilai",
        template="plotly_white"
    )

    return fig_aqi, fig_weather, dff.to_dict("records")

# ----- Main -----
if __name__ == "__main__":
    app.run(port=8050, debug=True)
