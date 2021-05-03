import plotly.graph_objects as go

years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
         2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]

fig = go.Figure()

fig.add_trace(go.Bar(x=years,
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                marker_color='rgb(55, 83, 109)'
                ))

fig.update_layout(
    title={
    'text': "Plot Title",
    'y':0.9,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'},

    xaxis=dict( #X-axis Settings
    title='X-axis Title', # Y-axis y-title
    titlefont_size=16, #X-axis title font-size
    tickfont_size=14,  #X-axis tick font-size
    ),

    yaxis=dict( #Y-axis Settings
    title='Y-axis Title', # Y-axis y-title
    titlefont_size=16, #Y-axis title font-size
    tickfont_size=14,  #Y-axis tick font-size
    ),

    barmode='group',
    bargap=0, # gap between bars of adjacent location coordinates.
    bargroupgap=0 # gap between bars of the same location coordinate.
)


fig.show()