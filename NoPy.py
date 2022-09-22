import encodings
import pandas as pd
diabetes_df =pd.read_excel("C:\Users\91910\Desktop\ML\Untitledspreadsheet.xlsx",sep='\t',encoding="utf-8");
diabetes_df.to_csv("hii.csv")