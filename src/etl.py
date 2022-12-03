#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
from bed_reader import open_bed, sample_file


# In[4]:


def get_expressions(expression, populations, chrom, pops):
    ''' takes in expressions data and populations data and outputs merged csv depeding on the chromsome
        and populations you want to look at
        :param expressions = a txt.gz file 
        :param populations = a .sample file
        :param chrom = an integere between 1-46
        :param pops = an array of population abbreviations 
    '''
    expressions = pd.read_csv(expression, sep='\t')
    pop = pd.read_csv(populations, sep =" ")
    exp_22 = expressions[expressions['Chr'] == chrom].sort_values(by='Coord')
    exp_trans_22 = exp_22.melt(list(exp_22.columns[:4]), var_name='sample_id', value_name='Value')
    pop = pop.rename(columns ={'sample': 'sample_id'})
    exp_pop = exp_trans_22.merge(pop, on = "sample_id", how = "outer")
    exp_pop = exp_pop.loc[exp_pop["population"].isin(pops)]
    exp_pop = exp_pop.dropna()
    
    return exp_pop


# In[5]:


def get_bim(bim):
    '''takes in a bim file generated from processing vcf.gz file outputs a readable csv with genotype information
        :param bim = .bim file 
    '''
    genotype_test = pd.read_csv(bim, sep = '\t', header = None)
    genotype_test.drop(columns = [2], inplace=True)
    genotype_test.columns = ['Chr', 'SNP_ID', 'POS', 'REF', 'ALT']
    none = genotype_test.loc[genotype_test['SNP_ID'] =='.'].index
    genotype_test.drop(labels = none, axis = 0, inplace = True)
    
    genotype_test['len_ref'] = genotype_test['REF'].apply(len)
    genotype_test['len_alt'] = genotype_test['ALT'].apply(len)
    index_1 = genotype_test.loc[genotype_test['len_ref'] > 1].index
    index_2 = genotype_test.loc[genotype_test['len_alt'] > 1].index
    genotype_test.drop(labels = index_1, axis = 0, inplace = True)
    genotype_test.drop(labels = index_2, axis = 0, inplace = True)
    genotype_test.drop(columns = ['len_alt', 'len_ref','len'], axis = 0, inplace = True)
 
    return genotype_test


# In[6]:


## how to handle bed file????
def get_bed(bed):
    ''' takes in a .bed file generated from processing vcf.gz file outputs a subscriptable bed.read() file 
        :param bed = .bed file 
    '''
    bed = open_bed(bed)
    read = bed.read()
    
    return read


# In[8]:


def save_data(data, file_path):
    os.makedirs(os.path(file_path), exist_ok=True)
    data.to_csv(file_path, index = False)
    return 


# In[ ]:





# In[ ]:




