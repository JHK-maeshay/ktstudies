#추가실습q4
"""
Q4
각 자리가 숫자(0부터 9)로만 이루어진 문자열을 사용자로 부터 입력받아, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기(x) 혹은 더하기(+) 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, + 보다 x 를 먼저 계산하는 일반적인 방식과 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
입출력 예
숫자로 이루어진 문자열을 입력하세요. 02984
0 + 2 x 9 x 8 x 4 = 576
숫자로 이루어진 문자열을 입력하세요. 567
5 x 6 x 7 = 210
"""

def solution(input):
  #print(input)
  result=0

  for n in input:
    #print(n)
    if n<=1 or result<=1:
      result+=int(n)
    else:
      result*=int(n)

  return result

print(solution('02984'))
print(solution('567'))