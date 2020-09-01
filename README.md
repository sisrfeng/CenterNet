https://blog.csdn.net/weixin_42634342/article/details/97756458
opt.py应该是opts.py

“由于图片路径问题，要在test函数里面修改一下数据集图片的绝对路径”,没找到相应代码。

不是修改，而是自己加一行dataset.img_dir='/d/COCO_my'

上面的博客不详细，参考这个
https://blog.csdn.net/weixin_41765699/article/details/100118353

super(AIC, self).__init__()
原来是COCO,改成AIC?   

一开始被
https://img-blog.csdnimg.cn/20190828210637735.png
误导了
其实，仿照coco.py自己建立的aic.py文件中相应部分应该是
valid_classids

`        self.class_name = [
            '__background__', 'car']
        self._valid_ids = [
            3]
`

coco中car对应类别3，aic中一致。如果把对应背景的0放进_valid_ids，训练时报错。


https://github.com/sisrfeng/CenterNet/blob/7a8be517d950001c6c2acbbac53c23e72b33094b/src/lib/opts.py#L338
对应原repo的

`
      'ctdet': {'default_resolution': [512, 512], 'num_classes': 80, 
                'mean': [0.408, 0.447, 0.470], 'std': [0.289, 0.274, 0.278],
                'dataset': 'coco'},
`

运行demo.py时要在opts.py中改回来，否则提示类别数目不对。

根据这个转数据集 /src/tools/convert_kitti_to_coco.py，后面再转


The learning rate 5e-4 is set for batchsize 128, you will need to linearly scale it to your batchsize (in your case, 5e-4 * 47 / 128).


https://blog.csdn.net/weixin_41765699/article/details/100118353中
指定
--master_batch 1 
加了这个，batch就不会平均分配到各个GPU。master GPU要存model的参数，平均分配batchsize不合理



https://github.com/xingyizhou/CenterNet/issues/660
We WILL predict peaks with very low confidence. This is not punished at all for the AP metric. However I do have tried to set a 0.01 threshold, and the results stayed the same for the specific model I tested.


如果采用了multi-scale测试，需要使用softnms作为后处理，需要额外编译   

https://blog.csdn.net/weixin_42634342/article/details/97756458   
说运行test.py时，不要加上 --keep_res, 但作者给的模型在指定--input_res 512和 --keep_res测试时，测出来的AP都是正常的。感觉这篇博客不太可靠。  



1.关于ctdet_coco_dla_1x.sh和ctdet_coco_dla_2x.sh中提到的训练设置：  
1x是训练了140个epoch，在90和120个epoch的时候学习率变为原来的十分之一。  
2x的训练，有两种：
方法一，是直接训练230个epoch，是在180和210个epoch的时候进行学习率衰减；
方法二，是在1x训练的基础上进行finetune，即继续原来的训练；

Hi Xingyi Zhou,

thank you for the implementation of the CenterNet algorithm. The idea behind it is amazing.
Can you please tell me if there is an easy way to use transfer learning from some already trained weights?
My dataset is very small (only 220 images) and I surely need transfer learning.
Tried using YOLO-tiny with Darknet and I just needed to extract the weights for the first 15 layers and I was ready to train. What is the equivalence of that in your implementation?  


I haven't tried freezing any layers. You can load the COCO pretrained model by --load_model ../models/ctdet_coco_2x.pth when finetuning on your own dataset.

