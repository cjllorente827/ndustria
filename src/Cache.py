import pickle, os
from tabulate import tabulate
from Logger import log, error

CACHE_PATH = "./temp"

class Cache:

    def __init__(self, path):
        self.setPath(path)
        self.table = []
        self.headers = [
            "Task",
            "File size (bytes)",
            "File name in cache"
        ]

    def writeCacheInfo(self):

        with open(self.info_file, "w") as info:
            info.write(f"\nCache location: {self.path}\n\n")
            info.write(tabulate(self.table, headers=self.headers))
            info.write("\n")


    def exists(self, task):
        cache_fname = os.path.join(self.path, task.getFilename())

        cache_hit = os.path.exists(cache_fname)
        
        return cache_hit 

    def load(self, task):
        
        cache_fname = os.path.join(self.path, task.getFilename())

        # if we have a previous result, serve that up
        try:
            with open(cache_fname, 'rb') as f:
                log(f"Found cache result for {cache_fname}")
                result = pickle.load(f)
        except FileNotFoundError as e:
            error(f"No cache result found for {cache_fname}")
        else:
            task.result = result

            return result

    def save(self, task):
        cache_fname = os.path.join(self.path, task.getFilename())
        
        with open(cache_fname, 'wb') as f:
            pickle.dump(task.result, f, protocol=0)

        file_size = os.stat(cache_fname).st_size
        self.table.append([
            str(task),
            file_size,
            os.path.basename(cache_fname)
        ])
        self.writeCacheInfo()
        log(f"Saved result of {task} to {cache_fname}")


    def remove(self, task):
        cache_fname = os.path.join(self.path, task.getFilename())
        try: 
            os.remove(cache_fname)
        except FileNotFoundError as e:
            pass



    def setPath(self, new_path):
        self.path = os.path.abspath(new_path)
        if not os.path.exists(self.path):
                os.mkdir(self.path)

        self.info_file = os.path.join(self.path, "cache_info")
        if not os.path.isfile(self.info_file):
            with open(self.info_file, 'a'):  # Create file if does not exist
                pass

  

    

    