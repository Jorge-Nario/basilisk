from multiprocessing import Pool
class Multiprocessor:
    def __init__(self, processors=None):
        self.commands = []
        self.processors = processors

    def submit_job(self, function, *args, **kwargs):
        self.commands.append((function, args, kwargs))

    def run_jobs(self):
        return self.__multithreader()

    def __multithreader(self):
        with Pool(processes=self.processors) as pool:
            results = [pool.apply_async(function, args = args, kwds = kwargs) for function, args, kwargs in self.commands]
            retrieved = [result.get() for result in results]
        return retrieved
