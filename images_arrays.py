# recommend to use .ipynb
# import useful library
import numpy as np
from skimage import io
from skimage import data
from skimage import color
from skimage import img_as_float, img_as_ubyte
from matplotlib import pyplot as plt


# generate random image
random_image = np.random.random([500, 500])
img = plt.imshow(random_image, cmap='Greens')
plt.colorbar(img);    # put ; at the end to remove the <> line


# show coin image with one color type is used
coins = data.coins()
print('type: ', type(coins))
print('dtype: ', coins.dtype)
print('shape: ', coins.shape)
print("Values min/max:", coins.min(), coins.max())
img = plt.imshow(coins, cmap='Greens')
plt.colorbar(img);


# show cat image with RGB
cat = data.chelsea()
print('type: ', type(cat))
print('dtype: ', cat.dtype)
print('shape: ', cat.shape)
print("values min/max:", cat.min(), cat.max())
img = plt.imshow(cat)
plt.colorbar(img);


# draw triangle on cat image
# cat[rows(y-axis), cols(x-axis), channel(RGB)] = [red, green, blue]
cat[50:160, 10:110, :] = [255, 0, 0]
plt.imshow(cat);


# show two images at the same time
img0 = data.chelsea()
img1 = data.rocket()

f, (ax0, ax1) = plt.subplots(1, 2, figsize=(20, 10))
ax0.imshow(img0)
ax0.set_title('Cat')
ax0.axis('off')

ax1.imshow(img1)
ax1.set_title('Rocket')
ax1.set_xlabel(r'Launching position $\alpha=320$');


# data type of array of image
linear1 = np.linspace(0, 1, 50).reshape(10, 5)
linear2 = np.linspace(0, 255, 50).reshape(10, 5).astype(np.uint8)

print('linear 1:', linear1.dtype, linear1.min(), linear1.max())
print('linear 2:', linear2.dtype, linear2.min(), linear2.max())

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(linear1)
ax2.imshow(linear2);


# data type of array of image (using library skimage)
img = data.chelsea()

image_float = img_as_float(img)
image_ubyte = img_as_ubyte(img)

print('type:', image_float.dtype, image_float.min(), image_float.max())
print('type:', image_ubyte.dtype, image_ubyte.min(), image_ubyte.max())


# visualize RGB channel
img = plt.imread('./wallpaper.png')

r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

f, axes = plt.subplots(1, 4, figsize=(16, 5))
(ax_r, ax_g, ax_b, ax_colour) = axes

ax_r.imshow(r)
ax_r.set_title('red channel')

ax_g.imshow(g)
ax_g.set_title('green channel')

ax_b.imshow(b)
ax_b.set_title('blue channel')

ax_colour.imshow(np.stack([r, g, b], axis=2))
ax_colour.set_title('original pic');
