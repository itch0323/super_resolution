import numpy as np
import cv2
import glob

#データセットのディレクトリパスを入力
paths = glob.glob("train/datasets/img_align_celeba/*")[:10000]

#すべてのデータを使用したい場合
#paths = glob.glob("/home/higuchi/Downloads/img_align_celeba/*")


def img_save(i, path):
    img = cv2.imread(path)
    hr = cv2.resize(img, dsize=(128, 128))
    lr = cv2.resize(img, dsize=(32, 32))

    cv2.imwrite('train/img_128/%d.jpg' %i, hr)
    cv2.imwrite('train/img_32/%d.jpg' %i, lr)
    
    np.save("train/bin_128/%d" %i, hr.transpose())
    np.save("train/bin_32/%d" %i, lr.transpose())


[img_save(i, path) for i, path in enumerate(paths)] 