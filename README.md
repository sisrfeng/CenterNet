https://blog.csdn.net/weixin_42634342/article/details/97756458
opt.py应该了opts.py

“由于图片路径问题，要在test函数里面修改一下数据集图片的绝对路径”,没找到相应代码。

不是修改，而是自己加一行dataset.img_dir='/d/COCO_my'

上面的博客不详细，参考这个
https://blog.csdn.net/weixin_41765699/article/details/100118353

super(AIC, self).__init__()
原来是COCO,改成AIC?    

根据这个转数据集 /src/tools/convert_kitti_to_coco.py，后面再转
