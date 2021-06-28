import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "%",
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["CYTech", "AMU", "EA", "UFC", "UPPA", "Autres", "Homme", "Femme", "Non Spécifié", "Digitalisation Elevé", "Digitalisation Moyenne", "Digitalisation Faible"],
      color = "red",
      hovertemplate='%{label} <extra></extra>',
    ),
    link = dict(
        source = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8], # indices correspond to labels, eg A1, A2, A1, B1, ...
        target = [6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 9, 10, 11, 9, 10, 11, 9, 10, 11],
        value =  [42, 53, 5, 35, 55, 10, 68, 32, 0, 47, 48, 5, 38, 20, 42, 45, 45, 10, 30, 45, 25, 40, 40, 20, 10, 65, 25],
        hovertemplate='Pourcentage de %{target} à %{source} <br>' +
        'with value %{value} <extra></extra>'
  ))])

 
fig.update_layout(title_text="Répartition du Genre et du niveau de Digitalisation des Enseignants de certaines Ecoles Supérieures ", font_size=10)
fig.show()