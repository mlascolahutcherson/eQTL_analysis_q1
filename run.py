#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import json
import pandas as pd


# In[3]:


sys.path.insert(0, 'src')
from etl import get_expressions, get_bim, get_bed
from eda import generate_regression, generate_pop_regression, bar_plot


# In[ ]:


def main(targets):
    epressions_config = json.load(open('config/exp_config.json'))
    bim_config = json.load(open('config/bim_config.json'))
    bed_config = json.load(open('config/bed_config.json'))
    reg_config = json.load(open('config/reg_config.json'))
    bar_plot_config = json.load(open('config/bar_plot_config.json'))
    
    if 'data' in targets:
        exp_pop = get_expressions(**expressions_config)
        genotype_df = get_bim(**bim_config)
        read = get_bed(**bed_config)
    
    if 'eda' in targets:
        generate_regression(exp_pop, genotype_df, read)
        
        pop_dfs = []
        for x in reg_config['pops']:
            pop_dfs.append(exp_pop.loc[exp_pop['population']== x])
        pop_specific = generate_pop_regression(pop_dfs, genotype_df, read, reg_config['sig_threshold'])
        
        to_plot = pop_specific.groupby(['pop']).count()
        bar_plot(to_plot.index, to_plot['p'], **bar_plot_config)
        
        
    return 


# In[ ]:


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)

