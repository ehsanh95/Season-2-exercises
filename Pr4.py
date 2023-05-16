import numpy as np
import matplotlib.pyplot as plt

f = open("Files/Pr4_project_data.csv" , "r" )
text=f.read()
f.close()
# print(text)
# quit()
lines=text.split("\n")  
# print(lines)
# quit()

table=[]        
for line in lines:
    if line:
        columns=line.split(",")
        table.append(columns)


table.pop(0)   
# print(table)
# quit()


values_columns=[]
for column in table:
    values_columns.append([int(column[1]),int(float(column[5]))])
values_columns.reverse() 
# print(values_columns)
# quit()
values_array=np.array(values_columns)
values_close=values_array[:,1]
days=values_array[:,0]
days=days
print(values_array)

move_size=150
moving_av=[]
for i in range(len(values_close)-move_size):
    values_mean=(values_close[i:i+move_size]).mean()
    moving_av.append(values_mean)




plt.plot(values_close)
plt.plot(moving_av)
plt.show()
