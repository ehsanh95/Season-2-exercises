import numpy as np
import matplotlib.pyplot as plt

f = open("Files/Pr4_project_data.csv" , "r" )
text=f.read()
f.close()
# print(text)

lines=text.split("\n")  
# print(lines)


table=[]        
for line in lines:
    if line:
        columns=line.split(",")
        table.append(columns)


table.pop(0)   
print(table)
quit()


values_columns=[]
for column in table:
    values_columns.append([int(column[1]),int(float(column[5]))])
values_columns.reverse() 
# print(values_columns)

values_array=np.array(values_columns)
values_close=values_array[:,1]
days=values_array[:,0]
days=days
print(days)
plt.plot(values_close)
plt.show()
