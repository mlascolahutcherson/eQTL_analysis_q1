#!/usr/bin/env python
# coding: utf-8

# In[1]:


##EDA code 


# In[2]:


import pandas as pd
import numpy as np 
import math
import scipy.stats as stats
import json
from bed_reader import open_bed, sample_file


# In[ ]:





# In[ ]:


def generate_regression(exp_pop, genotype_df, read ):
    output = pd.DataFrame(columns = ['SNP_ID', 'GENE',"SLOPE", 'SE', 'p'])
    genes = exp_pop['Gene_Symbol'].unique()
    for g in genes: 
        row = exp_pop.loc[exp_pop['Gene_Symbol'] == g]
        coord = row['Coord'].iloc[0]
        dist = abs(int(coord) - genotype_df['POS'])
        cis_dist = dist[dist <= 500000].index
        for i in cis_dist:
            gene = row['Gene_Symbol'].iloc[0]
            snp = read[np.s_[::,i]]
            snp_id = bed.sid[i]
            if len(snp)!= 1092:
                continue
            snp_df = pd.DataFrame(data = {'sample_id':samples, 'snp':snp})
            vals = exp_pop.loc[(exp_pop.Gene_Symbol == gene)]
            merged =  vals.merge(snp_df, on = 'sample_id')
            slope, intercept, r, p, se = stats.linregress((merged['snp'].astype(np.float), merged['Value'].astype(np.float)))
            geno_df = genotype_df[genotype_df['SNP_ID'] == snp_id]
            #p_val = -(math.log10(p))
            output.loc[len(output.index)] = [snp_id, gene, slope, se, p]
            
    return output 


# In[ ]:





# In[ ]:


def generate_pop_regression(POP, genotype_df, read, sig_threshold):
    for x in POP:
        output_ = pd.DataFrame(columns = ['SNP_ID', 'GENE',"SLOPE", 'SE', 'p'])
        genes = x['Gene_Symbol'].unique()
        for g in genes: 
            row = x.loc[x['Gene_Symbol'] == g]
            coord = row['Coord'].iloc[0]
            dist = abs(int(coord) - genotype_df['POS'])
            cis_dist = dist[dist <= 500000].index
            for i in cis_dist:
                gene = row['Gene_Symbol'].iloc[0]
                snp = read[np.s_[::,i]]
                snp_id = bed.sid[i]
                snp_df = pd.DataFrame(data = {'sample_id':samples, 'snp':snp})
                vals = x.loc[(x.Gene_Symbol == gene)]
                merged =  vals.merge(snp_df, on = 'sample_id')
                slope, intercept, r, p, se = stats.linregress((merged['snp'].astype(np.float), merged['Value'].astype(np.float)))
                geno_df = genotype_df[genotype_df['SNP_ID'] == snp_id]
                if p < sig_threshold:
                    output.loc[len(output.index)] = [snp_id, gene, slope, se, p]
    return output 


# In[ ]:





# In[ ]:


def bar_plot(x, y, title, ylabel, xlabel, color, font)
    plt.figure(figsize = (9,6))
    plt.bar(x = all_pops.index, height = all_pops['p'], color = ['lavender','slateblue', 'mediumslateblue','darkslateblue', 'navy'])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.rcParams.update({'font.size': font})
    plt.show()
    return


# In[ ]:




