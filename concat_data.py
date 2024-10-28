import pandas as pd 
import os 
import glob
import warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '{:.2f}'.format

oldpwd = os.getcwd()
os.chdir('data')
path = os.getcwd() 
csv_files = glob.glob(os.path.join(path, "*.xlsx")) 
os.chdir(oldpwd)

master = pd.read_excel("master.xlsx")

all_df = [master]
for i, file in enumerate(csv_files): 
    df = pd.read_excel(file) 
    df = df.rename(columns={'Amount spent (USD)': 'Amount spent (GBP)',
                            'Amount spent (CRC)': 'Amount spent (GBP)'})
    df = df.fillna(value=0)
    df = df.astype(str)
    all_df.append(df)
print("the entire file has been read")

all_data = pd.concat(all_df)
all_data = all_data.fillna(value=0)
all_data.to_excel("concat_all_data.xlsx", index = False)

print("data has been merged, check on concat_all_data.xlsx")