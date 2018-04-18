
# coding: utf-8

# In[118]:


#import package
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
py.init_notebook_mode(connected=True)


# In[117]:


#insert the data
df = pd.read_csv('epldata_final.csv')
df['fpl_ratio'] = pd.DataFrame(df['fpl_points']/df['fpl_value'])
df.head(7)


# In[100]:


#Distribution of Market value plot
plt.subplots(figsize=(15,6))
sns.set_color_codes()
sns.distplot(df['market_value'], color = "B")
plt.xticks(rotation=90)
plt.title('Distribution of Market value')
plt.show()


# In[104]:


#Distribution of Age plot
plt.subplots(figsize=(15,6))
sns.set_color_codes()
sns.distplot(df['age'], color = "G")
plt.xticks(rotation=90)
plt.title('Distribution of Premier League Players Age')
plt.show()


# In[119]:


#Distribution of Premier League Players position plot
plt.subplots(figsize=(15,6))
sns.set_color_codes()
sns.distplot(df['position_cat'], color = "R")
plt.xticks(rotation=90)
plt.title('Distribution of Premier League Players position')
plt.show()


# In[114]:


#Distribution of Page views plot
plt.subplots(figsize=(15,6))
sns.set_color_codes()
sns.distplot(df['page_views'], color = "M")
plt.xticks(rotation=90)
plt.title('Distribution of Page views')
plt.show()


# In[84]:


#Relation Between Age and Market value plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

pd.options.display.max_columns = 999

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

import warnings
warnings.filterwarnings('ignore')
#df['fage_pointration'] = pd.DataFrame(df['fpl_points']/df['fpl_value'])
trace1 = {
  "x": df['age'],
  "y": df['market_value'],
  "marker": {
    "color": 'red',
    "colorsrc": "Aldemuro:22:1a1899",
    #"size": df['fpl_ratio']
  }, 
  "mode": "markers", 
  "name": "market_value", 
  "text": df['name']+", Club:"+df['club']+", Pos:"+df['position'],
  #"textsrc": "Aldemuro:22:5dc54a", 
  "type": "scatter", 
  "uid": "0d217c", 
  "xsrc": "Aldemuro:22:d61533", 
  "ysrc": "Aldemuro:22:1c3243",
  
}
data = [trace1]
#data = [trace]
layout = {
  "autosize": True, 
  "hovermode": "closest",
  "title": "Relation between Age and Market_value",
  "xaxis": {
    "autorange": True, 
    "range": [3.48535752785, 13.0146424722], 
    "title": "player age", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-17.5245518316, 281.524551832], 
    "title": "market_value", 
    "type": "linear"
  }
}
# Plot and embed in ipython notebook!
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='basic-scatter')


# In[85]:


#Relation Between Position_cat and Market value plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

pd.options.display.max_columns = 999

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

import warnings
warnings.filterwarnings('ignore')
#df['fage_pointration'] = pd.DataFrame(df['fpl_points']/df['fpl_value'])
trace1 = {
  "x": df['position_cat'],
  "y": df['market_value'],
  "marker": {
    "color": 'red',
    "colorsrc": "Aldemuro:22:1a1899",
    #"size": df['fpl_ratio']
  }, 
  "mode": "markers", 
  "name": "market_value", 
  "text": df['name']+", Club:"+df['club']+", Pos:"+df['position'],
  #"textsrc": "Aldemuro:22:5dc54a", 
  "type": "scatter", 
  "uid": "0d217c", 
  "xsrc": "Aldemuro:22:d61533", 
  "ysrc": "Aldemuro:22:1c3243",
  
}
data = [trace1]
#data = [trace]
layout = {
  "autosize": True, 
  "hovermode": "closest",
  "title": "Relation between Position_cat and Market_value",
  "xaxis": {
    "autorange": True, 
    "range": [3.48535752785, 13.0146424722], 
    "title": "position_cat", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-17.5245518316, 281.524551832], 
    "title": "market_value", 
    "type": "linear"
  }
}
# Plot and embed in ipython notebook!
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='basic-scatter')


# In[86]:


#Relation Between Page views and Market value plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

pd.options.display.max_columns = 999

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

import warnings
warnings.filterwarnings('ignore')
#df['fage_pointration'] = pd.DataFrame(df['fpl_points']/df['fpl_value'])
trace1 = {
  "x": df['page_views'],
  "y": df['market_value'],
  "marker": {
    "color": 'red',
    "colorsrc": "Aldemuro:22:1a1899",
    #"size": df['fpl_ratio']
  }, 
  "mode": "markers", 
  "name": "market_value", 
  "text": df['name']+", Club:"+df['club']+", Pos:"+df['position'],
  #"textsrc": "Aldemuro:22:5dc54a", 
  "type": "scatter", 
  "uid": "0d217c", 
  "xsrc": "Aldemuro:22:d61533", 
  "ysrc": "Aldemuro:22:1c3243",
  
}
data = [trace1]
#data = [trace]
layout = {
  "autosize": True, 
  "hovermode": "closest",
  "title": "Relation between Page_views and Market_value",
  "xaxis": {
    "autorange": True, 
    "range": [3.48535752785, 13.0146424722], 
    "title": "page_views", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-17.5245518316, 281.524551832], 
    "title": "market_value", 
    "type": "linear"
  }
}
# Plot and embed in ipython notebook!
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='basic-scatter')


# In[120]:


#OLS Regression Result
import numpy as np

x = np.linspace(-5, 5, 20)
np.random.seed(1)

# normal distributed noise
y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
# Create a data frame containing all the relevant variables

import numpy as np
from statsmodels.formula.api import ols

data = pandas.DataFrame({'x': x, 'y': y})
model = ols("y ~ x", data).fit()
data = pandas.read_csv('epldata_final.csv')
model = ols('market_value ~ age + position_cat+page_views + 1', data).fit()
print(model.summary())  

