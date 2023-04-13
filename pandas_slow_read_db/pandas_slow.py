import pandas as pd
# This tackes 2 minutes to run
pd.read_sql("SELECT * FROM TABLE", con = "SOMESQLCONNECTION")
