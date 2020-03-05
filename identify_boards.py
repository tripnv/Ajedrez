"""The script below, in vague terms, gets the picture and returns the identified boards """
import numpy as np
import cv2 as cv
import os 
import matplotlib.pyplot as plt


def img_read(path):
    
    pict = cv.imread(path)
    gray = cv.cvtColor(pict, cv.COLOR_BGR2GRAY)

    
    return gray


def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_boards(pict):
    
    boards = []
    
    blur = cv.GaussianBlur(pict, (5,5), 0)
    thresh = cv.adaptiveThreshold(blur,255,1,1,11,2)
    
    contours, _hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        cnt_len = cv.arcLength(cnt, True)
        cnt = cv.approxPolyDP(cnt, 0.02*cnt_len, True)
        if len(cnt) == 4 and cv.contourArea(cnt) > 5000 and cv.isContourConvex(cnt):
            cnt = cnt.reshape(-1, 2)
            max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
            if max_cos < 0.1:
                boards.append(cnt)
                        
    return boards


def save_boards(boards,img):
    for i in range(len(boards)):
        x, y, width, height = cv.boundingRect(boards[i])
        roi = img[y:y+height, x:x+width]
        cv.imwrite("board_"+str(i)+".jpg",roi)

def main():
    if __name__ == "__main__":
        path = os.getcwd()
        picture_name = "sample.jpg"
        path = path + "/" + picture_name
        print(path)
        pict = img_read(path)
        cont = find_boards(pict)
        save_boards(cont,pict)

main()