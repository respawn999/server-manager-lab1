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


def main():
    number_of_servers = 10
    servers = []
    i = 0
    for i in range(number_of_servers):
        servers.append(Server(5))

    job_q = []

    for i in range(1, 51):
        workload = (1,10)
        jobs = Job(i, workload)
        job_q.append(jobs)


    for j in job_q:
        for i, server in enumerate(servers):
            if server.has_c(workload):
                server.start()
                print(f"Job {j.id} on Server {i}")
            

if __name__ == "__main__":
    main()




    

    
    


