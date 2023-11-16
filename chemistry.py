for t in range(int(input())):
  n,k = map(int,input().split())
  test_word = input()
  dic = {}

  for i in range(len(test_word)):
    if test_word[i] in dic:
      dic[test_word[i]] += 1
    else:
      dic[test_word[i]] = 1
  
  odds = 0
  for x in dic:
    if dic[x]%2 == 1:
      odds += 1
  
  if (n-k)%2 == 0:
    if odds <= k and (k-odds)%2 == 0:
        print("YES")
    else:
        print("NO")
  else:
    if odds-1 <= k and (k-odds)%2 == 1:
        print("YES")
    else:
        print("NO")