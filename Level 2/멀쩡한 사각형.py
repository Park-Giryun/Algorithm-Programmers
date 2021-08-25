# 0825
# 멀쩡한 사각형
# idea: 최대공약수가 1일 때와 그 이상일 때를 생각해보자
import math
def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))