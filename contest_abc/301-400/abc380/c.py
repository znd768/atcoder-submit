N,K = map(int,input().split())
S = input()

# split
idx = [0] + [i for i in range(1,N) if S[i-1]!=S[i]] + [N]
splited_S = [S[idx[i]:idx[i+1]] for i in range(len(idx)-1)]

# swap
if S[0] == '0':
  kth_1_idx = 2*K-1
else:
  kth_1_idx = 2*K-2

splited_S[kth_1_idx-1], splited_S[kth_1_idx] = splited_S[kth_1_idx], splited_S[kth_1_idx-1]

# join
T = "".join(splited_S)

print(T)
