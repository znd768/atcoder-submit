input_s = input()
len_s = len(input_s)
num_of_questions = int(input())
questions = list(map(lambda x: int(x)-1, input().split()))
for q in questions:
  if (q//len_s).bit_count() & 1:
    print(input_s[q%len_s].swapcase(), end=" ")
  else:
    print(input_s[q%len_s], end=" ")