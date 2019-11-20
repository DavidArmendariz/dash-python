import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import plotly.graph_objs as go
import pandas as pd

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'dashboard').document(u'cik8wqMjh7RZMgtmSGxj').collection(u'list').document(u'R9L8hUElfZ55FH4OG0TP')

doc = doc_ref.get().to_dict()

data = json.loads(doc["data"]["heatmap"])
center = json.loads(doc["data"]["center"])
df = pd.DataFrame.from_dict(data,orient="columns")

heatmap_fig = go.Figure(go.Densitymapbox(lat=df["lat"], lon=df["lng"], z=df["val"], radius=8))
heatmap_fig.update_layout(mapbox_style="open-street-map", mapbox_center_lon=center["lng"],
                          mapbox_center_lat=center["lat"],mapbox_zoom=17)
heatmap_fig.update_layout(margin={"r":0,"t":60,"l":20,"b":0})


