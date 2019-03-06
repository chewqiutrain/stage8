import pandas as pd
import re

######### Prostate Pathological #########
df = pd.read_csv("/Users/alakshmanan/Github/stage8/data/converted/prostate_path.csv")

# Subset to only the columns we need
df = df[['Tvalue/__text', 'Nvalue/__text', 'Mvalue/__text',
            'PSA', 'Grade group', 'stagegroup/__text']]

# Rename the columns (clean it up)
df = df.rename(columns = {'Tvalue/__text' : 't',
                     'Nvalue/__text' : 'n',
                     'Mvalue/__text' : 'm',
                     'PSA' : 'psa',
                     'Grade group' : 'grade_group',
                     'stagegroup/__text' : 'stage'
                    })



# Clean up psa column
df['psa'] = df['psa'].str.strip()
df['psa'] = df['psa'].str.replace("\n|\r|\t","")
df['psa'] = df['psa'].str.replace("/\s\s+/g","")
df['psa'] = df['psa'].str.lower()

# Rename the column values to something more meaningful/easily consumable by the downstream calculations
df['psa'] = df['psa'].map({'less than 10': 'less than 10',
                            'greater than or equal to 10, but less than        20': 'greater than or equal to 10, but less than 20',
                            'greater than or equal to        20' : 'greater than or equal to 20'})


#print(df.PSA.unique())
df.to_csv('prostate_path_cleaned.csv', index=False)





######### Prostate Clinical #########
df2 = pd.read_csv("/Users/alakshmanan/Github/stage8/data/converted/prostate_clinical.csv")

# Subset to only the columns we need
df2 = df2[['Tvalue/__text', 'Nvalue/__text', 'Mvalue/__text',
			'stagetablevalue/0/__text', 'stagetablevalue/1/__text', 'stagegroup/__text']]

# Rename the columns (clean it up)
df2 = df2.rename(columns = {'Tvalue/__text' : 't',
					 'Nvalue/__text' : 'n',
					 'Mvalue/__text' : 'm',
					 'stagetablevalue/0/__text' : 'psa',
					 'stagetablevalue/1/__text' : 'grade_group',
					 'stagegroup/__text' : 'stage'
					})



# Clean up psa column
df2['psa'] = df2['psa'].str.strip()
df2['psa'] = df2['psa'].str.replace("\n|\r|\t","")
df2['psa'] = df2['psa'].str.replace("/\s\s+/g","")
df2['psa'] = df2['psa'].str.lower()

# Rename the column values to something more meaningful/easily consumable by the downstream calculations
df2['psa'] = df2['psa'].map({'less than 10': 'less than 10',
							'greater than or equal to 10, but less than        20': 'greater than or equal to 10, but less than 20',
							'greater than or equal to        20' : 'greater than or equal to 20'})


#print(df.PSA.unique())
df2.to_csv('prostate_clinical_cleaned.csv', index=False)