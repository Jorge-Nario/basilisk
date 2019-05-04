from multiprocessing import Pool
import os
class Multiprocessor:
    def __init__(self, processors=None):
        self.commands = []
        self.processors = processors
        
    def get_default_workers(self):
        return os.cpu_count()
    
    def s(self, function, *args, **kwargs):
        self.submit_job(function, *args, **kwargs)
    
    def submit_job(self, function, *args, **kwargs):
        self.commands.append((function, args, kwargs))
        
    def r(self):
        return self.run_jobs()
        
    def run_jobs(self):
        return self.__multithreader()
    
    def __multithreader(self):
        with Pool(processes=self.processors) as pool:
            results = [pool.apply_async(function, args = args, kwds = kwargs) for function, args, kwargs in self.commands]
            retrieved = [result.get() for result in results]
        return retrieved