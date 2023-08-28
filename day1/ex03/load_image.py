from PIL import Image
from numpy import array

def ft_load(path: str) -> array or None:
    try:
        assert isinstance(path, str) and path != '', 'Error: bad argument'
        image = Image.open(path)
        npImage = array(image)
        print(f'The shape of image is {npImage.shape}\n{npImage}')
        return npImage
    except Exception as e:
        return e