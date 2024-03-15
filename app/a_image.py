import glob
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont

class Image_start:
    def __init__(self):
        pass
        # print('it is image')

    def image_edit(self, image_dir):
             
        mane_img = image_dir[:].split('\\')                
        name_img = mane_img[-1]                
        ext_img = name_img.split('.')
        ext = ext_img[1].lower()
        
        if(ext == 'jpg' or ext == 'jpeg' or ext == 'png'):
        
            image = Image.open(image_dir)

            # Увеличиваем четкость с помощью фильтра
            image_sharpened = image.filter(ImageFilter.SHARPEN)
            image_sharpened = image.filter(ImageFilter.DETAIL)
            # image_sharpened = image.filter(ImageFilter.BLUR)

            new_file = f"new_img/{name_img}"
            # Сохраняем улучшенное изображение
            image_sharpened.save(new_file)
            
            # Image_start.TextInImage(image, "This is my text", "watermark")
            
            return new_file
        
    
    def TextInImage(im, text, watermark_img=False):
               
        width, height = im.size
        
        draw = ImageDraw.Draw(im)
        
        if text == "":
            text = "sample watermark"
        
        font = ImageFont.truetype('Arial.ttf', 46)
        
        draw.multiline_text((10, 10), text, font=font, fill=(0, 0, 0))
        
        im.save('new_img/watermark.jpg')
        
          
    def effects(effect:str):        
        pass
        # image = Image.open('input.jpg')
        # filtered_image = image.filter(ImageFilter.CONTOUR)
        # filtered_image.save('output_contour.jpg')
        # Фильтр "Цветовой баланс" (ColorBalance)
        
        # from PIL import Image, ImageOps

        # image = Image.open('input.jpg')
        # filtered_image = ImageOps.colorize(image, (0, 0, 0), (255, 255, 255))
        # filtered_image.save('output_colorbalance.jpg')
        # Фильтр "Лепестки" (Emboss)
        
        # from PIL import Image, ImageFilter

        # image = Image.open('input.jpg')
        # filtered_image = image.filter(ImageFilter.EMBOSS)
        # filtered_image.save('output_emboss.jpg')
        # Фильтр "Негатив" (Invert)
        
        # from PIL import ImageOps

        # image = Image.open('input.jpg')
        # filtered_image = ImageOps.invert(image)
        # filtered_image.save('output_invert.jpg')
        # Фильтр "Размытие" (Blur)
        
        # copy
        # from PIL import Image, ImageFilter

        # image = Image.open('input.jpg')
        # filtered_image = image.filter(ImageFilter.BLUR)
        # filtered_image.save('output_blur.jpg')