processes = [['p1',0,2],['p2',1,2],['p3',5,3],['p4',6,4]]
ct = [0,0,0,0]
tat = [0]*len(ct)
wt = [0]*len(ct)
for i in range(4):
    ct[i] = processes[i][2]+ct[i-1]
    tat[i] = ct[i]-processes[i][1]
    wt[i] = tat[i]-processes[i][2]
print('Process','AT\t','BT\t','CT\t','TAT\t','WT\t')
for j in range(4):
    print(processes[j][0],'\t',processes[j][1],'\t',processes[j][2],'\t',ct[j],'\t',tat[j],'\t',wt[j])
    
    
# process = ['p1','p2','p3','p4']
# at = [0,1,4,5]
# bt = [2,2,3,4]
# at = [0,1,2,3]
# bt = [5,3,8,6]
