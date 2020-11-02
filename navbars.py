import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import base64
from config import CLIENT_LOGO, COMPANY_LOGO

encoded_client_logo = base64.b64encode(open(CLIENT_LOGO, 'rb').read())
encoded_company_LOGO = base64.b64encode(open(COMPANY_LOGO, 'rb').read())

def navbar_dash():
    navbar_from_dashboard = dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="data:image/jpg;base64,{}".format(encoded_client_logo.decode()),
                                         height="80px")),
                    ],
                ),
                # Esto debe cambiar segun el cliente
                href="https://www.myclient.com/",target="_blank"
            ),
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="data:image/png;base64,{}".format(encoded_company_LOGO.decode()),
                                         height="80px")),
                    ],
                ),
                href="https://www.mycompany.com/",target="_blank"
            ),
            dbc.NavbarBrand("Dashboard"),
            html.Span(dcc.LogoutButton(logout_url='/logout'), className="ml-auto")
        ],
        color="dark",
        dark=True,
    )
    return navbar_from_dashboard


def navbar_login():
    navbar_from_login = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="data:image/png;base64,{}".format(encoded_company_LOGO.decode()),
                                         height="80px")),
                        dbc.Col(dbc.NavbarBrand("Dashboard", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://www.mycompany.com/",
            ),
            # dbc.NavbarToggler(id="navbar-toggler"),
        ],
        color="dark",
        dark=True,
    )
    return navbar_from_login
