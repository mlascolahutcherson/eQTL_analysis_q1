#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import json
import pandas as pd


# In[3]:


sys.path.insert(0, 'src')
from etl import get_expressions, get_bim, get_bed
from eda import generate_regression


# In[ ]:


def main(targets):
    epressions_config = json.load(open('config/exp_config.json'))
    bim_config = json.load(open('config/bim_config.json'))
    bed_config = json.load(open('config/bed_config.json'))
    
    if 'data' om targets:
        exp_pop = get_expressions(**expressions_config)
        genotype_df = get_bim(**bim_config)
        read = get_bed(**bed_config)
    
    if 'eda' in targets:
        generate_regression(exp_pop, genotype_df, read)
    
    return 


# In[ ]:


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)

