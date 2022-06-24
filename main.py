from PIL import Image



def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

if __name__ == '__main__':
  im = Image.open('data/png/スクリーンショット 2022-06-12 195440.png')
  im_new = crop_center(im, 300, 150)
  im_new.save('data/png/001.png', quality=95)