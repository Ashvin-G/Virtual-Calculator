import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy import prod
from numpy import subtract

cap = cv2.VideoCapture(0)

blue_lower=np.array([100,150,0],np.uint8)
blue_upper=np.array([140,255,255],np.uint8)

kernel = np.ones((5, 5))


result = 0
num = []

def draw_border(frame):
    cv2.rectangle(frame, (32, 50), (242, 400), (0, 0, 255), 2)

def draw_display(frame):
    cv2.rectangle(frame, (44, 63), (230, 98), (0, 0, 255), 2)

def draw_buttons(frame):
    cv2.rectangle(frame, (44, 110), (84, 150), (0, 0, 255), 2)
    cv2.putText(frame, "1", (54, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (115, 110), (155, 150), (0, 0, 255), 2)
    cv2.putText(frame, "2", (125, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (190, 110), (230, 150), (0, 0, 255), 2)
    cv2.putText(frame, "3", (200, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (44, 170), (84, 210), (0, 0, 255), 2)
    cv2.putText(frame, "4", (54, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (115, 170), (155, 210), (0, 0, 255), 2)
    cv2.putText(frame, "5", (125, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (190, 170), (230, 210), (0, 0, 255), 2)
    cv2.putText(frame, "6", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (44, 230), (84, 270), (0, 0, 255), 2)
    cv2.putText(frame, "7", (54, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (115, 230), (155, 270), (0, 0, 255), 2)
    cv2.putText(frame, "8", (125, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (190, 230), (230, 270), (0, 0, 255), 2)
    cv2.putText(frame, "9", (200, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (44, 290), (84, 330), (0, 0, 255), 2)
    cv2.putText(frame, "+", (54, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (115, 290), (155, 330), (0, 0, 255), 2)
    cv2.putText(frame, "*", (125, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (190, 290), (230, 390), (0, 0, 255), 2)
    cv2.putText(frame, "=", (197, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (44, 350), (84, 390), (0, 0, 255), 2)
    cv2.putText(frame, "-", (54, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, (115, 350), (155, 390), (0, 0, 255), 2)
    cv2.putText(frame, "C", (129, 375), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


def process(frame):

    global result, num

    roi1 = frame[110:150, 44:84]
    hsv1 = cv2.cvtColor(roi1, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv1, blue_lower, blue_upper)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi2 = frame[110:150, 115:155]
    hsv2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(hsv2, blue_lower, blue_upper)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
    contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi3 = frame[110:150, 190:230]
    hsv3 = cv2.cvtColor(roi3, cv2.COLOR_BGR2HSV)
    mask3 = cv2.inRange(hsv3, blue_lower, blue_upper)
    mask3 = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, kernel)
    contours3, hierarchy = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi4 = frame[170:210, 44:84]
    hsv4 = cv2.cvtColor(roi4, cv2.COLOR_BGR2HSV)
    mask4 = cv2.inRange(hsv4, blue_lower, blue_upper)
    mask4 = cv2.morphologyEx(mask4, cv2.MORPH_OPEN, kernel)
    contours4, hierarchy = cv2.findContours(mask4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi5 = frame[170:210, 115:155]
    hsv5 = cv2.cvtColor(roi5, cv2.COLOR_BGR2HSV)
    mask5 = cv2.inRange(hsv5, blue_lower, blue_upper)
    mask5 = cv2.morphologyEx(mask5, cv2.MORPH_OPEN, kernel)
    contours5, hierarchy = cv2.findContours(mask5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi6 = frame[170:210, 190:230]
    hsv6 = cv2.cvtColor(roi6, cv2.COLOR_BGR2HSV)
    mask6 = cv2.inRange(hsv6, blue_lower, blue_upper)
    mask6 = cv2.morphologyEx(mask6, cv2.MORPH_OPEN, kernel)
    contours6, hierarchy = cv2.findContours(mask6, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi7 = frame[230:270, 44:84]
    hsv7 = cv2.cvtColor(roi7, cv2.COLOR_BGR2HSV)
    mask7 = cv2.inRange(hsv7, blue_lower, blue_upper)
    mask7 = cv2.morphologyEx(mask7, cv2.MORPH_OPEN, kernel)
    contours7, hierarchy = cv2.findContours(mask7, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi8 = frame[230:270, 115:155]
    hsv8 = cv2.cvtColor(roi8, cv2.COLOR_BGR2HSV)
    mask8 = cv2.inRange(hsv8, blue_lower, blue_upper)
    mask8 = cv2.morphologyEx(mask8, cv2.MORPH_OPEN, kernel)
    contours8, hierarchy = cv2.findContours(mask8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roi9 = frame[230:270, 190:230]
    hsv9 = cv2.cvtColor(roi9, cv2.COLOR_BGR2HSV)
    mask9 = cv2.inRange(hsv9, blue_lower, blue_upper)
    mask9 = cv2.morphologyEx(mask9, cv2.MORPH_OPEN, kernel)
    contours9, hierarchy = cv2.findContours(mask9, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    rois = frame[290:330, 44:84]
    hsvs = cv2.cvtColor(rois, cv2.COLOR_BGR2HSV)
    masks = cv2.inRange(hsvs, blue_lower, blue_upper)
    masks = cv2.morphologyEx(masks, cv2.MORPH_OPEN, kernel)
    contourss, hierarchy = cv2.findContours(masks, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    roip = frame[290:330, 115:155]
    hsvp = cv2.cvtColor(roip, cv2.COLOR_BGR2HSV)
    maskp = cv2.inRange(hsvp, blue_lower, blue_upper)
    maskp = cv2.morphologyEx(maskp, cv2.MORPH_OPEN, kernel)
    contoursp, hierarchy = cv2.findContours(maskp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roie = frame[290:390, 190:230]
    hsve = cv2.cvtColor(roie, cv2.COLOR_BGR2HSV)
    maske = cv2.inRange(hsve, blue_lower, blue_upper)
    maske = cv2.morphologyEx(maske, cv2.MORPH_OPEN, kernel)
    contourse, hierarchy = cv2.findContours(maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #roid = frame[350:390, 44:84]
    #hsvd = cv2.cvtColor(roid, cv2.COLOR_BGR2HSV)
    #maskd = cv2.inRange(hsvd, blue_lower, blue_upper)
    #maskd = cv2.morphologyEx(maskd, cv2.MORPH_OPEN, kernel)
    #contoursd, hierarchy = cv2.findContours(maskd, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    roic = frame[350:390, 115:155]
    hsvc = cv2.cvtColor(roic, cv2.COLOR_BGR2HSV)
    maskc = cv2.inRange(hsvc, blue_lower, blue_upper)
    maskc = cv2.morphologyEx(maskc, cv2.MORPH_OPEN, kernel)
    contoursc, hierarchy = cv2.findContours(maskc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    if (len(contours1) == 1):
        cv2.putText(frame, "1", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 1 not in num:
            num.append(1)

    if (len(contours2) == 1):
        cv2.putText(frame, "2", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 2 not in num:
            num.append(2)

    if (len(contours3) == 1):
        cv2.putText(frame, "3", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 3 not in num:
            num.append(3)

    if (len(contours4) == 1):
        cv2.putText(frame, "4", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 4 not in num:
            num.append(4)

    if (len(contours5) == 1):
        cv2.putText(frame, "5", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 5 not in num:
            num.append(5)

    if (len(contours6) == 1):
        cv2.putText(frame, "6", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 6 not in num:
            num.append(6)

    if (len(contours7) == 1):
        cv2.putText(frame, "7", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 7 not in num:
            num.append(7)

    if (len(contours8) == 1):
        cv2.putText(frame, "8", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 8 not in num:
            num.append(8)

    if (len(contours9) == 1):
        cv2.putText(frame, "9", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if 9 not in num:
            num.append(9)

    if (len(contourss) == 1):
        cv2.putText(frame, "+", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        result = sum(num)

    if (len(contoursp) == 1):
        cv2.putText(frame, "*", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        result = prod(num)

    if (len(contourse) == 1):
            cv2.putText(frame, str(result), (130, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if (len(contoursc) == 1):
        cv2.putText(frame, "CLEAR", (90, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        num.clear()
    #if (len(contoursd) == 1):
    #    cv2.putText(frame, "-", (200, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    #    result = num[0] - num[1]











    #cv2.imshow('ROI 1', maskd)
    #cv2.imshow('ROI 2', roi2)
    cv2.imshow('ROI 3', mask3)
    #cv2.imshow('ROI 4', roi4)
    #cv2.imshow('ROI 5', roi5)
    #cv2.imshow('ROI 6', roi6)
    #cv2.imshow('ROI 7', roi7)
    #cv2.imshow('ROI 8', roi8)
    #cv2.imshow('ROI 9', roi9)
    #cv2.imshow('ROI S', rois)
    #cv2.imshow('ROI P', roip)
    #cv2.imshow('ROI E', roie)






def main():

    while True:
        ret, frame = cap.read()

        process(frame)

        draw_border(frame)
        draw_display(frame)
        draw_buttons(frame)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) == 27:
            break

    # plt.imshow(frame)
    # plt.show()
    cap.release()
    cv2.destroyAllWindows()

main()
