from app import app
from dash import html, dcc


def get_all_components(component):
    components = [component]

    if hasattr(component, "children") and component.children is not None:
        children = component.children

        if isinstance(children, list):
            for child in children:
                components.extend(get_all_components(child))
        else:
            components.extend(get_all_components(children))

    return components


def test_header_present():
    components = get_all_components(app.layout)

    headers = [
        c for c in components
        if isinstance(c, html.H1)
    ]

    assert len(headers) > 0
    assert "Soul Foods Pink Morsel Sales Visualiser" in headers[0].children


def test_visualisation_present():
    components = get_all_components(app.layout)

    graphs = [
        c for c in components
        if isinstance(c, dcc.Graph)
    ]

    assert len(graphs) > 0
    assert graphs[0].id == "sales-chart"


def test_region_picker_present():
    components = get_all_components(app.layout)

    radio_items = [
        c for c in components
        if isinstance(c, dcc.RadioItems)
    ]

    assert len(radio_items) > 0
    assert radio_items[0].id == "region-filter"
