import cv2 as cv

def main():
    imageName = './ml_md/python.jpg'
    # Loads an image
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print("error")
        return -1
    
    for x in range(len(src)):
        for y in range(len(src[x])):
            src[x][y]=(src[x][y][0]+100,src[x][y][1]+100,src[x][y][2]+100)
    while True:
        
        cv.imshow("ok", src)
        c = cv.waitKey(100)
        if c == 27:
            break
    cv.imwrite("py2.jpg", src)
    return 0

if __name__=="__main__":
    main()