'''
Database class to handle data storage and export.
'''
import pandas as pd
class Database:
    def __init__(self):
        self.data = []
    def export_data(self, file_path):
        df = pd.DataFrame(self.data)
        df.to_excel(file_path, index=False)