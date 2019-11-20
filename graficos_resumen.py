import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("datos.csv")
visitas_ts = df.groupby("Fecha Ultima")["Visitas"].sum().reset_index()
visitas_genero = df.groupby("Genero")["Visitas"].sum().reset_index()
visitas_dia = df.groupby("Dia")["Visitas"].sum().reset_index()
visitas_conexion = df.groupby("Conexion")["Visitas"].sum().reset_index()
visitas_estado = df.groupby("Estado")["Visitas"].sum().reset_index()

#visitas en el tiempo
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=visitas_ts["Fecha Ultima"], y=visitas_ts["Visitas"], name="Visitas"))
fig1.update_layout(title_text='Cantidad de visitas en el tiempo',xaxis_rangeslider_visible=True)
#visitas por genero
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=visitas_genero["Visitas"],y=visitas_genero["Genero"],name="Visitas",orientation="h"))
fig2.update_layout(title_text="Cantidad de visitas por género")
#visitas por dia
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=visitas_dia["Dia"],y=visitas_dia["Visitas"],name="Visitas"))
fig3.update_layout(title_text="Cantidad de visitas por día")
#visitas por metodo de conexion
fig4 = go.Figure()
fig4.add_trace(go.Pie(labels=visitas_conexion["Conexion"], values=visitas_conexion["Visitas"]))
fig4.update_layout(title_text="Cantidad de visitas por método de conexión")
#visitas por estado
fig5 = go.Figure()
fig5.add_trace(go.Pie(labels=visitas_estado["Estado"],values=visitas_estado["Visitas"],hole=0.3))
fig5.update_layout(title_text="Cantidad de visitas por estado")