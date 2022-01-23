# this is answering question 4 and we can extend to see incubation rates for other variants
import pandas as pd
x = pd.read_csv("data.csv")
print(x)
#Index(['country', 'country_code', 'year_week', 'source', 'new_cases',
#       'number_sequenced', 'percent_cases_sequenced', 'valid_denominator',
#       'variant', 'number_detections_variant',
#       'number_sequenced_known_variant', 'percent_variant'],
#      dtype='object')
# remove valid denominator and source because that's for genomic data discrepancies

#https://academic.oup.com/mbe/article/38/4/1537/6028993I
#https://www.pnas.org/content/117/17/9241
#https://www.nature.com/articles/s41564-020-0770-5
#https://academic.oup.com/mbe/article/38/8/3046/6257226
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7246029/
#https://pubmed.ncbi.nlm.nih.gov/34323371/

# CHECK REPO OF PAPER AT THE END
