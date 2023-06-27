

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

