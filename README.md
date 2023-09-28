# Software Engineering lab 1

First university software eng. project, given a set of 9 requirements listed below

1. There are S=10 number of servers that are managed by the manager.
2. The server manager will start and stop servers based on the demand for compute power
by sending them a “start” or “stop” signal.
3. Demand for compute power, or “jobs”, are entered (generated) into a queue; new jobs
arrive every X time units, where X is a random value between 2 and 5.
4. Jobs have an iden;fier and a workload of J units. For example, a job of J=100 indicates
that it takes 100 time units to execute it.
5. A server has a certain capacity C, which means that it can execute jobs with a total
compute demand of C at any one moment. For example, if C is 5, then it can run 5 jobs in
parallel.
6. The server manager takes jobs from the input queue, and allocates them to a server that
has capacity. If there is no server with capacity, it will start a new server.
7. Servers may be “idle” (i.e. have no jobs to run) for a maximum of 5 time units, after
which they are stopped by the server manager.
8. The server manager application has a simple visualiza;on by drawing 1 “*” character for
each job it has; the visualization is updated every second.
9. Once a job is entered into the queue, it may have to wait before it can be allocated to a
server to be processed. The maximum waitng time is W=3.
