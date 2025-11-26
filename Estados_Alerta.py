import pandas as pd
import plotly.graph_objects as go

# Cargar datos
df = q.cells("homicidios_femeninos.csv")
df['anio'] = pd.to_numeric(df['anio'])
df['tasa'] = pd.to_numeric(df['tasa'])

# Estados con mayores tasas en período reciente (2020-2023)
recientes = df[df['anio'] >= 2020].groupby('entidad')['tasa'].mean().sort_values(ascending=False).head(15)

# Crear gráfica de barras
fig = go.Figure(go.Bar(
    x=recientes.values,
    y=recientes.index,
    orientation='h',
    marker=dict(
        color=recientes.values,
        colorscale='Reds',
        showscale=True,
        colorbar=dict(title="Tasa")
    ),
    text=recientes.values.round(2),
    textposition='outside'
))

fig.update_layout(
    title='Estados con Mayor Tasa de Feminicidios (Promedio 2020-2023)',
    xaxis_title='Tasa por 100,000 mujeres',
    yaxis_title='',
    height=600,
    width=800,
    plot_bgcolor='white',
    yaxis=dict(autorange="reversed")
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#ecf0f1')

fig.show()