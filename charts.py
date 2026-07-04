"""Composant réutilisable : graphiques Plotly standardisés."""
import plotly.graph_objects as go


def line_chart(x: list, y: list, title: str = "", y_label: str = "") -> go.Figure:
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode="lines+markers"))
    fig.update_layout(title=title, yaxis_title=y_label, template="plotly_white")
    return fig


def bar_chart(x: list, y: list, title: str = "", y_label: str = "") -> go.Figure:
    fig = go.Figure(data=go.Bar(x=x, y=y))
    fig.update_layout(title=title, yaxis_title=y_label, template="plotly_white")
    return fig
