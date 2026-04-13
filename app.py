from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_data.csv")


df["Date"] = pd.to_datetime(df["Date"])


app = Dash(__name__)

app.layout = html.Div(className="container", children=[
    html.H1("Soul Foods Pink Morsel Sales Visualiser", className="main-title"),

    html.Div([
        html.Label("Filter by Region:", className="radio-label"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            className="radio-items"
        )
    ], className="filter-box"),

    dcc.Graph(id="sales-chart")
])


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"].str.lower() == selected_region]

    
    filtered_df = filtered_df.groupby("Date", as_index=False)["Sales"].sum()
    filtered_df = filtered_df.sort_values("Date")

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time - {selected_region.capitalize()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
