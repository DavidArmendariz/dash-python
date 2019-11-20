import flask
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from firebase_login import sign_in_with_password
from login import login_form, login_form_invalid
from navbars import navbar_dash
from graficos_resumen import df, fig1, fig2, fig3, fig4, fig5
from heatmap import heatmap_fig

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True

_app_route = '/dashboard'

invalid_user = False

# Create a login route
@app.server.route('/login', methods=['POST'])
def route_login():
    global invalid_user
    data = flask.request.form
    email = data.get('email')
    password = data.get('password')
    verify = sign_in_with_password(email, password)
    if not verify:
        invalid_user = True
        return flask.redirect('/logout')
    else:
        invalid_user =False
        # Return a redirect with
        rep = flask.redirect(_app_route)

        # Here we just store the given username in a cookie.
        # Actual session cookies should be signed or use a JWT token.
        rep.set_cookie('custom-auth-session', email)
        return rep


# create a logout route
@app.server.route('/logout', methods=['POST'])
def route_logout():
    # Redirect back to the index and remove the session cookie.
    rep = flask.redirect(_app_route)
    rep.set_cookie('custom-auth-session', '', expires=0)
    return rep


app.layout = html.Div(id='custom-auth-frame')


# callback para el login
@app.callback(Output('custom-auth-frame', 'children'),
              [Input('custom-auth-frame', 'id')])
def dynamic_layout(_):
    global invalid_user
    session_cookie = flask.request.cookies.get('custom-auth-session')
    if not session_cookie:
        if invalid_user:
            return login_form_invalid
        else:
            return login_form
    return html.Div([
        navbar_dash(),
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Resumen', value='Resumen'),
            dcc.Tab(label='Frecuencia', value='Frecuencia'),
            dcc.Tab(label='Comportamiento', value='Comportamiento'),
            dcc.Tab(label='CRM', value='CRM'),
            dcc.Tab(label="Heatmap", value="Heatmap")
        ]),
        html.Div(id='tabs-content'),
    ])


# callback para los tabs del dashboard
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'Resumen':
        return html.Div([
            dbc.Row(
                [
                    dbc.Col(html.Div([dcc.Graph(figure=fig1)]))
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div([dcc.Graph(figure=fig2)]), width=6),
                    dbc.Col(html.Div([dcc.Graph(figure=fig3)]), width=6),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div([dcc.Graph(figure=fig4)]), width=6),
                    dbc.Col(html.Div([dcc.Graph(figure=fig5)]), width=6),
                ]
            ),
        ])
    elif tab == 'Frecuencia':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'Comportamiento':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'CRM':
        return html.Div([
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_size=20,
            )
        ])
    elif tab == "Heatmap":
        return html.Div([dcc.Graph(figure=heatmap_fig)])


if __name__ == '__main__':
    app.run_server(debug=True)
