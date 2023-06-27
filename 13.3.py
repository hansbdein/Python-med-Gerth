



st=open('students.txt')
stlines=st.readlines()
students = sorted([list(line.rstrip("\n").split(";")) for line in stlines])
st.close()

gr=open('grades.txt')
grlines=gr.readlines()
grades = sorted([list(line.rstrip("\n").split(";")) for line in grlines])
gr.close()


namelenmax=max(len(x) for x in list(zip(*students))[1])


print('Student id'+' '+'Name'+' '*(namelenmax-3)+'Average'+' '+'#Courses')
print('='*(28+namelenmax))



gnr=0

for nr in range(len(students)):
    totalgr=0
    coursenr=0
    
    while grades[gnr][0]==students[nr][0]:
        
        totalgr+=int(grades[gnr][2])
        coursenr+=1
        if gnr==len(grades)-1:
            break
        gnr+=1
    
    average=totalgr/coursenr if coursenr else 0
    
    
    print(students[nr][0]+' '*(7-len(students[nr][0]))+
          students[nr][1]+' '*(namelenmax-len(students[nr][1]))+
          ' '*8+ '%.2f' % average+
          ' '*8 + str(coursenr))