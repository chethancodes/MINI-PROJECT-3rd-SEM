import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

print('~~~~~~~"WELCOME TO QUICK-SCAN"~~~~~~~')
choice = 1
filename = input('Enter the file to register or inspect the data:')
listofdata = []

while choice != "E":
    print('"I"==> TO INSPECT')
    print('"R"==> TO REGISTER THE DATA')
    print('"E"==> TO EXIT')
    choice = input('ENTER YOUR CHOICE : ')
    f = open(filename, "r+")
    mydatalist = f.read().splitlines()
    if choice == "I":

        key = int(input('enter number of scans:'))
        count = 0

        while True:

            success, img = cap.read()
            if count >= key:
                break
            for barcode in decode(img):
                count = count + 1
                myData = barcode.data.decode('utf-8')
                print('The scaned data is:')
                print(myData)

                if myData in mydatalist:
                    print('valid')
                else:
                    print('invalid')

                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (171, 130, 255), 5)
                pts2 = barcode.rect
                cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

            cv2.imshow('Resultcam', img)
            cv2.waitKey(1)
        f.close()

    elif choice == "R":

        key2 = int(input('enter number of scans:'))
        count2 = 0

        while True:

            success, img = cap.read()
            if count2 >= key2 :
                break

            for barcode in decode(img):
                count2 = count2 + 1

                wrData = barcode.data.decode('utf-8')
                print('The scaned data is:')
                print(wrData)

                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (132, 112, 255), 5)

                if wrData not in listofdata:
                    listofdata.append(wrData)
                    f.writelines(wrData + '\n')

            cv2.imshow('Resultwcam', img)
            cv2.waitKey(1)
        f.close()

    elif choice == "E":
        print("Exiting from the program!!")

    else:
        print("~~~~~INVALID CHOICE~~~~~")
        print('PLEASE ENTER "I" OR "R" OR "E" \n\n\n')
