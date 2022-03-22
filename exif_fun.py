#!/usr/bin/env python

# Save a JPG with custom EXIF data
from PIL import Image

img = Image.open('image.png')
new_img = img.convert('RGB')

tags = img.getexif()

# Some useful tags, from https://www.exiftool.org/TagNames/EXIF.html
tags[0x010e] = 'my fancy prompt goes here | trending on ArtStation' # Image Description
tags[0x010f] = '--seed 123 --steps 1000' # Make (other options)
tags[0x0110] = '512x512_diffusion_uncond_finetune_008100 + ViTB32' # Model LOL
tags[0x0131] = 'Disco Diffusion v5' # Software
tags[0x013b] = '@hackerfriendly' # Artist

new_img.save('image.jpg', exif=tags)
