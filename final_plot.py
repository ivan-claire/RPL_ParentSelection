import sys; 
import plotly
#import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd
import datetime


#line 19215 parent selection stops for incrementation of pdr

#df = pd.read_csv('/home/wirdze/python2/Branches/OF0Simulator/bin/PlotData/simple_topology_cte_rssi_changing_pdr/parent_plots.csv')
#dff = pd.read_csv('/home/wirdze/python2/Branches/MrHoFSimulator/bin/PlotData/simple_topology_cte_rssi_changing_pdr/parent_plots.csv')

std = pd.read_csv('/home/wirdze/python2/Branches/standard_decrem.csv')	
#original = pd.read_csv('/home/wirdze/python2/simulator/simulator_new/bin/parent_plots.csv')
#std = pd.read_csv('/home/wirdze/python2/simulator/RPL_Extension/standard_decrem.csv')

#dfs = pd.read_csv('/home/wirdze/python2/Branches/OF0Simulator/bin/PlotData/simple_topology_cte_rssi_changing_pdr/pdr_plots.csv')
dfs = pd.read_csv('/home/wirdze/python2/Branches/OF0Simulator/bin/PlotData/simple_topology_varying_rssis/pdr_plots.csv')

df = pd.read_csv('/home/wirdze/python2/Branches/OF0Simulator/bin/PlotData/simple_topology_varying_rssis/parent_plots.csv')
dff = pd.read_csv('/home/wirdze/python2/Branches/MrHoFSimulator/bin/PlotData/simple_topology_varying_rssis/parent_plots.csv')




def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000


#of0
trace1 = go.Scatter(
    x=df['time_list'],
    y=df['parent_list'],
    name='OF0',
    xaxis ='x3',
    yaxis='y3',
    line=dict(
        shape='hv'
    )
)

#mrhof
trace2 = go.Scatter(
    x=dff['time_list'],
    y=dff['parent_list'],
    name='MRHOF',
    xaxis ='x3',
    yaxis='y3',
    line=dict(
        shape='hv'
    )
)
'''
#original of0
trace5 = go.Scatter(
    x=original['time_list'],
    y=original['parent_list'],
    name='OFO',
    xaxis ='x3',
    yaxis='y3',
    line=dict(
        shape='hv'
    )
)
'''
#standard
trace3 = go.Scatter(
    x=std['time_list'],
    y=std['parent_list'],
    name='Expected',
    xaxis ='x3',
    yaxis='y3',
    line=dict(
        shape='hv'
    )
)
#pdr
trace4 = go.Scatter(
    x=dfs['time_list'],
    y=dfs['pdr_list'],
    name='PDR changes',
    xaxis='x2',
    yaxis='y2',
    line=dict(
        shape='hv'
    )
    
)


'''
trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 3, 4]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[5, 5, 5],
    xaxis='x2',
    yaxis='y'
)
trace3 = go.Scatter(
    x=[2, 3, 4],
    y=[600, 700, 800],
    xaxis='x',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
    xaxis='x4',
    yaxis='y4'
)
'''

data = [trace1, trace2, trace3, trace4]
#data = [trace1, trace3,trace4]
layout = go.Layout(
                title='MrHoF/OF0 Parent Selection',
                xaxis2 = dict(
                   range = [to_unix_time(datetime.datetime(2018, 1, 20, 17, 50, 0)),
                            to_unix_time(datetime.datetime(2018, 1, 21, 9, 0, 0))],
                   #domain=[0, 0.55],
                   anchor = 'y3',
                   title='time'
                 ),
                yaxis2=dict(
                   domain=[0.7, 1],
                   anchor='x3',
                   title='pdr'
                 ),
                xaxis3 = dict(
                   range = [to_unix_time(datetime.datetime(2018, 1, 20, 17, 50, 0)),
                            to_unix_time(datetime.datetime(2018, 1, 21, 9, 0, 0))],
                   #domain=[0, 1],
                   anchor = 'y2'
                 ),
                yaxis3=dict(
                   domain=[0, 0.6],
                   anchor='x2',
                   title='parent_id'
                 )
)

plotly.offline.plot({
    "data": [trace1,trace2,trace3,trace4],
    "layout": layout
}, auto_open=True)



'''
plotly.offline.plot({
    "data": [trace1,trace2,trace3,trace4],
    "layout": layout
}, auto_open=True)
'''


'''
layout = go.Layout(
  
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='shared-axes-subplots')
'''
