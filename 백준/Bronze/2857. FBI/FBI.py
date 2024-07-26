#2857번
N=5
agent = []
ans = []
FBI = "FBI"
for i in range(N):
    agent.append(input())
for i in range(N):
    if FBI in agent[i]:
        ans.append(i+1)
if(len(ans)==0):
    print("HE GOT AWAY!")
else:
    for i in range(len(ans)):
        print(ans[i], end=' ')


