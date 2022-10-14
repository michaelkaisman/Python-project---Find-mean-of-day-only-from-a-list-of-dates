#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import pandas as pd


# In[2]:


def main(ds):
    d = [datetime.datetime.strptime(x, '%d/%m/%Y') for x in ds]
    df = pd.DataFrame(d, columns=['date'])
    df['days'] = [datetime.datetime.strftime(x, '%d') for x in df['date']]
    df['mean'] = df['days'].rolling(len(df)).mean()
    return df


# In[3]:


if __name__ == '__main__':
    ds = ['12/03/2022', '14/04/2022', '13/05/2022']
    #ds = ['30/01/2022', '02/03/2022', '29/03/2022']
    result = main(ds)
    print(round(result.loc[2,'mean'], 1))

