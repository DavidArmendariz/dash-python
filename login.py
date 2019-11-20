import dash_html_components as html
import dash_bootstrap_components as dbc
from navbars import navbar_login

email_input = dbc.FormGroup(
    [
        dbc.Col(width=4),
        dbc.Label("Email", width=1),
        dbc.Col(
            dbc.Input(
                type="email",
                name="email",
                placeholder="Email"
            ),
            width=3,
        ),
    ],
    row=True
)

password_input = dbc.FormGroup(
    [
        dbc.Col(width=4),
        dbc.Label("Contraseña", width=1),
        dbc.Col(
            dbc.Input(
                type="password",
                name="password",
                placeholder="Contraseña",
            ),
            width=3,
        ),
    ],
    row=True
)

submit_button = dbc.Row([
        html.Button("Entrar",type="submit",style={"margin":"auto"})
    ])


login_form = html.Div([
    navbar_login(),
    html.Br(),
    html.Form(
            [
                email_input,
                password_input,
                submit_button
            ],action='/login', method='post')
    ])

login_form_invalid = html.Div([
    navbar_login(),
    html.Br(),
    html.Form(
            [
                dbc.Alert("Usuario o contraseña inválido", color="danger",style={"width":"50%","margin":"auto"}),
                html.Br(),
                email_input,
                password_input,
                submit_button
            ],action='/login', method='post')
    ])