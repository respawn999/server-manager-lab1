import random
import time

class Server:

    def __init__(self, c):
        self.c = c
        self.started = False
        self.last_active = time.time()

    def has_c(self, workload):
        return self.started and (self.c-workload) >= 0
    
    def started(self):
        self.started = True
        self.last_active = time.time()

    def stop(self):
        self.started = False

    def idle(self):
        return not self.started and (time.time() - self.last_active) <= 5
    

class Job:

    def __init__(self, id, workload):
        self.id = id
        self.workload = workload


    def jobQueue(self,id,workload):
        queue = []
        for i in range(1,51):
            workload = random.randint(1,20)
            job = Job(i, workload)
            time.sleep(random.randint(2,5))
            job.append(queue)

        for i in queue:
            print(i)
        


    






    

    
    


