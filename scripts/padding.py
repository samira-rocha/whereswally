import numpy as np

def custom_padding(img):

    img = np.array(img)/255

    # COLOURED
    # =============
    if img.shape[-1] == 3:
        padded_img = np.zeros([256, 256, 3])

        ## Padding a "intermediate" image 128 x 128
        if img.shape == (128, 128, 3):
            padded_img[64:192, 64:192,:] = img
        ## Padding a "small" image 64 x 64
        if img.shape == (64,64, 3):
            padded_img[96:160, 96:160,:] = img

    # BLACK AND WHITE
    # =============
    if img.shape[-1] == 1:
        padded_img = np.zeros([256, 256, 1])

        ## Padding a "intermediate" image 128 x 128
        if img.shape == (128, 128, 1):
            padded_img[64:192, 64:192,:] = img
        ## Padding a "small" image 64 x 64
        if img.shape == (64,64, 1):
            padded_img[96:160, 96:160,:] = img

    return padded_img

def applying_padding(img):
    X_s = []
    for x in range(len(img)):
        temp = np.array(img[x])
        X_s.append(custom_padding(temp))
    return X_s
