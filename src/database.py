import os
from pymongo import MongoClient

class FileDB:
    
    def __init__(self): # , clientUrl:str, databaseName:str, collectionName:str
        # db and client, get user to config, config file ------------------------------------
        self.client = MongoClient("mongodb://localhost:27017/")
        self.database =  self.client["imageDB"]
        self.imgCollection = self.database['images']
        self.supported_filetypes = ['gif', 'jpeg', 'jpg', 'png', 'webp', 'mp4', 'webm', 'svg', 'ico', 'jfif', '']

        
    def bulk_add_files(self, directory:str, add_sub_directories:bool):

        # add stuff to db
        files_paths = self.dir_to_files_paths(dir=directory, subdirs=add_sub_directories)
        self.add_files_paths_to_db(files_paths)
        print(len(files_paths))
    
    # Repeat this pattern for each component of file dict in db (mostly)
        # or make a one fit all that indexes based on name and key
    def add_file(self):
        pass
    def remove_file(self):
        pass
    def update_file(self):
        pass

    def add_supported_file_type(self):
        pass
    def remove_supported_file_type(self):
        pass
    def get_supported_file_types(self):
        pass

    
    def get_db_filepaths(self):
        file_list = []
        for file in self.imgCollection.find():
            file_list.append(file['path']+'/'+file['_id'])
        return file_list

    def add_files_paths_to_db(self, files_paths:list[tuple[str, str]]):
        # need the option to configure other components of the file
            # separate this function out
                # individual add file function that contains all params
                    # add file type as a default tag?
        for file, path in files_paths:
            
            dict = {'_id': file, 'path':path,
                    'tags':{'Artist': {}, 'Copyright': {}, 'Character': {}, 'General': {}, 'Meta':{}}}
            
            try:
                x = self.imgCollection.insert_one(dict)
                print(x)
            except Exception as e:
                match type(e).__name__:
                    case 'DuplicateKeyError':
                        # if file is already in db 
                        # query user on which version of file they want to keep --------------------------------
                            # and if they want to repeat their choice on other instances of same error
                        
                        # print(type(e).__name__)
                        pass
                    case _:
                        print(f"New unhandled error: {type(e).__name__}")
                
                # write any terminal/console output to some log
                    # print(e)
            

            # track progress somehow on inserts -----------------------------------
                # display to user
                # we should get all files and then add to db if this is case

    def dir_to_files_paths(self, dir:str, subdirs:bool):
        '''Returns a list of filename-filepath tuples from the provided directory'''
        if not os.path.isdir(dir):
            return []
        
        filenames = next(os.walk(dir), (None, None, []))[2]  # [] if no file
        files_paths = []
        
        if subdirs: # function becomes recursive if subdirs is true
            dirnames = next(os.walk(dir), (None, None, []))[1]
            
            for directory in dirnames:
                subdir = dir+'/'+directory
                subdir_files_paths = self.dir_to_files_paths(dir=subdir, subdirs=True)
                
                if subdir_files_paths:
                    for file_path in subdir_files_paths: files_paths.append(file_path)
            
            # could query the user each iteration ----------------------------------------------
                # on whether they want to include a detected directory
                # or make this functionality in the ui
        
        for file in filenames: # constrain files based on extensions
            if file.split('.')[1].lower() in self.supported_filetypes:
                files_paths.append([file, dir])

        return files_paths
        # this can be used to display files and dirs to user in ui later
    
# x = FileDB()
# x.bulk_add_files(directory="E:/Downloads/ref", add_sub_directories=True)
# y = x.get_db_filepaths()