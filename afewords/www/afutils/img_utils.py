
import Image
import tempfile

image_type_doc = {
    'image/gif' : 'GIF',
    'image/jpeg' : 'JPEG',
    'image/pjpeg' : 'JPEG',
    'image/bmp' : 'BMP',
    'image/png' : 'PNG',
    'image/x-png' : 'PNG',
    'image/x-icon' : 'ICO',
}

def upload_img(uploaded_file, wl=16, wh=2000, hl=16, hh=2000):
    '''uploaded_file from handler, return a tmp file'''
    image_type_list = ['image/gif', 'image/jpeg', 'image/pjpeg', 
                            'image/bmp', 'image/png', 'image/x-png']
    if uploaded_file['content_type'] not in image_type_doc:
    #if uploaded_file['content_type'] not in image_type_list:
        return 51, 'Unsupported file type'
    img_format = image_type_doc[uploaded_file['content_type']]
    if len(uploaded_file['body']) > 2 * 1024 * 1024:
        return 52, 'Uploaded file too large'
    tmp_file = tempfile.NamedTemporaryFile(delete=True)   
    tmp_file.write(uploaded_file['body'])
    tmp_file.seek(0)
    try:
        img_tmp = Image.open(tmp_file.name)
    except IOError, e:
        tmp_file.close()
        return 53, 'Invalid image'
    tmp_file.close()
    if ((wl <= img_tmp.size[0] <= wh) and 
                (hl <= img_tmp.size[1] <= hh)) is False:
        return 54, 'Invalid Width or Height'
    if not img_tmp.format:
        img_tmp.format = img_format
    return 0, img_tmp 


def img_crop(img, box):
    try:
        box = [int(each) for each in box]
    except ValueError, e:
        return 56, 'Invalid crop arguments'
    if not (0 <= box[0] <= img.size[0]) or not (0 <= box[1] <= img.size[1]):
        return 56, 'Invalid crop arguments'
    if box[0] >= box[2] or box[1] >= box[2]:
        return 56, 'Invalid crop arguments'
    tmp = img.crop(box)
    tmp.format = img.format
    return 0, tmp
