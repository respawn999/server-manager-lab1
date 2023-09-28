import random
import time

class Server:
    # initilisation for the Server class
    def __init__(self, c):
        self.c = c
        self.started = False
        self.last_active = time.time()

    # Checking if server has capacity, labelled as c following requirements
    def has_c(self, workload):
        return self.started and (self.c-workload) >= 0
    
    # Function to start server
    def started(self):
        self.started = True
        self.last_active = time.time()

    # Function to stop server
    def stop(self):
        self.started = False

    # Function to label a server idle if inactive for more than 5 time units
    def idle(self):
        return not self.started and (time.time() - self.last_active) <= 5
    

class Job:
    # initilising Job class
    def __init__(self, id, workload):
        self.id = id
        self.workload = workload

    # Function to create a queue as a list, add jobs, assign ids and add created jobs onto the queue
    def jobQueue(self,id,workload):
        queue = []
        for i in range(1,51):
            workload = random.randint(1,20)
            job = Job(i, workload)
            # As per requirements, delay between jobs is implemented, with the wait time being a random time unit bwtween 2 and 5
            time.sleep(random.randint(2,5))
            # Adding job onto queue list
            job.append(queue)
        


    






    

    
    


