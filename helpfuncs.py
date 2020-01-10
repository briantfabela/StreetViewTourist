# Python 3.7.1 - Briant J. Fabela (12/26/2019)

from PIL import Image # PIL v7.0.0

def main():
    x = Image.open(r'screenshot.png')
    crop_img(x, 400,0,0,0,'helloworld', stamp='_ayylmao')

def crop_img(img, left, top, right, bottom, name, stamp='_cropped', ext="png"):
    """Crops and saves a PIL.Image.Image Object"""

    w, h = img.size
    result = img.crop((left, top, w-right, h-bottom))

    result.save(name+stamp+'.'+ext)
    img.close()
    
if __name__ == "__main__":
    main()