import matplotlib.pyplot as plt


jobs = [(1, 5), (6, 7), (3, 8), (2, 4), (8, 10), (5, 9), (1, 2), (9, 10)]

def solve(jobs):
    schedule = [0]*len(jobs)
    machines = []
      
    for job in sorted(list(enumerate(jobs)), key = lambda a : a[1]):       
        
        for i in range(len(schedule)):          
            
            try: machines[i]
            except: machines.append(0)
            
            if job[1][0]>machines[i]:
                
                machines[i]=job[1][1]                
                schedule[job[0]]=i+1
                break    
    return schedule


schedule=solve(jobs)

for i in range(len(jobs)):
    plt.plot(jobs[i],[schedule[i]]*2,'.-',linewidth=2,markersize=20)
    
plt.locator_params(axis="both", integer=True, tight=True)
plt.xlabel('time')
plt.ylabel('machine')