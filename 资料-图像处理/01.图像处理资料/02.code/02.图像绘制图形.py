import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 创建图像
img = np.zeros((512,512,3),np.uint8)

# 2 绘制图形
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.circle(img,(200,200),70,(0,0,255),-1)
cv.rectangle(img,(100,200),(300,400),(0,0,255),10)  # 定位顶点的位置
cv.putText(img,"hello",(100,150),cv.FONT_HERSHEY_COMPLEX,5,(255,255,255),3)


# 3 显示结果
# plt.imshow(img[:,:,::-1])
plt.imshow(img[:,:,::-1])  # 所有元素反转  rgb  bgr
plt.show()
