from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im= Image.open("beach.jpg")
l1st=list(im.getdata())
list_ler= len(list(im.getdata()))
lerp=[]


for i in range(list_ler):
    red= l1st[i][0]
    green= l1st[i][1]
    blue= l1st[i][2]
    intensity= red + green + blue
#print(intensity)
    if intensity<182:
        l1st[i]= darkBlue
    elif intensity>182 and intensity<364:
        l1st[i]=red
    elif intensity>364 and intensity<546:
        l1st[i]=lightBlue
    elif intensity>546:
        l1st[i]= yellow

im.putdata(l1st)
im.show()



#print(l1st)
#for loop ro add three values, change intenisty according to value
# pixel= value * scale + offset
# im.putdata(data)
# im.putdata(data, scale, offset)

# pixel= value * scale + offset
# im.putdata(data)
# im.putdata(data, scale, offset)
