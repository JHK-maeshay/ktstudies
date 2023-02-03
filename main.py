def solution(lottos, win_nums):
  answer = []

  var=0
  correct=0
  win_nums.sort()
  for i in lottos:
    if i==0:
      var+=1
    elif i in win_nums:
      correct+=1
    
  max=correct+var
  min=correct

  def rank(a):
    if 0<a<7: a=7-a
    elif a==0: a=6
    else:a=-1
    return a

  answer.append(rank(max))
  answer.append(rank(min))
  return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
answer = solution(lottos, win_nums)
print(answer)

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]	
answer = solution(lottos, win_nums)
print(answer)