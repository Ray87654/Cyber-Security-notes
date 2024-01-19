import os

tokens=[]
file_path="brokenAccessControl/hijackingSessionCookie/tokens"
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line: continue
        seq, epoch_time = line.replace('-', ' ').split(' ')
        tokens.append((seq, epoch_time))
print(tokens)
