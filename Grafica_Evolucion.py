import plotly.graph_objects as go
import pandas as pd

# Cargar datos de análisis temporal
df_temporal = q.cells("Analisis_Temporal")

# Crear gráfica de evolución temporal
fig = go.Figure()

# Tasa promedio nacional
fig.add_trace(go.Scatter(
    x=df_temporal['anio'],
    y=df_temporal['Tasa_Promedio'],
    mode='lines+markers',
    name='Tasa Promedio Nacional',
    line=dict(color='#e74c3c', width=3),
    marker=dict(size=6)
))

# Tasa máxima estatal
fig.add_trace(go.Scatter(
    x=df_temporal['anio'],
    y=df_temporal['Tasa_Maxima'],
    mode='lines',
    name='Tasa Máxima Estatal',
    line=dict(color='#c0392b', width=2, dash='dot'),
    fill='tonexty',
    fillcolor='rgba(231, 76, 60, 0.1)'
))

fig.update_layout(
    title='Evolución de la Tasa de Feminicidios en México (1990-2023)',
    xaxis_title='Año',
    yaxis_title='Tasa por 100,000 mujeres',
    hovermode='x unified',
    plot_bgcolor='white',
    height=500,
    width=800,
    showlegend=True,
    legend=dict(x=0.02, y=0.98)
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#ecf0f1')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#ecf0f1')

fig.show()