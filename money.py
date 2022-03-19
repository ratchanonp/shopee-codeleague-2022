N, T = map(int, input().split())

user = {}

for i in range(N):
    name, bal = input().split()
    bal = int(bal)
    
    if name not in user:
        user[name] = bal
    else:
        user[name] += bal

for i in range(T):
    send, receive, bal = input().split()
    bal = int(bal)
    
    if user[send] >= bal:
        user[send] -= bal
        user[receive] += bal

sorted_user = sorted(user.items(), key=lambda x: x[0], reverse=False)

for user in sorted_user:
    print(user[0], user[1]) 


"""
3 4
amir 10
brenda 10
charlie 10
amir brenda 5
brenda charlie 5
charlie amir 20
charlie amir 7
"""