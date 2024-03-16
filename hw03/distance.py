import math
print("두 지점 사이 거리 구하기. 단, 좌표는 정수로 입력하세요.")
ax = int(input("첫 번째 지점의 x좌표를 입력해주세요."))
ay = int(input("첫 번째 지점의 y좌표를 입력해주세요."))
         
bx = int(input("두 번째 지점의 x좌표를 입력해주세요."))
by = int(input("두 번째 지점의 y좌표를 입력해주세요.\n"))

cx = (bx-ax)
cy = (by-ay)
         
dis = math.sqrt((cx**2 + cy**2))

print("({},{})와(과) ({},{})사이의 거리는 {}입니다.\n".format(ax,ay,bx,by,dis))