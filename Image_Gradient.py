from PIL import Image
import cv2                      
import sys
from collections import Counter

#https://stackoverflow.com/questions/39842286/python-pillow-add-transparent-gradient-to-an-image

class BackgroundColorDetector():     
    def __init__(self, imageLoc):
        self.img =cv2.imread(imageLoc, 1)
        self.manual_count = {}
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w*self.h        
 
    def count(self):
        for y in range(0, self.h):
            for x in range(0, self.w):
                RGB = (self.img[x,y,2],self.img[x,y,1],self.img[x,y,0])
                if RGB in self.manual_count:
                    self.manual_count[RGB] += 1
                else:
                    self.manual_count[RGB] = 1
                    
    def Five_most_common(self):
        self.count()
        self.number_counter = Counter(self.manual_count).most_common(1)
            
    def detect(self):
        self.Five_most_common()
        try:
            self.percentage_of_first = (float(self.number_counter[0][1])/self.total_pixels)
            #self.percentage_of_second = (float(self.number_counter[1][1])/self.total_pixels)              
            topColour = self.number_counter[0][0]
            return (topColour[0] , topColour[1] , topColour[2])
        except:
            print("Error Type :",sys.exc_info()[0], "occured.")                     
            print("Exception observed during the calculation of top five colour elements")       
            return 1.0

dir = '.'
list_of_elements = os.listdir(dir)
list_of_elements = natsort.natsorted(list_of_elements)
list_of_elements_new =[]

for item in list_of_elements:
    if item.endswith('.jpg'):
        list_of_elements_new.append(item)   

for item in list_of_elements_new:
    im = Image.open(item)   
    width, height = im.size
    gradient_magnitude=2
    left=0
    right=width
    bottom=height
    top=round(0.70*bottom)
    box1 =(left,top,right,bottom)
    ic1 = im.crop(box1)
    ic1.save("bottom.jpg")            
            
    BackgroundColor  = BackgroundColorDetector('bottom.jpg')
    test             = BackgroundColor.detect()           
    
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    width, height = im.size
    gradient = Image.new('L', (1, height), color=0xFF)
    for x in range(height):
        gradient.putpixel((0, x), int(255 * (1 - gradient_magnitude * float(x)/height)))     
    alpha = gradient.resize(im.size)
    alpha = alpha.rotate(180)
    black_im = Image.new('RGBA', (width, height), color=test) # i.e. black
    black_im.putalpha(alpha)
    gradient_im = Image.alpha_composite(im, black_im)
    gradient_im.save(item)  


# =============================================================================
# img =Image.open('2.jpg')
# manual_count = {}
# w, h = img.size
# h=round(0.6*h)
# total_pixels = w*h
# =============================================================================


# =============================================================================
# left=0
# #top=100
# #right=577
# right=width
# #bottom=1029
# bottom=height
# #test=round(bottom/10)
# #top=bottom-test-10
# #top=700
# top=round(0.70*bottom)
# picture = Image.open('2.jpg')
# box1 =(left,top,right,bottom)
# ic1 = picture.crop(box1)
# ic1.save("bottom.jpg")    
# 
# ic1.show()
# 
# ic1=ic1.rotate(180)
# =============================================================================
