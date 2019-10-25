import math
pi = math.pi

f_len = 50
f_wid = 50
def PointsInCircum(r):
    return [(int(25+ math.cos(2*pi/1000*x)*r),int(25+ math.sin(2*pi/1000*x)*r)) for x in range(0,1000+1)]

final_image = [["  " for x in range(f_len)] for y in range(f_wid)]

for x,y in PointsInCircum(20):
    #print(x,y )
    final_image[x][y] = "0 "

print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
      for row in final_image]))

#def PointsInCircum(r,n=100):
#    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]