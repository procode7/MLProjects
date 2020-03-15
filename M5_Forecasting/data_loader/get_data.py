import pandas as pd
import os
from zipfile import ZipFile
from utility.file_size import FileStats

class DataLoader(object):
    

    def __init__(self):
        self.project_dir = os.getcwd() + '/data'

    def list_files(self):
        '''
        List all files in the folder
        '''  
        fs = FileStats() 
        self.file_list = os.listdir( self.project_dir )
        for file_name in self.file_list:
            print(file_name,'\t',fs.file_size(os.path.join(self.project_dir,file_name)),end='\n')
        return len(self.file_list)
    
    def read_files(self):
        '''
        Identify Extension and read files
        '''
        for file_txt in self.file_list:
            file_ext = file_txt.split('.')[1]
            if file_ext.__contains__('csv'):
                print('Reading Files...')
                file_txt_df = pd.read_csv(os.path.join(self.project_dir,file_txt))
                print(file_txt_df)
            elif file_ext.__contains__('zip') and self.list_files == 1:
                # if the .zip file if it contains only one zip file
                print('Extracting Files...')
                with ZipFile(file_txt,'r') as zip_obj:
                    zip_obj.extractall()
