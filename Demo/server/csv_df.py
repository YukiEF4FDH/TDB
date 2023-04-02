from asyncio.windows_events import NULL
import pandas as pd
import os
import glob
import flask
import re

class CsvDfs:
    csv_df_list = list()
    csv_df_id_list = list()

    def __init__(self):
        csv_df_list = list()
        csv_df_id_list = list()

    def append(self, csv_df):
        self.csv_df_list.append(csv_df)
        self.csv_df_id_list.append(csv_df.id)
# ------------------------------Def of Class CsvDf------------------------------
# A csv file -> The data of a Vis or a Sheet.
#               A Vis or a sheet -> could be map to a sec or multiple sections.
# 
# The calss to store the basic info of a csv file, 
# Including basic manipulations on it.

class CsvDf:

    id = NULL # Depends on the csv file name
    df = NULL # Dataframe of the csv
    json_of_df = NULL # Json of the df

    index_name = NULL # Index name of the df (Mainly for getting this one↓)
    index_list = NULL # Index-name list of the df
    col_list = NULL   # Column-name list of the df

    related_sec_id_set = NULL

    def __init__(self):
        pass
    
    def __init__(self, id_, df_):
        self.id = id_
        self.df = df_

        # Sometimes special preprocess of the df are requested
        # to generate the expected Vis/Text.
        # TODO: The requirements of preprocess should be denoted in Specification.json.
        self.preprocess() 

        self.index_name = str(self.df.columns.values[0])
        self.index_list = self.df.loc[:,self.index_name].values.tolist()
        self.col_list = self.df.columns.values[1:].tolist()

        self.json_of_df = self.df.to_json (orient="records")

        # self.update_related_sec_id_list([])
    def __repr__(self):
        return "CsvDf()"

    def __str__(self):
        str = "\n----------------------------\n"
        str  += "[Id: ]"+self.id+"\n"
        str  += "[Df: ]"+self.df.to_string()+"\n"
        str += "[Index List: ]"+"\n"
        for index in self.index_list:
            str+=index+" "
        str += "\n"
        str += "[Column List: ]"+"\n"
        for index in self.col_list:
            str+=index+" "
        str += "\n"
        str += "[Related Sec Id List: ]"+"\n"
        for index in self.related_sec_id_set:
            str+=index+" "
        str += "\n----------------------------\n"
        return str
    
    # NOTICE THAT This one is temporary.
    # Sometimes special preprocess of the df are requested
    # to generate the expected Vis/Text.
    # TODO: The requirements of preprocess should be denoted in Specification.json.
    def preprocess(self):
        if self.id=="sheet1":
            create_sum_col_for_df(self.df,"total")

    # Jsonify for Flask.
    # This function would be called behind @app.route
    # so as to send json data to the front-end (for Vis, etc.).
    def jsonify(self):
        return flask.jsonify(self.json_of_df)

    def update_related_sec_id_list(self, md_secs):
        self.related_sec_id_set = set()
        CSV_ID_RE = r"[a-zA-Z]+([0-9]+)[a-zA-Z]*"
        csv_index = str((re.search(CSV_ID_RE, self.id)).group(1))
        for sec_id in md_secs.md_sec_id_list:
            SEC_ID_RE = r"[a-zA-Z]+([0-9]+)"
            sec_index = str((re.search(SEC_ID_RE, sec_id)).group(1))
            if sec_index==csv_index:
                self.related_sec_id_set.add(sec_id)
                
                md_sec = md_secs.get_md_sec_by_id(sec_id)
                md_sec.add_related_csv_id(self.id)
                md_secs.update_md_sec_by_id(sec_id,md_sec)

# ------------------------------DF Manipulations------------------------------
# Create a sum column for the specified df, with specified sum_col_name.
def create_sum_col_for_df(df_, sum_col_name):
    sum_col = df_.sum(axis=1)
    df_[sum_col_name] = sum_col

# Get json of the specified df, with specified orientation.
def get_json_of_df(df, ori):
    json_of_df = df.to_json (orient=ori)
    return json_of_df

# Get the name of the index of the specified df.
def get_index_name_of_df(df):
    return str(df.columns.values[0])

# Get the list of the index-name of the specified df.
def get_index_list_of_df(df, index_name):
    return df.loc[:,index_name].values.tolist()

# Get the list of the column-name of the specified df.
def get_col_list_of_df(df):
    return df.columns.values[1:].tolist()

# ------------------------------Csv Files Loading------------------------------
#    Load all of the csv files under "\CSVFiles"
#    and turn them into instances of class:CsvDf.
#    Create a csv_df_list for the results.
#    csv_df_list[i] -> An instance of class:CsvDf of the csv file.
def load_csv_files(csv_dfs):

    # Load *all* of the csv files
    path = os.getcwd()
    path = path+"\CSVFiles"
    csv_files = glob.glob(os.path.join(path, "*.csv")) 

    for file in csv_files:

        file_name = (file.split("\\")[-1]).split(".")[0] # -> csv_df.id
        df = pd.read_csv(file,header=0) # -> csv_df.df

        csv_df = CsvDf(file_name, df) # An instance of CsvDf
        csv_dfs.append(csv_df) # The result list of CsvDf to return
