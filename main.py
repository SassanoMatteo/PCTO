import json
from urllib.request import urlopen
import plotly.graph_objects as go
import random

def main():
  import functions
  
  # Collegamento all'API da cui prendere i valori del meteo
  url = "https://api.openweathermap.org/data/2.5/onecall?lat=43.16077430791111&lon=13.709315015546679&appid" \
        "=d0cee4dc035f54a914aff899cc3fec3e&units=metric "
  
  # Inserimento dei dati ottenuti dall'API nel dizionario "data"
  response = urlopen(url)
  data = json.load(response)
  
  # Funzione per calcoli giornalieri, come parametro i dati metereologici
  daily = functions.data_daily(data)
  
  # Funzione per calcoli di ogni ora, come parametro i dati metereologici
  hourly = functions.data_hourly(data)
  
  # Unisco i dati giornalieri e di ogni ora per l'output su file
  json_data = daily + hourly
  
  # Input nome del file json
  file_name = input("Nome file [x.json]: ")
  
  # Funzione per l'output dei dat su file
  functions.output_file(json_data, file_name)








#  Get a convenient list of x-values
y = []
x = []
r = lambda: random.randint(0,255)

# Specify the plots
bar_plots = [
    go.Bar(x=list(json_data[0]["stats"]),
           y=list(json_data[0]["stats"].values()),
           name=json_data[0]["type"] + " 1",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[1]["stats"]),
           y=list(json_data[1]["stats"].values()),
           name=json_data[1]["type"] + " 2",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[2]["stats"]),
           y=list(json_data[2]["stats"].values()),
           name=json_data[2]["type"] + " 3",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[3]["stats"]),
           y=list(json_data[3]["stats"].values()),
           name=json_data[3]["type"] + " 4",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[4]["stats"]),
           y=list(json_data[4]["stats"].values()),
           name=json_data[4]["type"] + " 5",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[5]["stats"]),
           y=list(json_data[5]["stats"].values()),
           name=json_data[5]["type"] + " 6",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[6]["stats"]),
           y=list(json_data[6]["stats"].values()),
           name=json_data[6]["type"] + " 7",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[7]["stats"]),
           y=list(json_data[7]["stats"].values()),
           name=json_data[7]["type"] + " 8",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
    go.Bar(x=list(json_data[8]["stats"]),
           y=list(json_data[8]["stats"].values()),
           name=json_data[8]["type"] + " 1",
           marker=go.bar.Marker(color='#%02X%02X%02X' % (r(),r(),r()))),
]

# Customise some display properties
layout = go.Layout(
    title=go.layout.Title(text="stats", x=0.5),
)

# Make the multi-bar plot
fig = go.Figure(data=bar_plots, layout=layout)

# Tell Plotly to render it
fig.show()
