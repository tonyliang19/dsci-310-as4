#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from myst_nb import glue


# ## Aim
# 
# This project explores the historical population of horses in Canada
# between 1906 and 1972 for each province.

# ## Data
# 
# Horse population data were sourced from the [Government of Canada's Open Data website](http://open.canada.ca/en/open-data).
# Specifically, {cite}`horses1`, {cite}`horses2`.
# 
# 

# ## Methods
# 
# The R programming language {cite}`R` and the following R packages were used to perform the analysis: knitr {cite}`knitr`, tidyverse, {cite}`tidyverse`, and bookdown {cite}`bookdown`. Note: this report is adapted from {cite}`ttimbers_horses`.
# 

# Results

# ```{figure} ../../results/horse_pops_plot.png
# ---
# figwidth: 500px
# name: horse-pop-plot
# ---
# Horse populations for all provinces in Canada from 1906 - 1972
# 
# ```
# 
# We can see from {ref}`Fig <horse-pop-plot>`
# that Ontario, Saskatchewan and Alberta have had the highest horse populations in Canada.
# All provinces have had a decline in horse populations since 1940.
# This is likely due to the rebound of the Canadian automotive
# industry after the Great Depression and the Second World War.
# An interesting follow-up visualisation would be car sales per year for each
# Province over the time period visualised above to further support this hypothesis. 

# In[2]:


horses_sd = pd.read_csv("../../results/horses_sd.csv")

largest_sd_prov = str(horses_sd['Province'][0])
glue("largest-sd-prov", largest_sd_prov)

horses_sd_noindex = horses_sd.style.hide_index()
glue("horses-tbl", horses_sd_noindex)


# Suppose we were interested in looking in more closely at the
# province with the highest spread (in terms of standard deviation)
# of horse populations. We present the standard deviations here:
# 
# ```{glue:figure} horses-tbl
# ---
# figwidth: 500px
# name: horses-tbl-fig
# ---
# Standard deviation of number of horses for each province between 1940 - 1972
# 
# ```
# 
# Note that we define standard deviation (of a sample) as:
# 
# $$s = sqrt{sum_{i = 1}^n(x_i - \bar{x})} / {n-1}.$$
# 
# Additionally, note that in {ref}`Fig <horses-tbl-fig>`. we
# consider the sample standard deviation of the number of horses
# during the same time span as {ref}`Fig <horse-pop-plot>`.

# :::{figure-md} largest-sd-province-plot
# 
# <img src="../../results/horse_pop_plot_largest_sd.png" width="200px">
# 
# Horse populations for the province with the largest standard deviation
# :::
# 
# In {ref}`Fig <largest-sd-province-plot>` we zoom in
# on the province of {glue:}`largest-sd-prov`, which had the largest spread of values in
# terms of standard deviation.

# ## References
