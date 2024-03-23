import math


print("각도     sin      cos     tan")
print("=" * 45)


for angle in range(0,91,15):
    rad = angle / 180 * (math.pi) 
    sin = math.sin(rad)
    cos = math.cos(rad)

    
    if angle == 90:
        tan = "tan 90도는 정의되지 않습니다."

    else:
        tan = math.tan(rad)
 
    print("{}\t{:.4f}\t {:.4f}\t {}\t".format(angle,sin,cos,tan))

