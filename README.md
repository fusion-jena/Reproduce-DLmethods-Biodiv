# Reproducibility of deep learning models in the biodiversity domain
[![DOI](https://zenodo.org/badge/715482807.svg)](https://doi.org/10.5281/zenodo.14605015)

This Repo contains the data and codes that were used to extract and analyse the reproducibility information of Deep Learning methods from publications in the Biodiversity domain
* web_scraping.py ----> Python code that can scrape the publication information from Google Scholar with a specified query and time period (2015-2021)
* Google_scholar_500_publications_run1.json ----> Json file containing information on 500 Biodiversity publications based on the query and time period as mentioned in the code
* Variable_info_VK_v1.csv ----> Recorded variable level information as a binary response: available (y), not available (n) by annotator 1
* Variable_info_WA_v1.csv ----> Recorded variable level information as a binary response: available (y), not available (n) by annotator 2
* Inter_Annotator_Agreement.py ----> Python code for calculating the Inter-Annotator Agreement
* Compare_annotations.py ----> Python code for checking the mismatching responses between two annotators
* Data_after_inter_annotator_agreement.csv ----> Dataset after resolving the mismatches between two annotators responses
* Category_and_levels.py ----> Python code for compiling categorical and publication reproducibility level information using variable level information
* Final_data.csv ----> Final dataset containing variable, categorical, publication reproducibility level that was used for analysing the results
