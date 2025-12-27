from os import listdir, walk
from os.path import isdir
from pymongo import MongoClient
import PIL.Image

# add stuff to db
directory = 'E:/Downloads/ref'

# keep in file, make function in taskbar to configure... config file?
supported_filetypes = ['gif', 'jpeg', 'jpg', 'png', 'webp', 'mp4', 'webm']

# db and client
client = MongoClient("mongodb://localhost:27017/")
db = client["imageDB"]
imgCol = db['images']
print(client.list_database_names())


def add_files_to_db(files_paths:list[tuple[str, str]]):
    for file, path in files_paths:
        
        dict = {'_id': file, 'path':path,
                'tags':{'Artist': {}, 'Copyright': {}, 'Character': {}, 'General': {}, 'Meta':{}}}
        
        try:
            x = imgCol.insert_one(dict)
            print(x)
        except Exception as e:
            match type(e).__name__:
                case 'DuplicateKeyError':
                    # if file is already in db --------------------------------
                    # query user on which version of file they want to keep
                        # and if they want to repeat their choice on other instances of same error
                    
                    print(type(e).__name__)
                    pass
                case _:
                    print(f"New unhandled error: {type(e).__name__}")
            
            # write any terminal/console output to some log
                # print(e)
        

        # track progress somehow on inserts -----------------------------------
            # display to user
            # we should get all files and then add to db if this is case

def get_files_paths(dir:str, subdirs:bool):
    '''Returns a list of filename-filepath tuples from the provided directory'''
    if not isdir(dir):
        return []
    
    filenames = next(walk(dir), (None, None, []))[2]  # [] if no file
    files_paths = []
    
    if subdirs: # function becomes recursive if subdirs is true
        dirnames = next(walk(dir), (None, None, []))[1]
        
        for directory in dirnames:
            subdir = dir+'/'+directory
            subdir_files_paths = get_files_paths(dir=subdir, subdirs=True)
            
            if subdir_files_paths:
                for file_path in subdir_files_paths: files_paths.append(file_path)
        
        # could query the user each iteration ----------------------------------------------
            # on whether they want to include a detected directory
            # or make this functionality in the ui
    
    for file in filenames: # constrain files based on extensions
        if file.split('.')[1] in supported_filetypes:
            files_paths.append([file, dir])

    return files_paths
    # this can be used to display files and dirs to user in ui later

# files_paths = get_files_paths(dir=directory, subdirs=True)
files_paths = get_files_paths(dir=directory+'/test', subdirs=True)
add_files_to_db(files_paths)
print(len(files_paths))