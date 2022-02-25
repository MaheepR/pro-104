import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (75,90),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255))

cv2.putText(img,
            "Mercury",
            (105,180), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (185,270), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (290,270), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (390,270), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (490,90), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (720,115), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (940,130), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1080,130), 
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("output",img)

cv2.imwrite("Solar_Systemwithname.jpg",img)

cv2.waitKey(0)