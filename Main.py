import cv2

filename = ""

image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edged = cv2.Canny(gray, 10, 250)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

triangles = 0
squares = 0
circles = 0

for c in cnts:

    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

    if len(approx) == 3:
        cv2.drawContours(image, [approx], -1, (255, 0, 0), 2)
        triangles +=1
    if len(approx) ==4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        squares +=1
    if len(approx)>=7:
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
        circles +=1

print("Triangles: " + str(triangles))
print("Squares: "+ str(squares))
print("Circles: "+ str(circles))

cv2.imwrite('result.jpg',image)