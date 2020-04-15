nohup: ignoring input
Using tensorboardX
Fix size testing.
training chunk_sizes: [1, 8, 8, 8, 7]
The output will be saved to  /root/c/src/lib/../../exp/ctdet/coco_dla
heads {'hm': 2, 'wh': 2, 'reg': 2}
Namespace(K=100, aggr_weight=0.0, agnostic_ex=False, arch='dla_34', aug_ddd=0.5, aug_rot=0, batch_size=32, cat_spec_wh=False, center_thresh=0.1, chunk_sizes=[1, 8, 8, 8, 7], data_dir='/root/c/src/lib/../../data', dataset='aic', debug=0, debug_dir='/root/c/src/lib/../../exp/ctdet/coco_dla/debug', debugger_theme='white', demo='', dense_hp=False, dense_wh=False, dep_weight=1, dim_weight=1, down_ratio=4, eval_oracle_dep=False, eval_oracle_hm=False, eval_oracle_hmhp=False, eval_oracle_hp_offset=False, eval_oracle_kps=False, eval_oracle_offset=False, eval_oracle_wh=False, exp_dir='/root/c/src/lib/../../exp/ctdet', exp_id='coco_dla', fix_res=True, flip=0.5, flip_test=False, gpus=[0, 1, 2, 3, 4], gpus_str='0,1,2,3,4', head_conv=256, heads={'hm': 2, 'wh': 2, 'reg': 2}, hide_data_time=False, hm_hp=True, hm_hp_weight=1, hm_weight=1, hp_weight=1, input_h=512, input_res=512, input_w=512, keep_res=False, kitti_split='3dop', load_model='', lr=0.000125, lr_step=[90, 120], master_batch_size=1, mean=array([[[0.5863884 , 0.59135514, 0.6016471 ]]], dtype=float32), metric='loss', mse_loss=False, nms=False, no_color_aug=False, norm_wh=False, not_cuda_benchmark=False, not_hm_hp=False, not_prefetch_test=False, not_rand_crop=False, not_reg_bbox=False, not_reg_hp_offset=False, not_reg_offset=False, num_classes=2, num_epochs=140, num_iters=-1, num_stacks=1, num_workers=0, off_weight=1, output_h=128, output_res=128, output_w=128, pad=31, peak_thresh=0.2, print_iter=1, rect_mask=False, reg_bbox=True, reg_hp_offset=True, reg_loss='l1', reg_offset=True, resume=False, root_dir='/root/c/src/lib/../..', rot_weight=1, rotate=0, save_all=False, save_dir='/root/c/src/lib/../../exp/ctdet/coco_dla', scale=0.4, scores_thresh=0.1, seed=317, shift=0.1, std=array([[[0.17724997, 0.1771044 , 0.17422022]]], dtype=float32), task='ctdet', test=False, test_scales=[1.0], trainval=False, val_intervals=5, vis_thresh=0.3, wh_weight=0.1)
Creating model...
Setting up data...
self.img_dir:  /root/c/src/lib/../../data/COCO_my/val2017
split:  val
/root/c/src/lib/../../data/COCO_my/annotations/instances_val2017.json
==> initializing coco 2017 val data.
loading annotations into memory...
Done (t=0.09s)
creating index...
index created!
Loaded val 2110 samples
self.img_dir:  /root/c/src/lib/../../data/COCO_my/train2017
split:  train
/root/c/src/lib/../../data/COCO_my/annotations/instances_train2017.json
==> initializing coco 2017 train data.
loading annotations into memory...
Done (t=0.02s)
creating index...
index created!
Loaded train 1955 samples
Starting training...
0
ctdet/coco_dla| train: [1][0/61]|Tot: 0:00:23 |ETA: 0:00:00 |loss 253.6622 |hm_loss 252.2377 |wh_loss 12.7560 |off_loss 0.1488 |Data 0.789s(0.789s) |Net 23.530s
0
1
1
1
0
0
0
ctdet/coco_dla| train: [1][1/61]|Tot: 0:00:25 |ETA: 0:00:00 |loss 201.6354 |hm_loss 199.4867 |wh_loss 19.4979 |off_loss 0.1990 |Data 0.718s(0.753s) |Net 12.795s
1
0
1
0
0
0
ctdet/coco_dla| train: [1][2/61]|Tot: 0:00:26 |ETA: 0:00:00 |loss 182.9316 |hm_loss 180.4127 |wh_loss 22.8153 |off_loss 0.2374 |Data 0.701s(0.736s) |Net 8.990s
1
1
1
0
2
ctdet/coco_dla| train: [1][3/61]|Tot: 0:00:28 |ETA: 0:00:00 |loss 168.5024 |hm_loss 166.0885 |wh_loss 21.9044 |off_loss 0.2235 |Data 0.656s(0.716s) |Net 7.072s
0
0
1
2
ctdet/coco_dla| train: [1][4/61]|Tot: 0:00:29 |ETA: 0:00:00 |loss 162.6771 |hm_loss 160.0450 |wh_loss 24.1291 |off_loss 0.2192 |Data 0.710s(0.715s) |Net 5.932s
2
0
1
0
1
1
1
0
ctdet/coco_dla| train: [1][5/61]|Tot: 0:00:31 |ETA: 0:00:00 |loss 154.7450 |hm_loss 151.9525 |wh_loss 25.7044 |off_loss 0.2221 |Data 0.663s(0.706s) |Net 5.172s
0
0
2
1
2
1
0
ctdet/coco_dla| train: [1][6/61]|Tot: 0:00:32 |ETA: 0:00:00 |loss 146.0022 |hm_loss 142.9267 |wh_loss 28.4865 |off_loss 0.2269 |Data 0.697s(0.705s) |Net 4.633s
0
0
1
2
1
ctdet/coco_dla| train: [1][7/61]|Tot: 0:00:33 |ETA: 0:00:00 |loss 139.8169 |hm_loss 136.7095 |wh_loss 28.7618 |off_loss 0.2312 |Data 0.702s(0.704s) |Net 4.226s
2
1
0
2
0
2
0
0
ctdet/coco_dla| train: [1][8/61]|Tot: 0:00:35 |ETA: 0:00:00 |loss 131.6073 |hm_loss 128.3861 |wh_loss 29.9020 |off_loss 0.2310 |Data 0.667s(0.700s) |Net 3.904s
0
0
1
0
1
0
ctdet/coco_dla| train: [1][9/61]|Tot: 0:00:36 |ETA: 0:00:00 |loss 126.3906 |hm_loss 123.1763 |wh_loss 29.7408 |off_loss 0.2402 |Data 0.653s(0.695s) |Net 3.646s
0
0
1
0
0
ctdet/coco_dla| train: [1][10/61]|Tot: 0:00:37 |ETA: 0:00:00 |loss 121.4728 |hm_loss 118.1913 |wh_loss 30.4300 |off_loss 0.2385 |Data 0.646s(0.691s) |Net 3.433s
1
0
3
1
0
ctdet/coco_dla| train: [1][11/61]|Tot: 0:00:39 |ETA: 0:00:00 |loss 117.1920 |hm_loss 113.8334 |wh_loss 31.2389 |off_loss 0.2347 |Data 0.650s(0.688s) |Net 3.257s
2
0
0
ctdet/coco_dla| train: [1][12/61]|Tot: 0:00:40 |ETA: 0:00:00 |loss 113.5846 |hm_loss 110.2527 |wh_loss 30.9449 |off_loss 0.2374 |Data 0.680s(0.687s) |Net 3.110s
1
ctdet/coco_dla| train: [1][13/61]|Tot: 0:00:41 |ETA: 0:00:00 |loss 109.8465 |hm_loss 106.6703 |wh_loss 29.5293 |off_loss 0.2232 |Data 0.689s(0.687s) |Net 2.984s
0
2
2
0
0
0
ctdet/coco_dla| train: [1][14/61]|Tot: 0:00:43 |ETA: 0:00:00 |loss 105.3685 |hm_loss 102.1943 |wh_loss 29.5737 |off_loss 0.2168 |Data 0.676s(0.686s) |Net 2.880s
0
0
0
0
0
ctdet/coco_dla| train: [1][15/61]|Tot: 0:00:44 |ETA: 0:00:00 |loss 101.4148 |hm_loss 98.2536 |wh_loss 29.4726 |off_loss 0.2139 |Data 0.665s(0.685s) |Net 2.783s
1
0
2
1
ctdet/coco_dla| train: [1][16/61]|Tot: 0:00:45 |ETA: 0:00:00 |loss 97.7998 |hm_loss 94.7034 |wh_loss 28.9164 |off_loss 0.2048 |Data 0.681s(0.685s) |Net 2.699s
2
0
0
0
1
ctdet/coco_dla| train: [1][17/61]|Tot: 0:00:47 |ETA: 0:00:00 |loss 94.6994 |hm_loss 91.5217 |wh_loss 29.7714 |off_loss 0.2006 |Data 0.627s(0.682s) |Net 2.621s
0
0
0
1
ctdet/coco_dla| train: [1][18/61]|Tot: 0:00:48 |ETA: 0:00:00 |loss 91.6165 |hm_loss 88.4839 |wh_loss 29.3155 |off_loss 0.2011 |Data 0.682s(0.682s) |Net 2.554s
0
ctdet/coco_dla| train: [1][19/61]|Tot: 0:00:49 |ETA: 0:00:00 |loss 88.7937 |hm_loss 85.7672 |wh_loss 28.3227 |off_loss 0.1942 |Data 0.659s(0.680s) |Net 2.493s
0
1
0
0
0
0
1
0
2
ctdet/coco_dla| train: [1][20/61]|Tot: 0:00:51 |ETA: 0:00:00 |loss 85.5606 |hm_loss 82.4881 |wh_loss 28.7730 |off_loss 0.1952 |Data 0.683s(0.681s) |Net 2.438s
3
2
1
ctdet/coco_dla| train: [1][21/61]|Tot: 0:00:52 |ETA: 0:00:00 |loss 83.1104 |hm_loss 80.0894 |wh_loss 28.2698 |off_loss 0.1940 |Data 0.679s(0.681s) |Net 2.389s
2
1
2
0
3
2
1
0
ctdet/coco_dla| train: [1][22/61]|Tot: 0:00:53 |ETA: 0:00:00 |loss 80.4776 |hm_loss 77.3827 |wh_loss 29.0121 |off_loss 0.1937 |Data 0.649s(0.679s) |Net 2.342s
1
ctdet/coco_dla| train: [1][23/61]|Tot: 0:00:55 |ETA: 0:00:00 |loss 78.1676 |hm_loss 75.1724 |wh_loss 28.0804 |off_loss 0.1872 |Data 0.652s(0.678s) |Net 2.301s
0
0
0
2
3
2
0
2
ctdet/coco_dla| train: [1][24/61]|Tot: 0:00:56 |ETA: 0:00:00 |loss 75.9059 |hm_loss 72.8503 |wh_loss 28.6713 |off_loss 0.1884 |Data 0.693s(0.679s) |Net 2.264s
0
2
0
0
1
0
0
1
ctdet/coco_dla| train: [1][25/61]|Tot: 0:00:57 |ETA: 0:00:00 |loss 73.5901 |hm_loss 70.5463 |wh_loss 28.5693 |off_loss 0.1869 |Data 0.692s(0.679s) |Net 2.229s
1
1
0
ctdet/coco_dla| train: [1][26/61]|Tot: 0:00:59 |ETA: 0:00:00 |loss 71.6906 |hm_loss 68.6765 |wh_loss 28.2700 |off_loss 0.1871 |Data 0.635s(0.678s) |Net 2.195s
0
0
1
ctdet/coco_dla| train: [1][27/61]|Tot: 0:01:00 |ETA: 0:00:00 |loss 69.7846 |hm_loss 66.7969 |wh_loss 28.0269 |off_loss 0.1850 |Data 0.681s(0.678s) |Net 2.165s
0
ctdet/coco_dla| train: [1][28/61]|Tot: 0:01:01 |ETA: 0:00:00 |loss 67.9671 |hm_loss 65.0575 |wh_loss 27.2984 |off_loss 0.1797 |Data 0.633s(0.676s) |Net 2.135s
0
1
0
ctdet/coco_dla| train: [1][29/61]|Tot: 0:01:03 |ETA: 0:00:00 |loss 66.2175 |hm_loss 63.3494 |wh_loss 26.9144 |off_loss 0.1766 |Data 0.682s(0.676s) |Net 2.109s
0
0
2
0
2
ctdet/coco_dla| train: [1][30/61]|Tot: 0:01:04 |ETA: 0:00:00 |loss 64.5616 |hm_loss 61.6893 |wh_loss 26.9603 |off_loss 0.1762 |Data 0.663s(0.676s) |Net 2.084s
1
1
0
ctdet/coco_dla| train: [1][31/61]|Tot: 0:01:05 |ETA: 0:00:00 |loss 62.9090 |hm_loss 60.1039 |wh_loss 26.3279 |off_loss 0.1722 |Data 0.662s(0.675s) |Net 2.061s
0
0
0
1
0
1
0
1
0
ctdet/coco_dla| train: [1][32/61]|Tot: 0:01:07 |ETA: 0:00:00 |loss 61.3408 |hm_loss 58.5236 |wh_loss 26.4486 |off_loss 0.1723 |Data 0.666s(0.675s) |Net 2.040s
0
2
0
ctdet/coco_dla| train: [1][33/61]|Tot: 0:01:08 |ETA: 0:00:00 |loss 59.9857 |hm_loss 57.1720 |wh_loss 26.3934 |off_loss 0.1743 |Data 0.691s(0.676s) |Net 2.020s
0
1
1
ctdet/coco_dla| train: [1][34/61]|Tot: 0:01:10 |ETA: 0:00:00 |loss 58.6062 |hm_loss 55.8234 |wh_loss 26.1067 |off_loss 0.1721 |Data 0.671s(0.676s) |Net 2.000s
0
0
1
1
1
1
ctdet/coco_dla| train: [1][35/61]|Tot: 0:01:11 |ETA: 0:00:00 |loss 57.2898 |hm_loss 54.5142 |wh_loss 26.0219 |off_loss 0.1734 |Data 0.672s(0.675s) |Net 1.982s
0
0
0
1
1
ctdet/coco_dla| train: [1][36/61]|Tot: 0:01:12 |ETA: 0:00:00 |loss 56.0352 |hm_loss 53.2673 |wh_loss 25.9519 |off_loss 0.1728 |Data 0.672s(0.675s) |Net 1.965s
2
1
ctdet/coco_dla| train: [1][37/61]|Tot: 0:01:14 |ETA: 0:00:00 |loss 54.8880 |hm_loss 52.1129 |wh_loss 26.0436 |off_loss 0.1707 |Data 0.672s(0.675s) |Net 1.948s
0
0
3
1
ctdet/coco_dla| train: [1][38/61]|Tot: 0:01:15 |ETA: 0:00:00 |loss 53.7690 |hm_loss 51.0020 |wh_loss 25.9577 |off_loss 0.1712 |Data 0.686s(0.675s) |Net 1.933s
0
2
ctdet/coco_dla| train: [1][39/61]|Tot: 0:01:16 |ETA: 0:00:00 |loss 52.6289 |hm_loss 49.9002 |wh_loss 25.5999 |off_loss 0.1687 |Data 0.665s(0.675s) |Net 1.918s
0
1
0
1
0
0
ctdet/coco_dla| train: [1][40/61]|Tot: 0:01:18 |ETA: 0:00:00 |loss 51.6431 |hm_loss 48.8842 |wh_loss 25.9000 |off_loss 0.1688 |Data 0.671s(0.675s) |Net 1.904s
2
0
0
1
ctdet/coco_dla| train: [1][41/61]|Tot: 0:01:19 |ETA: 0:00:00 |loss 50.6581 |hm_loss 47.8996 |wh_loss 25.9057 |off_loss 0.1679 |Data 0.680s(0.675s) |Net 1.891s
0
0
1
1
2
0
0
ctdet/coco_dla| train: [1][42/61]|Tot: 0:01:20 |ETA: 0:00:00 |loss 49.7349 |hm_loss 46.9476 |wh_loss 26.1682 |off_loss 0.1705 |Data 0.663s(0.675s) |Net 1.878s
0
0
2
ctdet/coco_dla| train: [1][43/61]|Tot: 0:01:22 |ETA: 0:00:00 |loss 48.7944 |hm_loss 46.0243 |wh_loss 26.0068 |off_loss 0.1694 |Data 0.673s(0.675s) |Net 1.865s
1
0
1
ctdet/coco_dla| train: [1][44/61]|Tot: 0:01:23 |ETA: 0:00:00 |loss 47.9005 |hm_loss 45.1353 |wh_loss 25.9849 |off_loss 0.1668 |Data 0.668s(0.675s) |Net 1.854s
2
0
1
ctdet/coco_dla| train: [1][45/61]|Tot: 0:01:24 |ETA: 0:00:00 |loss 47.0162 |hm_loss 44.2827 |wh_loss 25.6746 |off_loss 0.1660 |Data 0.662s(0.674s) |Net 1.842s
0
0
1
0
1
0
1
2
ctdet/coco_dla| train: [1][46/61]|Tot: 0:01:26 |ETA: 0:00:00 |loss 46.2037 |hm_loss 43.4588 |wh_loss 25.7745 |off_loss 0.1675 |Data 0.682s(0.675s) |Net 1.832s
1
0
2
0
3
ctdet/coco_dla| train: [1][47/61]|Tot: 0:01:27 |ETA: 0:00:00 |loss 45.4759 |hm_loss 42.6934 |wh_loss 26.1373 |off_loss 0.1688 |Data 0.681s(0.675s) |Net 1.822s
1
0
0
3
2
0
ctdet/coco_dla| train: [1][48/61]|Tot: 0:01:28 |ETA: 0:00:00 |loss 44.7290 |hm_loss 41.9472 |wh_loss 26.1261 |off_loss 0.1692 |Data 0.670s(0.675s) |Net 1.812s
0
1
1
0
0
2
0
ctdet/coco_dla| train: [1][49/61]|Tot: 0:01:30 |ETA: 0:00:00 |loss 44.0239 |hm_loss 41.2233 |wh_loss 26.3126 |off_loss 0.1694 |Data 0.665s(0.674s) |Net 1.804s
1
2
1
1
3
3
0
ctdet/coco_dla| train: [1][50/61]|Tot: 0:01:31 |ETA: 0:00:00 |loss 43.3706 |hm_loss 40.5408 |wh_loss 26.5993 |off_loss 0.1699 |Data 0.669s(0.674s) |Net 1.795s
0
1
1
1
0
0
0
2
0
ctdet/coco_dla| train: [1][51/61]|Tot: 0:01:32 |ETA: 0:00:00 |loss 42.6866 |hm_loss 39.8487 |wh_loss 26.6790 |off_loss 0.1700 |Data 0.668s(0.674s) |Net 1.786s
1
0
0
0
2
ctdet/coco_dla| train: [1][52/61]|Tot: 0:01:34 |ETA: 0:00:00 |loss 42.0084 |hm_loss 39.1892 |wh_loss 26.4918 |off_loss 0.1700 |Data 0.683s(0.674s) |Net 1.778s
0
0
0
0
1
1
0
ctdet/coco_dla| train: [1][53/61]|Tot: 0:01:35 |ETA: 0:00:00 |loss 41.3573 |hm_loss 38.5415 |wh_loss 26.4671 |off_loss 0.1691 |Data 0.711s(0.675s) |Net 1.771s
0
2
0
1
1
ctdet/coco_dla| train: [1][54/61]|Tot: 0:01:36 |ETA: 0:00:00 |loss 40.7335 |hm_loss 37.9305 |wh_loss 26.3412 |off_loss 0.1689 |Data 0.674s(0.675s) |Net 1.763s
0
1
3
1
0
0
0
1
ctdet/coco_dla| train: [1][55/61]|Tot: 0:01:38 |ETA: 0:00:00 |loss 40.1276 |hm_loss 37.3235 |wh_loss 26.3548 |off_loss 0.1686 |Data 0.661s(0.675s) |Net 1.755s
0
0
1
2
0
1
0
ctdet/coco_dla| train: [1][56/61]|Tot: 0:01:39 |ETA: 0:00:00 |loss 39.5727 |hm_loss 36.7579 |wh_loss 26.4400 |off_loss 0.1708 |Data 0.665s(0.675s) |Net 1.748s
0
2
0
0
0
2
ctdet/coco_dla| train: [1][57/61]|Tot: 0:01:40 |ETA: 0:00:00 |loss 39.0103 |hm_loss 36.1951 |wh_loss 26.4517 |off_loss 0.1701 |Data 0.664s(0.674s) |Net 1.741s
2
0
0
1
ctdet/coco_dla| train: [1][58/61]|Tot: 0:01:42 |ETA: 0:00:00 |loss 38.4508 |hm_loss 35.6445 |wh_loss 26.3678 |off_loss 0.1695 |Data 0.663s(0.674s) |Net 1.735s
1
0
0
1
2
0
ctdet/coco_dla| train: [1][59/61]|Tot: 0:01:43 |ETA: 0:00:00 |loss 37.9388 |hm_loss 35.1197 |wh_loss 26.5061 |off_loss 0.1685 |Data 0.661s(0.674s) |Net 1.728s
1
0
ctdet/coco_dla| train: [1][60/61]|Tot: 0:01:45 |ETA: 0:00:00 |loss 37.4364 |hm_loss 34.6133 |wh_loss 26.5614 |off_loss 0.1670 |Data 0.667s(0.674s) |Net 1.722s
0
0
0
0
0
2
1
ctdet/coco_dla| train: [2][0/61]|Tot: 0:00:01 |ETA: 0:00:00 |loss 7.8970 |hm_loss 4.5787 |wh_loss 30.5631 |off_loss 0.2620 |Data 0.677s(0.677s) |Net 1.346s
1
1
0
0
ctdet/coco_dla| train: [2][1/61]|Tot: 0:00:02 |ETA: 0:00:00 |loss 7.3373 |hm_loss 4.5426 |wh_loss 25.7585 |off_loss 0.2189 |Data 0.672s(0.674s) |Net 1.344s
1
0
ctdet/coco_dla| train: [2][2/61]|Tot: 0:00:04 |ETA: 0:00:00 |loss 6.9271 |hm_loss 4.3735 |wh_loss 23.8088 |off_loss 0.1728 |Data 0.677s(0.675s) |Net 1.345s
0
0
0
1
0
ctdet/coco_dla| train: [2][3/61]|Tot: 0:00:05 |ETA: 0:00:00 |loss 7.4677 |hm_loss 4.5340 |wh_loss 27.6050 |off_loss 0.1732 |Data 0.687s(0.678s) |Net 1.348s
0
1
0
1
ctdet/coco_dla| train: [2][4/61]|Tot: 0:00:06 |ETA: 0:00:00 |loss 7.4141 |hm_loss 4.4826 |wh_loss 27.5736 |off_loss 0.1741 |Data 0.688s(0.680s) |Net 1.350s
2
0
0
3
2
0
1
0
0
1
ctdet/coco_dla| train: [2][5/61]|Tot: 0:00:08 |ETA: 0:00:00 |loss 7.5363 |hm_loss 4.4313 |wh_loss 29.2864 |off_loss 0.1764 |Data 0.677s(0.679s) |Net 1.349s
2
1
0
0
0
ctdet/coco_dla| train: [2][6/61]|Tot: 0:00:09 |ETA: 0:00:00 |loss 7.4953 |hm_loss 4.3576 |wh_loss 29.6286 |off_loss 0.1748 |Data 0.661s(0.677s) |Net 1.352s
0
2
1
ctdet/coco_dla| train: [2][7/61]|Tot: 0:00:10 |ETA: 0:00:00 |loss 7.2653 |hm_loss 4.2402 |wh_loss 28.6336 |off_loss 0.1618 |Data 0.659s(0.675s) |Net 1.351s
1
2
0
0
0
2
0
ctdet/coco_dla| train: [2][8/61]|Tot: 0:00:12 |ETA: 0:00:00 |loss 7.4156 |hm_loss 4.2402 |wh_loss 30.1574 |off_loss 0.1597 |Data 0.695s(0.677s) |Net 1.352s
2
0
0
0
0
2
1
ctdet/coco_dla| train: [2][9/61]|Tot: 0:00:13 |ETA: 0:00:00 |loss 7.4002 |hm_loss 4.2349 |wh_loss 30.0728 |off_loss 0.1581 |Data 0.662s(0.675s) |Net 1.350s
0
1
1
1
0
1
0
ctdet/coco_dla| train: [2][10/61]|Tot: 0:00:14 |ETA: 0:00:00 |loss 7.3870 |hm_loss 4.2506 |wh_loss 29.7447 |off_loss 0.1620 |Data 0.728s(0.680s) |Net 1.356s
1
3
1
0
0
0
3
ctdet/coco_dla| train: [2][11/61]|Tot: 0:00:16 |ETA: 0:00:00 |loss 7.4330 |hm_loss 4.3412 |wh_loss 29.1875 |off_loss 0.1730 |Data 0.659s(0.678s) |Net 1.354s
1
1
2
0
1
2
ctdet/coco_dla| train: [2][12/61]|Tot: 0:00:17 |ETA: 0:00:00 |loss 7.4447 |hm_loss 4.3456 |wh_loss 29.2882 |off_loss 0.1703 |Data 0.663s(0.677s) |Net 1.352s
0
0
1
0
3
ctdet/coco_dla| train: [2][13/61]|Tot: 0:00:18 |ETA: 0:00:00 |loss 7.3565 |hm_loss 4.2932 |wh_loss 28.9260 |off_loss 0.1707 |Data 0.669s(0.677s) |Net 1.352s
2
1
1
ctdet/coco_dla| train: [2][14/61]|Tot: 0:00:20 |ETA: 0:00:00 |loss 7.2000 |hm_loss 4.2185 |wh_loss 28.1382 |off_loss 0.1678 |Data 0.662s(0.676s) |Net 1.350s
0
1
0
0
1
2
ctdet/coco_dla| train: [2][15/61]|Tot: 0:00:21 |ETA: 0:00:00 |loss 7.0954 |hm_loss 4.1796 |wh_loss 27.4673 |off_loss 0.1691 |Data 0.676s(0.676s) |Net 1.353s
2
0
2
0
0
ctdet/coco_dla| train: [2][16/61]|Tot: 0:00:22 |ETA: 0:00:00 |loss 7.1807 |hm_loss 4.1971 |wh_loss 28.1011 |off_loss 0.1735 |Data 0.667s(0.675s) |Net 1.352s
0
1
3
1
2
1
0
0
ctdet/coco_dla| train: [2][17/61]|Tot: 0:00:24 |ETA: 0:00:00 |loss 7.2248 |hm_loss 4.1928 |wh_loss 28.5706 |off_loss 0.1750 |Data 0.677s(0.675s) |Net 1.352s
0
0
1
0
1
ctdet/coco_dla| train: [2][18/61]|Tot: 0:00:25 |ETA: 0:00:00 |loss 7.2140 |hm_loss 4.1558 |wh_loss 28.8669 |off_loss 0.1715 |Data 0.646s(0.674s) |Net 1.350s
1
2
0
1
3
ctdet/coco_dla| train: [2][19/61]|Tot: 0:00:27 |ETA: 0:00:00 |loss 7.1497 |hm_loss 4.1323 |wh_loss 28.4795 |off_loss 0.1695 |Data 0.683s(0.674s) |Net 1.351s
0
0
0
1
0
2
0
1
ctdet/coco_dla| train: [2][20/61]|Tot: 0:00:28 |ETA: 0:00:00 |loss 7.1876 |hm_loss 4.1240 |wh_loss 28.9457 |off_loss 0.1690 |Data 0.677s(0.674s) |Net 1.351s
1
0
1
0
ctdet/coco_dla| train: [2][21/61]|Tot: 0:00:29 |ETA: 0:00:00 |loss 7.1237 |hm_loss 4.1062 |wh_loss 28.5171 |off_loss 0.1658 |Data 0.682s(0.675s) |Net 1.351s
2
0
0
1
2
1
ctdet/coco_dla| train: [2][22/61]|Tot: 0:00:31 |ETA: 0:00:00 |loss 7.1436 |hm_loss 4.1077 |wh_loss 28.6797 |off_loss 0.1679 |Data 0.643s(0.673s) |Net 1.349s
1
0
1
1
1
1
ctdet/coco_dla| train: [2][23/61]|Tot: 0:00:32 |ETA: 0:00:00 |loss 7.0810 |hm_loss 4.0709 |wh_loss 28.4441 |off_loss 0.1657 |Data 0.644s(0.672s) |Net 1.348s
0
0
1
1
2
0
ctdet/coco_dla| train: [2][24/61]|Tot: 0:00:33 |ETA: 0:00:00 |loss 7.0504 |hm_loss 4.0397 |wh_loss 28.4566 |off_loss 0.1651 |Data 0.737s(0.675s) |Net 1.351s
3
0
0
0
ctdet/coco_dla| train: [2][25/61]|Tot: 0:00:35 |ETA: 0:00:00 |loss 7.0336 |hm_loss 4.0203 |wh_loss 28.4910 |off_loss 0.1642 |Data 0.685s(0.675s) |Net 1.351s
0
0
0
0
ctdet/coco_dla| train: [2][26/61]|Tot: 0:00:36 |ETA: 0:00:00 |loss 7.0665 |hm_loss 4.0360 |wh_loss 28.6671 |off_loss 0.1638 |Data 0.685s(0.675s) |Net 1.351s
1
2
0
ctdet/coco_dla| train: [2][27/61]|Tot: 0:00:37 |ETA: 0:00:00 |loss 7.0370 |hm_loss 4.0251 |wh_loss 28.4990 |off_loss 0.1620 |Data 0.680s(0.676s) |Net 1.351s
1
0
1
0
0
ctdet/coco_dla| train: [2][28/61]|Tot: 0:00:39 |ETA: 0:00:00 |loss 6.9997 |hm_loss 4.0014 |wh_loss 28.3571 |off_loss 0.1626 |Data 0.687s(0.676s) |Net 1.351s
0
1
1
1
ctdet/coco_dla| train: [2][29/61]|Tot: 0:00:40 |ETA: 0:00:00 |loss 6.9797 |hm_loss 3.9841 |wh_loss 28.3374 |off_loss 0.1619 |Data 0.679s(0.676s) |Net 1.351s
2
1
ctdet/coco_dla| train: [2][30/61]|Tot: 0:00:41 |ETA: 0:00:00 |loss 6.8924 |hm_loss 3.9494 |wh_loss 27.8399 |off_loss 0.1591 |Data 0.667s(0.676s) |Net 1.351s
0
2
0
0
0
1
1
0
ctdet/coco_dla| train: [2][31/61]|Tot: 0:00:43 |ETA: 0:00:00 |loss 6.9194 |hm_loss 3.9519 |wh_loss 28.0806 |off_loss 0.1594 |Data 0.661s(0.675s) |Net 1.351s
0
0
1
1
ctdet/coco_dla| train: [2][32/61]|Tot: 0:00:44 |ETA: 0:00:00 |loss 6.8808 |hm_loss 3.9355 |wh_loss 27.8511 |off_loss 0.1601 |Data 0.664s(0.675s) |Net 1.351s
0
0
2
0
1
ctdet/coco_dla| train: [2][33/61]|Tot: 0:00:45 |ETA: 0:00:00 |loss 6.8366 |hm_loss 3.9148 |wh_loss 27.6415 |off_loss 0.1576 |Data 0.694s(0.675s) |Net 1.352s
1
0
ctdet/coco_dla| train: [2][34/61]|Tot: 0:00:47 |ETA: 0:00:00 |loss 6.7361 |hm_loss 3.8842 |wh_loss 26.9678 |off_loss 0.1551 |Data 0.671s(0.675s) |Net 1.352s
0
1
2
0
3
ctdet/coco_dla| train: [2][35/61]|Tot: 0:00:48 |ETA: 0:00:00 |loss 6.6757 |hm_loss 3.8663 |wh_loss 26.5501 |off_loss 0.1544 |Data 0.679s(0.675s) |Net 1.352s
1
0
1
1
1
0
0
0
ctdet/coco_dla| train: [2][36/61]|Tot: 0:00:50 |ETA: 0:00:00 |loss 6.6996 |hm_loss 3.8662 |wh_loss 26.7777 |off_loss 0.1556 |Data 0.679s(0.676s) |Net 1.351s
2
0
0
1
0
0
1
ctdet/coco_dla| train: [2][37/61]|Tot: 0:00:51 |ETA: 0:00:00 |loss 6.7883 |hm_loss 3.8862 |wh_loss 27.4395 |off_loss 0.1581 |Data 0.677s(0.676s) |Net 1.351s
1
0
1
1
1
ctdet/coco_dla| train: [2][38/61]|Tot: 0:00:52 |ETA: 0:00:00 |loss 6.8174 |hm_loss 3.8909 |wh_loss 27.6862 |off_loss 0.1579 |Data 0.663s(0.675s) |Net 1.351s
0
1
ctdet/coco_dla| train: [2][39/61]|Tot: 0:00:54 |ETA: 0:00:00 |loss 6.7826 |hm_loss 3.8617 |wh_loss 27.6505 |off_loss 0.1558 |Data 0.682s(0.675s) |Net 1.351s
2
0
1
2
0
2
0
1
ctdet/coco_dla| train: [2][40/61]|Tot: 0:00:55 |ETA: 0:00:00 |loss 6.7404 |hm_loss 3.8392 |wh_loss 27.4542 |off_loss 0.1558 |Data 0.674s(0.675s) |Net 1.351s
0
ctdet/coco_dla| train: [2][41/61]|Tot: 0:00:56 |ETA: 0:00:00 |loss 6.6556 |hm_loss 3.7943 |wh_loss 27.0880 |off_loss 0.1525 |Data 0.661s(0.675s) |Net 1.352s
0
2
0
2
0
1
1
ctdet/coco_dla| train: [2][42/61]|Tot: 0:00:58 |ETA: 0:00:00 |loss 6.6285 |hm_loss 3.7758 |wh_loss 27.0087 |off_loss 0.1518 |Data 0.676s(0.675s) |Net 1.352s
2
0
1
ctdet/coco_dla| train: [2][43/61]|Tot: 0:00:59 |ETA: 0:00:00 |loss 6.6129 |hm_loss 3.7673 |wh_loss 26.9357 |off_loss 0.1521 |Data 0.662s(0.675s) |Net 1.351s
1
0
1
ctdet/coco_dla| train: [2][44/61]|Tot: 0:01:00 |ETA: 0:00:00 |loss 6.6078 |hm_loss 3.7582 |wh_loss 26.9716 |off_loss 0.1524 |Data 0.664s(0.675s) |Net 1.351s
1
1
1
ctdet/coco_dla| train: [2][45/61]|Tot: 0:01:02 |ETA: 0:00:00 |loss 6.5604 |hm_loss 3.7309 |wh_loss 26.7693 |off_loss 0.1526 |Data 0.676s(0.675s) |Net 1.351s
0
0
0
0
0
ctdet/coco_dla| train: [2][46/61]|Tot: 0:01:03 |ETA: 0:00:00 |loss 6.5308 |hm_loss 3.7154 |wh_loss 26.6291 |off_loss 0.1524 |Data 0.672s(0.675s) |Net 1.351s
0
2
0
1
0
ctdet/coco_dla| train: [2][47/61]|Tot: 0:01:04 |ETA: 0:00:00 |loss 6.4981 |hm_loss 3.7024 |wh_loss 26.4287 |off_loss 0.1529 |Data 0.672s(0.674s) |Net 1.351s
0
0
0
ctdet/coco_dla| train: [2][48/61]|Tot: 0:01:06 |ETA: 0:00:00 |loss 6.4744 |hm_loss 3.6945 |wh_loss 26.2845 |off_loss 0.1514 |Data 0.679s(0.675s) |Net 1.351s
2
3
0
0
1
0
ctdet/coco_dla| train: [2][49/61]|Tot: 0:01:07 |ETA: 0:00:00 |loss 6.4475 |hm_loss 3.6804 |wh_loss 26.1545 |off_loss 0.1516 |Data 0.695s(0.675s) |Net 1.351s
0
0
0
1
0
ctdet/coco_dla| train: [2][50/61]|Tot: 0:01:08 |ETA: 0:00:00 |loss 6.4450 |hm_loss 3.6691 |wh_loss 26.2356 |off_loss 0.1523 |Data 0.645s(0.674s) |Net 1.351s
0
3
1
0
0
0
ctdet/coco_dla| train: [2][51/61]|Tot: 0:01:10 |ETA: 0:00:00 |loss 6.4239 |hm_loss 3.6541 |wh_loss 26.1694 |off_loss 0.1528 |Data 0.668s(0.674s) |Net 1.351s
1
0
0
2
ctdet/coco_dla| train: [2][52/61]|Tot: 0:01:11 |ETA: 0:00:00 |loss 6.4254 |hm_loss 3.6442 |wh_loss 26.2894 |off_loss 0.1522 |Data 0.673s(0.674s) |Net 1.351s
3
0
0
0
0
2
ctdet/coco_dla| train: [2][53/61]|Tot: 0:01:12 |ETA: 0:00:00 |loss 6.4011 |hm_loss 3.6353 |wh_loss 26.1297 |off_loss 0.1528 |Data 0.701s(0.675s) |Net 1.351s
0
0
0
1
2
1
0
1
0
ctdet/coco_dla| train: [2][54/61]|Tot: 0:01:14 |ETA: 0:00:00 |loss 6.4069 |hm_loss 3.6331 |wh_loss 26.2000 |off_loss 0.1538 |Data 0.716s(0.675s) |Net 1.352s
0
0
1
0
ctdet/coco_dla| train: [2][55/61]|Tot: 0:01:15 |ETA: 0:00:00 |loss 6.4061 |hm_loss 3.6228 |wh_loss 26.2980 |off_loss 0.1535 |Data 0.665s(0.675s) |Net 1.352s
1
0
1
2
1
1
0
1
ctdet/coco_dla| train: [2][56/61]|Tot: 0:01:17 |ETA: 0:00:00 |loss 6.3966 |hm_loss 3.6235 |wh_loss 26.1796 |off_loss 0.1551 |Data 0.675s(0.675s) |Net 1.352s
0
0
1
0
2
0
ctdet/coco_dla| train: [2][57/61]|Tot: 0:01:18 |ETA: 0:00:00 |loss 6.4233 |hm_loss 3.6252 |wh_loss 26.4107 |off_loss 0.1570 |Data 0.672s(0.675s) |Net 1.352s
1
0
ctdet/coco_dla| train: [2][58/61]|Tot: 0:01:19 |ETA: 0:00:00 |loss 6.3680 |hm_loss 3.6049 |wh_loss 26.0756 |off_loss 0.1555 |Data 0.662s(0.675s) |Net 1.352s
1
0
1
0
1
ctdet/coco_dla| train: [2][59/61]|Tot: 0:01:21 |ETA: 0:00:00 |loss 6.3452 |hm_loss 3.5948 |wh_loss 25.9478 |off_loss 0.1556 |Data 0.665s(0.675s) |Net 1.352s
0
1
3
2
0
ctdet/coco_dla| train: [2][60/61]|Tot: 0:01:22 |ETA: 0:00:00 |loss 6.3282 |hm_loss 3.5839 |wh_loss 25.8901 |off_loss 0.1553 |Data 0.669s(0.675s) |Net 1.352s
0
2
1
1
2
ctdet/coco_dla| train: [3][0/61]|Tot: 0:00:01 |ETA: 0:00:00 |loss 6.0324 |hm_loss 3.7709 |wh_loss 20.6929 |off_loss 0.1922 |Data 0.684s(0.684s) |Net 1.359s
0
1
1
0
3
ctdet/coco_dla| train: [3][1/61]|Tot: 0:00:02 |ETA: 0:00:00 |loss 5.6076 |hm_loss 3.3727 |wh_loss 20.7310 |off_loss 0.1618 |Data 0.674s(0.679s) |Net 1.353s
1
0
1
1
2
0
ctdet/coco_dla| train: [3][2/61]|Tot: 0:00:04 |ETA: 0:00:00 |loss 5.9570 |hm_loss 3.4641 |wh_loss 23.0638 |off_loss 0.1865 |Data 0.680s(0.679s) |Net 1.355s
0
1
0
1
0
2
2
1
0
ctdet/coco_dla| train: [3][3/61]|Tot: 0:00:05 |ETA: 0:00:00 |loss 6.5862 |hm_loss 3.6837 |wh_loss 27.0346 |off_loss 0.1991 |Data 0.677s(0.679s) |Net 1.354s
2
0
0
0
0
2
2
0
ctdet/coco_dla| train: [3][4/61]|Tot: 0:00:06 |ETA: 0:00:00 |loss 6.5455 |hm_loss 3.6656 |wh_loss 26.7175 |off_loss 0.2081 |Data 0.662s(0.675s) |Net 1.350s
0
3
1
2
0
1
2
ctdet/coco_dla| train: [3][5/61]|Tot: 0:00:08 |ETA: 0:00:00 |loss 6.4757 |hm_loss 3.6756 |wh_loss 25.9339 |off_loss 0.2067 |Data 0.669s(0.674s) |Net 1.348s
0
1
0
0
0
1
0
ctdet/coco_dla| train: [3][6/61]|Tot: 0:00:09 |ETA: 0:00:00 |loss 6.5751 |hm_loss 3.6717 |wh_loss 26.9995 |off_loss 0.2034 |Data 0.677s(0.675s) |Net 1.357s
0
1
1
1
2
ctdet/coco_dla| train: [3][7/61]|Tot: 0:00:10 |ETA: 0:00:00 |loss 6.4882 |hm_loss 3.5725 |wh_loss 27.2231 |off_loss 0.1934 |Data 0.677s(0.675s) |Net 1.356s
0
0
0
2
1
0
ctdet/coco_dla| train: [3][8/61]|Tot: 0:00:12 |ETA: 0:00:00 |loss 6.6504 |hm_loss 3.5862 |wh_loss 28.6044 |off_loss 0.2037 |Data 0.658s(0.673s) |Net 1.353s
1
2
3
0
1
1
1
ctdet/coco_dla| train: [3][9/61]|Tot: 0:00:13 |ETA: 0:00:00 |loss 6.6197 |hm_loss 3.5873 |wh_loss 28.3316 |off_loss 0.1993 |Data 0.643s(0.670s) |Net 1.350s
0
1
0
2
1
ctdet/coco_dla| train: [3][10/61]|Tot: 0:00:14 |ETA: 0:00:00 |loss 6.7300 |hm_loss 3.6024 |wh_loss 29.2875 |off_loss 0.1989 |Data 0.667s(0.670s) |Net 1.349s
0
0
0
1
0
2
1
1
1
ctdet/coco_dla| train: [3][11/61]|Tot: 0:00:16 |ETA: 0:00:00 |loss 6.6361 |hm_loss 3.5932 |wh_loss 28.4270 |off_loss 0.2002 |Data 0.652s(0.668s) |Net 1.347s
0
1
0
ctdet/coco_dla| train: [3][12/61]|Tot: 0:00:17 |ETA: 0:00:00 |loss 6.4216 |hm_loss 3.4858 |wh_loss 27.3952 |off_loss 0.1963 |Data 0.674s(0.669s) |Net 1.347s
0
0
0
0
1
0
ctdet/coco_dla| train: [3][13/61]|Tot: 0:00:18 |ETA: 0:00:00 |loss 6.2701 |hm_loss 3.4488 |wh_loss 26.2787 |off_loss 0.1934 |Data 0.664s(0.669s) |Net 1.346s
1
1
0
0
1
ctdet/coco_dla| train: [3][14/61]|Tot: 0:00:20 |ETA: 0:00:00 |loss 6.0733 |hm_loss 3.3534 |wh_loss 25.2980 |off_loss 0.1900 |Data 0.752s(0.674s) |Net 1.352s
0
0
0
0
0
ctdet/coco_dla| train: [3][15/61]|Tot: 0:00:21 |ETA: 0:00:00 |loss 6.0412 |hm_loss 3.3235 |wh_loss 25.3161 |off_loss 0.1860 |Data 0.663s(0.673s) |Net 1.353s
1
0
0
ctdet/coco_dla| train: [3][16/61]|Tot: 0:00:22 |ETA: 0:00:00 |loss 5.8801 |hm_loss 3.2567 |wh_loss 24.4195 |off_loss 0.1814 |Data 0.650s(0.672s) |Net 1.351s
1
1
1
ctdet/coco_dla| train: [3][17/61]|Tot: 0:00:24 |ETA: 0:00:00 |loss 5.7247 |hm_loss 3.1960 |wh_loss 23.5205 |off_loss 0.1767 |Data 0.676s(0.672s) |Net 1.351s
0
0
0
2
1
ctdet/coco_dla| train: [3][18/61]|Tot: 0:00:25 |ETA: 0:00:00 |loss 5.7960 |hm_loss 3.2218 |wh_loss 23.9667 |off_loss 0.1775 |Data 0.682s(0.673s) |Net 1.352s
1
2
1
1
0
ctdet/coco_dla| train: [3][19/61]|Tot: 0:00:27 |ETA: 0:00:00 |loss 5.8753 |hm_loss 3.2434 |wh_loss 24.5258 |off_loss 0.1793 |Data 0.673s(0.673s) |Net 1.352s
1
0
0
0
1
1
ctdet/coco_dla| train: [3][20/61]|Tot: 0:00:28 |ETA: 0:00:00 |loss 5.8035 |hm_loss 3.2246 |wh_loss 23.9906 |off_loss 0.1798 |Data 0.672s(0.673s) |Net 1.351s
0
1
0
2
1
ctdet/coco_dla| train: [3][21/61]|Tot: 0:00:29 |ETA: 0:00:00 |loss 5.7232 |hm_loss 3.1712 |wh_loss 23.7624 |off_loss 0.1758 |Data 0.674s(0.673s) |Net 1.351s
1
0
1
0
0
0
2
0
ctdet/coco_dla| train: [3][22/61]|Tot: 0:00:31 |ETA: 0:00:00 |loss 5.8565 |hm_loss 3.2224 |wh_loss 24.5494 |off_loss 0.1791 |Data 0.669s(0.673s) |Net 1.351s
0
1
0
1
0
0
ctdet/coco_dla| train: [3][23/61]|Tot: 0:00:32 |ETA: 0:00:00 |loss 5.7811 |hm_loss 3.1780 |wh_loss 24.2801 |off_loss 0.1752 |Data 0.724s(0.675s) |Net 1.353s
1
0
ctdet/coco_dla| train: [3][24/61]|Tot: 0:00:33 |ETA: 0:00:00 |loss 5.7177 |hm_loss 3.1393 |wh_loss 24.0611 |off_loss 0.1724 |Data 0.677s(0.675s) |Net 1.355s
0
ctdet/coco_dla| train: [3][25/61]|Tot: 0:00:35 |ETA: 0:00:00 |loss 5.5623 |hm_loss 3.0753 |wh_loss 23.2012 |off_loss 0.1669 |Data 0.658s(0.674s) |Net 1.354s
1
1
ctdet/coco_dla| train: [3][26/61]|Tot: 0:00:36 |ETA: 0:00:00 |loss 5.4950 |hm_loss 3.0426 |wh_loss 22.8811 |off_loss 0.1642 |Data 0.663s(0.674s) |Net 1.353s
1
0
0
0
1
ctdet/coco_dla| train: [3][27/61]|Tot: 0:00:37 |ETA: 0:00:00 |loss 5.5746 |hm_loss 3.0655 |wh_loss 23.4095 |off_loss 0.1681 |Data 0.663s(0.673s) |Net 1.353s
0
0
1
2
1
1
ctdet/coco_dla| train: [3][28/61]|Tot: 0:00:39 |ETA: 0:00:00 |loss 5.5657 |hm_loss 3.0843 |wh_loss 23.1250 |off_loss 0.1689 |Data 0.666s(0.673s) |Net 1.352s
0
ctdet/coco_dla| train: [3][29/61]|Tot: 0:00:40 |ETA: 0:00:00 |loss 5.4383 |hm_loss 3.0292 |wh_loss 22.4576 |off_loss 0.1633 |Data 0.658s(0.673s) |Net 1.351s
1
0
0
0
ctdet/coco_dla| train: [3][30/61]|Tot: 0:00:41 |ETA: 0:00:00 |loss 5.4429 |hm_loss 3.0261 |wh_loss 22.5363 |off_loss 0.1632 |Data 0.667s(0.672s) |Net 1.351s
2
0
3
0
0
0
ctdet/coco_dla| train: [3][31/61]|Tot: 0:00:43 |ETA: 0:00:00 |loss 5.3660 |hm_loss 2.9947 |wh_loss 22.0964 |off_loss 0.1616 |Data 0.687s(0.673s) |Net 1.351s
2
0
0
2
3
1
0
ctdet/coco_dla| train: [3][32/61]|Tot: 0:00:44 |ETA: 0:00:00 |loss 5.4626 |hm_loss 3.0349 |wh_loss 22.6076 |off_loss 0.1669 |Data 0.830s(0.678s) |Net 1.356s
0
1
1
1
2
0
0
2
0
ctdet/coco_dla| train: [3][33/61]|Tot: 0:00:46 |ETA: 0:00:00 |loss 5.4907 |hm_loss 3.0695 |wh_loss 22.5190 |off_loss 0.1693 |Data 0.659s(0.677s) |Net 1.357s
0
1
0
0
1
0
0
ctdet/coco_dla| train: [3][34/61]|Tot: 0:00:47 |ETA: 0:00:00 |loss 5.5028 |hm_loss 3.0811 |wh_loss 22.4891 |off_loss 0.1727 |Data 0.759s(0.680s) |Net 1.360s
0
1
3
0
1
ctdet/coco_dla| train: [3][35/61]|Tot: 0:00:48 |ETA: 0:00:00 |loss 5.4851 |hm_loss 3.0732 |wh_loss 22.3997 |off_loss 0.1720 |Data 0.669s(0.679s) |Net 1.359s
0
0
1
0
ctdet/coco_dla| train: [3][36/61]|Tot: 0:00:50 |ETA: 0:00:00 |loss 5.5324 |hm_loss 3.0882 |wh_loss 22.6602 |off_loss 0.1782 |Data 0.670s(0.679s) |Net 1.359s
1
0
0
0
1
ctdet/coco_dla| train: [3][37/61]|Tot: 0:00:51 |ETA: 0:00:00 |loss 5.5348 |hm_loss 3.1012 |wh_loss 22.5559 |off_loss 0.1780 |Data 0.691s(0.679s) |Net 1.359s
2
2
0
1
0
0
ctdet/coco_dla| train: [3][38/61]|Tot: 0:00:52 |ETA: 0:00:00 |loss 5.5180 |hm_loss 3.0950 |wh_loss 22.4418 |off_loss 0.1788 |Data 0.687s(0.680s) |Net 1.359s
1
0
1
0
0
0
ctdet/coco_dla| train: [3][39/61]|Tot: 0:00:54 |ETA: 0:00:00 |loss 5.5360 |hm_loss 3.1070 |wh_loss 22.4937 |off_loss 0.1796 |Data 0.659s(0.679s) |Net 1.358s
0
1
0
2
ctdet/coco_dla| train: [3][40/61]|Tot: 0:00:55 |ETA: 0:00:00 |loss 5.5017 |hm_loss 3.1000 |wh_loss 22.2214 |off_loss 0.1796 |Data 0.626s(0.678s) |Net 1.357s
1
1
ctdet/coco_dla| train: [3][41/61]|Tot: 0:00:56 |ETA: 0:00:00 |loss 5.4145 |hm_loss 3.0571 |wh_loss 21.8085 |off_loss 0.1765 |Data 0.635s(0.677s) |Net 1.356s
0
2
2
0
1
2
ctdet/coco_dla| train: [3][42/61]|Tot: 0:00:58 |ETA: 0:00:00 |loss 5.4215 |hm_loss 3.0675 |wh_loss 21.7706 |off_loss 0.1769 |Data 0.672s(0.677s) |Net 1.357s
0
3
0
0
ctdet/coco_dla| train: [3][43/61]|Tot: 0:00:59 |ETA: 0:00:00 |loss 5.4403 |hm_loss 3.0811 |wh_loss 21.8130 |off_loss 0.1779 |Data 0.645s(0.676s) |Net 1.356s
1
1
0
0
1
3
0
ctdet/coco_dla| train: [3][44/61]|Tot: 0:01:01 |ETA: 0:00:00 |loss 5.4327 |hm_loss 3.0714 |wh_loss 21.8404 |off_loss 0.1773 |Data 0.677s(0.676s) |Net 1.356s
0
1
0
2
ctdet/coco_dla| train: [3][45/61]|Tot: 0:01:02 |ETA: 0:00:00 |loss 5.3777 |hm_loss 3.0478 |wh_loss 21.5371 |off_loss 0.1761 |Data 0.658s(0.675s) |Net 1.355s
0
1
ctdet/coco_dla| train: [3][46/61]|Tot: 0:01:03 |ETA: 0:00:00 |loss 5.3031 |hm_loss 3.0101 |wh_loss 21.1932 |off_loss 0.1737 |Data 0.668s(0.675s) |Net 1.355s
0
0
1
1
0
ctdet/coco_dla| train: [3][47/61]|Tot: 0:01:05 |ETA: 0:00:00 |loss 5.3141 |hm_loss 3.0213 |wh_loss 21.1873 |off_loss 0.1741 |Data 0.657s(0.675s) |Net 1.354s
1
0
ctdet/coco_dla| train: [3][48/61]|Tot: 0:01:06 |ETA: 0:00:00 |loss 5.3002 |hm_loss 3.0029 |wh_loss 21.2473 |off_loss 0.1726 |Data 0.785s(0.677s) |Net 1.357s
0
0
0
1
0
0
ctdet/coco_dla| train: [3][49/61]|Tot: 0:01:07 |ETA: 0:00:00 |loss 5.3190 |hm_loss 3.0151 |wh_loss 21.2988 |off_loss 0.1741 |Data 0.671s(0.677s) |Net 1.357s
0
0
0
1
0
0
1
ctdet/coco_dla| train: [3][50/61]|Tot: 0:01:09 |ETA: 0:00:00 |loss 5.3472 |hm_loss 3.0257 |wh_loss 21.4699 |off_loss 0.1745 |Data 0.673s(0.677s) |Net 1.356s
0
1
1
1
1
0
ctdet/coco_dla| train: [3][51/61]|Tot: 0:01:10 |ETA: 0:00:00 |loss 5.3326 |hm_loss 3.0204 |wh_loss 21.3796 |off_loss 0.1742 |Data 0.666s(0.677s) |Net 1.357s
0
0
2
1
1
0
2
ctdet/coco_dla| train: [3][52/61]|Tot: 0:01:11 |ETA: 0:00:00 |loss 5.3411 |hm_loss 3.0298 |wh_loss 21.3630 |off_loss 0.1750 |Data 0.659s(0.676s) |Net 1.357s
0
1
1
0
1
ctdet/coco_dla| train: [3][53/61]|Tot: 0:01:13 |ETA: 0:00:00 |loss 5.3236 |hm_loss 3.0246 |wh_loss 21.2502 |off_loss 0.1740 |Data 0.660s(0.676s) |Net 1.356s
0
1
ctdet/coco_dla| train: [3][54/61]|Tot: 0:01:14 |ETA: 0:00:00 |loss 5.2786 |hm_loss 3.0075 |wh_loss 20.9885 |off_loss 0.1723 |Data 0.663s(0.676s) |Net 1.356s
2
1
2
0
1
0
3
ctdet/coco_dla| train: [3][55/61]|Tot: 0:01:15 |ETA: 0:00:00 |loss 5.2588 |hm_loss 3.0012 |wh_loss 20.8595 |off_loss 0.1717 |Data 0.676s(0.676s) |Net 1.356s
0
1
1
2
0
1
ctdet/coco_dla| train: [3][56/61]|Tot: 0:01:17 |ETA: 0:00:00 |loss 5.2544 |hm_loss 2.9971 |wh_loss 20.8538 |off_loss 0.1719 |Data 0.658s(0.676s) |Net 1.356s
2
0
2
0
ctdet/coco_dla| train: [3][57/61]|Tot: 0:01:18 |ETA: 0:00:00 |loss 5.1973 |hm_loss 2.9664 |wh_loss 20.6099 |off_loss 0.1699 |Data 0.674s(0.676s) |Net 1.356s
0
0
0
0
2
1
ctdet/coco_dla| train: [3][58/61]|Tot: 0:01:20 |ETA: 0:00:00 |loss 5.1977 |hm_loss 2.9629 |wh_loss 20.6504 |off_loss 0.1698 |Data 0.703s(0.676s) |Net 1.356s
0
0
2
0
2
ctdet/coco_dla| train: [3][59/61]|Tot: 0:01:21 |ETA: 0:00:00 |loss 5.2520 |hm_loss 2.9866 |wh_loss 20.9399 |off_loss 0.1714 |Data 0.669s(0.676s) |Net 1.356s
1
3
0
0
ctdet/coco_dla| train: [3][60/61]|Tot: 0:01:22 |ETA: 0:00:00 |loss 5.2448 |hm_loss 2.9847 |wh_loss 20.8921 |off_loss 0.1708 |Data 0.701s(0.676s) |Net 1.357s
0
0
0
0
2
ctdet/coco_dla| train: [4][0/61]|Tot: 0:00:01 |ETA: 0:00:00 |loss 6.8391 |hm_loss 3.5569 |wh_loss 30.5758 |off_loss 0.2246 |Data 0.654s(0.654s) |Net 1.328s
1
2
0
0
1
1
0
ctdet/coco_dla| train: [4][1/61]|Tot: 0:00:02 |ETA: 0:00:00 |loss 5.8781 |hm_loss 3.5141 |wh_loss 21.3636 |off_loss 0.2276 |Data 0.644s(0.649s) |Net 1.322s
0
1
ctdet/coco_dla| train: [4][2/61]|Tot: 0:00:04 |ETA: 0:00:00 |loss 5.0385 |hm_loss 3.0320 |wh_loss 18.1421 |off_loss 0.1923 |Data 0.685s(0.661s) |Net 1.335s
1
0
2
2
2
ctdet/coco_dla| train: [4][3/61]|Tot: 0:00:05 |ETA: 0:00:00 |loss 4.8915 |hm_loss 2.9558 |wh_loss 17.5188 |off_loss 0.1838 |Data 0.739s(0.681s) |Net 1.354s
1
0
0
1
ctdet/coco_dla| train: [4][4/61]|Tot: 0:00:06 |ETA: 0:00:00 |loss 4.5493 |hm_loss 2.7538 |wh_loss 16.2880 |off_loss 0.1667 |Data 0.717s(0.688s) |Net 1.362s
2
2
0
0
1
ctdet/coco_dla| train: [4][5/61]|Tot: 0:00:08 |ETA: 0:00:00 |loss 4.7698 |hm_loss 2.8832 |wh_loss 17.1313 |off_loss 0.1735 |Data 0.664s(0.684s) |Net 1.358s
0
0
3
0
0
ctdet/coco_dla| train: [4][6/61]|Tot: 0:00:09 |ETA: 0:00:00 |loss 4.7892 |hm_loss 2.8584 |wh_loss 17.5785 |off_loss 0.1730 |Data 0.633s(0.677s) |Net 1.351s
1
0
1
0
0
1
0
0
ctdet/coco_dla| train: [4][7/61]|Tot: 0:00:10 |ETA: 0:00:00 |loss 4.9306 |hm_loss 2.9295 |wh_loss 18.2066 |off_loss 0.1804 |Data 0.701s(0.680s) |Net 1.359s
1
2
0
0
ctdet/coco_dla| train: [4][8/61]|Tot: 0:00:12 |ETA: 0:00:00 |loss 4.9367 |hm_loss 2.9106 |wh_loss 18.4361 |off_loss 0.1825 |Data 0.678s(0.680s) |Net 1.359s
1
0
0
1
1
ctdet/coco_dla| train: [4][9/61]|Tot: 0:00:13 |ETA: 0:00:00 |loss 4.9380 |hm_loss 2.9775 |wh_loss 17.7603 |off_loss 0.1845 |Data 0.734s(0.685s) |Net 1.364s
1
1
1
ctdet/coco_dla| train: [4][10/61]|Tot: 0:00:15 |ETA: 0:00:00 |loss 4.8249 |hm_loss 2.8878 |wh_loss 17.5894 |off_loss 0.1781 |Data 0.686s(0.685s) |Net 1.364s
2
1
1
0
0
1
3
1
1
0
ctdet/coco_dla| train: [4][11/61]|Tot: 0:00:16 |ETA: 0:00:00 |loss 4.7881 |hm_loss 2.8589 |wh_loss 17.5415 |off_loss 0.1751 |Data 0.694s(0.686s) |Net 1.364s
0
0
ctdet/coco_dla| train: [4][12/61]|Tot: 0:00:17 |ETA: 0:00:00 |loss 4.7006 |hm_loss 2.8004 |wh_loss 17.3104 |off_loss 0.1691 |Data 0.698s(0.687s) |Net 1.365s
1
1
0
1
1
0
0
0
0
ctdet/coco_dla| train: [4][13/61]|Tot: 0:00:19 |ETA: 0:00:00 |loss 4.8060 |hm_loss 2.8431 |wh_loss 17.9371 |off_loss 0.1692 |Data 0.687s(0.687s) |Net 1.365s
1
ctdet/coco_dla| train: [4][14/61]|Tot: 0:00:20 |ETA: 0:00:00 |loss 4.5913 |hm_loss 2.7391 |wh_loss 16.9356 |off_loss 0.1586 |Data 0.694s(0.687s) |Net 1.365s
0
0
0
2
2
3
ctdet/coco_dla| train: [4][15/61]|Tot: 0:00:21 |ETA: 0:00:00 |loss 4.6717 |hm_loss 2.7872 |wh_loss 17.2070 |off_loss 0.1639 |Data 0.686s(0.687s) |Net 1.365s
0
0
1
0
1
1
ctdet/coco_dla| train: [4][16/61]|Tot: 0:00:23 |ETA: 0:00:00 |loss 4.7666 |hm_loss 2.8281 |wh_loss 17.7448 |off_loss 0.1640 |Data 0.694s(0.688s) |Net 1.368s
0
1
ctdet/coco_dla| train: [4][17/61]|Tot: 0:00:24 |ETA: 0:00:00 |loss 4.6937 |hm_loss 2.7840 |wh_loss 17.5051 |off_loss 0.1592 |Data 0.682s(0.687s) |Net 1.367s
1
0
2
3
0
0
ctdet/coco_dla| train: [4][18/61]|Tot: 0:00:25 |ETA: 0:00:00 |loss 4.6557 |hm_loss 2.7804 |wh_loss 17.1700 |off_loss 0.1583 |Data 0.686s(0.687s) |Net 1.367s
1
1
2
0
1
ctdet/coco_dla| train: [4][19/61]|Tot: 0:00:27 |ETA: 0:00:00 |loss 4.6864 |hm_loss 2.7766 |wh_loss 17.5303 |off_loss 0.1568 |Data 0.728s(0.689s) |Net 1.368s
0
1
2
ctdet/coco_dla| train: [4][20/61]|Tot: 0:00:28 |ETA: 0:00:00 |loss 4.6533 |hm_loss 2.7814 |wh_loss 17.1836 |off_loss 0.1536 |Data 0.689s(0.689s) |Net 1.368s
1
1
0
0
2
ctdet/coco_dla| train: [4][21/61]|Tot: 0:00:30 |ETA: 0:00:00 |loss 4.6199 |hm_loss 2.7762 |wh_loss 16.9230 |off_loss 0.1514 |Data 0.679s(0.689s) |Net 1.368s
0
1
1
0
2
ctdet/coco_dla| train: [4][22/61]|Tot: 0:00:31 |ETA: 0:00:00 |loss 4.5436 |hm_loss 2.7405 |wh_loss 16.5332 |off_loss 0.1498 |Data 0.699s(0.689s) |Net 1.368s
2
1
ctdet/coco_dla| train: [4][23/61]|Tot: 0:00:32 |ETA: 0:00:00 |loss 4.4846 |hm_loss 2.7148 |wh_loss 16.2267 |off_loss 0.1471 |Data 0.684s(0.689s) |Net 1.368s
0
1
1
0
2
1
1
0
ctdet/coco_dla| train: [4][24/61]|Tot: 0:00:34 |ETA: 0:00:00 |loss 4.5460 |hm_loss 2.7403 |wh_loss 16.5785 |off_loss 0.1478 |Data 0.697s(0.689s) |Net 1.368s
0
0
1
1
0
ctdet/coco_dla| train: [4][25/61]|Tot: 0:00:35 |ETA: 0:00:00 |loss 4.5998 |hm_loss 2.7695 |wh_loss 16.7973 |off_loss 0.1506 |Data 0.693s(0.689s) |Net 1.369s
0
1
ctdet/coco_dla| train: [4][26/61]|Tot: 0:00:36 |ETA: 0:00:00 |loss 4.5035 |hm_loss 2.7115 |wh_loss 16.4486 |off_loss 0.1472 |Data 0.684s(0.689s) |Net 1.369s
0
0
0
0
0
2
ctdet/coco_dla| train: [4][27/61]|Tot: 0:00:38 |ETA: 0:00:00 |loss 4.5594 |hm_loss 2.7367 |wh_loss 16.7351 |off_loss 0.1491 |Data 0.705s(0.690s) |Net 1.370s
0
1
0
1
2
1
0
0
1
ctdet/coco_dla| train: [4][28/61]|Tot: 0:00:39 |ETA: 0:00:00 |loss 4.6520 |hm_loss 2.7863 |wh_loss 17.1235 |off_loss 0.1533 |Data 0.699s(0.690s) |Net 1.370s
0
0
0
1
0
0
0
ctdet/coco_dla| train: [4][29/61]|Tot: 0:00:41 |ETA: 0:00:00 |loss 4.7060 |hm_loss 2.8055 |wh_loss 17.4476 |off_loss 0.1558 |Data 0.690s(0.690s) |Net 1.369s
3
0
2
2
ctdet/coco_dla| train: [4][30/61]|Tot: 0:00:42 |ETA: 0:00:00 |loss 4.6545 |hm_loss 2.7777 |wh_loss 17.2332 |off_loss 0.1535 |Data 0.700s(0.690s) |Net 1.370s
0
2
1
1
0
1
ctdet/coco_dla| train: [4][31/61]|Tot: 0:00:43 |ETA: 0:00:00 |loss 4.6660 |hm_loss 2.8007 |wh_loss 17.0931 |off_loss 0.1560 |Data 0.736s(0.692s) |Net 1.371s
2
0
0
ctdet/coco_dla| train: [4][32/61]|Tot: 0:00:45 |ETA: 0:00:00 |loss 4.5836 |hm_loss 2.7523 |wh_loss 16.7896 |off_loss 0.1524 |Data 0.693s(0.692s) |Net 1.371s
1
1
ctdet/coco_dla| train: [4][33/61]|Tot: 0:00:46 |ETA: 0:00:00 |loss 4.5688 |hm_loss 2.7329 |wh_loss 16.8574 |off_loss 0.1501 |Data 0.691s(0.692s) |Net 1.371s
0
0
ctdet/coco_dla| train: [4][34/61]|Tot: 0:00:48 |ETA: 0:00:00 |loss 4.4943 |hm_loss 2.6883 |wh_loss 16.5859 |off_loss 0.1475 |Data 0.741s(0.693s) |Net 1.373s
2
0
ctdet/coco_dla| train: [4][35/61]|Tot: 0:00:49 |ETA: 0:00:00 |loss 4.4538 |hm_loss 2.6679 |wh_loss 16.3926 |off_loss 0.1467 |Data 0.686s(0.693s) |Net 1.373s
1
1
0
ctdet/coco_dla| train: [4][36/61]|Tot: 0:00:50 |ETA: 0:00:00 |loss 4.4481 |hm_loss 2.6717 |wh_loss 16.2840 |off_loss 0.1480 |Data 0.695s(0.693s) |Net 1.373s
1
0
1
0
2
2
1
0
1
0
ctdet/coco_dla| train: [4][37/61]|Tot: 0:00:52 |ETA: 0:00:00 |loss 4.4559 |hm_loss 2.6882 |wh_loss 16.1834 |off_loss 0.1493 |Data 0.687s(0.693s) |Net 1.373s
0
0
2
2
2
0
0
ctdet/coco_dla| train: [4][38/61]|Tot: 0:00:53 |ETA: 0:00:00 |loss 4.4517 |hm_loss 2.6887 |wh_loss 16.1300 |off_loss 0.1500 |Data 0.681s(0.693s) |Net 1.372s
0
1
ctdet/coco_dla| train: [4][39/61]|Tot: 0:00:54 |ETA: 0:00:00 |loss 4.3815 |hm_loss 2.6516 |wh_loss 15.8260 |off_loss 0.1473 |Data 0.686s(0.692s) |Net 1.372s
0
0
0
ctdet/coco_dla| train: [4][40/61]|Tot: 0:00:56 |ETA: 0:00:00 |loss 4.3806 |hm_loss 2.6542 |wh_loss 15.7903 |off_loss 0.1473 |Data 0.735s(0.694s) |Net 1.373s
0
0
0
1
1
0
ctdet/coco_dla| train: [4][41/61]|Tot: 0:00:57 |ETA: 0:00:00 |loss 4.3622 |hm_loss 2.6534 |wh_loss 15.6104 |off_loss 0.1478 |Data 0.684s(0.693s) |Net 1.372s
1
2
0
0
0
0
ctdet/coco_dla| train: [4][42/61]|Tot: 0:00:59 |ETA: 0:00:00 |loss 4.4118 |hm_loss 2.6687 |wh_loss 15.9339 |off_loss 0.1497 |Data 0.693s(0.693s) |Net 1.372s
2
0
0
1
ctdet/coco_dla| train: [4][43/61]|Tot: 0:01:00 |ETA: 0:00:00 |loss 4.3941 |hm_loss 2.6686 |wh_loss 15.7519 |off_loss 0.1503 |Data 0.675s(0.693s) |Net 1.372s
1
0
0
ctdet/coco_dla| train: [4][44/61]|Tot: 0:01:01 |ETA: 0:00:00 |loss 4.3854 |hm_loss 2.6705 |wh_loss 15.6405 |off_loss 0.1508 |Data 0.697s(0.693s) |Net 1.372s
2
2
0
0
ctdet/coco_dla| train: [4][45/61]|Tot: 0:01:03 |ETA: 0:00:00 |loss 4.4322 |hm_loss 2.6893 |wh_loss 15.8975 |off_loss 0.1531 |Data 0.695s(0.693s) |Net 1.372s
ctdet/coco_dla| train: [4][46/61]|Tot: 0:01:04 |ETA: 0:00:00 |loss 4.3483 |hm_loss 2.6425 |wh_loss 15.5593 |off_loss 0.1499 |Data 0.690s(0.693s) |Net 1.372s
0
0
0
1
1
1
0
ctdet/coco_dla| train: [4][47/61]|Tot: 0:01:05 |ETA: 0:00:00 |loss 4.3374 |hm_loss 2.6422 |wh_loss 15.4524 |off_loss 0.1499 |Data 0.674s(0.693s) |Net 1.371s
0
3
1
1
2
0
ctdet/coco_dla| train: [4][48/61]|Tot: 0:01:07 |ETA: 0:00:00 |loss 4.3623 |hm_loss 2.6564 |wh_loss 15.5479 |off_loss 0.1511 |Data 0.696s(0.693s) |Net 1.371s
0
0
0
1
0
1
0
0
2
ctdet/coco_dla| train: [4][49/61]|Tot: 0:01:08 |ETA: 0:00:00 |loss 4.3505 |hm_loss 2.6558 |wh_loss 15.4359 |off_loss 0.1511 |Data 0.686s(0.693s) |Net 1.371s
2
0
0
0
ctdet/coco_dla| train: [4][50/61]|Tot: 0:01:09 |ETA: 0:00:00 |loss 4.3875 |hm_loss 2.6727 |wh_loss 15.6186 |off_loss 0.1530 |Data 0.689s(0.692s) |Net 1.371s
0
1
1
ctdet/coco_dla| train: [4][51/61]|Tot: 0:01:11 |ETA: 0:00:00 |loss 4.3560 |hm_loss 2.6596 |wh_loss 15.4423 |off_loss 0.1521 |Data 0.685s(0.692s) |Net 1.372s
0
1
1
0
0
0
0
0
1
ctdet/coco_dla| train: [4][52/61]|Tot: 0:01:12 |ETA: 0:00:00 |loss 4.3716 |hm_loss 2.6732 |wh_loss 15.4435 |off_loss 0.1541 |Data 0.728s(0.693s) |Net 1.372s
0
1
1
0
ctdet/coco_dla| train: [4][53/61]|Tot: 0:01:14 |ETA: 0:00:00 |loss 4.3641 |hm_loss 2.6754 |wh_loss 15.3470 |off_loss 0.1540 |Data 0.681s(0.693s) |Net 1.372s
0
2
0
0
3
2
ctdet/coco_dla| train: [4][54/61]|Tot: 0:01:15 |ETA: 0:00:00 |loss 4.4076 |hm_loss 2.7065 |wh_loss 15.4402 |off_loss 0.1571 |Data 0.685s(0.693s) |Net 1.372s
1
1
1
0
1
ctdet/coco_dla| train: [4][55/61]|Tot: 0:01:16 |ETA: 0:00:00 |loss 4.4201 |hm_loss 2.7056 |wh_loss 15.5608 |off_loss 0.1584 |Data 0.675s(0.692s) |Net 1.371s
1
0
1
1
1
2
ctdet/coco_dla| train: [4][56/61]|Tot: 0:01:18 |ETA: 0:00:00 |loss 4.4403 |hm_loss 2.7189 |wh_loss 15.6205 |off_loss 0.1593 |Data 0.680s(0.692s) |Net 1.371s
3
2
1
0
ctdet/coco_dla| train: [4][57/61]|Tot: 0:01:19 |ETA: 0:00:00 |loss 4.4279 |hm_loss 2.7178 |wh_loss 15.5112 |off_loss 0.1590 |Data 0.688s(0.692s) |Net 1.371s
0
0
1
0
1
ctdet/coco_dla| train: [4][58/61]|Tot: 0:01:20 |ETA: 0:00:00 |loss 4.4614 |hm_loss 2.7296 |wh_loss 15.7163 |off_loss 0.1602 |Data 0.697s(0.692s) |Net 1.371s
0
1
2
0
ctdet/coco_dla| train: [4][59/61]|Tot: 0:01:22 |ETA: 0:00:00 |loss 4.4774 |hm_loss 2.7436 |wh_loss 15.7253 |off_loss 0.1613 |Data 0.694s(0.692s) |Net 1.371s
1
0
1
1
ctdet/coco_dla| train: [4][60/61]|Tot: 0:01:23 |ETA: 0:00:00 |loss 4.4840 |hm_loss 2.7420 |wh_loss 15.8181 |off_loss 0.1601 |Data 0.688s(0.692s) |Net 1.372s
2
1
0
1
ctdet/coco_dla| train: [5][0/61]|Tot: 0:00:01 |ETA: 0:00:00 |loss 6.2810 |hm_loss 3.4552 |wh_loss 26.6255 |off_loss 0.1633 |Data 0.691s(0.691s) |Net 1.400s
2
1
0
0
1
ctdet/coco_dla| train: [5][1/61]|Tot: 0:00:02 |ETA: 0:00:00 |loss 4.6292 |hm_loss 2.6923 |wh_loss 18.0613 |off_loss 0.1308 |Data 0.686s(0.689s) |Net 1.382s
0
0
0
1
0
1
1
1
0
ctdet/coco_dla| train: [5][2/61]|Tot: 0:00:04 |ETA: 0:00:00 |loss 5.0069 |hm_loss 2.8899 |wh_loss 19.5087 |off_loss 0.1661 |Data 0.689s(0.689s) |Net 1.377s
1
0
0
0
0
ctdet/coco_dla| train: [5][3/61]|Tot: 0:00:05 |ETA: 0:00:00 |loss 5.1853 |hm_loss 3.0480 |wh_loss 19.5032 |off_loss 0.1870 |Data 0.667s(0.683s) |Net 1.369s
0
1
0
1
1
ctdet/coco_dla| train: [5][4/61]|Tot: 0:00:06 |ETA: 0:00:00 |loss 5.0112 |hm_loss 2.9411 |wh_loss 18.8552 |off_loss 0.1846 |Data 0.684s(0.683s) |Net 1.367s
1
0
0
2
2
1
0
ctdet/coco_dla| train: [5][5/61]|Tot: 0:00:08 |ETA: 0:00:00 |loss 4.7808 |hm_loss 2.8660 |wh_loss 17.3692 |off_loss 0.1778 |Data 0.664s(0.680s) |Net 1.361s
0
0
2
ctdet/coco_dla| train: [5][6/61]|Tot: 0:00:09 |ETA: 0:00:00 |loss 4.4994 |hm_loss 2.7323 |wh_loss 15.9489 |off_loss 0.1722 |Data 0.677s(0.680s) |Net 1.359s
2
1
0
0
2
ctdet/coco_dla| train: [5][7/61]|Tot: 0:00:10 |ETA: 0:00:00 |loss 4.2881 |hm_loss 2.6240 |wh_loss 15.0307 |off_loss 0.1611 |Data 0.677s(0.679s) |Net 1.358s
0
2
1
1
ctdet/coco_dla| train: [5][8/61]|Tot: 0:00:12 |ETA: 0:00:00 |loss 4.1517 |hm_loss 2.5500 |wh_loss 14.4800 |off_loss 0.1538 |Data 0.694s(0.681s) |Net 1.364s
0
2
0
1
ctdet/coco_dla| train: [5][9/61]|Tot: 0:00:13 |ETA: 0:00:00 |loss 4.2940 |hm_loss 2.6545 |wh_loss 14.7839 |off_loss 0.1611 |Data 0.693s(0.682s) |Net 1.364s
1
1
0
0
2
ctdet/coco_dla| train: [5][10/61]|Tot: 0:00:15 |ETA: 0:00:00 |loss 4.3365 |hm_loss 2.6613 |wh_loss 15.0804 |off_loss 0.1671 |Data 0.688s(0.683s) |Net 1.364s
1
0
0
ctdet/coco_dla| train: [5][11/61]|Tot: 0:00:16 |ETA: 0:00:00 |loss 4.2523 |hm_loss 2.6054 |wh_loss 14.8332 |off_loss 0.1636 |Data 0.686s(0.683s) |Net 1.364s
0
0
0
1
0
0
ctdet/coco_dla| train: [5][12/61]|Tot: 0:00:17 |ETA: 0:00:00 |loss 4.3845 |hm_loss 2.6711 |wh_loss 15.4698 |off_loss 0.1664 |Data 0.679s(0.683s) |Net 1.363s
0
1
0
0
0
ctdet/coco_dla| train: [5][13/61]|Tot: 0:00:19 |ETA: 0:00:00 |loss 4.5067 |hm_loss 2.7268 |wh_loss 16.1049 |off_loss 0.1694 |Data 0.679s(0.682s) |Net 1.362s
0
2
1
2
0
ctdet/coco_dla| train: [5][14/61]|Tot: 0:00:20 |ETA: 0:00:00 |loss 4.5418 |hm_loss 2.7719 |wh_loss 16.0079 |off_loss 0.1691 |Data 0.678s(0.682s) |Net 1.361s
0
0
2
3
ctdet/coco_dla| train: [5][15/61]|Tot: 0:00:21 |ETA: 0:00:00 |loss 4.6611 |hm_loss 2.8166 |wh_loss 16.7744 |off_loss 0.1671 |Data 0.746s(0.686s) |Net 1.365s
0
1
0
1
ctdet/coco_dla| train: [5][16/61]|Tot: 0:00:23 |ETA: 0:00:00 |loss 4.5023 |hm_loss 2.7201 |wh_loss 16.2085 |off_loss 0.1614 |Data 0.671s(0.685s) |Net 1.364s
1
0
0
ctdet/coco_dla| train: [5][17/61]|Tot: 0:00:24 |ETA: 0:00:00 |loss 4.4690 |hm_loss 2.7167 |wh_loss 15.9068 |off_loss 0.1616 |Data 0.681s(0.685s) |Net 1.365s
0
2
3
0
0
0
1
ctdet/coco_dla| train: [5][18/61]|Tot: 0:00:25 |ETA: 0:00:00 |loss 4.5032 |hm_loss 2.7450 |wh_loss 15.8864 |off_loss 0.1695 |Data 0.680s(0.685s) |Net 1.365s
0
0
ctdet/coco_dla| train: [5][19/61]|Tot: 0:00:27 |ETA: 0:00:00 |loss 4.4135 |hm_loss 2.7031 |wh_loss 15.4417 |off_loss 0.1662 |Data 0.679s(0.684s) |Net 1.364s
1
2
1
0
2
0
1
0
0
ctdet/coco_dla| train: [5][20/61]|Tot: 0:00:28 |ETA: 0:00:00 |loss 4.4840 |hm_loss 2.7282 |wh_loss 15.8566 |off_loss 0.1702 |Data 0.680s(0.684s) |Net 1.364s
2
2
ctdet/coco_dla| train: [5][21/61]|Tot: 0:00:29 |ETA: 0:00:00 |loss 4.4426 |hm_loss 2.6924 |wh_loss 15.8266 |off_loss 0.1676 |Data 0.683s(0.684s) |Net 1.363s
2
1
0
1
0
0
ctdet/coco_dla| train: [5][22/61]|Tot: 0:00:31 |ETA: 0:00:00 |loss 4.4229 |hm_loss 2.6859 |wh_loss 15.7177 |off_loss 0.1652 |Data 0.683s(0.684s) |Net 1.363s
0
0
ctdet/coco_dla| train: [5][23/61]|Tot: 0:00:32 |ETA: 0:00:00 |loss 4.3458 |hm_loss 2.6520 |wh_loss 15.3002 |off_loss 0.1638 |Data 0.681s(0.684s) |Net 1.363s
1
0
0
1
0
0
ctdet/coco_dla| train: [5][24/61]|Tot: 0:00:34 |ETA: 0:00:00 |loss 4.4077 |hm_loss 2.6857 |wh_loss 15.5491 |off_loss 0.1671 |Data 0.679s(0.684s) |Net 1.362s
1
0
1
ctdet/coco_dla| train: [5][25/61]|Tot: 0:00:35 |ETA: 0:00:00 |loss 4.3490 |hm_loss 2.6552 |wh_loss 15.2984 |off_loss 0.1639 |Data 0.744s(0.686s) |Net 1.365s
2
2
0
0
ctdet/coco_dla| train: [5][26/61]|Tot: 0:00:36 |ETA: 0:00:00 |loss 4.4002 |hm_loss 2.6906 |wh_loss 15.4187 |off_loss 0.1677 |Data 0.751s(0.688s) |Net 1.367s
1
1
0
0
0
ctdet/coco_dla| train: [5][27/61]|Tot: 0:00:38 |ETA: 0:00:00 |loss 4.3886 |hm_loss 2.6886 |wh_loss 15.3111 |off_loss 0.1689 |Data 0.680s(0.688s) |Net 1.367s
3
0
3
2
0
2
0
0
1
ctdet/coco_dla| train: [5][28/61]|Tot: 0:00:39 |ETA: 0:00:00 |loss 4.4344 |hm_loss 2.7175 |wh_loss 15.4538 |off_loss 0.1716 |Data 0.682s(0.688s) |Net 1.366s
2
0
1
1
2
1
1
0
ctdet/coco_dla| train: [5][29/61]|Tot: 0:00:40 |ETA: 0:00:00 |loss 4.4417 |hm_loss 2.7168 |wh_loss 15.5458 |off_loss 0.1703 |Data 0.687s(0.688s) |Net 1.366s
0
2
ctdet/coco_dla| train: [5][30/61]|Tot: 0:00:42 |ETA: 0:00:00 |loss 4.3500 |hm_loss 2.6661 |wh_loss 15.1786 |off_loss 0.1661 |Data 0.795s(0.691s) |Net 1.369s
0
2
0
0
1
ctdet/coco_dla| train: [5][31/61]|Tot: 0:00:43 |ETA: 0:00:00 |loss 4.3295 |hm_loss 2.6658 |wh_loss 14.9747 |off_loss 0.1663 |Data 0.682s(0.691s) |Net 1.369s
0
1
0
0
ctdet/coco_dla| train: [5][32/61]|Tot: 0:00:45 |ETA: 0:00:00 |loss 4.3175 |hm_loss 2.6691 |wh_loss 14.8272 |off_loss 0.1658 |Data 0.695s(0.691s) |Net 1.369s
0
1
0
ctdet/coco_dla| train: [5][33/61]|Tot: 0:00:46 |ETA: 0:00:00 |loss 4.2398 |hm_loss 2.6246 |wh_loss 14.5277 |off_loss 0.1624 |Data 0.684s(0.691s) |Net 1.369s
1
0
1
1
3
1
ctdet/coco_dla| train: [5][34/61]|Tot: 0:00:47 |ETA: 0:00:00 |loss 4.2660 |hm_loss 2.6427 |wh_loss 14.5859 |off_loss 0.1646 |Data 0.687s(0.691s) |Net 1.370s
1
0
0
1
ctdet/coco_dla| train: [5][35/61]|Tot: 0:00:49 |ETA: 0:00:00 |loss 4.2547 |hm_loss 2.6370 |wh_loss 14.5364 |off_loss 0.1640 |Data 0.739s(0.692s) |Net 1.371s
1
0
1
ctdet/coco_dla| train: [5][36/61]|Tot: 0:00:50 |ETA: 0:00:00 |loss 4.2614 |hm_loss 2.6367 |wh_loss 14.6249 |off_loss 0.1622 |Data 0.775s(0.694s) |Net 1.373s
1
0
0
0
2
1
ctdet/coco_dla| train: [5][37/61]|Tot: 0:00:52 |ETA: 0:00:00 |loss 4.2484 |hm_loss 2.6385 |wh_loss 14.4835 |off_loss 0.1616 |Data 0.674s(0.694s) |Net 1.373s
0
0
0
0
0
0
0
0
3
2
1
ctdet/coco_dla| train: [5][38/61]|Tot: 0:00:53 |ETA: 0:00:00 |loss 4.2758 |hm_loss 2.6522 |wh_loss 14.6165 |off_loss 0.1620 |Data 0.721s(0.695s) |Net 1.373s
2
0
0
0
ctdet/coco_dla| train: [5][39/61]|Tot: 0:00:54 |ETA: 0:00:00 |loss 4.2818 |hm_loss 2.6526 |wh_loss 14.6768 |off_loss 0.1615 |Data 0.676s(0.694s) |Net 1.373s
1
1
1
0
0
1
ctdet/coco_dla| train: [5][40/61]|Tot: 0:00:56 |ETA: 0:00:00 |loss 4.3064 |hm_loss 2.6694 |wh_loss 14.7374 |off_loss 0.1633 |Data 0.684s(0.694s) |Net 1.372s
0
0
0
ctdet/coco_dla| train: [5][41/61]|Tot: 0:00:57 |ETA: 0:00:00 |loss 4.2553 |hm_loss 2.6494 |wh_loss 14.4494 |off_loss 0.1609 |Data 0.683s(0.694s) |Net 1.372s
2
0
0
0
2
0
1
ctdet/coco_dla| train: [5][42/61]|Tot: 0:00:58 |ETA: 0:00:00 |loss 4.2857 |hm_loss 2.6600 |wh_loss 14.6495 |off_loss 0.1608 |Data 0.672s(0.693s) |Net 1.372s
1
2
ctdet/coco_dla| train: [5][43/61]|Tot: 0:01:00 |ETA: 0:00:00 |loss 4.2265 |hm_loss 2.6296 |wh_loss 14.3850 |off_loss 0.1584 |Data 0.736s(0.694s) |Net 1.374s
0
0
3
1
0
1
1
0
ctdet/coco_dla| train: [5][44/61]|Tot: 0:01:01 |ETA: 0:00:00 |loss 4.2155 |hm_loss 2.6275 |wh_loss 14.3002 |off_loss 0.1580 |Data 0.672s(0.694s) |Net 1.373s
0
0
3
0
0
ctdet/coco_dla| train: [5][45/61]|Tot: 0:01:03 |ETA: 0:00:00 |loss 4.2022 |hm_loss 2.6229 |wh_loss 14.2250 |off_loss 0.1569 |Data 0.679s(0.693s) |Net 1.373s
2
0
1
2
ctdet/coco_dla| train: [5][46/61]|Tot: 0:01:04 |ETA: 0:00:00 |loss 4.1930 |hm_loss 2.6236 |wh_loss 14.1222 |off_loss 0.1572 |Data 0.683s(0.693s) |Net 1.372s
0
3
0
0
2
0
1
0
1
ctdet/coco_dla| train: [5][47/61]|Tot: 0:01:05 |ETA: 0:00:00 |loss 4.2236 |hm_loss 2.6516 |wh_loss 14.1289 |off_loss 0.1591 |Data 0.687s(0.693s) |Net 1.372s
0
1
0
ctdet/coco_dla| train: [5][48/61]|Tot: 0:01:07 |ETA: 0:00:00 |loss 4.2130 |hm_loss 2.6524 |wh_loss 14.0140 |off_loss 0.1592 |Data 0.689s(0.693s) |Net 1.372s
0
1
ctdet/coco_dla| train: [5][49/61]|Tot: 0:01:08 |ETA: 0:00:00 |loss 4.1609 |hm_loss 2.6204 |wh_loss 13.8358 |off_loss 0.1570 |Data 0.687s(0.693s) |Net 1.372s
1
0
2
1
ctdet/coco_dla| train: [5][50/61]|Tot: 0:01:09 |ETA: 0:00:00 |loss 4.1520 |hm_loss 2.6196 |wh_loss 13.7404 |off_loss 0.1584 |Data 0.691s(0.693s) |Net 1.372s
1
0
1
2
1
0
ctdet/coco_dla| train: [5][51/61]|Tot: 0:01:11 |ETA: 0:00:00 |loss 4.1601 |hm_loss 2.6329 |wh_loss 13.6881 |off_loss 0.1584 |Data 0.678s(0.692s) |Net 1.371s
0
0
0
0
1
ctdet/coco_dla| train: [5][52/61]|Tot: 0:01:12 |ETA: 0:00:00 |loss 4.1575 |hm_loss 2.6322 |wh_loss 13.6707 |off_loss 0.1582 |Data 0.677s(0.692s) |Net 1.372s
0
0
1
1
0
0
ctdet/coco_dla| train: [5][53/61]|Tot: 0:01:14 |ETA: 0:00:00 |loss 4.1302 |hm_loss 2.6190 |wh_loss 13.5373 |off_loss 0.1574 |Data 0.745s(0.693s) |Net 1.372s
1
1
1
ctdet/coco_dla| train: [5][54/61]|Tot: 0:01:15 |ETA: 0:00:00 |loss 4.1041 |hm_loss 2.6041 |wh_loss 13.4383 |off_loss 0.1561 |Data 0.686s(0.693s) |Net 1.372s
3
1
2
1
0
0
0
0
1
ctdet/coco_dla| train: [5][55/61]|Tot: 0:01:16 |ETA: 0:00:00 |loss 4.1227 |hm_loss 2.6176 |wh_loss 13.4809 |off_loss 0.1570 |Data 0.676s(0.693s) |Net 1.372s
1
1
0
ctdet/coco_dla| train: [5][56/61]|Tot: 0:01:18 |ETA: 0:00:00 |loss 4.0995 |hm_loss 2.6043 |wh_loss 13.3911 |off_loss 0.1560 |Data 0.687s(0.693s) |Net 1.372s
0
ctdet/coco_dla| train: [5][57/61]|Tot: 0:01:19 |ETA: 0:00:00 |loss 4.0531 |hm_loss 2.5788 |wh_loss 13.1943 |off_loss 0.1549 |Data 0.688s(0.692s) |Net 1.372s
0
0
0
0
0
1
0
0
ctdet/coco_dla| train: [5][58/61]|Tot: 0:01:20 |ETA: 0:00:00 |loss 4.0597 |hm_loss 2.5896 |wh_loss 13.1492 |off_loss 0.1552 |Data 0.694s(0.693s) |Net 1.371s
1
0
1
0
ctdet/coco_dla| train: [5][59/61]|Tot: 0:01:22 |ETA: 0:00:00 |loss 4.0503 |hm_loss 2.5878 |wh_loss 13.0638 |off_loss 0.1561 |Data 0.756s(0.694s) |Net 1.373s
1
0
0
1
ctdet/coco_dla| train: [5][60/61]|Tot: 0:01:23 |ETA: 0:00:00 |loss 4.0290 |hm_loss 2.5750 |wh_loss 12.9887 |off_loss 0.1551 |Data 0.699s(0.694s) |Net 1.373s
/root/.pyenv/versions/3.6.9/lib/python3.6/site-packages/torch/nn/functional.py:52: UserWarning: size_average and reduce args will be deprecated, please use reduction='sum' instead.
  warnings.warn(warning.format(ret))
/root/.pyenv/versions/3.6.9/lib/python3.6/site-packages/torch/nn/parallel/_functions.py:58: UserWarning: Was asked to gather along dimension 0, but all input tensors were scalars; will instead unsqueeze and return a vector.
  warnings.warn('Was asked to gather along dimension 0, but all '
ctdet/coco_dla| val: [5][0/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 7.7391 |hm_loss 4.1923 |wh_loss 31.1896 |off_loss 0.4279 |Data 0.211s(0.211s) |Net 0.256s
ctdet/coco_dla| val: [5][1/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 7.3524 |hm_loss 4.1069 |wh_loss 27.8113 |off_loss 0.4644 |Data 0.001s(0.106s) |Net 0.138s
ctdet/coco_dla| val: [5][2/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 6.9210 |hm_loss 4.0701 |wh_loss 24.2181 |off_loss 0.4291 |Data 0.000s(0.071s) |Net 0.099s
ctdet/coco_dla| val: [5][3/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 6.7402 |hm_loss 4.0596 |wh_loss 22.8348 |off_loss 0.3972 |Data 0.001s(0.053s) |Net 0.079s
ctdet/coco_dla| val: [5][4/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 6.7516 |hm_loss 4.0433 |wh_loss 23.5554 |off_loss 0.3528 |Data 0.001s(0.043s) |Net 0.068s
ctdet/coco_dla| val: [5][5/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 6.6216 |hm_loss 3.9569 |wh_loss 23.1387 |off_loss 0.3508 |Data 0.001s(0.036s) |Net 0.060s
ctdet/coco_dla| val: [5][6/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 5.6832 |hm_loss 3.3991 |wh_loss 19.8332 |off_loss 0.3007 |Data 0.001s(0.031s) |Net 0.054s
ctdet/coco_dla| val: [5][7/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 4.9792 |hm_loss 2.9806 |wh_loss 17.3540 |off_loss 0.2631 |Data 0.002s(0.027s) |Net 0.050s
ctdet/coco_dla| val: [5][8/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 4.4316 |hm_loss 2.6551 |wh_loss 15.4258 |off_loss 0.2339 |Data 0.000s(0.024s) |Net 0.047s
ctdet/coco_dla| val: [5][9/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 3.9936 |hm_loss 2.3948 |wh_loss 13.8832 |off_loss 0.2105 |Data 0.000s(0.022s) |Net 0.045s
ctdet/coco_dla| val: [5][10/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 3.6351 |hm_loss 2.1817 |wh_loss 12.6211 |off_loss 0.1914 |Data 0.001s(0.020s) |Net 0.043s
ctdet/coco_dla| val: [5][11/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 3.3365 |hm_loss 2.0041 |wh_loss 11.5694 |off_loss 0.1754 |Data 0.001s(0.018s) |Net 0.041s
ctdet/coco_dla| val: [5][12/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 3.0838 |hm_loss 1.8540 |wh_loss 10.6794 |off_loss 0.1619 |Data 0.001s(0.017s) |Net 0.039s
ctdet/coco_dla| val: [5][13/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.8673 |hm_loss 1.7252 |wh_loss 9.9166 |off_loss 0.1504 |Data 0.001s(0.016s) |Net 0.038s
ctdet/coco_dla| val: [5][14/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.6796 |hm_loss 1.6137 |wh_loss 9.2555 |off_loss 0.1403 |Data 0.001s(0.015s) |Net 0.037s
ctdet/coco_dla| val: [5][15/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.5154 |hm_loss 1.5161 |wh_loss 8.6770 |off_loss 0.1316 |Data 0.001s(0.014s) |Net 0.036s
ctdet/coco_dla| val: [5][16/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.3705 |hm_loss 1.4300 |wh_loss 8.1666 |off_loss 0.1238 |Data 0.001s(0.013s) |Net 0.035s
ctdet/coco_dla| val: [5][17/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.2417 |hm_loss 1.3535 |wh_loss 7.7129 |off_loss 0.1169 |Data 0.001s(0.012s) |Net 0.034s
ctdet/coco_dla| val: [5][18/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.1264 |hm_loss 1.2850 |wh_loss 7.3070 |off_loss 0.1108 |Data 0.001s(0.012s) |Net 0.034s
ctdet/coco_dla| val: [5][19/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 2.0227 |hm_loss 1.2233 |wh_loss 6.9416 |off_loss 0.1053 |Data 0.001s(0.011s) |Net 0.033s
ctdet/coco_dla| val: [5][20/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.9289 |hm_loss 1.1675 |wh_loss 6.6111 |off_loss 0.1002 |Data 0.000s(0.011s) |Net 0.033s
ctdet/coco_dla| val: [5][21/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.8436 |hm_loss 1.1169 |wh_loss 6.3106 |off_loss 0.0957 |Data 0.000s(0.010s) |Net 0.032s
ctdet/coco_dla| val: [5][22/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.7657 |hm_loss 1.0706 |wh_loss 6.0362 |off_loss 0.0915 |Data 0.000s(0.010s) |Net 0.032s
ctdet/coco_dla| val: [5][23/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.6943 |hm_loss 1.0281 |wh_loss 5.7847 |off_loss 0.0877 |Data 0.001s(0.009s) |Net 0.031s
ctdet/coco_dla| val: [5][24/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.6286 |hm_loss 0.9891 |wh_loss 5.5533 |off_loss 0.0842 |Data 0.000s(0.009s) |Net 0.031s
ctdet/coco_dla| val: [5][25/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.5679 |hm_loss 0.9530 |wh_loss 5.3397 |off_loss 0.0810 |Data 0.001s(0.009s) |Net 0.031s
ctdet/coco_dla| val: [5][26/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.5118 |hm_loss 0.9196 |wh_loss 5.1419 |off_loss 0.0780 |Data 0.000s(0.008s) |Net 0.030s
ctdet/coco_dla| val: [5][27/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.4596 |hm_loss 0.8886 |wh_loss 4.9583 |off_loss 0.0752 |Data 0.001s(0.008s) |Net 0.030s
ctdet/coco_dla| val: [5][28/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.4111 |hm_loss 0.8598 |wh_loss 4.7873 |off_loss 0.0726 |Data 0.001s(0.008s) |Net 0.030s
ctdet/coco_dla| val: [5][29/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.3658 |hm_loss 0.8329 |wh_loss 4.6277 |off_loss 0.0702 |Data 0.000s(0.008s) |Net 0.029s
ctdet/coco_dla| val: [5][30/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.3234 |hm_loss 0.8077 |wh_loss 4.4785 |off_loss 0.0679 |Data 0.000s(0.007s) |Net 0.029s
ctdet/coco_dla| val: [5][31/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.2837 |hm_loss 0.7841 |wh_loss 4.3385 |off_loss 0.0658 |Data 0.000s(0.007s) |Net 0.029s
ctdet/coco_dla| val: [5][32/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.2464 |hm_loss 0.7619 |wh_loss 4.2070 |off_loss 0.0638 |Data 0.001s(0.007s) |Net 0.028s
ctdet/coco_dla| val: [5][33/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.2113 |hm_loss 0.7411 |wh_loss 4.0833 |off_loss 0.0619 |Data 0.001s(0.007s) |Net 0.028s
ctdet/coco_dla| val: [5][34/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.1782 |hm_loss 0.7214 |wh_loss 3.9666 |off_loss 0.0601 |Data 0.000s(0.007s) |Net 0.028s
ctdet/coco_dla| val: [5][35/2110]|Tot: 0:00:00 |ETA: 0:00:00 |loss 1.1470 |hm_loss 0.7029 |wh_loss 3.8565 |off_loss 0.0585 |Data 0.001s(0.006s) |Net 0.028s
ctdet/coco_dla| val: [5][36/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.3029 |hm_loss 0.8024 |wh_loss 4.3731 |off_loss 0.0632 |Data 0.001s(0.006s) |Net 0.028s
ctdet/coco_dla| val: [5][37/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.4443 |hm_loss 0.8883 |wh_loss 4.8267 |off_loss 0.0733 |Data 0.001s(0.006s) |Net 0.027s
ctdet/coco_dla| val: [5][38/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.5587 |hm_loss 0.9579 |wh_loss 5.2360 |off_loss 0.0772 |Data 0.001s(0.006s) |Net 0.027s
ctdet/coco_dla| val: [5][39/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.6603 |hm_loss 1.0254 |wh_loss 5.5706 |off_loss 0.0778 |Data 0.001s(0.006s) |Net 0.027s
ctdet/coco_dla| val: [5][40/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.7568 |hm_loss 1.0919 |wh_loss 5.8314 |off_loss 0.0817 |Data 0.001s(0.006s) |Net 0.027s
ctdet/coco_dla| val: [5][41/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.8482 |hm_loss 1.1591 |wh_loss 6.0568 |off_loss 0.0834 |Data 0.001s(0.006s) |Net 0.027s
ctdet/coco_dla| val: [5][42/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.9419 |hm_loss 1.2279 |wh_loss 6.2292 |off_loss 0.0911 |Data 0.001s(0.005s) |Net 0.027s
ctdet/coco_dla| val: [5][43/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.0251 |hm_loss 1.2956 |wh_loss 6.2921 |off_loss 0.1003 |Data 0.001s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][44/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.0887 |hm_loss 1.3613 |wh_loss 6.2797 |off_loss 0.0994 |Data 0.001s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][45/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.1485 |hm_loss 1.4249 |wh_loss 6.2013 |off_loss 0.1034 |Data 0.001s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][46/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.1998 |hm_loss 1.4856 |wh_loss 6.1221 |off_loss 0.1020 |Data 0.000s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][47/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.2611 |hm_loss 1.5440 |wh_loss 6.1135 |off_loss 0.1058 |Data 0.001s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][48/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.3338 |hm_loss 1.6005 |wh_loss 6.2481 |off_loss 0.1085 |Data 0.000s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][49/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.4052 |hm_loss 1.6538 |wh_loss 6.3806 |off_loss 0.1133 |Data 0.001s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][50/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.4918 |hm_loss 1.7076 |wh_loss 6.6489 |off_loss 0.1193 |Data 0.001s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][51/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.5802 |hm_loss 1.7596 |wh_loss 6.9553 |off_loss 0.1251 |Data 0.000s(0.005s) |Net 0.026s
ctdet/coco_dla| val: [5][52/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.6660 |hm_loss 1.8088 |wh_loss 7.2900 |off_loss 0.1282 |Data 0.001s(0.005s) |Net 0.025s
ctdet/coco_dla| val: [5][53/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.7503 |hm_loss 1.8566 |wh_loss 7.6684 |off_loss 0.1269 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][54/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.8198 |hm_loss 1.9022 |wh_loss 7.9157 |off_loss 0.1260 |Data 0.000s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][55/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.7705 |hm_loss 1.8692 |wh_loss 7.7743 |off_loss 0.1238 |Data 0.000s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][56/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.7228 |hm_loss 1.8374 |wh_loss 7.6379 |off_loss 0.1216 |Data 0.000s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][57/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.6768 |hm_loss 1.8066 |wh_loss 7.5062 |off_loss 0.1195 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][58/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.6323 |hm_loss 1.7769 |wh_loss 7.3790 |off_loss 0.1175 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][59/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.5894 |hm_loss 1.7482 |wh_loss 7.2560 |off_loss 0.1155 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][60/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.5478 |hm_loss 1.7205 |wh_loss 7.1371 |off_loss 0.1136 |Data 0.000s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][61/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.5076 |hm_loss 1.6936 |wh_loss 7.0220 |off_loss 0.1118 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][62/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.4687 |hm_loss 1.6676 |wh_loss 6.9105 |off_loss 0.1100 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][63/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.4309 |hm_loss 1.6423 |wh_loss 6.8025 |off_loss 0.1083 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][64/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.3943 |hm_loss 1.6179 |wh_loss 6.6979 |off_loss 0.1067 |Data 0.000s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][65/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.3588 |hm_loss 1.5942 |wh_loss 6.5964 |off_loss 0.1050 |Data 0.001s(0.004s) |Net 0.024s
ctdet/coco_dla| val: [5][66/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.3244 |hm_loss 1.5712 |wh_loss 6.4979 |off_loss 0.1035 |Data 0.001s(0.004s) |Net 0.024s
ctdet/coco_dla| val: [5][67/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.2910 |hm_loss 1.5488 |wh_loss 6.4024 |off_loss 0.1019 |Data 0.001s(0.004s) |Net 0.025s
ctdet/coco_dla| val: [5][68/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.2586 |hm_loss 1.5271 |wh_loss 6.3096 |off_loss 0.1005 |Data 0.001s(0.004s) |Net 0.024s
ctdet/coco_dla| val: [5][69/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.2271 |hm_loss 1.5061 |wh_loss 6.2194 |off_loss 0.0990 |Data 0.001s(0.004s) |Net 0.024s
ctdet/coco_dla| val: [5][70/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.1964 |hm_loss 1.4856 |wh_loss 6.1318 |off_loss 0.0976 |Data 0.001s(0.004s) |Net 0.024s
ctdet/coco_dla| val: [5][71/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.1667 |hm_loss 1.4657 |wh_loss 6.0467 |off_loss 0.0963 |Data 0.001s(0.004s) |Net 0.024s
ctdet/coco_dla| val: [5][72/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.1377 |hm_loss 1.4464 |wh_loss 5.9638 |off_loss 0.0950 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][73/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.1095 |hm_loss 1.4275 |wh_loss 5.8833 |off_loss 0.0937 |Data 0.002s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][74/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.0821 |hm_loss 1.4092 |wh_loss 5.8048 |off_loss 0.0924 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][75/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.0554 |hm_loss 1.3913 |wh_loss 5.7284 |off_loss 0.0912 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][76/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.0294 |hm_loss 1.3739 |wh_loss 5.6540 |off_loss 0.0900 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][77/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 2.0040 |hm_loss 1.3570 |wh_loss 5.5816 |off_loss 0.0889 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][78/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.9793 |hm_loss 1.3405 |wh_loss 5.5109 |off_loss 0.0878 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][79/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.9552 |hm_loss 1.3244 |wh_loss 5.4420 |off_loss 0.0867 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][80/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.9317 |hm_loss 1.3087 |wh_loss 5.3748 |off_loss 0.0856 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][81/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.9088 |hm_loss 1.2934 |wh_loss 5.3093 |off_loss 0.0845 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][82/2110]|Tot: 0:00:01 |ETA: 0:00:00 |loss 1.8865 |hm_loss 1.2784 |wh_loss 5.2453 |off_loss 0.0835 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][83/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.8647 |hm_loss 1.2638 |wh_loss 5.1829 |off_loss 0.0825 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][84/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.8433 |hm_loss 1.2496 |wh_loss 5.1219 |off_loss 0.0816 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][85/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.8225 |hm_loss 1.2357 |wh_loss 5.0623 |off_loss 0.0806 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][86/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.8022 |hm_loss 1.2221 |wh_loss 5.0041 |off_loss 0.0797 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][87/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.7823 |hm_loss 1.2088 |wh_loss 4.9473 |off_loss 0.0788 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][88/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.7629 |hm_loss 1.1958 |wh_loss 4.8917 |off_loss 0.0779 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][89/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.7439 |hm_loss 1.1832 |wh_loss 4.8373 |off_loss 0.0770 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][90/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.7253 |hm_loss 1.1707 |wh_loss 4.7842 |off_loss 0.0762 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][91/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.7072 |hm_loss 1.1586 |wh_loss 4.7322 |off_loss 0.0754 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][92/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.6894 |hm_loss 1.1467 |wh_loss 4.6813 |off_loss 0.0745 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][93/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.6719 |hm_loss 1.1350 |wh_loss 4.6315 |off_loss 0.0738 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][94/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.6549 |hm_loss 1.1236 |wh_loss 4.5827 |off_loss 0.0730 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][95/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.6382 |hm_loss 1.1124 |wh_loss 4.5350 |off_loss 0.0722 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][96/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.6218 |hm_loss 1.1015 |wh_loss 4.4883 |off_loss 0.0715 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][97/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.6058 |hm_loss 1.0908 |wh_loss 4.4425 |off_loss 0.0707 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][98/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5902 |hm_loss 1.0804 |wh_loss 4.3976 |off_loss 0.0700 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][99/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5748 |hm_loss 1.0701 |wh_loss 4.3536 |off_loss 0.0693 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][100/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5597 |hm_loss 1.0600 |wh_loss 4.3105 |off_loss 0.0686 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][101/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5450 |hm_loss 1.0502 |wh_loss 4.2682 |off_loss 0.0680 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][102/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5305 |hm_loss 1.0405 |wh_loss 4.2268 |off_loss 0.0673 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][103/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5163 |hm_loss 1.0310 |wh_loss 4.1862 |off_loss 0.0667 |Data 0.000s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][104/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.5024 |hm_loss 1.0218 |wh_loss 4.1463 |off_loss 0.0660 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][105/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4888 |hm_loss 1.0127 |wh_loss 4.1072 |off_loss 0.0654 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][106/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4754 |hm_loss 1.0037 |wh_loss 4.0688 |off_loss 0.0648 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][107/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4623 |hm_loss 0.9949 |wh_loss 4.0311 |off_loss 0.0642 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][108/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4494 |hm_loss 0.9863 |wh_loss 3.9941 |off_loss 0.0636 |Data 0.001s(0.003s) |Net 0.024s
ctdet/coco_dla| val: [5][109/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4367 |hm_loss 0.9779 |wh_loss 3.9578 |off_loss 0.0630 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][110/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4243 |hm_loss 0.9696 |wh_loss 3.9222 |off_loss 0.0625 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][111/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4120 |hm_loss 0.9614 |wh_loss 3.8872 |off_loss 0.0619 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][112/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.4001 |hm_loss 0.9534 |wh_loss 3.8528 |off_loss 0.0613 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][113/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3883 |hm_loss 0.9456 |wh_loss 3.8190 |off_loss 0.0608 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][114/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3767 |hm_loss 0.9378 |wh_loss 3.7857 |off_loss 0.0603 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][115/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3653 |hm_loss 0.9302 |wh_loss 3.7531 |off_loss 0.0598 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][116/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3541 |hm_loss 0.9228 |wh_loss 3.7210 |off_loss 0.0593 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][117/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3431 |hm_loss 0.9154 |wh_loss 3.6895 |off_loss 0.0588 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][118/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3323 |hm_loss 0.9082 |wh_loss 3.6585 |off_loss 0.0583 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][119/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3217 |hm_loss 0.9011 |wh_loss 3.6280 |off_loss 0.0578 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][120/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3113 |hm_loss 0.8942 |wh_loss 3.5980 |off_loss 0.0573 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][121/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.3010 |hm_loss 0.8873 |wh_loss 3.5685 |off_loss 0.0568 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][122/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.2909 |hm_loss 0.8806 |wh_loss 3.5395 |off_loss 0.0564 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][123/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.2810 |hm_loss 0.8739 |wh_loss 3.5110 |off_loss 0.0559 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][124/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.2712 |hm_loss 0.8674 |wh_loss 3.4829 |off_loss 0.0555 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][125/2110]|Tot: 0:00:02 |ETA: 0:00:00 |loss 1.2615 |hm_loss 0.8610 |wh_loss 3.4552 |off_loss 0.0550 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][126/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2521 |hm_loss 0.8547 |wh_loss 3.4280 |off_loss 0.0546 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][127/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2427 |hm_loss 0.8485 |wh_loss 3.4013 |off_loss 0.0542 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][128/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2336 |hm_loss 0.8423 |wh_loss 3.3749 |off_loss 0.0537 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][129/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2245 |hm_loss 0.8363 |wh_loss 3.3489 |off_loss 0.0533 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][130/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2156 |hm_loss 0.8304 |wh_loss 3.3234 |off_loss 0.0529 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][131/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2069 |hm_loss 0.8245 |wh_loss 3.2982 |off_loss 0.0525 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][132/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.1983 |hm_loss 0.8188 |wh_loss 3.2734 |off_loss 0.0521 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][133/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.1898 |hm_loss 0.8131 |wh_loss 3.2490 |off_loss 0.0517 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][134/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.1814 |hm_loss 0.8076 |wh_loss 3.2249 |off_loss 0.0514 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][135/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2166 |hm_loss 0.8280 |wh_loss 3.3400 |off_loss 0.0547 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][136/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2588 |hm_loss 0.8518 |wh_loss 3.5030 |off_loss 0.0567 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][137/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.2973 |hm_loss 0.8768 |wh_loss 3.6331 |off_loss 0.0572 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][138/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.3323 |hm_loss 0.9019 |wh_loss 3.7348 |off_loss 0.0569 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][139/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.3754 |hm_loss 0.9270 |wh_loss 3.9019 |off_loss 0.0582 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][140/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4149 |hm_loss 0.9516 |wh_loss 4.0390 |off_loss 0.0595 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][141/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4525 |hm_loss 0.9761 |wh_loss 4.1609 |off_loss 0.0603 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][142/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4888 |hm_loss 1.0001 |wh_loss 4.2626 |off_loss 0.0625 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][143/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4788 |hm_loss 0.9935 |wh_loss 4.2330 |off_loss 0.0620 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][144/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4690 |hm_loss 0.9870 |wh_loss 4.2038 |off_loss 0.0616 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][145/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4593 |hm_loss 0.9807 |wh_loss 4.1750 |off_loss 0.0612 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][146/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4498 |hm_loss 0.9744 |wh_loss 4.1466 |off_loss 0.0608 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][147/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.4794 |hm_loss 0.9909 |wh_loss 4.2533 |off_loss 0.0632 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][148/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5107 |hm_loss 1.0080 |wh_loss 4.3680 |off_loss 0.0659 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][149/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5423 |hm_loss 1.0281 |wh_loss 4.4804 |off_loss 0.0662 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][150/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5743 |hm_loss 1.0476 |wh_loss 4.5695 |off_loss 0.0697 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][151/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6120 |hm_loss 1.0688 |wh_loss 4.7273 |off_loss 0.0705 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][152/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6527 |hm_loss 1.0894 |wh_loss 4.9002 |off_loss 0.0732 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][153/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6915 |hm_loss 1.1078 |wh_loss 5.0802 |off_loss 0.0756 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][154/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6809 |hm_loss 1.1011 |wh_loss 5.0474 |off_loss 0.0751 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][155/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6706 |hm_loss 1.0944 |wh_loss 5.0150 |off_loss 0.0747 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][156/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6603 |hm_loss 1.0879 |wh_loss 4.9831 |off_loss 0.0742 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][157/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6503 |hm_loss 1.0814 |wh_loss 4.9516 |off_loss 0.0737 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][158/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6403 |hm_loss 1.0750 |wh_loss 4.9204 |off_loss 0.0733 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][159/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6305 |hm_loss 1.0687 |wh_loss 4.8897 |off_loss 0.0728 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][160/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6207 |hm_loss 1.0625 |wh_loss 4.8593 |off_loss 0.0723 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][161/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6111 |hm_loss 1.0563 |wh_loss 4.8293 |off_loss 0.0719 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][162/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.6016 |hm_loss 1.0502 |wh_loss 4.7997 |off_loss 0.0715 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][163/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5922 |hm_loss 1.0442 |wh_loss 4.7704 |off_loss 0.0710 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][164/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5829 |hm_loss 1.0382 |wh_loss 4.7415 |off_loss 0.0706 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][165/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5737 |hm_loss 1.0323 |wh_loss 4.7129 |off_loss 0.0702 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][166/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5647 |hm_loss 1.0264 |wh_loss 4.6847 |off_loss 0.0697 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][167/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5557 |hm_loss 1.0207 |wh_loss 4.6568 |off_loss 0.0693 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][168/2110]|Tot: 0:00:03 |ETA: 0:00:00 |loss 1.5468 |hm_loss 1.0149 |wh_loss 4.6293 |off_loss 0.0689 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][169/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5707 |hm_loss 1.0296 |wh_loss 4.7153 |off_loss 0.0696 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][170/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6018 |hm_loss 1.0472 |wh_loss 4.8244 |off_loss 0.0722 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][171/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6324 |hm_loss 1.0662 |wh_loss 4.9057 |off_loss 0.0755 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][172/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6567 |hm_loss 1.0859 |wh_loss 4.9462 |off_loss 0.0762 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][173/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6828 |hm_loss 1.1053 |wh_loss 4.9991 |off_loss 0.0776 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][174/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7141 |hm_loss 1.1244 |wh_loss 5.1003 |off_loss 0.0797 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][175/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7478 |hm_loss 1.1430 |wh_loss 5.2357 |off_loss 0.0812 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][176/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7382 |hm_loss 1.1368 |wh_loss 5.2061 |off_loss 0.0807 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][177/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7287 |hm_loss 1.1307 |wh_loss 5.1769 |off_loss 0.0803 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][178/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7194 |hm_loss 1.1247 |wh_loss 5.1480 |off_loss 0.0798 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][179/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7101 |hm_loss 1.1188 |wh_loss 5.1194 |off_loss 0.0794 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][180/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.7009 |hm_loss 1.1129 |wh_loss 5.0911 |off_loss 0.0790 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][181/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6919 |hm_loss 1.1070 |wh_loss 5.0631 |off_loss 0.0785 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][182/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6829 |hm_loss 1.1013 |wh_loss 5.0354 |off_loss 0.0781 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][183/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6741 |hm_loss 1.0956 |wh_loss 5.0081 |off_loss 0.0777 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][184/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6653 |hm_loss 1.0899 |wh_loss 4.9810 |off_loss 0.0773 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][185/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6566 |hm_loss 1.0843 |wh_loss 4.9542 |off_loss 0.0768 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][186/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6480 |hm_loss 1.0788 |wh_loss 4.9277 |off_loss 0.0764 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][187/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6395 |hm_loss 1.0734 |wh_loss 4.9015 |off_loss 0.0760 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][188/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6311 |hm_loss 1.0680 |wh_loss 4.8756 |off_loss 0.0756 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][189/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6228 |hm_loss 1.0626 |wh_loss 4.8499 |off_loss 0.0752 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][190/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6146 |hm_loss 1.0573 |wh_loss 4.8245 |off_loss 0.0748 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][191/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6064 |hm_loss 1.0521 |wh_loss 4.7994 |off_loss 0.0744 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][192/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5984 |hm_loss 1.0469 |wh_loss 4.7745 |off_loss 0.0741 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][193/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5904 |hm_loss 1.0418 |wh_loss 4.7499 |off_loss 0.0737 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][194/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5825 |hm_loss 1.0367 |wh_loss 4.7256 |off_loss 0.0733 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][195/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5747 |hm_loss 1.0317 |wh_loss 4.7014 |off_loss 0.0729 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][196/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5670 |hm_loss 1.0267 |wh_loss 4.6776 |off_loss 0.0726 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][197/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5594 |hm_loss 1.0218 |wh_loss 4.6540 |off_loss 0.0722 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][198/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5518 |hm_loss 1.0169 |wh_loss 4.6306 |off_loss 0.0718 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][199/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5443 |hm_loss 1.0121 |wh_loss 4.6074 |off_loss 0.0715 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][200/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5660 |hm_loss 1.0249 |wh_loss 4.6863 |off_loss 0.0724 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][201/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5879 |hm_loss 1.0410 |wh_loss 4.7428 |off_loss 0.0727 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][202/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6171 |hm_loss 1.0575 |wh_loss 4.8549 |off_loss 0.0741 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][203/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6094 |hm_loss 1.0526 |wh_loss 4.8311 |off_loss 0.0738 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][204/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.6019 |hm_loss 1.0477 |wh_loss 4.8076 |off_loss 0.0734 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][205/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5943 |hm_loss 1.0429 |wh_loss 4.7842 |off_loss 0.0730 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][206/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5869 |hm_loss 1.0381 |wh_loss 4.7611 |off_loss 0.0727 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][207/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5795 |hm_loss 1.0334 |wh_loss 4.7382 |off_loss 0.0723 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][208/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5722 |hm_loss 1.0287 |wh_loss 4.7155 |off_loss 0.0720 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][209/2110]|Tot: 0:00:04 |ETA: 0:00:00 |loss 1.5650 |hm_loss 1.0240 |wh_loss 4.6931 |off_loss 0.0717 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][210/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5579 |hm_loss 1.0195 |wh_loss 4.6708 |off_loss 0.0713 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][211/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5508 |hm_loss 1.0149 |wh_loss 4.6488 |off_loss 0.0710 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][212/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5437 |hm_loss 1.0104 |wh_loss 4.6270 |off_loss 0.0706 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][213/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5368 |hm_loss 1.0059 |wh_loss 4.6054 |off_loss 0.0703 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][214/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5299 |hm_loss 1.0015 |wh_loss 4.5839 |off_loss 0.0700 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][215/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5231 |hm_loss 0.9971 |wh_loss 4.5627 |off_loss 0.0697 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][216/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5163 |hm_loss 0.9928 |wh_loss 4.5417 |off_loss 0.0693 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][217/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5096 |hm_loss 0.9885 |wh_loss 4.5209 |off_loss 0.0690 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][218/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5029 |hm_loss 0.9842 |wh_loss 4.5002 |off_loss 0.0687 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][219/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4964 |hm_loss 0.9800 |wh_loss 4.4798 |off_loss 0.0684 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][220/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4898 |hm_loss 0.9758 |wh_loss 4.4595 |off_loss 0.0681 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][221/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4834 |hm_loss 0.9716 |wh_loss 4.4394 |off_loss 0.0678 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][222/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4770 |hm_loss 0.9675 |wh_loss 4.4195 |off_loss 0.0675 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][223/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4706 |hm_loss 0.9635 |wh_loss 4.3998 |off_loss 0.0672 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][224/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4643 |hm_loss 0.9594 |wh_loss 4.3802 |off_loss 0.0669 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][225/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4581 |hm_loss 0.9554 |wh_loss 4.3608 |off_loss 0.0666 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][226/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4519 |hm_loss 0.9514 |wh_loss 4.3416 |off_loss 0.0663 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][227/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4457 |hm_loss 0.9475 |wh_loss 4.3226 |off_loss 0.0660 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][228/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4397 |hm_loss 0.9436 |wh_loss 4.3037 |off_loss 0.0657 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][229/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4605 |hm_loss 0.9558 |wh_loss 4.3766 |off_loss 0.0670 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][230/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4825 |hm_loss 0.9708 |wh_loss 4.4397 |off_loss 0.0677 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][231/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5045 |hm_loss 0.9856 |wh_loss 4.4959 |off_loss 0.0693 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][232/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5264 |hm_loss 1.0004 |wh_loss 4.5565 |off_loss 0.0704 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][233/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5201 |hm_loss 0.9963 |wh_loss 4.5370 |off_loss 0.0701 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][234/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5139 |hm_loss 0.9923 |wh_loss 4.5177 |off_loss 0.0698 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][235/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5077 |hm_loss 0.9883 |wh_loss 4.4986 |off_loss 0.0695 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][236/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.5016 |hm_loss 0.9844 |wh_loss 4.4796 |off_loss 0.0692 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][237/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4955 |hm_loss 0.9805 |wh_loss 4.4608 |off_loss 0.0689 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][238/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4894 |hm_loss 0.9766 |wh_loss 4.4421 |off_loss 0.0686 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][239/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4835 |hm_loss 0.9727 |wh_loss 4.4236 |off_loss 0.0684 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][240/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4775 |hm_loss 0.9689 |wh_loss 4.4053 |off_loss 0.0681 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][241/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4717 |hm_loss 0.9652 |wh_loss 4.3870 |off_loss 0.0678 |Data 0.005s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][242/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4658 |hm_loss 0.9614 |wh_loss 4.3690 |off_loss 0.0675 |Data 0.003s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][243/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4600 |hm_loss 0.9577 |wh_loss 4.3511 |off_loss 0.0672 |Data 0.005s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][244/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4543 |hm_loss 0.9540 |wh_loss 4.3333 |off_loss 0.0670 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][245/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4486 |hm_loss 0.9503 |wh_loss 4.3157 |off_loss 0.0667 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][246/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4429 |hm_loss 0.9467 |wh_loss 4.2982 |off_loss 0.0664 |Data 0.002s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][247/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4373 |hm_loss 0.9431 |wh_loss 4.2809 |off_loss 0.0661 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][248/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4318 |hm_loss 0.9395 |wh_loss 4.2637 |off_loss 0.0659 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][249/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4263 |hm_loss 0.9360 |wh_loss 4.2467 |off_loss 0.0656 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][250/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4208 |hm_loss 0.9324 |wh_loss 4.2297 |off_loss 0.0654 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][251/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4153 |hm_loss 0.9290 |wh_loss 4.2130 |off_loss 0.0651 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][252/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4100 |hm_loss 0.9255 |wh_loss 4.1963 |off_loss 0.0648 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][253/2110]|Tot: 0:00:05 |ETA: 0:00:00 |loss 1.4046 |hm_loss 0.9221 |wh_loss 4.1798 |off_loss 0.0646 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][254/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3993 |hm_loss 0.9186 |wh_loss 4.1634 |off_loss 0.0643 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][255/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3941 |hm_loss 0.9153 |wh_loss 4.1471 |off_loss 0.0641 |Data 0.001s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][256/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3888 |hm_loss 0.9119 |wh_loss 4.1310 |off_loss 0.0638 |Data 0.000s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][257/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3836 |hm_loss 0.9086 |wh_loss 4.1150 |off_loss 0.0636 |Data 0.004s(0.002s) |Net 0.024s
ctdet/coco_dla| val: [5][258/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3785 |hm_loss 0.9053 |wh_loss 4.0991 |off_loss 0.0633 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][259/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3734 |hm_loss 0.9020 |wh_loss 4.0833 |off_loss 0.0631 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][260/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3683 |hm_loss 0.8987 |wh_loss 4.0677 |off_loss 0.0629 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][261/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3633 |hm_loss 0.8955 |wh_loss 4.0522 |off_loss 0.0626 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][262/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3583 |hm_loss 0.8923 |wh_loss 4.0368 |off_loss 0.0624 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][263/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3534 |hm_loss 0.8891 |wh_loss 4.0215 |off_loss 0.0621 |Data 0.002s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][264/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3485 |hm_loss 0.8859 |wh_loss 4.0063 |off_loss 0.0619 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][265/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3436 |hm_loss 0.8828 |wh_loss 3.9912 |off_loss 0.0617 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][266/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3388 |hm_loss 0.8797 |wh_loss 3.9763 |off_loss 0.0614 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][267/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3340 |hm_loss 0.8766 |wh_loss 3.9614 |off_loss 0.0612 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][268/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3292 |hm_loss 0.8736 |wh_loss 3.9467 |off_loss 0.0610 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][269/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3245 |hm_loss 0.8705 |wh_loss 3.9321 |off_loss 0.0608 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][270/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3198 |hm_loss 0.8675 |wh_loss 3.9176 |off_loss 0.0605 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][271/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3151 |hm_loss 0.8645 |wh_loss 3.9032 |off_loss 0.0603 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][272/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3105 |hm_loss 0.8615 |wh_loss 3.8889 |off_loss 0.0601 |Data 0.003s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][273/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3059 |hm_loss 0.8586 |wh_loss 3.8747 |off_loss 0.0599 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][274/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3014 |hm_loss 0.8557 |wh_loss 3.8606 |off_loss 0.0597 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][275/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2969 |hm_loss 0.8528 |wh_loss 3.8466 |off_loss 0.0594 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][276/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2924 |hm_loss 0.8499 |wh_loss 3.8327 |off_loss 0.0592 |Data 0.002s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][277/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2879 |hm_loss 0.8470 |wh_loss 3.8189 |off_loss 0.0590 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][278/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2835 |hm_loss 0.8442 |wh_loss 3.8053 |off_loss 0.0588 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][279/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3008 |hm_loss 0.8551 |wh_loss 3.8630 |off_loss 0.0594 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][280/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3180 |hm_loss 0.8678 |wh_loss 3.9029 |off_loss 0.0599 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][281/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3347 |hm_loss 0.8806 |wh_loss 3.9440 |off_loss 0.0597 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][282/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3574 |hm_loss 0.8932 |wh_loss 4.0262 |off_loss 0.0615 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][283/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3528 |hm_loss 0.8903 |wh_loss 4.0121 |off_loss 0.0613 |Data 0.002s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][284/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3482 |hm_loss 0.8873 |wh_loss 3.9980 |off_loss 0.0611 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][285/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3437 |hm_loss 0.8844 |wh_loss 3.9840 |off_loss 0.0609 |Data 0.002s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][286/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3392 |hm_loss 0.8815 |wh_loss 3.9701 |off_loss 0.0607 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][287/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3347 |hm_loss 0.8786 |wh_loss 3.9563 |off_loss 0.0605 |Data 0.006s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][288/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3303 |hm_loss 0.8758 |wh_loss 3.9426 |off_loss 0.0602 |Data 0.003s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][289/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3259 |hm_loss 0.8729 |wh_loss 3.9290 |off_loss 0.0600 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][290/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3215 |hm_loss 0.8701 |wh_loss 3.9155 |off_loss 0.0598 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][291/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3172 |hm_loss 0.8673 |wh_loss 3.9021 |off_loss 0.0596 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][292/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3129 |hm_loss 0.8646 |wh_loss 3.8888 |off_loss 0.0594 |Data 0.003s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][293/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3086 |hm_loss 0.8618 |wh_loss 3.8756 |off_loss 0.0592 |Data 0.005s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][294/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3043 |hm_loss 0.8591 |wh_loss 3.8625 |off_loss 0.0590 |Data 0.002s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][295/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.3001 |hm_loss 0.8563 |wh_loss 3.8494 |off_loss 0.0588 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][296/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2959 |hm_loss 0.8536 |wh_loss 3.8364 |off_loss 0.0586 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][297/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2917 |hm_loss 0.8509 |wh_loss 3.8236 |off_loss 0.0584 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][298/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2876 |hm_loss 0.8483 |wh_loss 3.8108 |off_loss 0.0582 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][299/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2835 |hm_loss 0.8456 |wh_loss 3.7981 |off_loss 0.0580 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][300/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2794 |hm_loss 0.8430 |wh_loss 3.7855 |off_loss 0.0578 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][301/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2753 |hm_loss 0.8404 |wh_loss 3.7729 |off_loss 0.0576 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][302/2110]|Tot: 0:00:06 |ETA: 0:00:00 |loss 1.2713 |hm_loss 0.8378 |wh_loss 3.7605 |off_loss 0.0575 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][303/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2673 |hm_loss 0.8352 |wh_loss 3.7481 |off_loss 0.0573 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][304/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2633 |hm_loss 0.8326 |wh_loss 3.7358 |off_loss 0.0571 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][305/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2593 |hm_loss 0.8301 |wh_loss 3.7236 |off_loss 0.0569 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][306/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2554 |hm_loss 0.8275 |wh_loss 3.7115 |off_loss 0.0567 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][307/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2515 |hm_loss 0.8250 |wh_loss 3.6994 |off_loss 0.0565 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][308/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2476 |hm_loss 0.8225 |wh_loss 3.6875 |off_loss 0.0563 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][309/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2438 |hm_loss 0.8200 |wh_loss 3.6756 |off_loss 0.0562 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][310/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2399 |hm_loss 0.8176 |wh_loss 3.6637 |off_loss 0.0560 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][311/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2361 |hm_loss 0.8151 |wh_loss 3.6520 |off_loss 0.0558 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][312/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2324 |hm_loss 0.8127 |wh_loss 3.6403 |off_loss 0.0556 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][313/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2286 |hm_loss 0.8103 |wh_loss 3.6287 |off_loss 0.0554 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][314/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2249 |hm_loss 0.8079 |wh_loss 3.6172 |off_loss 0.0553 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][315/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2212 |hm_loss 0.8055 |wh_loss 3.6058 |off_loss 0.0551 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][316/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2175 |hm_loss 0.8031 |wh_loss 3.5944 |off_loss 0.0549 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][317/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2138 |hm_loss 0.8008 |wh_loss 3.5831 |off_loss 0.0547 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][318/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2102 |hm_loss 0.7984 |wh_loss 3.5719 |off_loss 0.0546 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][319/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2066 |hm_loss 0.7961 |wh_loss 3.5607 |off_loss 0.0544 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][320/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2030 |hm_loss 0.7938 |wh_loss 3.5496 |off_loss 0.0542 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][321/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1994 |hm_loss 0.7915 |wh_loss 3.5386 |off_loss 0.0541 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][322/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1958 |hm_loss 0.7892 |wh_loss 3.5276 |off_loss 0.0539 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][323/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1923 |hm_loss 0.7869 |wh_loss 3.5167 |off_loss 0.0537 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][324/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1888 |hm_loss 0.7847 |wh_loss 3.5059 |off_loss 0.0536 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][325/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1853 |hm_loss 0.7824 |wh_loss 3.4952 |off_loss 0.0534 |Data 0.003s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][326/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1993 |hm_loss 0.7912 |wh_loss 3.5428 |off_loss 0.0539 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][327/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2144 |hm_loss 0.8006 |wh_loss 3.5947 |off_loss 0.0544 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][328/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2346 |hm_loss 0.8109 |wh_loss 3.6934 |off_loss 0.0544 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][329/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2310 |hm_loss 0.8086 |wh_loss 3.6822 |off_loss 0.0542 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][330/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2275 |hm_loss 0.8064 |wh_loss 3.6711 |off_loss 0.0540 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][331/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2240 |hm_loss 0.8041 |wh_loss 3.6600 |off_loss 0.0539 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][332/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2204 |hm_loss 0.8018 |wh_loss 3.6491 |off_loss 0.0537 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][333/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2170 |hm_loss 0.7996 |wh_loss 3.6381 |off_loss 0.0535 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][334/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2135 |hm_loss 0.7974 |wh_loss 3.6273 |off_loss 0.0534 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][335/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2100 |hm_loss 0.7952 |wh_loss 3.6165 |off_loss 0.0532 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][336/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2066 |hm_loss 0.7930 |wh_loss 3.6057 |off_loss 0.0531 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][337/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2032 |hm_loss 0.7908 |wh_loss 3.5951 |off_loss 0.0529 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][338/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1998 |hm_loss 0.7886 |wh_loss 3.5845 |off_loss 0.0528 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][339/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1964 |hm_loss 0.7864 |wh_loss 3.5739 |off_loss 0.0526 |Data 0.004s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][340/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1931 |hm_loss 0.7843 |wh_loss 3.5635 |off_loss 0.0524 |Data 0.002s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][341/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1898 |hm_loss 0.7822 |wh_loss 3.5530 |off_loss 0.0523 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][342/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1864 |hm_loss 0.7800 |wh_loss 3.5427 |off_loss 0.0521 |Data 0.007s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][343/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1831 |hm_loss 0.7779 |wh_loss 3.5324 |off_loss 0.0520 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][344/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1799 |hm_loss 0.7758 |wh_loss 3.5221 |off_loss 0.0518 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][345/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.1919 |hm_loss 0.7833 |wh_loss 3.5588 |off_loss 0.0527 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][346/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2075 |hm_loss 0.7934 |wh_loss 3.6115 |off_loss 0.0529 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][347/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2223 |hm_loss 0.8039 |wh_loss 3.6384 |off_loss 0.0546 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][348/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2401 |hm_loss 0.8144 |wh_loss 3.6972 |off_loss 0.0561 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][349/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2368 |hm_loss 0.8122 |wh_loss 3.6866 |off_loss 0.0559 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][350/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2334 |hm_loss 0.8100 |wh_loss 3.6761 |off_loss 0.0558 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][351/2110]|Tot: 0:00:07 |ETA: 0:00:00 |loss 1.2300 |hm_loss 0.8079 |wh_loss 3.6657 |off_loss 0.0556 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][352/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2267 |hm_loss 0.8057 |wh_loss 3.6553 |off_loss 0.0554 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][353/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2234 |hm_loss 0.8036 |wh_loss 3.6450 |off_loss 0.0553 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][354/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2201 |hm_loss 0.8015 |wh_loss 3.6347 |off_loss 0.0551 |Data 0.002s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][355/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2168 |hm_loss 0.7994 |wh_loss 3.6245 |off_loss 0.0550 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][356/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2136 |hm_loss 0.7973 |wh_loss 3.6143 |off_loss 0.0548 |Data 0.005s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][357/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2103 |hm_loss 0.7953 |wh_loss 3.6042 |off_loss 0.0547 |Data 0.002s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][358/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2071 |hm_loss 0.7932 |wh_loss 3.5942 |off_loss 0.0545 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][359/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2039 |hm_loss 0.7911 |wh_loss 3.5842 |off_loss 0.0544 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][360/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.2007 |hm_loss 0.7891 |wh_loss 3.5743 |off_loss 0.0542 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][361/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1976 |hm_loss 0.7871 |wh_loss 3.5644 |off_loss 0.0541 |Data 0.016s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][362/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1944 |hm_loss 0.7851 |wh_loss 3.5546 |off_loss 0.0539 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][363/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1913 |hm_loss 0.7830 |wh_loss 3.5448 |off_loss 0.0538 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][364/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1882 |hm_loss 0.7810 |wh_loss 3.5351 |off_loss 0.0536 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][365/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1851 |hm_loss 0.7791 |wh_loss 3.5254 |off_loss 0.0535 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][366/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1820 |hm_loss 0.7771 |wh_loss 3.5158 |off_loss 0.0533 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][367/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1789 |hm_loss 0.7751 |wh_loss 3.5063 |off_loss 0.0532 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][368/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1759 |hm_loss 0.7732 |wh_loss 3.4968 |off_loss 0.0530 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][369/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1728 |hm_loss 0.7712 |wh_loss 3.4873 |off_loss 0.0529 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][370/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1698 |hm_loss 0.7693 |wh_loss 3.4779 |off_loss 0.0527 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][371/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1668 |hm_loss 0.7673 |wh_loss 3.4686 |off_loss 0.0526 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][372/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1638 |hm_loss 0.7654 |wh_loss 3.4593 |off_loss 0.0525 |Data 0.000s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][373/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1608 |hm_loss 0.7635 |wh_loss 3.4500 |off_loss 0.0523 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][374/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1579 |hm_loss 0.7616 |wh_loss 3.4408 |off_loss 0.0522 |Data 0.001s(0.002s) |Net 0.023s
ctdet/coco_dla| val: [5][375/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1549 |hm_loss 0.7597 |wh_loss 3.4317 |off_loss 0.0520 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][376/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1520 |hm_loss 0.7579 |wh_loss 3.4226 |off_loss 0.0519 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][377/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1491 |hm_loss 0.7560 |wh_loss 3.4135 |off_loss 0.0518 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][378/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1462 |hm_loss 0.7541 |wh_loss 3.4045 |off_loss 0.0516 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][379/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1433 |hm_loss 0.7523 |wh_loss 3.3956 |off_loss 0.0515 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][380/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1405 |hm_loss 0.7505 |wh_loss 3.3866 |off_loss 0.0514 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][381/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1376 |hm_loss 0.7486 |wh_loss 3.3778 |off_loss 0.0512 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][382/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1348 |hm_loss 0.7468 |wh_loss 3.3690 |off_loss 0.0511 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][383/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1320 |hm_loss 0.7450 |wh_loss 3.3602 |off_loss 0.0510 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][384/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1292 |hm_loss 0.7432 |wh_loss 3.3515 |off_loss 0.0508 |Data 0.000s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][385/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1264 |hm_loss 0.7414 |wh_loss 3.3428 |off_loss 0.0507 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][386/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1236 |hm_loss 0.7396 |wh_loss 3.3341 |off_loss 0.0506 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][387/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1209 |hm_loss 0.7379 |wh_loss 3.3255 |off_loss 0.0504 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][388/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1181 |hm_loss 0.7361 |wh_loss 3.3170 |off_loss 0.0503 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][389/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1154 |hm_loss 0.7344 |wh_loss 3.3085 |off_loss 0.0502 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][390/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1127 |hm_loss 0.7326 |wh_loss 3.3000 |off_loss 0.0500 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][391/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1100 |hm_loss 0.7309 |wh_loss 3.2916 |off_loss 0.0499 |Data 0.001s(0.001s) |Net 0.023s
ctdet/coco_dla| val: [5][392/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1073 |hm_loss 0.7291 |wh_loss 3.2832 |off_loss 0.0498 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][393/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1046 |hm_loss 0.7274 |wh_loss 3.2749 |off_loss 0.0497 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][394/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.1019 |hm_loss 0.7257 |wh_loss 3.2666 |off_loss 0.0495 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][395/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.0993 |hm_loss 0.7240 |wh_loss 3.2584 |off_loss 0.0494 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][396/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.0966 |hm_loss 0.7223 |wh_loss 3.2502 |off_loss 0.0493 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][397/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.0940 |hm_loss 0.7207 |wh_loss 3.2420 |off_loss 0.0492 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][398/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.0914 |hm_loss 0.7190 |wh_loss 3.2339 |off_loss 0.0490 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][399/2110]|Tot: 0:00:08 |ETA: 0:00:00 |loss 1.0888 |hm_loss 0.7173 |wh_loss 3.2258 |off_loss 0.0489 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][400/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0862 |hm_loss 0.7156 |wh_loss 3.2177 |off_loss 0.0488 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][401/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0837 |hm_loss 0.7140 |wh_loss 3.2097 |off_loss 0.0487 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][402/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0811 |hm_loss 0.7124 |wh_loss 3.2018 |off_loss 0.0486 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][403/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0785 |hm_loss 0.7107 |wh_loss 3.1938 |off_loss 0.0484 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][404/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0760 |hm_loss 0.7091 |wh_loss 3.1860 |off_loss 0.0483 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][405/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0735 |hm_loss 0.7075 |wh_loss 3.1781 |off_loss 0.0482 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][406/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0710 |hm_loss 0.7059 |wh_loss 3.1703 |off_loss 0.0481 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][407/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0685 |hm_loss 0.7043 |wh_loss 3.1625 |off_loss 0.0480 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][408/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0660 |hm_loss 0.7027 |wh_loss 3.1548 |off_loss 0.0478 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][409/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0636 |hm_loss 0.7011 |wh_loss 3.1471 |off_loss 0.0477 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][410/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0611 |hm_loss 0.6996 |wh_loss 3.1394 |off_loss 0.0476 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][411/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0587 |hm_loss 0.6980 |wh_loss 3.1318 |off_loss 0.0475 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][412/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0563 |hm_loss 0.6964 |wh_loss 3.1242 |off_loss 0.0474 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][413/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0538 |hm_loss 0.6949 |wh_loss 3.1167 |off_loss 0.0473 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][414/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0514 |hm_loss 0.6934 |wh_loss 3.1092 |off_loss 0.0472 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][415/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0490 |hm_loss 0.6918 |wh_loss 3.1017 |off_loss 0.0470 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][416/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0467 |hm_loss 0.6903 |wh_loss 3.0943 |off_loss 0.0469 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][417/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0443 |hm_loss 0.6888 |wh_loss 3.0869 |off_loss 0.0468 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][418/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0419 |hm_loss 0.6873 |wh_loss 3.0795 |off_loss 0.0467 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][419/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0396 |hm_loss 0.6858 |wh_loss 3.0722 |off_loss 0.0466 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][420/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0372 |hm_loss 0.6843 |wh_loss 3.0649 |off_loss 0.0465 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][421/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0349 |hm_loss 0.6828 |wh_loss 3.0576 |off_loss 0.0464 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][422/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0326 |hm_loss 0.6813 |wh_loss 3.0504 |off_loss 0.0463 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][423/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0303 |hm_loss 0.6798 |wh_loss 3.0432 |off_loss 0.0462 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][424/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0280 |hm_loss 0.6783 |wh_loss 3.0360 |off_loss 0.0460 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][425/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0257 |hm_loss 0.6769 |wh_loss 3.0289 |off_loss 0.0459 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][426/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0234 |hm_loss 0.6754 |wh_loss 3.0218 |off_loss 0.0458 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][427/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0212 |hm_loss 0.6740 |wh_loss 3.0147 |off_loss 0.0457 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][428/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0189 |hm_loss 0.6725 |wh_loss 3.0077 |off_loss 0.0456 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][429/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0167 |hm_loss 0.6711 |wh_loss 3.0007 |off_loss 0.0455 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][430/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0145 |hm_loss 0.6697 |wh_loss 2.9938 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][431/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0122 |hm_loss 0.6682 |wh_loss 2.9868 |off_loss 0.0453 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][432/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0100 |hm_loss 0.6668 |wh_loss 2.9799 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][433/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0078 |hm_loss 0.6654 |wh_loss 2.9731 |off_loss 0.0451 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][434/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0056 |hm_loss 0.6640 |wh_loss 2.9662 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][435/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0174 |hm_loss 0.6713 |wh_loss 3.0026 |off_loss 0.0458 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][436/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0280 |hm_loss 0.6799 |wh_loss 3.0201 |off_loss 0.0462 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][437/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0425 |hm_loss 0.6885 |wh_loss 3.0671 |off_loss 0.0472 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][438/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0402 |hm_loss 0.6871 |wh_loss 3.0601 |off_loss 0.0471 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][439/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0380 |hm_loss 0.6857 |wh_loss 3.0532 |off_loss 0.0470 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][440/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0357 |hm_loss 0.6842 |wh_loss 3.0462 |off_loss 0.0469 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][441/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0335 |hm_loss 0.6828 |wh_loss 3.0393 |off_loss 0.0468 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][442/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0313 |hm_loss 0.6814 |wh_loss 3.0325 |off_loss 0.0467 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][443/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0291 |hm_loss 0.6800 |wh_loss 3.0256 |off_loss 0.0466 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][444/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0269 |hm_loss 0.6786 |wh_loss 3.0188 |off_loss 0.0465 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][445/2110]|Tot: 0:00:09 |ETA: 0:00:00 |loss 1.0247 |hm_loss 0.6772 |wh_loss 3.0121 |off_loss 0.0464 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][446/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0226 |hm_loss 0.6758 |wh_loss 3.0053 |off_loss 0.0463 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][447/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0204 |hm_loss 0.6744 |wh_loss 2.9986 |off_loss 0.0462 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][448/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0183 |hm_loss 0.6730 |wh_loss 2.9920 |off_loss 0.0461 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][449/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0161 |hm_loss 0.6716 |wh_loss 2.9853 |off_loss 0.0460 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][450/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0140 |hm_loss 0.6703 |wh_loss 2.9787 |off_loss 0.0459 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][451/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0119 |hm_loss 0.6689 |wh_loss 2.9721 |off_loss 0.0457 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][452/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0098 |hm_loss 0.6676 |wh_loss 2.9655 |off_loss 0.0456 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][453/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0077 |hm_loss 0.6662 |wh_loss 2.9590 |off_loss 0.0455 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][454/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0056 |hm_loss 0.6649 |wh_loss 2.9525 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][455/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0035 |hm_loss 0.6635 |wh_loss 2.9460 |off_loss 0.0453 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][456/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0014 |hm_loss 0.6622 |wh_loss 2.9396 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][457/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9993 |hm_loss 0.6609 |wh_loss 2.9332 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][458/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9973 |hm_loss 0.6595 |wh_loss 2.9268 |off_loss 0.0451 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][459/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9952 |hm_loss 0.6582 |wh_loss 2.9204 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][460/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9932 |hm_loss 0.6569 |wh_loss 2.9141 |off_loss 0.0449 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][461/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9911 |hm_loss 0.6556 |wh_loss 2.9078 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][462/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9891 |hm_loss 0.6543 |wh_loss 2.9015 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][463/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9871 |hm_loss 0.6530 |wh_loss 2.8952 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][464/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9851 |hm_loss 0.6517 |wh_loss 2.8890 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][465/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9831 |hm_loss 0.6504 |wh_loss 2.8828 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][466/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9811 |hm_loss 0.6491 |wh_loss 2.8766 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][467/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9791 |hm_loss 0.6479 |wh_loss 2.8705 |off_loss 0.0442 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][468/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9771 |hm_loss 0.6466 |wh_loss 2.8644 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][469/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9752 |hm_loss 0.6453 |wh_loss 2.8583 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][470/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9732 |hm_loss 0.6441 |wh_loss 2.8522 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][471/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9713 |hm_loss 0.6428 |wh_loss 2.8462 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][472/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9693 |hm_loss 0.6416 |wh_loss 2.8401 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][473/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9674 |hm_loss 0.6404 |wh_loss 2.8341 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][474/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9655 |hm_loss 0.6391 |wh_loss 2.8282 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][475/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9780 |hm_loss 0.6463 |wh_loss 2.8730 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][476/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9882 |hm_loss 0.6543 |wh_loss 2.8905 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][477/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0001 |hm_loss 0.6622 |wh_loss 2.9246 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][478/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0110 |hm_loss 0.6701 |wh_loss 2.9540 |off_loss 0.0455 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][479/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0090 |hm_loss 0.6689 |wh_loss 2.9479 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][480/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0070 |hm_loss 0.6676 |wh_loss 2.9418 |off_loss 0.0453 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][481/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0051 |hm_loss 0.6663 |wh_loss 2.9357 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][482/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0031 |hm_loss 0.6650 |wh_loss 2.9296 |off_loss 0.0451 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][483/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 1.0011 |hm_loss 0.6638 |wh_loss 2.9235 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][484/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9992 |hm_loss 0.6625 |wh_loss 2.9175 |off_loss 0.0449 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][485/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9972 |hm_loss 0.6613 |wh_loss 2.9115 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][486/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9953 |hm_loss 0.6600 |wh_loss 2.9055 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][487/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9934 |hm_loss 0.6588 |wh_loss 2.8996 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][488/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9915 |hm_loss 0.6575 |wh_loss 2.8936 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][489/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9895 |hm_loss 0.6563 |wh_loss 2.8877 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][490/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9876 |hm_loss 0.6551 |wh_loss 2.8818 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][491/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9857 |hm_loss 0.6539 |wh_loss 2.8760 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][492/2110]|Tot: 0:00:10 |ETA: 0:00:00 |loss 0.9839 |hm_loss 0.6527 |wh_loss 2.8702 |off_loss 0.0442 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][493/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9820 |hm_loss 0.6514 |wh_loss 2.8643 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][494/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9801 |hm_loss 0.6502 |wh_loss 2.8586 |off_loss 0.0440 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][495/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9782 |hm_loss 0.6490 |wh_loss 2.8528 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][496/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9764 |hm_loss 0.6478 |wh_loss 2.8471 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][497/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9745 |hm_loss 0.6466 |wh_loss 2.8413 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][498/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9727 |hm_loss 0.6455 |wh_loss 2.8356 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][499/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9708 |hm_loss 0.6443 |wh_loss 2.8300 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][500/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9690 |hm_loss 0.6431 |wh_loss 2.8243 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][501/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9672 |hm_loss 0.6419 |wh_loss 2.8187 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][502/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9654 |hm_loss 0.6408 |wh_loss 2.8131 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][503/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9636 |hm_loss 0.6396 |wh_loss 2.8075 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][504/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9618 |hm_loss 0.6384 |wh_loss 2.8020 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][505/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9600 |hm_loss 0.6373 |wh_loss 2.7964 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][506/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9582 |hm_loss 0.6361 |wh_loss 2.7909 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][507/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9564 |hm_loss 0.6350 |wh_loss 2.7854 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][508/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9546 |hm_loss 0.6338 |wh_loss 2.7799 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][509/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9529 |hm_loss 0.6327 |wh_loss 2.7745 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][510/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9511 |hm_loss 0.6316 |wh_loss 2.7691 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][511/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9493 |hm_loss 0.6304 |wh_loss 2.7636 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][512/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9476 |hm_loss 0.6293 |wh_loss 2.7583 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][513/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9459 |hm_loss 0.6282 |wh_loss 2.7529 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][514/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9441 |hm_loss 0.6271 |wh_loss 2.7475 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][515/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9424 |hm_loss 0.6260 |wh_loss 2.7422 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][516/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9407 |hm_loss 0.6249 |wh_loss 2.7369 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][517/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9390 |hm_loss 0.6238 |wh_loss 2.7316 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][518/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9373 |hm_loss 0.6227 |wh_loss 2.7264 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][519/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9356 |hm_loss 0.6216 |wh_loss 2.7211 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][520/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9339 |hm_loss 0.6205 |wh_loss 2.7159 |off_loss 0.0418 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][521/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9322 |hm_loss 0.6194 |wh_loss 2.7107 |off_loss 0.0417 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][522/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9305 |hm_loss 0.6183 |wh_loss 2.7055 |off_loss 0.0417 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][523/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9288 |hm_loss 0.6172 |wh_loss 2.7004 |off_loss 0.0416 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][524/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9272 |hm_loss 0.6161 |wh_loss 2.6952 |off_loss 0.0415 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][525/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9255 |hm_loss 0.6151 |wh_loss 2.6901 |off_loss 0.0414 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][526/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9238 |hm_loss 0.6140 |wh_loss 2.6850 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][527/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9222 |hm_loss 0.6130 |wh_loss 2.6799 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][528/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9206 |hm_loss 0.6119 |wh_loss 2.6748 |off_loss 0.0412 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][529/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9189 |hm_loss 0.6108 |wh_loss 2.6698 |off_loss 0.0411 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][530/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9173 |hm_loss 0.6098 |wh_loss 2.6648 |off_loss 0.0410 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][531/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9157 |hm_loss 0.6087 |wh_loss 2.6598 |off_loss 0.0409 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][532/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9140 |hm_loss 0.6077 |wh_loss 2.6548 |off_loss 0.0409 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][533/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9124 |hm_loss 0.6067 |wh_loss 2.6498 |off_loss 0.0408 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][534/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9108 |hm_loss 0.6056 |wh_loss 2.6448 |off_loss 0.0407 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][535/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9092 |hm_loss 0.6046 |wh_loss 2.6399 |off_loss 0.0406 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][536/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9076 |hm_loss 0.6036 |wh_loss 2.6350 |off_loss 0.0406 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][537/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9060 |hm_loss 0.6025 |wh_loss 2.6301 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][538/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9045 |hm_loss 0.6015 |wh_loss 2.6252 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][539/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9029 |hm_loss 0.6005 |wh_loss 2.6203 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][540/2110]|Tot: 0:00:11 |ETA: 0:00:00 |loss 0.9013 |hm_loss 0.5995 |wh_loss 2.6155 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][541/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8998 |hm_loss 0.5985 |wh_loss 2.6107 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][542/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8983 |hm_loss 0.5976 |wh_loss 2.6059 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][543/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8967 |hm_loss 0.5966 |wh_loss 2.6011 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][544/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8952 |hm_loss 0.5956 |wh_loss 2.5963 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][545/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8937 |hm_loss 0.5947 |wh_loss 2.5916 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][546/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8922 |hm_loss 0.5937 |wh_loss 2.5868 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][547/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8907 |hm_loss 0.5928 |wh_loss 2.5821 |off_loss 0.0398 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][548/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8892 |hm_loss 0.5918 |wh_loss 2.5774 |off_loss 0.0397 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][549/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8878 |hm_loss 0.5909 |wh_loss 2.5727 |off_loss 0.0396 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][550/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8863 |hm_loss 0.5899 |wh_loss 2.5680 |off_loss 0.0395 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][551/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8848 |hm_loss 0.5890 |wh_loss 2.5634 |off_loss 0.0395 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][552/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8833 |hm_loss 0.5880 |wh_loss 2.5587 |off_loss 0.0394 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][553/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8818 |hm_loss 0.5871 |wh_loss 2.5541 |off_loss 0.0393 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][554/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8803 |hm_loss 0.5861 |wh_loss 2.5495 |off_loss 0.0392 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][555/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8788 |hm_loss 0.5851 |wh_loss 2.5449 |off_loss 0.0392 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][556/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8773 |hm_loss 0.5842 |wh_loss 2.5404 |off_loss 0.0391 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][557/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8758 |hm_loss 0.5832 |wh_loss 2.5358 |off_loss 0.0390 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][558/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8744 |hm_loss 0.5823 |wh_loss 2.5313 |off_loss 0.0390 |Data 0.007s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][559/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8729 |hm_loss 0.5813 |wh_loss 2.5268 |off_loss 0.0389 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][560/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8714 |hm_loss 0.5804 |wh_loss 2.5223 |off_loss 0.0388 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][561/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8700 |hm_loss 0.5794 |wh_loss 2.5178 |off_loss 0.0388 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][562/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8685 |hm_loss 0.5785 |wh_loss 2.5133 |off_loss 0.0387 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][563/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8671 |hm_loss 0.5776 |wh_loss 2.5088 |off_loss 0.0386 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][564/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8656 |hm_loss 0.5766 |wh_loss 2.5044 |off_loss 0.0386 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][565/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8642 |hm_loss 0.5757 |wh_loss 2.5000 |off_loss 0.0385 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][566/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8627 |hm_loss 0.5748 |wh_loss 2.4956 |off_loss 0.0384 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][567/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8613 |hm_loss 0.5738 |wh_loss 2.4912 |off_loss 0.0384 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][568/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8599 |hm_loss 0.5729 |wh_loss 2.4868 |off_loss 0.0383 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][569/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8585 |hm_loss 0.5720 |wh_loss 2.4824 |off_loss 0.0382 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][570/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8571 |hm_loss 0.5711 |wh_loss 2.4781 |off_loss 0.0381 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][571/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8557 |hm_loss 0.5702 |wh_loss 2.4738 |off_loss 0.0381 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][572/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8543 |hm_loss 0.5693 |wh_loss 2.4694 |off_loss 0.0380 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][573/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8529 |hm_loss 0.5684 |wh_loss 2.4651 |off_loss 0.0379 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][574/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8515 |hm_loss 0.5675 |wh_loss 2.4608 |off_loss 0.0379 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][575/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8501 |hm_loss 0.5666 |wh_loss 2.4566 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][576/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8487 |hm_loss 0.5657 |wh_loss 2.4523 |off_loss 0.0378 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][577/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8473 |hm_loss 0.5648 |wh_loss 2.4481 |off_loss 0.0377 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][578/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8460 |hm_loss 0.5640 |wh_loss 2.4438 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][579/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8446 |hm_loss 0.5631 |wh_loss 2.4396 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][580/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8432 |hm_loss 0.5622 |wh_loss 2.4354 |off_loss 0.0375 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][581/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8419 |hm_loss 0.5613 |wh_loss 2.4312 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][582/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8405 |hm_loss 0.5605 |wh_loss 2.4271 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][583/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8392 |hm_loss 0.5596 |wh_loss 2.4229 |off_loss 0.0373 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][584/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8378 |hm_loss 0.5587 |wh_loss 2.4188 |off_loss 0.0372 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][585/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8365 |hm_loss 0.5579 |wh_loss 2.4147 |off_loss 0.0372 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][586/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8352 |hm_loss 0.5570 |wh_loss 2.4105 |off_loss 0.0371 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][587/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8338 |hm_loss 0.5561 |wh_loss 2.4064 |off_loss 0.0370 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][588/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8325 |hm_loss 0.5553 |wh_loss 2.4024 |off_loss 0.0370 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][589/2110]|Tot: 0:00:12 |ETA: 0:00:00 |loss 0.8312 |hm_loss 0.5544 |wh_loss 2.3983 |off_loss 0.0369 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][590/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8299 |hm_loss 0.5536 |wh_loss 2.3942 |off_loss 0.0369 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][591/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8286 |hm_loss 0.5527 |wh_loss 2.3902 |off_loss 0.0368 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][592/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8273 |hm_loss 0.5519 |wh_loss 2.3862 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][593/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8260 |hm_loss 0.5511 |wh_loss 2.3821 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][594/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8247 |hm_loss 0.5502 |wh_loss 2.3781 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][595/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8234 |hm_loss 0.5494 |wh_loss 2.3741 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][596/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8221 |hm_loss 0.5486 |wh_loss 2.3702 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][597/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8208 |hm_loss 0.5477 |wh_loss 2.3662 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][598/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8195 |hm_loss 0.5469 |wh_loss 2.3622 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][599/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8182 |hm_loss 0.5461 |wh_loss 2.3583 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][600/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8267 |hm_loss 0.5511 |wh_loss 2.3884 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][601/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8353 |hm_loss 0.5565 |wh_loss 2.4203 |off_loss 0.0368 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][602/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8341 |hm_loss 0.5557 |wh_loss 2.4163 |off_loss 0.0367 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][603/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8328 |hm_loss 0.5548 |wh_loss 2.4123 |off_loss 0.0367 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][604/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8315 |hm_loss 0.5540 |wh_loss 2.4083 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][605/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8302 |hm_loss 0.5532 |wh_loss 2.4043 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][606/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8289 |hm_loss 0.5524 |wh_loss 2.4004 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][607/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8276 |hm_loss 0.5516 |wh_loss 2.3964 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][608/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8264 |hm_loss 0.5507 |wh_loss 2.3925 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][609/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8251 |hm_loss 0.5499 |wh_loss 2.3886 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][610/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8238 |hm_loss 0.5491 |wh_loss 2.3846 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][611/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8226 |hm_loss 0.5483 |wh_loss 2.3807 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][612/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8326 |hm_loss 0.5546 |wh_loss 2.4164 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][613/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8407 |hm_loss 0.5596 |wh_loss 2.4460 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][614/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8490 |hm_loss 0.5649 |wh_loss 2.4704 |off_loss 0.0371 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][615/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8571 |hm_loss 0.5704 |wh_loss 2.4898 |off_loss 0.0377 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][616/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8649 |hm_loss 0.5762 |wh_loss 2.5060 |off_loss 0.0380 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][617/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8721 |hm_loss 0.5821 |wh_loss 2.5175 |off_loss 0.0382 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][618/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8794 |hm_loss 0.5881 |wh_loss 2.5236 |off_loss 0.0389 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][619/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8857 |hm_loss 0.5940 |wh_loss 2.5253 |off_loss 0.0391 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][620/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.8927 |hm_loss 0.5999 |wh_loss 2.5342 |off_loss 0.0393 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][621/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9009 |hm_loss 0.6058 |wh_loss 2.5527 |off_loss 0.0398 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][622/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9098 |hm_loss 0.6118 |wh_loss 2.5740 |off_loss 0.0406 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][623/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9193 |hm_loss 0.6178 |wh_loss 2.6009 |off_loss 0.0415 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][624/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9283 |hm_loss 0.6237 |wh_loss 2.6243 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][625/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9366 |hm_loss 0.6295 |wh_loss 2.6453 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][626/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9352 |hm_loss 0.6286 |wh_loss 2.6411 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][627/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9338 |hm_loss 0.6277 |wh_loss 2.6369 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][628/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9324 |hm_loss 0.6268 |wh_loss 2.6327 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][629/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9310 |hm_loss 0.6259 |wh_loss 2.6285 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][630/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9296 |hm_loss 0.6249 |wh_loss 2.6243 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][631/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9283 |hm_loss 0.6240 |wh_loss 2.6202 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][632/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9269 |hm_loss 0.6231 |wh_loss 2.6161 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][633/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9348 |hm_loss 0.6278 |wh_loss 2.6454 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][634/2110]|Tot: 0:00:13 |ETA: 0:00:00 |loss 0.9424 |hm_loss 0.6325 |wh_loss 2.6710 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][635/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9496 |hm_loss 0.6375 |wh_loss 2.6907 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][636/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9572 |hm_loss 0.6428 |wh_loss 2.7123 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][637/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9655 |hm_loss 0.6486 |wh_loss 2.7360 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][638/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9734 |hm_loss 0.6544 |wh_loss 2.7510 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][639/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9805 |hm_loss 0.6602 |wh_loss 2.7583 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][640/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9887 |hm_loss 0.6660 |wh_loss 2.7791 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][641/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 0.9978 |hm_loss 0.6719 |wh_loss 2.8056 |off_loss 0.0453 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][642/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0070 |hm_loss 0.6777 |wh_loss 2.8301 |off_loss 0.0463 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][643/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0160 |hm_loss 0.6835 |wh_loss 2.8544 |off_loss 0.0471 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][644/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0244 |hm_loss 0.6893 |wh_loss 2.8740 |off_loss 0.0477 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][645/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0229 |hm_loss 0.6883 |wh_loss 2.8695 |off_loss 0.0476 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][646/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0214 |hm_loss 0.6873 |wh_loss 2.8651 |off_loss 0.0475 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][647/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0199 |hm_loss 0.6864 |wh_loss 2.8607 |off_loss 0.0475 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][648/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0184 |hm_loss 0.6854 |wh_loss 2.8563 |off_loss 0.0474 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][649/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0169 |hm_loss 0.6844 |wh_loss 2.8519 |off_loss 0.0473 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][650/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0155 |hm_loss 0.6835 |wh_loss 2.8475 |off_loss 0.0472 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][651/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0235 |hm_loss 0.6882 |wh_loss 2.8773 |off_loss 0.0476 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][652/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0307 |hm_loss 0.6930 |wh_loss 2.9004 |off_loss 0.0477 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][653/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0379 |hm_loss 0.6980 |wh_loss 2.9164 |off_loss 0.0483 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][654/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0443 |hm_loss 0.7032 |wh_loss 2.9274 |off_loss 0.0483 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][655/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0510 |hm_loss 0.7086 |wh_loss 2.9342 |off_loss 0.0489 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][656/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0567 |hm_loss 0.7141 |wh_loss 2.9344 |off_loss 0.0492 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][657/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0634 |hm_loss 0.7196 |wh_loss 2.9397 |off_loss 0.0499 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][658/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0704 |hm_loss 0.7250 |wh_loss 2.9528 |off_loss 0.0501 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][659/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0779 |hm_loss 0.7306 |wh_loss 2.9686 |off_loss 0.0505 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][660/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0856 |hm_loss 0.7362 |wh_loss 2.9844 |off_loss 0.0510 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][661/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0932 |hm_loss 0.7417 |wh_loss 3.0002 |off_loss 0.0515 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][662/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0917 |hm_loss 0.7407 |wh_loss 2.9957 |off_loss 0.0514 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][663/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0901 |hm_loss 0.7396 |wh_loss 2.9911 |off_loss 0.0514 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][664/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0886 |hm_loss 0.7386 |wh_loss 2.9867 |off_loss 0.0513 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][665/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0870 |hm_loss 0.7376 |wh_loss 2.9822 |off_loss 0.0512 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][666/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0855 |hm_loss 0.7366 |wh_loss 2.9777 |off_loss 0.0511 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][667/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0839 |hm_loss 0.7355 |wh_loss 2.9732 |off_loss 0.0511 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][668/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0824 |hm_loss 0.7345 |wh_loss 2.9688 |off_loss 0.0510 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][669/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0808 |hm_loss 0.7335 |wh_loss 2.9644 |off_loss 0.0509 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][670/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0793 |hm_loss 0.7325 |wh_loss 2.9599 |off_loss 0.0508 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][671/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0778 |hm_loss 0.7315 |wh_loss 2.9555 |off_loss 0.0508 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][672/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0763 |hm_loss 0.7305 |wh_loss 2.9511 |off_loss 0.0507 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][673/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0747 |hm_loss 0.7295 |wh_loss 2.9468 |off_loss 0.0506 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][674/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0732 |hm_loss 0.7285 |wh_loss 2.9424 |off_loss 0.0505 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][675/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0717 |hm_loss 0.7275 |wh_loss 2.9381 |off_loss 0.0505 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][676/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0702 |hm_loss 0.7265 |wh_loss 2.9337 |off_loss 0.0504 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][677/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0687 |hm_loss 0.7255 |wh_loss 2.9294 |off_loss 0.0503 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][678/2110]|Tot: 0:00:14 |ETA: 0:00:00 |loss 1.0672 |hm_loss 0.7245 |wh_loss 2.9251 |off_loss 0.0502 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][679/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0657 |hm_loss 0.7235 |wh_loss 2.9208 |off_loss 0.0502 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][680/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0642 |hm_loss 0.7225 |wh_loss 2.9165 |off_loss 0.0501 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][681/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0627 |hm_loss 0.7215 |wh_loss 2.9122 |off_loss 0.0500 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][682/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0613 |hm_loss 0.7205 |wh_loss 2.9079 |off_loss 0.0499 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][683/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0598 |hm_loss 0.7196 |wh_loss 2.9037 |off_loss 0.0499 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][684/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0583 |hm_loss 0.7186 |wh_loss 2.8994 |off_loss 0.0498 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][685/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0569 |hm_loss 0.7176 |wh_loss 2.8952 |off_loss 0.0497 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][686/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0554 |hm_loss 0.7167 |wh_loss 2.8910 |off_loss 0.0496 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][687/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0540 |hm_loss 0.7157 |wh_loss 2.8868 |off_loss 0.0496 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][688/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0525 |hm_loss 0.7148 |wh_loss 2.8826 |off_loss 0.0495 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][689/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0511 |hm_loss 0.7138 |wh_loss 2.8784 |off_loss 0.0494 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][690/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0496 |hm_loss 0.7129 |wh_loss 2.8743 |off_loss 0.0494 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][691/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0482 |hm_loss 0.7119 |wh_loss 2.8701 |off_loss 0.0493 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][692/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0468 |hm_loss 0.7110 |wh_loss 2.8660 |off_loss 0.0492 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][693/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0453 |hm_loss 0.7100 |wh_loss 2.8618 |off_loss 0.0491 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][694/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0439 |hm_loss 0.7091 |wh_loss 2.8577 |off_loss 0.0491 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][695/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0425 |hm_loss 0.7081 |wh_loss 2.8536 |off_loss 0.0490 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][696/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0411 |hm_loss 0.7072 |wh_loss 2.8495 |off_loss 0.0489 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][697/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0397 |hm_loss 0.7062 |wh_loss 2.8454 |off_loss 0.0489 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][698/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0382 |hm_loss 0.7053 |wh_loss 2.8414 |off_loss 0.0488 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][699/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0368 |hm_loss 0.7044 |wh_loss 2.8373 |off_loss 0.0487 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][700/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0354 |hm_loss 0.7035 |wh_loss 2.8333 |off_loss 0.0487 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][701/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0340 |hm_loss 0.7025 |wh_loss 2.8292 |off_loss 0.0486 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][702/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0327 |hm_loss 0.7016 |wh_loss 2.8252 |off_loss 0.0485 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][703/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0313 |hm_loss 0.7007 |wh_loss 2.8212 |off_loss 0.0484 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][704/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0299 |hm_loss 0.6998 |wh_loss 2.8172 |off_loss 0.0484 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][705/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0285 |hm_loss 0.6989 |wh_loss 2.8132 |off_loss 0.0483 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][706/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0271 |hm_loss 0.6980 |wh_loss 2.8092 |off_loss 0.0482 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][707/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0257 |hm_loss 0.6970 |wh_loss 2.8053 |off_loss 0.0482 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][708/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0244 |hm_loss 0.6961 |wh_loss 2.8013 |off_loss 0.0481 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][709/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0230 |hm_loss 0.6952 |wh_loss 2.7974 |off_loss 0.0480 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][710/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0216 |hm_loss 0.6943 |wh_loss 2.7934 |off_loss 0.0480 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][711/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0203 |hm_loss 0.6934 |wh_loss 2.7895 |off_loss 0.0479 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][712/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0189 |hm_loss 0.6925 |wh_loss 2.7856 |off_loss 0.0478 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][713/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0176 |hm_loss 0.6916 |wh_loss 2.7817 |off_loss 0.0478 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][714/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0162 |hm_loss 0.6907 |wh_loss 2.7778 |off_loss 0.0477 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][715/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0149 |hm_loss 0.6898 |wh_loss 2.7739 |off_loss 0.0476 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][716/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0135 |hm_loss 0.6890 |wh_loss 2.7700 |off_loss 0.0476 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][717/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0122 |hm_loss 0.6881 |wh_loss 2.7662 |off_loss 0.0475 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][718/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0109 |hm_loss 0.6872 |wh_loss 2.7623 |off_loss 0.0474 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][719/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0095 |hm_loss 0.6863 |wh_loss 2.7585 |off_loss 0.0474 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][720/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0082 |hm_loss 0.6854 |wh_loss 2.7547 |off_loss 0.0473 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][721/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0069 |hm_loss 0.6846 |wh_loss 2.7509 |off_loss 0.0472 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][722/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0056 |hm_loss 0.6837 |wh_loss 2.7471 |off_loss 0.0472 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][723/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0043 |hm_loss 0.6828 |wh_loss 2.7433 |off_loss 0.0471 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][724/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0029 |hm_loss 0.6820 |wh_loss 2.7395 |off_loss 0.0470 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][725/2110]|Tot: 0:00:15 |ETA: 0:00:00 |loss 1.0016 |hm_loss 0.6811 |wh_loss 2.7357 |off_loss 0.0470 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][726/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 1.0003 |hm_loss 0.6802 |wh_loss 2.7319 |off_loss 0.0469 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][727/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9990 |hm_loss 0.6794 |wh_loss 2.7282 |off_loss 0.0468 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][728/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9977 |hm_loss 0.6785 |wh_loss 2.7244 |off_loss 0.0468 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][729/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9964 |hm_loss 0.6777 |wh_loss 2.7207 |off_loss 0.0467 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][730/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9952 |hm_loss 0.6768 |wh_loss 2.7170 |off_loss 0.0467 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][731/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9939 |hm_loss 0.6759 |wh_loss 2.7133 |off_loss 0.0466 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][732/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9926 |hm_loss 0.6751 |wh_loss 2.7096 |off_loss 0.0465 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][733/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9913 |hm_loss 0.6743 |wh_loss 2.7059 |off_loss 0.0465 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][734/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9900 |hm_loss 0.6734 |wh_loss 2.7022 |off_loss 0.0464 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][735/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9888 |hm_loss 0.6726 |wh_loss 2.6985 |off_loss 0.0463 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][736/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9875 |hm_loss 0.6717 |wh_loss 2.6949 |off_loss 0.0463 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][737/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9862 |hm_loss 0.6709 |wh_loss 2.6912 |off_loss 0.0462 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][738/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9850 |hm_loss 0.6701 |wh_loss 2.6876 |off_loss 0.0462 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][739/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9837 |hm_loss 0.6692 |wh_loss 2.6839 |off_loss 0.0461 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][740/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9825 |hm_loss 0.6684 |wh_loss 2.6803 |off_loss 0.0460 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][741/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9812 |hm_loss 0.6676 |wh_loss 2.6767 |off_loss 0.0460 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][742/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9799 |hm_loss 0.6667 |wh_loss 2.6731 |off_loss 0.0459 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][743/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9787 |hm_loss 0.6659 |wh_loss 2.6695 |off_loss 0.0458 |Data 0.008s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][744/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9775 |hm_loss 0.6651 |wh_loss 2.6659 |off_loss 0.0458 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][745/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9762 |hm_loss 0.6643 |wh_loss 2.6624 |off_loss 0.0457 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][746/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9750 |hm_loss 0.6634 |wh_loss 2.6588 |off_loss 0.0457 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][747/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9737 |hm_loss 0.6626 |wh_loss 2.6552 |off_loss 0.0456 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][748/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9725 |hm_loss 0.6618 |wh_loss 2.6517 |off_loss 0.0455 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][749/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9713 |hm_loss 0.6610 |wh_loss 2.6482 |off_loss 0.0455 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][750/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9701 |hm_loss 0.6602 |wh_loss 2.6446 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][751/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9689 |hm_loss 0.6594 |wh_loss 2.6411 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][752/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9676 |hm_loss 0.6586 |wh_loss 2.6376 |off_loss 0.0453 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][753/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9664 |hm_loss 0.6578 |wh_loss 2.6341 |off_loss 0.0452 |Data 0.015s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][754/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9652 |hm_loss 0.6570 |wh_loss 2.6306 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][755/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9640 |hm_loss 0.6562 |wh_loss 2.6271 |off_loss 0.0451 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][756/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9628 |hm_loss 0.6554 |wh_loss 2.6237 |off_loss 0.0451 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][757/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9616 |hm_loss 0.6546 |wh_loss 2.6202 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][758/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9604 |hm_loss 0.6538 |wh_loss 2.6168 |off_loss 0.0449 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][759/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9592 |hm_loss 0.6530 |wh_loss 2.6133 |off_loss 0.0449 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][760/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9580 |hm_loss 0.6522 |wh_loss 2.6099 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][761/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9568 |hm_loss 0.6514 |wh_loss 2.6065 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][762/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9557 |hm_loss 0.6507 |wh_loss 2.6030 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][763/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9545 |hm_loss 0.6499 |wh_loss 2.5996 |off_loss 0.0446 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][764/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9533 |hm_loss 0.6491 |wh_loss 2.5962 |off_loss 0.0446 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][765/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9521 |hm_loss 0.6483 |wh_loss 2.5928 |off_loss 0.0445 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][766/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9509 |hm_loss 0.6475 |wh_loss 2.5895 |off_loss 0.0445 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][767/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9498 |hm_loss 0.6468 |wh_loss 2.5861 |off_loss 0.0444 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][768/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9486 |hm_loss 0.6460 |wh_loss 2.5827 |off_loss 0.0444 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][769/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9474 |hm_loss 0.6452 |wh_loss 2.5794 |off_loss 0.0443 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][770/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9463 |hm_loss 0.6444 |wh_loss 2.5760 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][771/2110]|Tot: 0:00:16 |ETA: 0:00:00 |loss 0.9451 |hm_loss 0.6437 |wh_loss 2.5727 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][772/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9440 |hm_loss 0.6429 |wh_loss 2.5694 |off_loss 0.0441 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][773/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9428 |hm_loss 0.6422 |wh_loss 2.5660 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][774/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9417 |hm_loss 0.6414 |wh_loss 2.5627 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][775/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9405 |hm_loss 0.6406 |wh_loss 2.5594 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][776/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9394 |hm_loss 0.6399 |wh_loss 2.5561 |off_loss 0.0439 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][777/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9383 |hm_loss 0.6391 |wh_loss 2.5529 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][778/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9371 |hm_loss 0.6384 |wh_loss 2.5496 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][779/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9360 |hm_loss 0.6376 |wh_loss 2.5463 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][780/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9348 |hm_loss 0.6369 |wh_loss 2.5431 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][781/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9337 |hm_loss 0.6361 |wh_loss 2.5398 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][782/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9326 |hm_loss 0.6354 |wh_loss 2.5366 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][783/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9315 |hm_loss 0.6346 |wh_loss 2.5333 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][784/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9303 |hm_loss 0.6339 |wh_loss 2.5301 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][785/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9292 |hm_loss 0.6332 |wh_loss 2.5269 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][786/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9281 |hm_loss 0.6324 |wh_loss 2.5237 |off_loss 0.0433 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][787/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9270 |hm_loss 0.6317 |wh_loss 2.5205 |off_loss 0.0433 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][788/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9259 |hm_loss 0.6309 |wh_loss 2.5173 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][789/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9248 |hm_loss 0.6302 |wh_loss 2.5141 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][790/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9237 |hm_loss 0.6295 |wh_loss 2.5109 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][791/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9226 |hm_loss 0.6288 |wh_loss 2.5077 |off_loss 0.0431 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][792/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9215 |hm_loss 0.6280 |wh_loss 2.5046 |off_loss 0.0430 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][793/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9204 |hm_loss 0.6273 |wh_loss 2.5014 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][794/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9193 |hm_loss 0.6266 |wh_loss 2.4983 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][795/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9182 |hm_loss 0.6259 |wh_loss 2.4951 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][796/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9171 |hm_loss 0.6251 |wh_loss 2.4920 |off_loss 0.0428 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][797/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9161 |hm_loss 0.6244 |wh_loss 2.4889 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][798/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9150 |hm_loss 0.6237 |wh_loss 2.4858 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][799/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9139 |hm_loss 0.6230 |wh_loss 2.4827 |off_loss 0.0426 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][800/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9128 |hm_loss 0.6223 |wh_loss 2.4796 |off_loss 0.0426 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][801/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9192 |hm_loss 0.6261 |wh_loss 2.5027 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][802/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9251 |hm_loss 0.6299 |wh_loss 2.5222 |off_loss 0.0429 |Data 0.008s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][803/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9309 |hm_loss 0.6340 |wh_loss 2.5353 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][804/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9373 |hm_loss 0.6383 |wh_loss 2.5491 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][805/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9429 |hm_loss 0.6428 |wh_loss 2.5587 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][806/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9475 |hm_loss 0.6473 |wh_loss 2.5600 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][807/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9529 |hm_loss 0.6518 |wh_loss 2.5640 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][808/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9591 |hm_loss 0.6563 |wh_loss 2.5780 |off_loss 0.0451 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][809/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9656 |hm_loss 0.6608 |wh_loss 2.5968 |off_loss 0.0452 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][810/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9731 |hm_loss 0.6654 |wh_loss 2.6207 |off_loss 0.0457 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][811/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9796 |hm_loss 0.6699 |wh_loss 2.6381 |off_loss 0.0459 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][812/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9784 |hm_loss 0.6691 |wh_loss 2.6349 |off_loss 0.0458 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][813/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9773 |hm_loss 0.6684 |wh_loss 2.6316 |off_loss 0.0458 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][814/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9761 |hm_loss 0.6676 |wh_loss 2.6284 |off_loss 0.0457 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][815/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9750 |hm_loss 0.6668 |wh_loss 2.6252 |off_loss 0.0457 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][816/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9739 |hm_loss 0.6661 |wh_loss 2.6220 |off_loss 0.0456 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][817/2110]|Tot: 0:00:17 |ETA: 0:00:00 |loss 0.9728 |hm_loss 0.6653 |wh_loss 2.6188 |off_loss 0.0455 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][818/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9716 |hm_loss 0.6646 |wh_loss 2.6156 |off_loss 0.0455 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][819/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9705 |hm_loss 0.6638 |wh_loss 2.6124 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][820/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9694 |hm_loss 0.6631 |wh_loss 2.6092 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][821/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9683 |hm_loss 0.6623 |wh_loss 2.6060 |off_loss 0.0453 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][822/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9672 |hm_loss 0.6616 |wh_loss 2.6029 |off_loss 0.0453 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][823/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9660 |hm_loss 0.6609 |wh_loss 2.5997 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][824/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9649 |hm_loss 0.6601 |wh_loss 2.5966 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][825/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9638 |hm_loss 0.6594 |wh_loss 2.5934 |off_loss 0.0451 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][826/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9627 |hm_loss 0.6587 |wh_loss 2.5903 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][827/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9616 |hm_loss 0.6579 |wh_loss 2.5871 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][828/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9605 |hm_loss 0.6572 |wh_loss 2.5840 |off_loss 0.0449 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][829/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9594 |hm_loss 0.6565 |wh_loss 2.5809 |off_loss 0.0449 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][830/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9583 |hm_loss 0.6557 |wh_loss 2.5778 |off_loss 0.0448 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][831/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9572 |hm_loss 0.6550 |wh_loss 2.5747 |off_loss 0.0448 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][832/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9562 |hm_loss 0.6543 |wh_loss 2.5716 |off_loss 0.0447 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][833/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9551 |hm_loss 0.6536 |wh_loss 2.5685 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][834/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9540 |hm_loss 0.6528 |wh_loss 2.5655 |off_loss 0.0446 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][835/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9529 |hm_loss 0.6521 |wh_loss 2.5624 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][836/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9518 |hm_loss 0.6514 |wh_loss 2.5593 |off_loss 0.0445 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][837/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9508 |hm_loss 0.6507 |wh_loss 2.5563 |off_loss 0.0445 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][838/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9497 |hm_loss 0.6500 |wh_loss 2.5532 |off_loss 0.0444 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][839/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9486 |hm_loss 0.6493 |wh_loss 2.5502 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][840/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9476 |hm_loss 0.6485 |wh_loss 2.5472 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][841/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9465 |hm_loss 0.6478 |wh_loss 2.5441 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][842/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9454 |hm_loss 0.6471 |wh_loss 2.5411 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][843/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9444 |hm_loss 0.6464 |wh_loss 2.5381 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][844/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9433 |hm_loss 0.6457 |wh_loss 2.5351 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][845/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9423 |hm_loss 0.6450 |wh_loss 2.5321 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][846/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9412 |hm_loss 0.6443 |wh_loss 2.5291 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][847/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9402 |hm_loss 0.6436 |wh_loss 2.5261 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][848/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9391 |hm_loss 0.6429 |wh_loss 2.5232 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][849/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9381 |hm_loss 0.6422 |wh_loss 2.5202 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][850/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9370 |hm_loss 0.6415 |wh_loss 2.5172 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][851/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9360 |hm_loss 0.6408 |wh_loss 2.5143 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][852/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9350 |hm_loss 0.6402 |wh_loss 2.5113 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][853/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9339 |hm_loss 0.6395 |wh_loss 2.5084 |off_loss 0.0436 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][854/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9329 |hm_loss 0.6388 |wh_loss 2.5054 |off_loss 0.0436 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][855/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9319 |hm_loss 0.6381 |wh_loss 2.5025 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][856/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9308 |hm_loss 0.6374 |wh_loss 2.4996 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][857/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9298 |hm_loss 0.6367 |wh_loss 2.4967 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][858/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9288 |hm_loss 0.6361 |wh_loss 2.4938 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][859/2110]|Tot: 0:00:18 |ETA: 0:00:00 |loss 0.9278 |hm_loss 0.6354 |wh_loss 2.4909 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][860/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9268 |hm_loss 0.6347 |wh_loss 2.4880 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][861/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9257 |hm_loss 0.6340 |wh_loss 2.4851 |off_loss 0.0432 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][862/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9247 |hm_loss 0.6334 |wh_loss 2.4822 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][863/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9237 |hm_loss 0.6327 |wh_loss 2.4793 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][864/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9227 |hm_loss 0.6320 |wh_loss 2.4765 |off_loss 0.0431 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][865/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9217 |hm_loss 0.6313 |wh_loss 2.4736 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][866/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9301 |hm_loss 0.6354 |wh_loss 2.5145 |off_loss 0.0432 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][867/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9380 |hm_loss 0.6395 |wh_loss 2.5477 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][868/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9446 |hm_loss 0.6435 |wh_loss 2.5699 |off_loss 0.0440 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][869/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9503 |hm_loss 0.6477 |wh_loss 2.5847 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][870/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9565 |hm_loss 0.6519 |wh_loss 2.6014 |off_loss 0.0445 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][871/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9637 |hm_loss 0.6559 |wh_loss 2.6295 |off_loss 0.0448 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][872/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9709 |hm_loss 0.6598 |wh_loss 2.6583 |off_loss 0.0452 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][873/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9770 |hm_loss 0.6634 |wh_loss 2.6807 |off_loss 0.0456 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][874/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9759 |hm_loss 0.6627 |wh_loss 2.6777 |off_loss 0.0455 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][875/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9749 |hm_loss 0.6620 |wh_loss 2.6746 |off_loss 0.0454 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][876/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9738 |hm_loss 0.6613 |wh_loss 2.6716 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][877/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9728 |hm_loss 0.6606 |wh_loss 2.6685 |off_loss 0.0453 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][878/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9717 |hm_loss 0.6599 |wh_loss 2.6655 |off_loss 0.0453 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][879/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9707 |hm_loss 0.6592 |wh_loss 2.6625 |off_loss 0.0452 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][880/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9696 |hm_loss 0.6585 |wh_loss 2.6594 |off_loss 0.0452 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][881/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9686 |hm_loss 0.6578 |wh_loss 2.6564 |off_loss 0.0451 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][882/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9676 |hm_loss 0.6571 |wh_loss 2.6534 |off_loss 0.0451 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][883/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9665 |hm_loss 0.6564 |wh_loss 2.6504 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][884/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9655 |hm_loss 0.6558 |wh_loss 2.6474 |off_loss 0.0450 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][885/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9645 |hm_loss 0.6551 |wh_loss 2.6444 |off_loss 0.0449 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][886/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9634 |hm_loss 0.6544 |wh_loss 2.6415 |off_loss 0.0449 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][887/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9624 |hm_loss 0.6537 |wh_loss 2.6385 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][888/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9614 |hm_loss 0.6531 |wh_loss 2.6355 |off_loss 0.0448 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][889/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9604 |hm_loss 0.6524 |wh_loss 2.6325 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][890/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9594 |hm_loss 0.6517 |wh_loss 2.6296 |off_loss 0.0447 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][891/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9583 |hm_loss 0.6510 |wh_loss 2.6266 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][892/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9573 |hm_loss 0.6504 |wh_loss 2.6237 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][893/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9563 |hm_loss 0.6497 |wh_loss 2.6208 |off_loss 0.0445 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][894/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9553 |hm_loss 0.6490 |wh_loss 2.6178 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][895/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9543 |hm_loss 0.6484 |wh_loss 2.6149 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][896/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9533 |hm_loss 0.6477 |wh_loss 2.6120 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][897/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9523 |hm_loss 0.6470 |wh_loss 2.6091 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][898/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9513 |hm_loss 0.6464 |wh_loss 2.6062 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][899/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9503 |hm_loss 0.6457 |wh_loss 2.6033 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][900/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9493 |hm_loss 0.6451 |wh_loss 2.6004 |off_loss 0.0442 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][901/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9483 |hm_loss 0.6444 |wh_loss 2.5975 |off_loss 0.0441 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][902/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9473 |hm_loss 0.6438 |wh_loss 2.5946 |off_loss 0.0441 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][903/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9463 |hm_loss 0.6431 |wh_loss 2.5918 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][904/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9453 |hm_loss 0.6425 |wh_loss 2.5889 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][905/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9444 |hm_loss 0.6418 |wh_loss 2.5861 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][906/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9434 |hm_loss 0.6412 |wh_loss 2.5832 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][907/2110]|Tot: 0:00:19 |ETA: 0:00:00 |loss 0.9424 |hm_loss 0.6405 |wh_loss 2.5804 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][908/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9414 |hm_loss 0.6399 |wh_loss 2.5775 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][909/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9405 |hm_loss 0.6392 |wh_loss 2.5747 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][910/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9395 |hm_loss 0.6386 |wh_loss 2.5719 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][911/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9385 |hm_loss 0.6379 |wh_loss 2.5690 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][912/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9375 |hm_loss 0.6373 |wh_loss 2.5662 |off_loss 0.0436 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][913/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9366 |hm_loss 0.6367 |wh_loss 2.5634 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][914/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9356 |hm_loss 0.6360 |wh_loss 2.5606 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][915/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9346 |hm_loss 0.6354 |wh_loss 2.5578 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][916/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9337 |hm_loss 0.6348 |wh_loss 2.5550 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][917/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9327 |hm_loss 0.6341 |wh_loss 2.5523 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][918/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9318 |hm_loss 0.6335 |wh_loss 2.5495 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][919/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9308 |hm_loss 0.6329 |wh_loss 2.5467 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][920/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9299 |hm_loss 0.6322 |wh_loss 2.5439 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][921/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9289 |hm_loss 0.6316 |wh_loss 2.5412 |off_loss 0.0432 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][922/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9280 |hm_loss 0.6310 |wh_loss 2.5384 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][923/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9270 |hm_loss 0.6304 |wh_loss 2.5357 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][924/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9261 |hm_loss 0.6297 |wh_loss 2.5329 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][925/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9251 |hm_loss 0.6291 |wh_loss 2.5302 |off_loss 0.0430 |Data 0.011s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][926/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9242 |hm_loss 0.6285 |wh_loss 2.5275 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][927/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9233 |hm_loss 0.6279 |wh_loss 2.5248 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][928/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9223 |hm_loss 0.6273 |wh_loss 2.5220 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][929/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9214 |hm_loss 0.6266 |wh_loss 2.5193 |off_loss 0.0428 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][930/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9205 |hm_loss 0.6260 |wh_loss 2.5166 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][931/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9195 |hm_loss 0.6254 |wh_loss 2.5139 |off_loss 0.0427 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][932/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9186 |hm_loss 0.6248 |wh_loss 2.5112 |off_loss 0.0427 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][933/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9177 |hm_loss 0.6242 |wh_loss 2.5085 |off_loss 0.0426 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][934/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9167 |hm_loss 0.6236 |wh_loss 2.5058 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][935/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9158 |hm_loss 0.6230 |wh_loss 2.5032 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][936/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9149 |hm_loss 0.6224 |wh_loss 2.5005 |off_loss 0.0425 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][937/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9140 |hm_loss 0.6218 |wh_loss 2.4978 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][938/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9131 |hm_loss 0.6212 |wh_loss 2.4952 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][939/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9122 |hm_loss 0.6206 |wh_loss 2.4925 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][940/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9113 |hm_loss 0.6200 |wh_loss 2.4899 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][941/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9103 |hm_loss 0.6194 |wh_loss 2.4872 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][942/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9094 |hm_loss 0.6188 |wh_loss 2.4846 |off_loss 0.0422 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][943/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9085 |hm_loss 0.6182 |wh_loss 2.4820 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][944/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9076 |hm_loss 0.6176 |wh_loss 2.4793 |off_loss 0.0421 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][945/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9067 |hm_loss 0.6170 |wh_loss 2.4767 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][946/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9058 |hm_loss 0.6164 |wh_loss 2.4741 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][947/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9049 |hm_loss 0.6158 |wh_loss 2.4715 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][948/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9040 |hm_loss 0.6152 |wh_loss 2.4689 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][949/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9031 |hm_loss 0.6146 |wh_loss 2.4663 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][950/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9022 |hm_loss 0.6140 |wh_loss 2.4637 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][951/2110]|Tot: 0:00:20 |ETA: 0:00:00 |loss 0.9013 |hm_loss 0.6134 |wh_loss 2.4611 |off_loss 0.0418 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][952/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.9005 |hm_loss 0.6128 |wh_loss 2.4585 |off_loss 0.0418 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][953/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8996 |hm_loss 0.6122 |wh_loss 2.4559 |off_loss 0.0417 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][954/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8987 |hm_loss 0.6117 |wh_loss 2.4534 |off_loss 0.0417 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][955/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8978 |hm_loss 0.6111 |wh_loss 2.4508 |off_loss 0.0416 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][956/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8969 |hm_loss 0.6105 |wh_loss 2.4482 |off_loss 0.0416 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][957/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8960 |hm_loss 0.6099 |wh_loss 2.4457 |off_loss 0.0416 |Data 0.008s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][958/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8952 |hm_loss 0.6093 |wh_loss 2.4431 |off_loss 0.0415 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][959/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8943 |hm_loss 0.6088 |wh_loss 2.4406 |off_loss 0.0415 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][960/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8934 |hm_loss 0.6082 |wh_loss 2.4381 |off_loss 0.0414 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][961/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8925 |hm_loss 0.6076 |wh_loss 2.4355 |off_loss 0.0414 |Data 0.010s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][962/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8917 |hm_loss 0.6070 |wh_loss 2.4330 |off_loss 0.0413 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][963/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8908 |hm_loss 0.6065 |wh_loss 2.4305 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][964/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8899 |hm_loss 0.6059 |wh_loss 2.4279 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][965/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8891 |hm_loss 0.6053 |wh_loss 2.4254 |off_loss 0.0412 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][966/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8882 |hm_loss 0.6047 |wh_loss 2.4229 |off_loss 0.0412 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][967/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8873 |hm_loss 0.6042 |wh_loss 2.4204 |off_loss 0.0411 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][968/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8865 |hm_loss 0.6036 |wh_loss 2.4179 |off_loss 0.0411 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][969/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8856 |hm_loss 0.6030 |wh_loss 2.4154 |off_loss 0.0410 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][970/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8848 |hm_loss 0.6025 |wh_loss 2.4129 |off_loss 0.0410 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][971/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8839 |hm_loss 0.6019 |wh_loss 2.4105 |off_loss 0.0410 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][972/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8831 |hm_loss 0.6014 |wh_loss 2.4080 |off_loss 0.0409 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][973/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8822 |hm_loss 0.6008 |wh_loss 2.4055 |off_loss 0.0409 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][974/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8814 |hm_loss 0.6002 |wh_loss 2.4030 |off_loss 0.0408 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][975/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8805 |hm_loss 0.5997 |wh_loss 2.4006 |off_loss 0.0408 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][976/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8797 |hm_loss 0.5991 |wh_loss 2.3981 |off_loss 0.0407 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][977/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8788 |hm_loss 0.5986 |wh_loss 2.3957 |off_loss 0.0407 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][978/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8780 |hm_loss 0.5980 |wh_loss 2.3932 |off_loss 0.0407 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][979/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8771 |hm_loss 0.5974 |wh_loss 2.3908 |off_loss 0.0406 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][980/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8763 |hm_loss 0.5969 |wh_loss 2.3883 |off_loss 0.0406 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][981/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8755 |hm_loss 0.5963 |wh_loss 2.3859 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][982/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8746 |hm_loss 0.5958 |wh_loss 2.3835 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][983/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8738 |hm_loss 0.5952 |wh_loss 2.3811 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][984/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8730 |hm_loss 0.5947 |wh_loss 2.3786 |off_loss 0.0404 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][985/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8721 |hm_loss 0.5941 |wh_loss 2.3762 |off_loss 0.0404 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][986/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8713 |hm_loss 0.5936 |wh_loss 2.3738 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][987/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8705 |hm_loss 0.5930 |wh_loss 2.3714 |off_loss 0.0403 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][988/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8696 |hm_loss 0.5925 |wh_loss 2.3690 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][989/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8688 |hm_loss 0.5919 |wh_loss 2.3666 |off_loss 0.0402 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][990/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8680 |hm_loss 0.5914 |wh_loss 2.3642 |off_loss 0.0402 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][991/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8672 |hm_loss 0.5909 |wh_loss 2.3619 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][992/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8664 |hm_loss 0.5903 |wh_loss 2.3595 |off_loss 0.0401 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][993/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8655 |hm_loss 0.5898 |wh_loss 2.3571 |off_loss 0.0401 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][994/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8647 |hm_loss 0.5892 |wh_loss 2.3547 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][995/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8639 |hm_loss 0.5887 |wh_loss 2.3524 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][996/2110]|Tot: 0:00:21 |ETA: 0:00:00 |loss 0.8631 |hm_loss 0.5882 |wh_loss 2.3500 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][997/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8623 |hm_loss 0.5876 |wh_loss 2.3477 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][998/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8615 |hm_loss 0.5871 |wh_loss 2.3453 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][999/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8675 |hm_loss 0.5907 |wh_loss 2.3635 |off_loss 0.0404 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1000/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8741 |hm_loss 0.5945 |wh_loss 2.3902 |off_loss 0.0406 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1001/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8785 |hm_loss 0.5973 |wh_loss 2.4043 |off_loss 0.0409 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1002/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8833 |hm_loss 0.6007 |wh_loss 2.4161 |off_loss 0.0410 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1003/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8890 |hm_loss 0.6040 |wh_loss 2.4362 |off_loss 0.0414 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1004/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.8957 |hm_loss 0.6076 |wh_loss 2.4621 |off_loss 0.0418 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1005/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9026 |hm_loss 0.6112 |wh_loss 2.4920 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1006/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9088 |hm_loss 0.6148 |wh_loss 2.5167 |off_loss 0.0423 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1007/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9080 |hm_loss 0.6143 |wh_loss 2.5142 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1008/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9071 |hm_loss 0.6137 |wh_loss 2.5117 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1009/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9063 |hm_loss 0.6132 |wh_loss 2.5092 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1010/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9054 |hm_loss 0.6126 |wh_loss 2.5068 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1011/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9105 |hm_loss 0.6157 |wh_loss 2.5246 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1012/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9162 |hm_loss 0.6192 |wh_loss 2.5447 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1013/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9210 |hm_loss 0.6229 |wh_loss 2.5566 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1014/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9265 |hm_loss 0.6266 |wh_loss 2.5702 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1015/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9332 |hm_loss 0.6303 |wh_loss 2.5944 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1016/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9408 |hm_loss 0.6340 |wh_loss 2.6288 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1017/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9399 |hm_loss 0.6335 |wh_loss 2.6262 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1018/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9390 |hm_loss 0.6329 |wh_loss 2.6236 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1019/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9382 |hm_loss 0.6323 |wh_loss 2.6210 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1020/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9373 |hm_loss 0.6317 |wh_loss 2.6185 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1021/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9414 |hm_loss 0.6345 |wh_loss 2.6311 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1022/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9469 |hm_loss 0.6377 |wh_loss 2.6502 |off_loss 0.0442 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1023/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9527 |hm_loss 0.6412 |wh_loss 2.6684 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1024/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9582 |hm_loss 0.6448 |wh_loss 2.6879 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1025/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9632 |hm_loss 0.6484 |wh_loss 2.7007 |off_loss 0.0447 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1026/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9691 |hm_loss 0.6521 |wh_loss 2.7181 |off_loss 0.0452 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1027/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9752 |hm_loss 0.6558 |wh_loss 2.7393 |off_loss 0.0455 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1028/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9812 |hm_loss 0.6594 |wh_loss 2.7570 |off_loss 0.0461 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1029/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9864 |hm_loss 0.6631 |wh_loss 2.7678 |off_loss 0.0465 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1030/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9855 |hm_loss 0.6625 |wh_loss 2.7651 |off_loss 0.0465 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1031/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9846 |hm_loss 0.6619 |wh_loss 2.7625 |off_loss 0.0464 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1032/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9837 |hm_loss 0.6613 |wh_loss 2.7598 |off_loss 0.0464 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1033/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9828 |hm_loss 0.6607 |wh_loss 2.7571 |off_loss 0.0464 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1034/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9819 |hm_loss 0.6602 |wh_loss 2.7545 |off_loss 0.0463 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1035/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9810 |hm_loss 0.6596 |wh_loss 2.7518 |off_loss 0.0463 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1036/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9801 |hm_loss 0.6590 |wh_loss 2.7491 |off_loss 0.0462 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1037/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9792 |hm_loss 0.6584 |wh_loss 2.7465 |off_loss 0.0462 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1038/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9783 |hm_loss 0.6578 |wh_loss 2.7439 |off_loss 0.0461 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1039/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9774 |hm_loss 0.6572 |wh_loss 2.7412 |off_loss 0.0461 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1040/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9766 |hm_loss 0.6567 |wh_loss 2.7386 |off_loss 0.0460 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1041/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9757 |hm_loss 0.6561 |wh_loss 2.7360 |off_loss 0.0460 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1042/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9748 |hm_loss 0.6555 |wh_loss 2.7333 |off_loss 0.0460 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1043/2110]|Tot: 0:00:22 |ETA: 0:00:00 |loss 0.9739 |hm_loss 0.6549 |wh_loss 2.7307 |off_loss 0.0459 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1044/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9730 |hm_loss 0.6543 |wh_loss 2.7281 |off_loss 0.0459 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1045/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9721 |hm_loss 0.6538 |wh_loss 2.7255 |off_loss 0.0458 |Data 0.009s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1046/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9713 |hm_loss 0.6532 |wh_loss 2.7229 |off_loss 0.0458 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1047/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9704 |hm_loss 0.6526 |wh_loss 2.7203 |off_loss 0.0457 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1048/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9695 |hm_loss 0.6520 |wh_loss 2.7177 |off_loss 0.0457 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1049/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9686 |hm_loss 0.6515 |wh_loss 2.7151 |off_loss 0.0457 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1050/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9678 |hm_loss 0.6509 |wh_loss 2.7125 |off_loss 0.0456 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1051/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9669 |hm_loss 0.6503 |wh_loss 2.7099 |off_loss 0.0456 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1052/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9660 |hm_loss 0.6498 |wh_loss 2.7074 |off_loss 0.0455 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1053/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9652 |hm_loss 0.6492 |wh_loss 2.7048 |off_loss 0.0455 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1054/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9643 |hm_loss 0.6486 |wh_loss 2.7022 |off_loss 0.0454 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1055/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9634 |hm_loss 0.6481 |wh_loss 2.6997 |off_loss 0.0454 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1056/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9626 |hm_loss 0.6475 |wh_loss 2.6971 |off_loss 0.0453 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1057/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9617 |hm_loss 0.6469 |wh_loss 2.6946 |off_loss 0.0453 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1058/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9608 |hm_loss 0.6464 |wh_loss 2.6920 |off_loss 0.0453 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1059/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9600 |hm_loss 0.6458 |wh_loss 2.6895 |off_loss 0.0452 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1060/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9591 |hm_loss 0.6453 |wh_loss 2.6870 |off_loss 0.0452 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1061/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9583 |hm_loss 0.6447 |wh_loss 2.6844 |off_loss 0.0451 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1062/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9574 |hm_loss 0.6441 |wh_loss 2.6819 |off_loss 0.0451 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1063/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9566 |hm_loss 0.6436 |wh_loss 2.6794 |off_loss 0.0451 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1064/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9557 |hm_loss 0.6430 |wh_loss 2.6769 |off_loss 0.0450 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1065/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9549 |hm_loss 0.6425 |wh_loss 2.6744 |off_loss 0.0450 |Data 0.019s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1066/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9540 |hm_loss 0.6419 |wh_loss 2.6718 |off_loss 0.0449 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1067/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9532 |hm_loss 0.6414 |wh_loss 2.6693 |off_loss 0.0449 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1068/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9523 |hm_loss 0.6408 |wh_loss 2.6668 |off_loss 0.0448 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1069/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9515 |hm_loss 0.6403 |wh_loss 2.6644 |off_loss 0.0448 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1070/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9507 |hm_loss 0.6397 |wh_loss 2.6619 |off_loss 0.0448 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1071/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9498 |hm_loss 0.6392 |wh_loss 2.6594 |off_loss 0.0447 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1072/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9490 |hm_loss 0.6386 |wh_loss 2.6569 |off_loss 0.0447 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1073/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9481 |hm_loss 0.6381 |wh_loss 2.6544 |off_loss 0.0446 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1074/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9473 |hm_loss 0.6375 |wh_loss 2.6520 |off_loss 0.0446 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1075/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9465 |hm_loss 0.6370 |wh_loss 2.6495 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1076/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9456 |hm_loss 0.6364 |wh_loss 2.6470 |off_loss 0.0445 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1077/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9448 |hm_loss 0.6359 |wh_loss 2.6446 |off_loss 0.0445 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1078/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9440 |hm_loss 0.6353 |wh_loss 2.6421 |off_loss 0.0444 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1079/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9432 |hm_loss 0.6348 |wh_loss 2.6397 |off_loss 0.0444 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1080/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9423 |hm_loss 0.6343 |wh_loss 2.6372 |off_loss 0.0443 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1081/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9415 |hm_loss 0.6337 |wh_loss 2.6348 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1082/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9407 |hm_loss 0.6332 |wh_loss 2.6324 |off_loss 0.0443 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1083/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9399 |hm_loss 0.6327 |wh_loss 2.6299 |off_loss 0.0442 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1084/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9391 |hm_loss 0.6321 |wh_loss 2.6275 |off_loss 0.0442 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1085/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9382 |hm_loss 0.6316 |wh_loss 2.6251 |off_loss 0.0441 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1086/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9374 |hm_loss 0.6311 |wh_loss 2.6227 |off_loss 0.0441 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1087/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9366 |hm_loss 0.6305 |wh_loss 2.6203 |off_loss 0.0441 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1088/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9358 |hm_loss 0.6300 |wh_loss 2.6179 |off_loss 0.0440 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1089/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9350 |hm_loss 0.6295 |wh_loss 2.6155 |off_loss 0.0440 |Data 0.016s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1090/2110]|Tot: 0:00:23 |ETA: 0:00:00 |loss 0.9342 |hm_loss 0.6289 |wh_loss 2.6131 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1091/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9334 |hm_loss 0.6284 |wh_loss 2.6107 |off_loss 0.0439 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1092/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9326 |hm_loss 0.6279 |wh_loss 2.6083 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1093/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9318 |hm_loss 0.6274 |wh_loss 2.6059 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1094/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9310 |hm_loss 0.6268 |wh_loss 2.6035 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1095/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9302 |hm_loss 0.6263 |wh_loss 2.6012 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1096/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9294 |hm_loss 0.6258 |wh_loss 2.5988 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1097/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9286 |hm_loss 0.6253 |wh_loss 2.5964 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1098/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9278 |hm_loss 0.6247 |wh_loss 2.5941 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1099/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9270 |hm_loss 0.6242 |wh_loss 2.5917 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1100/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9262 |hm_loss 0.6237 |wh_loss 2.5893 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1101/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9254 |hm_loss 0.6232 |wh_loss 2.5870 |off_loss 0.0435 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1102/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9246 |hm_loss 0.6227 |wh_loss 2.5846 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1103/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9290 |hm_loss 0.6253 |wh_loss 2.6005 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1104/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9336 |hm_loss 0.6288 |wh_loss 2.6083 |off_loss 0.0440 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1105/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9384 |hm_loss 0.6322 |wh_loss 2.6171 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1106/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9444 |hm_loss 0.6357 |wh_loss 2.6400 |off_loss 0.0447 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1107/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9436 |hm_loss 0.6351 |wh_loss 2.6376 |off_loss 0.0447 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1108/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9428 |hm_loss 0.6346 |wh_loss 2.6352 |off_loss 0.0446 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1109/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9420 |hm_loss 0.6341 |wh_loss 2.6328 |off_loss 0.0446 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1110/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9412 |hm_loss 0.6336 |wh_loss 2.6305 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1111/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9404 |hm_loss 0.6330 |wh_loss 2.6281 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1112/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9396 |hm_loss 0.6325 |wh_loss 2.6257 |off_loss 0.0445 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1113/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9388 |hm_loss 0.6320 |wh_loss 2.6234 |off_loss 0.0444 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1114/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9380 |hm_loss 0.6315 |wh_loss 2.6210 |off_loss 0.0444 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1115/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9372 |hm_loss 0.6310 |wh_loss 2.6187 |off_loss 0.0443 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1116/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9364 |hm_loss 0.6305 |wh_loss 2.6163 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1117/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9356 |hm_loss 0.6299 |wh_loss 2.6140 |off_loss 0.0443 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1118/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9348 |hm_loss 0.6294 |wh_loss 2.6117 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1119/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9340 |hm_loss 0.6289 |wh_loss 2.6093 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1120/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9332 |hm_loss 0.6284 |wh_loss 2.6070 |off_loss 0.0442 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1121/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9325 |hm_loss 0.6279 |wh_loss 2.6047 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1122/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9317 |hm_loss 0.6274 |wh_loss 2.6024 |off_loss 0.0441 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1123/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9309 |hm_loss 0.6269 |wh_loss 2.6000 |off_loss 0.0440 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1124/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9301 |hm_loss 0.6263 |wh_loss 2.5977 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1125/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9293 |hm_loss 0.6258 |wh_loss 2.5954 |off_loss 0.0440 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1126/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9285 |hm_loss 0.6253 |wh_loss 2.5931 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1127/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9278 |hm_loss 0.6248 |wh_loss 2.5908 |off_loss 0.0439 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1128/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9270 |hm_loss 0.6243 |wh_loss 2.5885 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1129/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9262 |hm_loss 0.6238 |wh_loss 2.5862 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1130/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9255 |hm_loss 0.6233 |wh_loss 2.5840 |off_loss 0.0438 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1131/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9247 |hm_loss 0.6228 |wh_loss 2.5817 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1132/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9239 |hm_loss 0.6223 |wh_loss 2.5794 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1133/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9231 |hm_loss 0.6218 |wh_loss 2.5771 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1134/2110]|Tot: 0:00:24 |ETA: 0:00:00 |loss 0.9224 |hm_loss 0.6213 |wh_loss 2.5749 |off_loss 0.0436 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1135/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9216 |hm_loss 0.6208 |wh_loss 2.5726 |off_loss 0.0436 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1136/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9208 |hm_loss 0.6203 |wh_loss 2.5703 |off_loss 0.0435 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1137/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9201 |hm_loss 0.6198 |wh_loss 2.5681 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1138/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9193 |hm_loss 0.6193 |wh_loss 2.5658 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1139/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9185 |hm_loss 0.6188 |wh_loss 2.5636 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1140/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9178 |hm_loss 0.6183 |wh_loss 2.5613 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1141/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9170 |hm_loss 0.6178 |wh_loss 2.5591 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1142/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9163 |hm_loss 0.6173 |wh_loss 2.5568 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1143/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9155 |hm_loss 0.6168 |wh_loss 2.5546 |off_loss 0.0433 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1144/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9148 |hm_loss 0.6163 |wh_loss 2.5524 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1145/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9140 |hm_loss 0.6158 |wh_loss 2.5501 |off_loss 0.0432 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1146/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9133 |hm_loss 0.6153 |wh_loss 2.5479 |off_loss 0.0432 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1147/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9125 |hm_loss 0.6148 |wh_loss 2.5457 |off_loss 0.0431 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1148/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9118 |hm_loss 0.6143 |wh_loss 2.5435 |off_loss 0.0431 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1149/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9110 |hm_loss 0.6139 |wh_loss 2.5413 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1150/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9103 |hm_loss 0.6134 |wh_loss 2.5391 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1151/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9095 |hm_loss 0.6129 |wh_loss 2.5369 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1152/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9088 |hm_loss 0.6124 |wh_loss 2.5347 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1153/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9080 |hm_loss 0.6119 |wh_loss 2.5325 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1154/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9073 |hm_loss 0.6114 |wh_loss 2.5303 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1155/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9066 |hm_loss 0.6109 |wh_loss 2.5281 |off_loss 0.0428 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1156/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9058 |hm_loss 0.6105 |wh_loss 2.5259 |off_loss 0.0428 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1157/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9051 |hm_loss 0.6100 |wh_loss 2.5237 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1158/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9044 |hm_loss 0.6095 |wh_loss 2.5215 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1159/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9036 |hm_loss 0.6090 |wh_loss 2.5194 |off_loss 0.0427 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1160/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9029 |hm_loss 0.6085 |wh_loss 2.5172 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1161/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9022 |hm_loss 0.6081 |wh_loss 2.5150 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1162/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9014 |hm_loss 0.6076 |wh_loss 2.5129 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1163/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9007 |hm_loss 0.6071 |wh_loss 2.5107 |off_loss 0.0425 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1164/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9000 |hm_loss 0.6066 |wh_loss 2.5085 |off_loss 0.0425 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1165/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.8993 |hm_loss 0.6062 |wh_loss 2.5064 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1166/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.8985 |hm_loss 0.6057 |wh_loss 2.5042 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1167/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.8978 |hm_loss 0.6052 |wh_loss 2.5021 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1168/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.8971 |hm_loss 0.6047 |wh_loss 2.5000 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1169/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9019 |hm_loss 0.6074 |wh_loss 2.5189 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1170/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9067 |hm_loss 0.6106 |wh_loss 2.5313 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1171/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9105 |hm_loss 0.6139 |wh_loss 2.5351 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1172/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9162 |hm_loss 0.6171 |wh_loss 2.5548 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1173/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9154 |hm_loss 0.6166 |wh_loss 2.5526 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1174/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9147 |hm_loss 0.6162 |wh_loss 2.5505 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1175/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9139 |hm_loss 0.6157 |wh_loss 2.5483 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1176/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9132 |hm_loss 0.6152 |wh_loss 2.5461 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1177/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9125 |hm_loss 0.6147 |wh_loss 2.5440 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1178/2110]|Tot: 0:00:25 |ETA: 0:00:00 |loss 0.9117 |hm_loss 0.6142 |wh_loss 2.5418 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1179/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9110 |hm_loss 0.6138 |wh_loss 2.5397 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1180/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9103 |hm_loss 0.6133 |wh_loss 2.5375 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1181/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9096 |hm_loss 0.6128 |wh_loss 2.5354 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1182/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9145 |hm_loss 0.6159 |wh_loss 2.5516 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1183/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9185 |hm_loss 0.6192 |wh_loss 2.5557 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1184/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9233 |hm_loss 0.6224 |wh_loss 2.5707 |off_loss 0.0439 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1185/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9226 |hm_loss 0.6219 |wh_loss 2.5685 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1186/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9219 |hm_loss 0.6214 |wh_loss 2.5664 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1187/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9211 |hm_loss 0.6209 |wh_loss 2.5642 |off_loss 0.0438 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1188/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9204 |hm_loss 0.6205 |wh_loss 2.5621 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1189/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9197 |hm_loss 0.6200 |wh_loss 2.5599 |off_loss 0.0437 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1190/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9189 |hm_loss 0.6195 |wh_loss 2.5577 |off_loss 0.0437 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1191/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9182 |hm_loss 0.6190 |wh_loss 2.5556 |off_loss 0.0436 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1192/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9175 |hm_loss 0.6186 |wh_loss 2.5535 |off_loss 0.0436 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1193/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9168 |hm_loss 0.6181 |wh_loss 2.5513 |off_loss 0.0435 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1194/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9160 |hm_loss 0.6176 |wh_loss 2.5492 |off_loss 0.0435 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1195/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9153 |hm_loss 0.6171 |wh_loss 2.5471 |off_loss 0.0435 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1196/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9146 |hm_loss 0.6167 |wh_loss 2.5449 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1197/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9139 |hm_loss 0.6162 |wh_loss 2.5428 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1198/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9131 |hm_loss 0.6157 |wh_loss 2.5407 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1199/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9124 |hm_loss 0.6152 |wh_loss 2.5386 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1200/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9117 |hm_loss 0.6148 |wh_loss 2.5365 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1201/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9110 |hm_loss 0.6143 |wh_loss 2.5343 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1202/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9103 |hm_loss 0.6138 |wh_loss 2.5322 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1203/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9096 |hm_loss 0.6134 |wh_loss 2.5301 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1204/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9088 |hm_loss 0.6129 |wh_loss 2.5280 |off_loss 0.0431 |Data 0.016s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1205/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9081 |hm_loss 0.6124 |wh_loss 2.5259 |off_loss 0.0431 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1206/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9074 |hm_loss 0.6120 |wh_loss 2.5238 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1207/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9067 |hm_loss 0.6115 |wh_loss 2.5218 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1208/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9060 |hm_loss 0.6110 |wh_loss 2.5197 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1209/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9053 |hm_loss 0.6106 |wh_loss 2.5176 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1210/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9046 |hm_loss 0.6101 |wh_loss 2.5155 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1211/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9039 |hm_loss 0.6096 |wh_loss 2.5134 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1212/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9032 |hm_loss 0.6092 |wh_loss 2.5114 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1213/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9025 |hm_loss 0.6087 |wh_loss 2.5093 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1214/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9018 |hm_loss 0.6083 |wh_loss 2.5072 |off_loss 0.0428 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1215/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9011 |hm_loss 0.6078 |wh_loss 2.5052 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1216/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.9004 |hm_loss 0.6073 |wh_loss 2.5031 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1217/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.8997 |hm_loss 0.6069 |wh_loss 2.5010 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1218/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.8990 |hm_loss 0.6064 |wh_loss 2.4990 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1219/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.8983 |hm_loss 0.6060 |wh_loss 2.4969 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1220/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.8976 |hm_loss 0.6055 |wh_loss 2.4949 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1221/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.8969 |hm_loss 0.6051 |wh_loss 2.4929 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1222/2110]|Tot: 0:00:26 |ETA: 0:00:00 |loss 0.8962 |hm_loss 0.6046 |wh_loss 2.4908 |off_loss 0.0425 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1223/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8955 |hm_loss 0.6042 |wh_loss 2.4888 |off_loss 0.0425 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1224/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8948 |hm_loss 0.6037 |wh_loss 2.4868 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1225/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8942 |hm_loss 0.6033 |wh_loss 2.4847 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1226/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8935 |hm_loss 0.6028 |wh_loss 2.4827 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1227/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8928 |hm_loss 0.6024 |wh_loss 2.4807 |off_loss 0.0423 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1228/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8921 |hm_loss 0.6019 |wh_loss 2.4787 |off_loss 0.0423 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1229/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8914 |hm_loss 0.6015 |wh_loss 2.4766 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1230/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8907 |hm_loss 0.6010 |wh_loss 2.4746 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1231/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8901 |hm_loss 0.6006 |wh_loss 2.4726 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1232/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8894 |hm_loss 0.6002 |wh_loss 2.4706 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1233/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8887 |hm_loss 0.5997 |wh_loss 2.4686 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1234/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8880 |hm_loss 0.5993 |wh_loss 2.4666 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1235/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8874 |hm_loss 0.5988 |wh_loss 2.4646 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1236/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8867 |hm_loss 0.5984 |wh_loss 2.4626 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1237/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8860 |hm_loss 0.5979 |wh_loss 2.4606 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1238/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8853 |hm_loss 0.5975 |wh_loss 2.4587 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1239/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8847 |hm_loss 0.5971 |wh_loss 2.4567 |off_loss 0.0419 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1240/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8840 |hm_loss 0.5966 |wh_loss 2.4547 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1241/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8833 |hm_loss 0.5962 |wh_loss 2.4527 |off_loss 0.0419 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1242/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8827 |hm_loss 0.5958 |wh_loss 2.4507 |off_loss 0.0418 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1243/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8820 |hm_loss 0.5953 |wh_loss 2.4488 |off_loss 0.0418 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1244/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8813 |hm_loss 0.5949 |wh_loss 2.4468 |off_loss 0.0418 |Data 0.010s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1245/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8807 |hm_loss 0.5944 |wh_loss 2.4448 |off_loss 0.0417 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1246/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8800 |hm_loss 0.5940 |wh_loss 2.4429 |off_loss 0.0417 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1247/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8793 |hm_loss 0.5936 |wh_loss 2.4409 |off_loss 0.0417 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1248/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8787 |hm_loss 0.5931 |wh_loss 2.4390 |off_loss 0.0416 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1249/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8780 |hm_loss 0.5927 |wh_loss 2.4370 |off_loss 0.0416 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1250/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8773 |hm_loss 0.5923 |wh_loss 2.4351 |off_loss 0.0416 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1251/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8767 |hm_loss 0.5918 |wh_loss 2.4331 |off_loss 0.0415 |Data 0.021s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1252/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8760 |hm_loss 0.5914 |wh_loss 2.4312 |off_loss 0.0415 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1253/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8754 |hm_loss 0.5910 |wh_loss 2.4292 |off_loss 0.0415 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1254/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8747 |hm_loss 0.5906 |wh_loss 2.4273 |off_loss 0.0414 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1255/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8741 |hm_loss 0.5901 |wh_loss 2.4254 |off_loss 0.0414 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1256/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8734 |hm_loss 0.5897 |wh_loss 2.4235 |off_loss 0.0414 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1257/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8727 |hm_loss 0.5893 |wh_loss 2.4215 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1258/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8721 |hm_loss 0.5888 |wh_loss 2.4196 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1259/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8714 |hm_loss 0.5884 |wh_loss 2.4177 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1260/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8708 |hm_loss 0.5880 |wh_loss 2.4158 |off_loss 0.0412 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1261/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8701 |hm_loss 0.5876 |wh_loss 2.4138 |off_loss 0.0412 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1262/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8695 |hm_loss 0.5871 |wh_loss 2.4119 |off_loss 0.0412 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1263/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8735 |hm_loss 0.5896 |wh_loss 2.4260 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1264/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8782 |hm_loss 0.5926 |wh_loss 2.4385 |off_loss 0.0417 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1265/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8827 |hm_loss 0.5956 |wh_loss 2.4497 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1266/2110]|Tot: 0:00:27 |ETA: 0:00:00 |loss 0.8870 |hm_loss 0.5987 |wh_loss 2.4603 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1267/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8864 |hm_loss 0.5982 |wh_loss 2.4584 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1268/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8857 |hm_loss 0.5978 |wh_loss 2.4564 |off_loss 0.0423 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1269/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8892 |hm_loss 0.6000 |wh_loss 2.4680 |off_loss 0.0424 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1270/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8940 |hm_loss 0.6029 |wh_loss 2.4845 |off_loss 0.0427 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1271/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8985 |hm_loss 0.6057 |wh_loss 2.4981 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1272/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.9038 |hm_loss 0.6087 |wh_loss 2.5167 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1273/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.9031 |hm_loss 0.6082 |wh_loss 2.5148 |off_loss 0.0434 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1274/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.9025 |hm_loss 0.6078 |wh_loss 2.5128 |off_loss 0.0434 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1275/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.9018 |hm_loss 0.6074 |wh_loss 2.5108 |off_loss 0.0433 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1276/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.9011 |hm_loss 0.6069 |wh_loss 2.5088 |off_loss 0.0433 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1277/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.9005 |hm_loss 0.6065 |wh_loss 2.5069 |off_loss 0.0433 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1278/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8998 |hm_loss 0.6061 |wh_loss 2.5049 |off_loss 0.0432 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1279/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8991 |hm_loss 0.6056 |wh_loss 2.5030 |off_loss 0.0432 |Data 0.007s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1280/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8985 |hm_loss 0.6052 |wh_loss 2.5010 |off_loss 0.0432 |Data 0.009s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1281/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8978 |hm_loss 0.6048 |wh_loss 2.4991 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1282/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8972 |hm_loss 0.6044 |wh_loss 2.4971 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1283/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8965 |hm_loss 0.6039 |wh_loss 2.4952 |off_loss 0.0431 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1284/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8958 |hm_loss 0.6035 |wh_loss 2.4932 |off_loss 0.0430 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1285/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8952 |hm_loss 0.6031 |wh_loss 2.4913 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1286/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8945 |hm_loss 0.6026 |wh_loss 2.4894 |off_loss 0.0430 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1287/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8939 |hm_loss 0.6022 |wh_loss 2.4874 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1288/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8932 |hm_loss 0.6018 |wh_loss 2.4855 |off_loss 0.0429 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1289/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8926 |hm_loss 0.6014 |wh_loss 2.4836 |off_loss 0.0429 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1290/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8919 |hm_loss 0.6009 |wh_loss 2.4816 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1291/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8913 |hm_loss 0.6005 |wh_loss 2.4797 |off_loss 0.0428 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1292/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8906 |hm_loss 0.6001 |wh_loss 2.4778 |off_loss 0.0428 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1293/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8900 |hm_loss 0.5997 |wh_loss 2.4759 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1294/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8893 |hm_loss 0.5992 |wh_loss 2.4740 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1295/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8887 |hm_loss 0.5988 |wh_loss 2.4721 |off_loss 0.0427 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1296/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8880 |hm_loss 0.5984 |wh_loss 2.4702 |off_loss 0.0426 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1297/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8874 |hm_loss 0.5980 |wh_loss 2.4683 |off_loss 0.0426 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1298/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8868 |hm_loss 0.5976 |wh_loss 2.4664 |off_loss 0.0426 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1299/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8861 |hm_loss 0.5971 |wh_loss 2.4645 |off_loss 0.0425 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1300/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8855 |hm_loss 0.5967 |wh_loss 2.4626 |off_loss 0.0425 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1301/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8848 |hm_loss 0.5963 |wh_loss 2.4607 |off_loss 0.0425 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1302/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8842 |hm_loss 0.5959 |wh_loss 2.4588 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1303/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8836 |hm_loss 0.5955 |wh_loss 2.4569 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1304/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8829 |hm_loss 0.5951 |wh_loss 2.4550 |off_loss 0.0424 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1305/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8823 |hm_loss 0.5946 |wh_loss 2.4531 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1306/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8817 |hm_loss 0.5942 |wh_loss 2.4513 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1307/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8810 |hm_loss 0.5938 |wh_loss 2.4494 |off_loss 0.0423 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1308/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8804 |hm_loss 0.5934 |wh_loss 2.4475 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1309/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8798 |hm_loss 0.5930 |wh_loss 2.4456 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1310/2110]|Tot: 0:00:28 |ETA: 0:00:00 |loss 0.8791 |hm_loss 0.5926 |wh_loss 2.4438 |off_loss 0.0422 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1311/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8785 |hm_loss 0.5922 |wh_loss 2.4419 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1312/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8779 |hm_loss 0.5918 |wh_loss 2.4401 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1313/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8773 |hm_loss 0.5914 |wh_loss 2.4382 |off_loss 0.0421 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1314/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8766 |hm_loss 0.5909 |wh_loss 2.4363 |off_loss 0.0420 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1315/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8760 |hm_loss 0.5905 |wh_loss 2.4345 |off_loss 0.0420 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1316/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8754 |hm_loss 0.5901 |wh_loss 2.4327 |off_loss 0.0420 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1317/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8748 |hm_loss 0.5897 |wh_loss 2.4308 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1318/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8741 |hm_loss 0.5893 |wh_loss 2.4290 |off_loss 0.0419 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1319/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8735 |hm_loss 0.5889 |wh_loss 2.4271 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1320/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8729 |hm_loss 0.5885 |wh_loss 2.4253 |off_loss 0.0419 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1321/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8723 |hm_loss 0.5881 |wh_loss 2.4234 |off_loss 0.0418 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1322/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8716 |hm_loss 0.5877 |wh_loss 2.4216 |off_loss 0.0418 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1323/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8710 |hm_loss 0.5873 |wh_loss 2.4198 |off_loss 0.0418 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1324/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8704 |hm_loss 0.5869 |wh_loss 2.4180 |off_loss 0.0417 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1325/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8698 |hm_loss 0.5865 |wh_loss 2.4161 |off_loss 0.0417 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1326/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8692 |hm_loss 0.5861 |wh_loss 2.4143 |off_loss 0.0417 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1327/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8686 |hm_loss 0.5857 |wh_loss 2.4125 |off_loss 0.0416 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1328/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8679 |hm_loss 0.5853 |wh_loss 2.4107 |off_loss 0.0416 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1329/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8673 |hm_loss 0.5849 |wh_loss 2.4089 |off_loss 0.0416 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1330/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8667 |hm_loss 0.5845 |wh_loss 2.4071 |off_loss 0.0415 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1331/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8661 |hm_loss 0.5841 |wh_loss 2.4053 |off_loss 0.0415 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1332/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8655 |hm_loss 0.5837 |wh_loss 2.4035 |off_loss 0.0415 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1333/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8649 |hm_loss 0.5833 |wh_loss 2.4016 |off_loss 0.0414 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1334/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8643 |hm_loss 0.5829 |wh_loss 2.3999 |off_loss 0.0414 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1335/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8637 |hm_loss 0.5825 |wh_loss 2.3981 |off_loss 0.0414 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1336/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8631 |hm_loss 0.5821 |wh_loss 2.3963 |off_loss 0.0414 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1337/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8625 |hm_loss 0.5817 |wh_loss 2.3945 |off_loss 0.0413 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1338/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8619 |hm_loss 0.5813 |wh_loss 2.3927 |off_loss 0.0413 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1339/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8612 |hm_loss 0.5809 |wh_loss 2.3909 |off_loss 0.0413 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1340/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8606 |hm_loss 0.5805 |wh_loss 2.3891 |off_loss 0.0412 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1341/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8600 |hm_loss 0.5801 |wh_loss 2.3873 |off_loss 0.0412 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1342/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8594 |hm_loss 0.5797 |wh_loss 2.3856 |off_loss 0.0412 |Data 0.020s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1343/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8588 |hm_loss 0.5793 |wh_loss 2.3838 |off_loss 0.0411 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1344/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8582 |hm_loss 0.5789 |wh_loss 2.3820 |off_loss 0.0411 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1345/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8576 |hm_loss 0.5785 |wh_loss 2.3802 |off_loss 0.0411 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1346/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8571 |hm_loss 0.5782 |wh_loss 2.3785 |off_loss 0.0410 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1347/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8565 |hm_loss 0.5778 |wh_loss 2.3767 |off_loss 0.0410 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1348/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8559 |hm_loss 0.5774 |wh_loss 2.3749 |off_loss 0.0410 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1349/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8553 |hm_loss 0.5770 |wh_loss 2.3732 |off_loss 0.0410 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1350/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8547 |hm_loss 0.5766 |wh_loss 2.3714 |off_loss 0.0409 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1351/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8541 |hm_loss 0.5762 |wh_loss 2.3697 |off_loss 0.0409 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1352/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8535 |hm_loss 0.5758 |wh_loss 2.3679 |off_loss 0.0409 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1353/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8529 |hm_loss 0.5755 |wh_loss 2.3662 |off_loss 0.0408 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1354/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8523 |hm_loss 0.5751 |wh_loss 2.3644 |off_loss 0.0408 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1355/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8517 |hm_loss 0.5747 |wh_loss 2.3627 |off_loss 0.0408 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1356/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8511 |hm_loss 0.5743 |wh_loss 2.3609 |off_loss 0.0407 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1357/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8506 |hm_loss 0.5739 |wh_loss 2.3592 |off_loss 0.0407 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1358/2110]|Tot: 0:00:29 |ETA: 0:00:00 |loss 0.8500 |hm_loss 0.5735 |wh_loss 2.3575 |off_loss 0.0407 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1359/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8494 |hm_loss 0.5732 |wh_loss 2.3557 |off_loss 0.0407 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1360/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8488 |hm_loss 0.5728 |wh_loss 2.3540 |off_loss 0.0406 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1361/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8482 |hm_loss 0.5724 |wh_loss 2.3523 |off_loss 0.0406 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1362/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8476 |hm_loss 0.5720 |wh_loss 2.3506 |off_loss 0.0406 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1363/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8470 |hm_loss 0.5716 |wh_loss 2.3488 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1364/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8465 |hm_loss 0.5712 |wh_loss 2.3471 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1365/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8459 |hm_loss 0.5709 |wh_loss 2.3454 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1366/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8453 |hm_loss 0.5705 |wh_loss 2.3437 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1367/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8447 |hm_loss 0.5701 |wh_loss 2.3420 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1368/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8441 |hm_loss 0.5697 |wh_loss 2.3402 |off_loss 0.0404 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1369/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8436 |hm_loss 0.5694 |wh_loss 2.3385 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1370/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8430 |hm_loss 0.5690 |wh_loss 2.3368 |off_loss 0.0403 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1371/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8424 |hm_loss 0.5686 |wh_loss 2.3351 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1372/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8418 |hm_loss 0.5682 |wh_loss 2.3334 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1373/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8413 |hm_loss 0.5679 |wh_loss 2.3317 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1374/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8407 |hm_loss 0.5675 |wh_loss 2.3300 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1375/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8401 |hm_loss 0.5671 |wh_loss 2.3283 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1376/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8396 |hm_loss 0.5667 |wh_loss 2.3267 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1377/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8390 |hm_loss 0.5664 |wh_loss 2.3250 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1378/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8384 |hm_loss 0.5660 |wh_loss 2.3233 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1379/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8378 |hm_loss 0.5656 |wh_loss 2.3216 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1380/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8373 |hm_loss 0.5653 |wh_loss 2.3199 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1381/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8367 |hm_loss 0.5649 |wh_loss 2.3182 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1382/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8361 |hm_loss 0.5645 |wh_loss 2.3166 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1383/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8356 |hm_loss 0.5641 |wh_loss 2.3149 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1384/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8350 |hm_loss 0.5638 |wh_loss 2.3132 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1385/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8345 |hm_loss 0.5634 |wh_loss 2.3115 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1386/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8339 |hm_loss 0.5630 |wh_loss 2.3099 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1387/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8333 |hm_loss 0.5627 |wh_loss 2.3082 |off_loss 0.0398 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1388/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8328 |hm_loss 0.5623 |wh_loss 2.3066 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1389/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8360 |hm_loss 0.5644 |wh_loss 2.3169 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1390/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8402 |hm_loss 0.5671 |wh_loss 2.3298 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1391/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8441 |hm_loss 0.5699 |wh_loss 2.3391 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1392/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8485 |hm_loss 0.5727 |wh_loss 2.3543 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1393/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8479 |hm_loss 0.5723 |wh_loss 2.3526 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1394/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8473 |hm_loss 0.5719 |wh_loss 2.3509 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1395/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8468 |hm_loss 0.5715 |wh_loss 2.3492 |off_loss 0.0403 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1396/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8462 |hm_loss 0.5712 |wh_loss 2.3475 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1397/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8456 |hm_loss 0.5708 |wh_loss 2.3459 |off_loss 0.0402 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1398/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8451 |hm_loss 0.5704 |wh_loss 2.3442 |off_loss 0.0402 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1399/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8445 |hm_loss 0.5701 |wh_loss 2.3425 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1400/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8439 |hm_loss 0.5697 |wh_loss 2.3408 |off_loss 0.0401 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1401/2110]|Tot: 0:00:30 |ETA: 0:00:00 |loss 0.8434 |hm_loss 0.5693 |wh_loss 2.3392 |off_loss 0.0401 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1402/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8428 |hm_loss 0.5690 |wh_loss 2.3375 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1403/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8422 |hm_loss 0.5686 |wh_loss 2.3358 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1404/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8417 |hm_loss 0.5682 |wh_loss 2.3342 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1405/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8411 |hm_loss 0.5679 |wh_loss 2.3325 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1406/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8406 |hm_loss 0.5675 |wh_loss 2.3309 |off_loss 0.0400 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1407/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8400 |hm_loss 0.5671 |wh_loss 2.3292 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1408/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8394 |hm_loss 0.5668 |wh_loss 2.3276 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1409/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8389 |hm_loss 0.5664 |wh_loss 2.3259 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1410/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8383 |hm_loss 0.5660 |wh_loss 2.3243 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1411/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8378 |hm_loss 0.5657 |wh_loss 2.3226 |off_loss 0.0398 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1412/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8372 |hm_loss 0.5653 |wh_loss 2.3210 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1413/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8367 |hm_loss 0.5649 |wh_loss 2.3193 |off_loss 0.0398 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1414/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8361 |hm_loss 0.5646 |wh_loss 2.3177 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1415/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8356 |hm_loss 0.5642 |wh_loss 2.3160 |off_loss 0.0397 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1416/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8350 |hm_loss 0.5639 |wh_loss 2.3144 |off_loss 0.0397 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1417/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8391 |hm_loss 0.5663 |wh_loss 2.3300 |off_loss 0.0398 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1418/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8429 |hm_loss 0.5690 |wh_loss 2.3393 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1419/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8473 |hm_loss 0.5717 |wh_loss 2.3530 |off_loss 0.0403 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1420/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8515 |hm_loss 0.5744 |wh_loss 2.3646 |off_loss 0.0407 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1421/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8510 |hm_loss 0.5740 |wh_loss 2.3629 |off_loss 0.0407 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1422/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8504 |hm_loss 0.5736 |wh_loss 2.3613 |off_loss 0.0406 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1423/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8499 |hm_loss 0.5733 |wh_loss 2.3596 |off_loss 0.0406 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1424/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8493 |hm_loss 0.5729 |wh_loss 2.3580 |off_loss 0.0406 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1425/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8487 |hm_loss 0.5725 |wh_loss 2.3563 |off_loss 0.0406 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1426/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8482 |hm_loss 0.5722 |wh_loss 2.3547 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1427/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8476 |hm_loss 0.5718 |wh_loss 2.3530 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1428/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8471 |hm_loss 0.5715 |wh_loss 2.3514 |off_loss 0.0405 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1429/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8465 |hm_loss 0.5711 |wh_loss 2.3497 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1430/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8460 |hm_loss 0.5707 |wh_loss 2.3481 |off_loss 0.0404 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1431/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8454 |hm_loss 0.5704 |wh_loss 2.3464 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1432/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8449 |hm_loss 0.5700 |wh_loss 2.3448 |off_loss 0.0404 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1433/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8443 |hm_loss 0.5697 |wh_loss 2.3432 |off_loss 0.0403 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1434/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8438 |hm_loss 0.5693 |wh_loss 2.3415 |off_loss 0.0403 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1435/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8432 |hm_loss 0.5689 |wh_loss 2.3399 |off_loss 0.0403 |Data 0.008s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1436/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8427 |hm_loss 0.5686 |wh_loss 2.3383 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1437/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8421 |hm_loss 0.5682 |wh_loss 2.3366 |off_loss 0.0402 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1438/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8416 |hm_loss 0.5679 |wh_loss 2.3350 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1439/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8410 |hm_loss 0.5675 |wh_loss 2.3334 |off_loss 0.0402 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1440/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8405 |hm_loss 0.5671 |wh_loss 2.3318 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1441/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8399 |hm_loss 0.5668 |wh_loss 2.3302 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1442/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8394 |hm_loss 0.5664 |wh_loss 2.3285 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1443/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8388 |hm_loss 0.5661 |wh_loss 2.3269 |off_loss 0.0401 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1444/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8383 |hm_loss 0.5657 |wh_loss 2.3253 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1445/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8377 |hm_loss 0.5654 |wh_loss 2.3237 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1446/2110]|Tot: 0:00:31 |ETA: 0:00:00 |loss 0.8372 |hm_loss 0.5650 |wh_loss 2.3221 |off_loss 0.0400 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1447/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8367 |hm_loss 0.5647 |wh_loss 2.3205 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1448/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8361 |hm_loss 0.5643 |wh_loss 2.3189 |off_loss 0.0399 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1449/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8356 |hm_loss 0.5640 |wh_loss 2.3173 |off_loss 0.0399 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1450/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8351 |hm_loss 0.5636 |wh_loss 2.3157 |off_loss 0.0399 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1451/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8345 |hm_loss 0.5633 |wh_loss 2.3141 |off_loss 0.0398 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1452/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8340 |hm_loss 0.5629 |wh_loss 2.3125 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1453/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8335 |hm_loss 0.5626 |wh_loss 2.3109 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1454/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8329 |hm_loss 0.5623 |wh_loss 2.3093 |off_loss 0.0398 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1455/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8324 |hm_loss 0.5619 |wh_loss 2.3078 |off_loss 0.0397 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1456/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8319 |hm_loss 0.5616 |wh_loss 2.3062 |off_loss 0.0397 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1457/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8314 |hm_loss 0.5612 |wh_loss 2.3046 |off_loss 0.0397 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1458/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8308 |hm_loss 0.5609 |wh_loss 2.3030 |off_loss 0.0396 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1459/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8303 |hm_loss 0.5605 |wh_loss 2.3014 |off_loss 0.0396 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1460/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8298 |hm_loss 0.5602 |wh_loss 2.2999 |off_loss 0.0396 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1461/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8292 |hm_loss 0.5599 |wh_loss 2.2983 |off_loss 0.0396 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1462/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8287 |hm_loss 0.5595 |wh_loss 2.2967 |off_loss 0.0395 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1463/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8282 |hm_loss 0.5592 |wh_loss 2.2951 |off_loss 0.0395 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1464/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8277 |hm_loss 0.5588 |wh_loss 2.2936 |off_loss 0.0395 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1465/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8271 |hm_loss 0.5585 |wh_loss 2.2920 |off_loss 0.0395 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1466/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8266 |hm_loss 0.5581 |wh_loss 2.2905 |off_loss 0.0394 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1467/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8261 |hm_loss 0.5578 |wh_loss 2.2889 |off_loss 0.0394 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1468/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8256 |hm_loss 0.5574 |wh_loss 2.2873 |off_loss 0.0394 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1469/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8250 |hm_loss 0.5571 |wh_loss 2.2858 |off_loss 0.0393 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1470/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8245 |hm_loss 0.5568 |wh_loss 2.2842 |off_loss 0.0393 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1471/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8240 |hm_loss 0.5564 |wh_loss 2.2827 |off_loss 0.0393 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1472/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8235 |hm_loss 0.5561 |wh_loss 2.2811 |off_loss 0.0393 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1473/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8229 |hm_loss 0.5557 |wh_loss 2.2796 |off_loss 0.0392 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1474/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8224 |hm_loss 0.5554 |wh_loss 2.2780 |off_loss 0.0392 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1475/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8219 |hm_loss 0.5551 |wh_loss 2.2765 |off_loss 0.0392 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1476/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8214 |hm_loss 0.5547 |wh_loss 2.2749 |off_loss 0.0392 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1477/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8208 |hm_loss 0.5544 |wh_loss 2.2734 |off_loss 0.0391 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1478/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8203 |hm_loss 0.5540 |wh_loss 2.2719 |off_loss 0.0391 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1479/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8198 |hm_loss 0.5537 |wh_loss 2.2703 |off_loss 0.0391 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1480/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8193 |hm_loss 0.5534 |wh_loss 2.2688 |off_loss 0.0391 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1481/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8188 |hm_loss 0.5530 |wh_loss 2.2673 |off_loss 0.0390 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1482/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8183 |hm_loss 0.5527 |wh_loss 2.2657 |off_loss 0.0390 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1483/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8177 |hm_loss 0.5523 |wh_loss 2.2642 |off_loss 0.0390 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1484/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8172 |hm_loss 0.5520 |wh_loss 2.2627 |off_loss 0.0389 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1485/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8167 |hm_loss 0.5517 |wh_loss 2.2612 |off_loss 0.0389 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1486/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8162 |hm_loss 0.5513 |wh_loss 2.2596 |off_loss 0.0389 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1487/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8157 |hm_loss 0.5510 |wh_loss 2.2581 |off_loss 0.0389 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1488/2110]|Tot: 0:00:32 |ETA: 0:00:00 |loss 0.8152 |hm_loss 0.5507 |wh_loss 2.2566 |off_loss 0.0388 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1489/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8147 |hm_loss 0.5503 |wh_loss 2.2551 |off_loss 0.0388 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1490/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8141 |hm_loss 0.5500 |wh_loss 2.2536 |off_loss 0.0388 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1491/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8136 |hm_loss 0.5497 |wh_loss 2.2521 |off_loss 0.0388 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1492/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8131 |hm_loss 0.5493 |wh_loss 2.2506 |off_loss 0.0387 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1493/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8126 |hm_loss 0.5490 |wh_loss 2.2491 |off_loss 0.0387 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1494/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8121 |hm_loss 0.5487 |wh_loss 2.2476 |off_loss 0.0387 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1495/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8116 |hm_loss 0.5483 |wh_loss 2.2461 |off_loss 0.0387 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1496/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8111 |hm_loss 0.5480 |wh_loss 2.2446 |off_loss 0.0386 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1497/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8106 |hm_loss 0.5477 |wh_loss 2.2431 |off_loss 0.0386 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1498/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8101 |hm_loss 0.5473 |wh_loss 2.2416 |off_loss 0.0386 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1499/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8096 |hm_loss 0.5470 |wh_loss 2.2401 |off_loss 0.0386 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1500/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8091 |hm_loss 0.5467 |wh_loss 2.2386 |off_loss 0.0385 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1501/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8086 |hm_loss 0.5464 |wh_loss 2.2371 |off_loss 0.0385 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1502/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8081 |hm_loss 0.5460 |wh_loss 2.2356 |off_loss 0.0385 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1503/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8076 |hm_loss 0.5457 |wh_loss 2.2341 |off_loss 0.0385 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1504/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8071 |hm_loss 0.5454 |wh_loss 2.2326 |off_loss 0.0384 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1505/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8066 |hm_loss 0.5450 |wh_loss 2.2311 |off_loss 0.0384 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1506/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8061 |hm_loss 0.5447 |wh_loss 2.2297 |off_loss 0.0384 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1507/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8056 |hm_loss 0.5444 |wh_loss 2.2282 |off_loss 0.0384 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1508/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8051 |hm_loss 0.5441 |wh_loss 2.2267 |off_loss 0.0383 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1509/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8046 |hm_loss 0.5437 |wh_loss 2.2252 |off_loss 0.0383 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1510/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8041 |hm_loss 0.5434 |wh_loss 2.2238 |off_loss 0.0383 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1511/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8036 |hm_loss 0.5431 |wh_loss 2.2223 |off_loss 0.0383 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1512/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8031 |hm_loss 0.5428 |wh_loss 2.2208 |off_loss 0.0382 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1513/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8026 |hm_loss 0.5424 |wh_loss 2.2193 |off_loss 0.0382 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1514/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8021 |hm_loss 0.5421 |wh_loss 2.2179 |off_loss 0.0382 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1515/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8016 |hm_loss 0.5418 |wh_loss 2.2164 |off_loss 0.0382 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1516/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8011 |hm_loss 0.5415 |wh_loss 2.2150 |off_loss 0.0381 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1517/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8006 |hm_loss 0.5412 |wh_loss 2.2135 |off_loss 0.0381 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1518/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.8001 |hm_loss 0.5408 |wh_loss 2.2120 |off_loss 0.0381 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1519/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7996 |hm_loss 0.5405 |wh_loss 2.2106 |off_loss 0.0381 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1520/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7991 |hm_loss 0.5402 |wh_loss 2.2091 |off_loss 0.0380 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1521/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7986 |hm_loss 0.5399 |wh_loss 2.2077 |off_loss 0.0380 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1522/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7981 |hm_loss 0.5395 |wh_loss 2.2062 |off_loss 0.0380 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1523/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7977 |hm_loss 0.5392 |wh_loss 2.2048 |off_loss 0.0380 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1524/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7972 |hm_loss 0.5389 |wh_loss 2.2033 |off_loss 0.0379 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1525/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7967 |hm_loss 0.5386 |wh_loss 2.2019 |off_loss 0.0379 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1526/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7962 |hm_loss 0.5383 |wh_loss 2.2005 |off_loss 0.0379 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1527/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7957 |hm_loss 0.5379 |wh_loss 2.1990 |off_loss 0.0379 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1528/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7952 |hm_loss 0.5376 |wh_loss 2.1976 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1529/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7947 |hm_loss 0.5373 |wh_loss 2.1961 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1530/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7942 |hm_loss 0.5370 |wh_loss 2.1947 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1531/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7938 |hm_loss 0.5367 |wh_loss 2.1933 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1532/2110]|Tot: 0:00:33 |ETA: 0:00:00 |loss 0.7933 |hm_loss 0.5364 |wh_loss 2.1918 |off_loss 0.0377 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1533/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7928 |hm_loss 0.5360 |wh_loss 2.1904 |off_loss 0.0377 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1534/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7923 |hm_loss 0.5357 |wh_loss 2.1890 |off_loss 0.0377 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1535/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7918 |hm_loss 0.5354 |wh_loss 2.1876 |off_loss 0.0377 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1536/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7913 |hm_loss 0.5351 |wh_loss 2.1861 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1537/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7909 |hm_loss 0.5348 |wh_loss 2.1847 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1538/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7904 |hm_loss 0.5345 |wh_loss 2.1833 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1539/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7899 |hm_loss 0.5342 |wh_loss 2.1819 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1540/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7894 |hm_loss 0.5338 |wh_loss 2.1805 |off_loss 0.0375 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1541/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7889 |hm_loss 0.5335 |wh_loss 2.1790 |off_loss 0.0375 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1542/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7885 |hm_loss 0.5332 |wh_loss 2.1776 |off_loss 0.0375 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1543/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7880 |hm_loss 0.5329 |wh_loss 2.1762 |off_loss 0.0375 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1544/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7875 |hm_loss 0.5326 |wh_loss 2.1748 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1545/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7870 |hm_loss 0.5323 |wh_loss 2.1734 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1546/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7866 |hm_loss 0.5320 |wh_loss 2.1720 |off_loss 0.0374 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1547/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7861 |hm_loss 0.5317 |wh_loss 2.1706 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1548/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7856 |hm_loss 0.5314 |wh_loss 2.1692 |off_loss 0.0373 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1549/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7852 |hm_loss 0.5311 |wh_loss 2.1678 |off_loss 0.0373 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1550/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7847 |hm_loss 0.5307 |wh_loss 2.1664 |off_loss 0.0373 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1551/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7842 |hm_loss 0.5304 |wh_loss 2.1650 |off_loss 0.0373 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1552/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7837 |hm_loss 0.5301 |wh_loss 2.1636 |off_loss 0.0372 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1553/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7833 |hm_loss 0.5298 |wh_loss 2.1622 |off_loss 0.0372 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1554/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7828 |hm_loss 0.5295 |wh_loss 2.1608 |off_loss 0.0372 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1555/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7875 |hm_loss 0.5316 |wh_loss 2.1845 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1556/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7922 |hm_loss 0.5337 |wh_loss 2.2085 |off_loss 0.0376 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1557/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7965 |hm_loss 0.5358 |wh_loss 2.2289 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1558/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.8005 |hm_loss 0.5380 |wh_loss 2.2467 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1559/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.8000 |hm_loss 0.5377 |wh_loss 2.2453 |off_loss 0.0378 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1560/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7996 |hm_loss 0.5374 |wh_loss 2.2438 |off_loss 0.0378 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1561/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7991 |hm_loss 0.5371 |wh_loss 2.2424 |off_loss 0.0378 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1562/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7986 |hm_loss 0.5368 |wh_loss 2.2410 |off_loss 0.0377 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1563/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7981 |hm_loss 0.5365 |wh_loss 2.2395 |off_loss 0.0377 |Data 0.015s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1564/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7976 |hm_loss 0.5361 |wh_loss 2.2381 |off_loss 0.0377 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1565/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7972 |hm_loss 0.5358 |wh_loss 2.2367 |off_loss 0.0377 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1566/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7967 |hm_loss 0.5355 |wh_loss 2.2352 |off_loss 0.0376 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1567/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7962 |hm_loss 0.5352 |wh_loss 2.2338 |off_loss 0.0376 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1568/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7957 |hm_loss 0.5349 |wh_loss 2.2324 |off_loss 0.0376 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1569/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7953 |hm_loss 0.5346 |wh_loss 2.2310 |off_loss 0.0376 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1570/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7948 |hm_loss 0.5343 |wh_loss 2.2295 |off_loss 0.0375 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1571/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7943 |hm_loss 0.5340 |wh_loss 2.2281 |off_loss 0.0375 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1572/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7939 |hm_loss 0.5337 |wh_loss 2.2267 |off_loss 0.0375 |Data 0.008s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1573/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7934 |hm_loss 0.5334 |wh_loss 2.2253 |off_loss 0.0375 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1574/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7929 |hm_loss 0.5331 |wh_loss 2.2239 |off_loss 0.0375 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1575/2110]|Tot: 0:00:34 |ETA: 0:00:00 |loss 0.7925 |hm_loss 0.5328 |wh_loss 2.2225 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1576/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7920 |hm_loss 0.5325 |wh_loss 2.2211 |off_loss 0.0374 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1577/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7915 |hm_loss 0.5322 |wh_loss 2.2196 |off_loss 0.0374 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1578/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7910 |hm_loss 0.5319 |wh_loss 2.2182 |off_loss 0.0374 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1579/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7906 |hm_loss 0.5316 |wh_loss 2.2168 |off_loss 0.0373 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1580/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7901 |hm_loss 0.5313 |wh_loss 2.2154 |off_loss 0.0373 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1581/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7896 |hm_loss 0.5310 |wh_loss 2.2140 |off_loss 0.0373 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1582/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7892 |hm_loss 0.5307 |wh_loss 2.2126 |off_loss 0.0373 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1583/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7887 |hm_loss 0.5304 |wh_loss 2.2112 |off_loss 0.0372 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1584/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7883 |hm_loss 0.5301 |wh_loss 2.2098 |off_loss 0.0372 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1585/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7878 |hm_loss 0.5298 |wh_loss 2.2085 |off_loss 0.0372 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1586/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7873 |hm_loss 0.5295 |wh_loss 2.2071 |off_loss 0.0372 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1587/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7869 |hm_loss 0.5292 |wh_loss 2.2057 |off_loss 0.0371 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1588/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7864 |hm_loss 0.5289 |wh_loss 2.2043 |off_loss 0.0371 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1589/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7859 |hm_loss 0.5286 |wh_loss 2.2029 |off_loss 0.0371 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1590/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7855 |hm_loss 0.5283 |wh_loss 2.2015 |off_loss 0.0371 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1591/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7850 |hm_loss 0.5280 |wh_loss 2.2001 |off_loss 0.0371 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1592/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7846 |hm_loss 0.5277 |wh_loss 2.1987 |off_loss 0.0370 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1593/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7841 |hm_loss 0.5274 |wh_loss 2.1974 |off_loss 0.0370 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1594/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7837 |hm_loss 0.5271 |wh_loss 2.1960 |off_loss 0.0370 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1595/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7832 |hm_loss 0.5268 |wh_loss 2.1946 |off_loss 0.0370 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1596/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7827 |hm_loss 0.5265 |wh_loss 2.1932 |off_loss 0.0369 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1597/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7823 |hm_loss 0.5262 |wh_loss 2.1919 |off_loss 0.0369 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1598/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7818 |hm_loss 0.5259 |wh_loss 2.1905 |off_loss 0.0369 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1599/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7814 |hm_loss 0.5256 |wh_loss 2.1891 |off_loss 0.0369 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1600/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7809 |hm_loss 0.5253 |wh_loss 2.1878 |off_loss 0.0368 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1601/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7805 |hm_loss 0.5250 |wh_loss 2.1864 |off_loss 0.0368 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1602/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7800 |hm_loss 0.5247 |wh_loss 2.1850 |off_loss 0.0368 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1603/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7796 |hm_loss 0.5244 |wh_loss 2.1837 |off_loss 0.0368 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1604/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7791 |hm_loss 0.5241 |wh_loss 2.1823 |off_loss 0.0368 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1605/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7786 |hm_loss 0.5238 |wh_loss 2.1810 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1606/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7782 |hm_loss 0.5235 |wh_loss 2.1796 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1607/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7777 |hm_loss 0.5232 |wh_loss 2.1782 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1608/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7773 |hm_loss 0.5229 |wh_loss 2.1769 |off_loss 0.0367 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1609/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7768 |hm_loss 0.5226 |wh_loss 2.1755 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1610/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7764 |hm_loss 0.5224 |wh_loss 2.1742 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1611/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7759 |hm_loss 0.5221 |wh_loss 2.1728 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1612/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7755 |hm_loss 0.5218 |wh_loss 2.1715 |off_loss 0.0366 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1613/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7750 |hm_loss 0.5215 |wh_loss 2.1701 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1614/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7746 |hm_loss 0.5212 |wh_loss 2.1688 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1615/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7742 |hm_loss 0.5209 |wh_loss 2.1675 |off_loss 0.0365 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1616/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7737 |hm_loss 0.5206 |wh_loss 2.1661 |off_loss 0.0365 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1617/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7733 |hm_loss 0.5203 |wh_loss 2.1648 |off_loss 0.0365 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1618/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7728 |hm_loss 0.5200 |wh_loss 2.1634 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1619/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7724 |hm_loss 0.5198 |wh_loss 2.1621 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1620/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7719 |hm_loss 0.5195 |wh_loss 2.1608 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1621/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7715 |hm_loss 0.5192 |wh_loss 2.1594 |off_loss 0.0364 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1622/2110]|Tot: 0:00:35 |ETA: 0:00:00 |loss 0.7711 |hm_loss 0.5189 |wh_loss 2.1581 |off_loss 0.0363 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1623/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7706 |hm_loss 0.5186 |wh_loss 2.1568 |off_loss 0.0363 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1624/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7702 |hm_loss 0.5183 |wh_loss 2.1555 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1625/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7697 |hm_loss 0.5180 |wh_loss 2.1541 |off_loss 0.0363 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1626/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7693 |hm_loss 0.5177 |wh_loss 2.1528 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1627/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7688 |hm_loss 0.5175 |wh_loss 2.1515 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1628/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7684 |hm_loss 0.5172 |wh_loss 2.1502 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1629/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7680 |hm_loss 0.5169 |wh_loss 2.1488 |off_loss 0.0362 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1630/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7675 |hm_loss 0.5166 |wh_loss 2.1475 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1631/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7671 |hm_loss 0.5163 |wh_loss 2.1462 |off_loss 0.0361 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1632/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7667 |hm_loss 0.5160 |wh_loss 2.1449 |off_loss 0.0361 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1633/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7662 |hm_loss 0.5158 |wh_loss 2.1436 |off_loss 0.0361 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1634/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7658 |hm_loss 0.5155 |wh_loss 2.1423 |off_loss 0.0361 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1635/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7653 |hm_loss 0.5152 |wh_loss 2.1410 |off_loss 0.0361 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1636/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7649 |hm_loss 0.5149 |wh_loss 2.1396 |off_loss 0.0360 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1637/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7645 |hm_loss 0.5146 |wh_loss 2.1383 |off_loss 0.0360 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1638/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7640 |hm_loss 0.5143 |wh_loss 2.1370 |off_loss 0.0360 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1639/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7636 |hm_loss 0.5141 |wh_loss 2.1357 |off_loss 0.0360 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1640/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7632 |hm_loss 0.5138 |wh_loss 2.1344 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1641/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7627 |hm_loss 0.5135 |wh_loss 2.1331 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1642/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7623 |hm_loss 0.5132 |wh_loss 2.1318 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1643/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7619 |hm_loss 0.5129 |wh_loss 2.1305 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1644/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7614 |hm_loss 0.5127 |wh_loss 2.1292 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1645/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7610 |hm_loss 0.5124 |wh_loss 2.1280 |off_loss 0.0358 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1646/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7606 |hm_loss 0.5121 |wh_loss 2.1267 |off_loss 0.0358 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1647/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7602 |hm_loss 0.5118 |wh_loss 2.1254 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1648/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7597 |hm_loss 0.5116 |wh_loss 2.1241 |off_loss 0.0358 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1649/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7593 |hm_loss 0.5113 |wh_loss 2.1228 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1650/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7589 |hm_loss 0.5110 |wh_loss 2.1215 |off_loss 0.0357 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1651/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7585 |hm_loss 0.5107 |wh_loss 2.1202 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1652/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7580 |hm_loss 0.5104 |wh_loss 2.1189 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1653/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7576 |hm_loss 0.5102 |wh_loss 2.1177 |off_loss 0.0357 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1654/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7572 |hm_loss 0.5099 |wh_loss 2.1164 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1655/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7568 |hm_loss 0.5096 |wh_loss 2.1151 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1656/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7563 |hm_loss 0.5093 |wh_loss 2.1138 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1657/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7559 |hm_loss 0.5091 |wh_loss 2.1125 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1658/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7555 |hm_loss 0.5088 |wh_loss 2.1113 |off_loss 0.0356 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1659/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7551 |hm_loss 0.5085 |wh_loss 2.1100 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1660/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7546 |hm_loss 0.5082 |wh_loss 2.1087 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1661/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7542 |hm_loss 0.5080 |wh_loss 2.1075 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1662/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7538 |hm_loss 0.5077 |wh_loss 2.1062 |off_loss 0.0355 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1663/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7534 |hm_loss 0.5074 |wh_loss 2.1049 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1664/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7530 |hm_loss 0.5072 |wh_loss 2.1037 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1665/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7525 |hm_loss 0.5069 |wh_loss 2.1024 |off_loss 0.0354 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1666/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7521 |hm_loss 0.5066 |wh_loss 2.1011 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1667/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7517 |hm_loss 0.5063 |wh_loss 2.0999 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1668/2110]|Tot: 0:00:36 |ETA: 0:00:00 |loss 0.7513 |hm_loss 0.5061 |wh_loss 2.0986 |off_loss 0.0353 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1669/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7509 |hm_loss 0.5058 |wh_loss 2.0974 |off_loss 0.0353 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1670/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7504 |hm_loss 0.5055 |wh_loss 2.0961 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1671/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7500 |hm_loss 0.5053 |wh_loss 2.0949 |off_loss 0.0353 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1672/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7496 |hm_loss 0.5050 |wh_loss 2.0936 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1673/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7492 |hm_loss 0.5047 |wh_loss 2.0924 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1674/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7488 |hm_loss 0.5045 |wh_loss 2.0911 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1675/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7484 |hm_loss 0.5042 |wh_loss 2.0899 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1676/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7480 |hm_loss 0.5039 |wh_loss 2.0886 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1677/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7475 |hm_loss 0.5037 |wh_loss 2.0874 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1678/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7471 |hm_loss 0.5034 |wh_loss 2.0861 |off_loss 0.0351 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1679/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7467 |hm_loss 0.5031 |wh_loss 2.0849 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1680/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7463 |hm_loss 0.5029 |wh_loss 2.0836 |off_loss 0.0351 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1681/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7459 |hm_loss 0.5026 |wh_loss 2.0824 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1682/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7455 |hm_loss 0.5023 |wh_loss 2.0812 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1683/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7451 |hm_loss 0.5021 |wh_loss 2.0799 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1684/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7447 |hm_loss 0.5018 |wh_loss 2.0787 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1685/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7443 |hm_loss 0.5015 |wh_loss 2.0775 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1686/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7438 |hm_loss 0.5013 |wh_loss 2.0762 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1687/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7434 |hm_loss 0.5010 |wh_loss 2.0750 |off_loss 0.0349 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1688/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7476 |hm_loss 0.5035 |wh_loss 2.0903 |off_loss 0.0351 |Data 0.006s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1689/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7472 |hm_loss 0.5032 |wh_loss 2.0890 |off_loss 0.0350 |Data 0.003s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1690/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7468 |hm_loss 0.5030 |wh_loss 2.0878 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1691/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7464 |hm_loss 0.5027 |wh_loss 2.0866 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1692/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7460 |hm_loss 0.5024 |wh_loss 2.0853 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1693/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7455 |hm_loss 0.5022 |wh_loss 2.0841 |off_loss 0.0350 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1694/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7451 |hm_loss 0.5019 |wh_loss 2.0829 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1695/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7447 |hm_loss 0.5016 |wh_loss 2.0817 |off_loss 0.0349 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1696/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7443 |hm_loss 0.5014 |wh_loss 2.0804 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1697/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7439 |hm_loss 0.5011 |wh_loss 2.0792 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1698/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7435 |hm_loss 0.5009 |wh_loss 2.0780 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1699/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7431 |hm_loss 0.5006 |wh_loss 2.0768 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1700/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7427 |hm_loss 0.5003 |wh_loss 2.0755 |off_loss 0.0348 |Data 0.010s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1701/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7423 |hm_loss 0.5001 |wh_loss 2.0743 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1702/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7419 |hm_loss 0.4998 |wh_loss 2.0731 |off_loss 0.0348 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1703/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7415 |hm_loss 0.4995 |wh_loss 2.0719 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1704/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7411 |hm_loss 0.4993 |wh_loss 2.0707 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1705/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7407 |hm_loss 0.4990 |wh_loss 2.0695 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1706/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7403 |hm_loss 0.4988 |wh_loss 2.0682 |off_loss 0.0347 |Data 0.009s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1707/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7399 |hm_loss 0.4985 |wh_loss 2.0670 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1708/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7395 |hm_loss 0.4982 |wh_loss 2.0658 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1709/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7391 |hm_loss 0.4980 |wh_loss 2.0646 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1710/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7387 |hm_loss 0.4977 |wh_loss 2.0634 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1711/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7383 |hm_loss 0.4975 |wh_loss 2.0622 |off_loss 0.0346 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1712/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7379 |hm_loss 0.4972 |wh_loss 2.0610 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1713/2110]|Tot: 0:00:37 |ETA: 0:00:00 |loss 0.7375 |hm_loss 0.4969 |wh_loss 2.0598 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1714/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7371 |hm_loss 0.4967 |wh_loss 2.0586 |off_loss 0.0345 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1715/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7367 |hm_loss 0.4964 |wh_loss 2.0574 |off_loss 0.0345 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1716/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7363 |hm_loss 0.4962 |wh_loss 2.0562 |off_loss 0.0345 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1717/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7359 |hm_loss 0.4959 |wh_loss 2.0550 |off_loss 0.0345 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1718/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7355 |hm_loss 0.4957 |wh_loss 2.0538 |off_loss 0.0345 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1719/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7351 |hm_loss 0.4954 |wh_loss 2.0526 |off_loss 0.0344 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1720/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7347 |hm_loss 0.4951 |wh_loss 2.0514 |off_loss 0.0344 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1721/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7343 |hm_loss 0.4949 |wh_loss 2.0502 |off_loss 0.0344 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1722/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7381 |hm_loss 0.4971 |wh_loss 2.0641 |off_loss 0.0346 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1723/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7411 |hm_loss 0.4989 |wh_loss 2.0747 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1724/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7439 |hm_loss 0.5006 |wh_loss 2.0836 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1725/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7435 |hm_loss 0.5003 |wh_loss 2.0824 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1726/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7431 |hm_loss 0.5001 |wh_loss 2.0812 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1727/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7427 |hm_loss 0.4998 |wh_loss 2.0800 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1728/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7423 |hm_loss 0.4995 |wh_loss 2.0788 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1729/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7419 |hm_loss 0.4993 |wh_loss 2.0776 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1730/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7415 |hm_loss 0.4990 |wh_loss 2.0764 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1731/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7411 |hm_loss 0.4988 |wh_loss 2.0752 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1732/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7407 |hm_loss 0.4985 |wh_loss 2.0740 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1733/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7403 |hm_loss 0.4983 |wh_loss 2.0728 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1734/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7399 |hm_loss 0.4980 |wh_loss 2.0716 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1735/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7395 |hm_loss 0.4977 |wh_loss 2.0704 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1736/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7391 |hm_loss 0.4975 |wh_loss 2.0692 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1737/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7387 |hm_loss 0.4972 |wh_loss 2.0681 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1738/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7383 |hm_loss 0.4970 |wh_loss 2.0669 |off_loss 0.0346 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1739/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7379 |hm_loss 0.4967 |wh_loss 2.0657 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1740/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7375 |hm_loss 0.4965 |wh_loss 2.0645 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1741/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7371 |hm_loss 0.4962 |wh_loss 2.0633 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1742/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7400 |hm_loss 0.4980 |wh_loss 2.0740 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1743/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7432 |hm_loss 0.4999 |wh_loss 2.0847 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1744/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7428 |hm_loss 0.4996 |wh_loss 2.0835 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1745/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7424 |hm_loss 0.4994 |wh_loss 2.0823 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1746/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7420 |hm_loss 0.4991 |wh_loss 2.0812 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1747/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7416 |hm_loss 0.4989 |wh_loss 2.0800 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1748/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7412 |hm_loss 0.4986 |wh_loss 2.0788 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1749/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7408 |hm_loss 0.4983 |wh_loss 2.0776 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1750/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7404 |hm_loss 0.4981 |wh_loss 2.0764 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1751/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7400 |hm_loss 0.4978 |wh_loss 2.0752 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1752/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7396 |hm_loss 0.4976 |wh_loss 2.0740 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1753/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7392 |hm_loss 0.4973 |wh_loss 2.0728 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1754/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7389 |hm_loss 0.4971 |wh_loss 2.0717 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1755/2110]|Tot: 0:00:38 |ETA: 0:00:00 |loss 0.7385 |hm_loss 0.4968 |wh_loss 2.0705 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1756/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7381 |hm_loss 0.4966 |wh_loss 2.0693 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1757/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7377 |hm_loss 0.4963 |wh_loss 2.0681 |off_loss 0.0346 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1758/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7373 |hm_loss 0.4961 |wh_loss 2.0670 |off_loss 0.0345 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1759/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7369 |hm_loss 0.4958 |wh_loss 2.0658 |off_loss 0.0345 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1760/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7365 |hm_loss 0.4956 |wh_loss 2.0646 |off_loss 0.0345 |Data 0.016s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1761/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7361 |hm_loss 0.4953 |wh_loss 2.0634 |off_loss 0.0345 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1762/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7358 |hm_loss 0.4951 |wh_loss 2.0623 |off_loss 0.0345 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1763/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7354 |hm_loss 0.4948 |wh_loss 2.0611 |off_loss 0.0344 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1764/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7350 |hm_loss 0.4946 |wh_loss 2.0599 |off_loss 0.0344 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1765/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7346 |hm_loss 0.4943 |wh_loss 2.0588 |off_loss 0.0344 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1766/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7342 |hm_loss 0.4941 |wh_loss 2.0576 |off_loss 0.0344 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1767/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7372 |hm_loss 0.4960 |wh_loss 2.0669 |off_loss 0.0344 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1768/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7403 |hm_loss 0.4981 |wh_loss 2.0764 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1769/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7437 |hm_loss 0.5002 |wh_loss 2.0846 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1770/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7463 |hm_loss 0.5024 |wh_loss 2.0883 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1771/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7491 |hm_loss 0.5046 |wh_loss 2.0935 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1772/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7522 |hm_loss 0.5068 |wh_loss 2.1009 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1773/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7556 |hm_loss 0.5090 |wh_loss 2.1118 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1774/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7591 |hm_loss 0.5112 |wh_loss 2.1230 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1775/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7623 |hm_loss 0.5135 |wh_loss 2.1318 |off_loss 0.0357 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1776/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7619 |hm_loss 0.5132 |wh_loss 2.1306 |off_loss 0.0357 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1777/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7615 |hm_loss 0.5129 |wh_loss 2.1294 |off_loss 0.0356 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1778/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7611 |hm_loss 0.5127 |wh_loss 2.1282 |off_loss 0.0356 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1779/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7607 |hm_loss 0.5124 |wh_loss 2.1270 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1780/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7603 |hm_loss 0.5122 |wh_loss 2.1258 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1781/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7599 |hm_loss 0.5119 |wh_loss 2.1246 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1782/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7595 |hm_loss 0.5117 |wh_loss 2.1234 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1783/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7591 |hm_loss 0.5114 |wh_loss 2.1222 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1784/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7588 |hm_loss 0.5112 |wh_loss 2.1210 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1785/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7584 |hm_loss 0.5109 |wh_loss 2.1199 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1786/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7580 |hm_loss 0.5106 |wh_loss 2.1187 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1787/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7576 |hm_loss 0.5104 |wh_loss 2.1175 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1788/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7572 |hm_loss 0.5101 |wh_loss 2.1163 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1789/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7568 |hm_loss 0.5099 |wh_loss 2.1151 |off_loss 0.0354 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1790/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7564 |hm_loss 0.5096 |wh_loss 2.1139 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1791/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7560 |hm_loss 0.5094 |wh_loss 2.1128 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1792/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7556 |hm_loss 0.5091 |wh_loss 2.1116 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1793/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7552 |hm_loss 0.5089 |wh_loss 2.1104 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1794/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7548 |hm_loss 0.5086 |wh_loss 2.1092 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1795/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7544 |hm_loss 0.5084 |wh_loss 2.1080 |off_loss 0.0353 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1796/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7541 |hm_loss 0.5081 |wh_loss 2.1069 |off_loss 0.0353 |Data 0.005s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1797/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7537 |hm_loss 0.5079 |wh_loss 2.1057 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1798/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7533 |hm_loss 0.5076 |wh_loss 2.1045 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1799/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7529 |hm_loss 0.5074 |wh_loss 2.1034 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1800/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7525 |hm_loss 0.5071 |wh_loss 2.1022 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1801/2110]|Tot: 0:00:39 |ETA: 0:00:00 |loss 0.7521 |hm_loss 0.5068 |wh_loss 2.1010 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1802/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7517 |hm_loss 0.5066 |wh_loss 2.0999 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1803/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7513 |hm_loss 0.5063 |wh_loss 2.0987 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1804/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7510 |hm_loss 0.5061 |wh_loss 2.0975 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1805/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7506 |hm_loss 0.5058 |wh_loss 2.0964 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1806/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7502 |hm_loss 0.5056 |wh_loss 2.0952 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1807/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7498 |hm_loss 0.5053 |wh_loss 2.0941 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1808/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7494 |hm_loss 0.5051 |wh_loss 2.0929 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1809/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7490 |hm_loss 0.5048 |wh_loss 2.0917 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1810/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7486 |hm_loss 0.5046 |wh_loss 2.0906 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1811/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7483 |hm_loss 0.5043 |wh_loss 2.0894 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1812/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7479 |hm_loss 0.5041 |wh_loss 2.0883 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1813/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7475 |hm_loss 0.5038 |wh_loss 2.0871 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1814/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7471 |hm_loss 0.5036 |wh_loss 2.0860 |off_loss 0.0349 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1815/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7467 |hm_loss 0.5033 |wh_loss 2.0848 |off_loss 0.0349 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1816/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7463 |hm_loss 0.5031 |wh_loss 2.0837 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1817/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7460 |hm_loss 0.5029 |wh_loss 2.0825 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1818/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7456 |hm_loss 0.5026 |wh_loss 2.0814 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1819/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7452 |hm_loss 0.5024 |wh_loss 2.0803 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1820/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7448 |hm_loss 0.5021 |wh_loss 2.0791 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1821/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7444 |hm_loss 0.5019 |wh_loss 2.0780 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1822/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7440 |hm_loss 0.5016 |wh_loss 2.0768 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1823/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7437 |hm_loss 0.5014 |wh_loss 2.0757 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1824/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7433 |hm_loss 0.5011 |wh_loss 2.0746 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1825/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7429 |hm_loss 0.5009 |wh_loss 2.0734 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1826/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7425 |hm_loss 0.5006 |wh_loss 2.0723 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1827/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7422 |hm_loss 0.5004 |wh_loss 2.0711 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1828/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7418 |hm_loss 0.5001 |wh_loss 2.0700 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1829/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7451 |hm_loss 0.5021 |wh_loss 2.0822 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1830/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7487 |hm_loss 0.5043 |wh_loss 2.0945 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1831/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7483 |hm_loss 0.5041 |wh_loss 2.0934 |off_loss 0.0349 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1832/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7479 |hm_loss 0.5038 |wh_loss 2.0922 |off_loss 0.0349 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1833/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7475 |hm_loss 0.5036 |wh_loss 2.0911 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1834/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7472 |hm_loss 0.5034 |wh_loss 2.0899 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1835/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7468 |hm_loss 0.5031 |wh_loss 2.0888 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1836/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7464 |hm_loss 0.5029 |wh_loss 2.0877 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1837/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7460 |hm_loss 0.5026 |wh_loss 2.0865 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1838/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7457 |hm_loss 0.5024 |wh_loss 2.0854 |off_loss 0.0347 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1839/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7484 |hm_loss 0.5041 |wh_loss 2.0942 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1840/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7511 |hm_loss 0.5059 |wh_loss 2.1016 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1841/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7540 |hm_loss 0.5078 |wh_loss 2.1097 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1842/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7569 |hm_loss 0.5097 |wh_loss 2.1191 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1843/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7599 |hm_loss 0.5117 |wh_loss 2.1280 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1844/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7626 |hm_loss 0.5138 |wh_loss 2.1332 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1845/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7652 |hm_loss 0.5159 |wh_loss 2.1379 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1846/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7683 |hm_loss 0.5180 |wh_loss 2.1468 |off_loss 0.0357 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1847/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7713 |hm_loss 0.5200 |wh_loss 2.1551 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1848/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7746 |hm_loss 0.5221 |wh_loss 2.1654 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1849/2110]|Tot: 0:00:40 |ETA: 0:00:00 |loss 0.7781 |hm_loss 0.5242 |wh_loss 2.1762 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1850/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7811 |hm_loss 0.5263 |wh_loss 2.1848 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1851/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7807 |hm_loss 0.5260 |wh_loss 2.1836 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1852/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7803 |hm_loss 0.5258 |wh_loss 2.1825 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1853/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7799 |hm_loss 0.5255 |wh_loss 2.1813 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1854/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7795 |hm_loss 0.5253 |wh_loss 2.1801 |off_loss 0.0363 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1855/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7791 |hm_loss 0.5250 |wh_loss 2.1789 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1856/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7788 |hm_loss 0.5248 |wh_loss 2.1778 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1857/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7784 |hm_loss 0.5245 |wh_loss 2.1766 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1858/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7780 |hm_loss 0.5243 |wh_loss 2.1754 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1859/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7776 |hm_loss 0.5240 |wh_loss 2.1742 |off_loss 0.0362 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1860/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7772 |hm_loss 0.5237 |wh_loss 2.1731 |off_loss 0.0361 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1861/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7768 |hm_loss 0.5235 |wh_loss 2.1719 |off_loss 0.0361 |Data 0.009s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1862/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7764 |hm_loss 0.5232 |wh_loss 2.1707 |off_loss 0.0361 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1863/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7760 |hm_loss 0.5230 |wh_loss 2.1696 |off_loss 0.0361 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1864/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7756 |hm_loss 0.5227 |wh_loss 2.1684 |off_loss 0.0361 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1865/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7753 |hm_loss 0.5225 |wh_loss 2.1673 |off_loss 0.0360 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1866/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7749 |hm_loss 0.5222 |wh_loss 2.1661 |off_loss 0.0360 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1867/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7745 |hm_loss 0.5220 |wh_loss 2.1649 |off_loss 0.0360 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1868/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7741 |hm_loss 0.5217 |wh_loss 2.1638 |off_loss 0.0360 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1869/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7737 |hm_loss 0.5215 |wh_loss 2.1626 |off_loss 0.0360 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1870/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7733 |hm_loss 0.5212 |wh_loss 2.1615 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1871/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7729 |hm_loss 0.5210 |wh_loss 2.1603 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1872/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7726 |hm_loss 0.5207 |wh_loss 2.1592 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1873/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7722 |hm_loss 0.5205 |wh_loss 2.1580 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1874/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7718 |hm_loss 0.5202 |wh_loss 2.1569 |off_loss 0.0359 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1875/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7714 |hm_loss 0.5200 |wh_loss 2.1557 |off_loss 0.0359 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1876/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7710 |hm_loss 0.5197 |wh_loss 2.1546 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1877/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7706 |hm_loss 0.5195 |wh_loss 2.1534 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1878/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7703 |hm_loss 0.5192 |wh_loss 2.1523 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1879/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7699 |hm_loss 0.5190 |wh_loss 2.1511 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1880/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7695 |hm_loss 0.5187 |wh_loss 2.1500 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1881/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7691 |hm_loss 0.5185 |wh_loss 2.1488 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1882/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7687 |hm_loss 0.5182 |wh_loss 2.1477 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1883/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7720 |hm_loss 0.5203 |wh_loss 2.1601 |off_loss 0.0358 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1884/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7747 |hm_loss 0.5221 |wh_loss 2.1687 |off_loss 0.0358 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1885/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7743 |hm_loss 0.5218 |wh_loss 2.1676 |off_loss 0.0357 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1886/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7739 |hm_loss 0.5216 |wh_loss 2.1664 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1887/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7735 |hm_loss 0.5213 |wh_loss 2.1653 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1888/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7732 |hm_loss 0.5211 |wh_loss 2.1641 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1889/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7728 |hm_loss 0.5208 |wh_loss 2.1630 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1890/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7724 |hm_loss 0.5206 |wh_loss 2.1618 |off_loss 0.0357 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1891/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7720 |hm_loss 0.5203 |wh_loss 2.1607 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1892/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7716 |hm_loss 0.5201 |wh_loss 2.1596 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1893/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7713 |hm_loss 0.5198 |wh_loss 2.1584 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1894/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7709 |hm_loss 0.5196 |wh_loss 2.1573 |off_loss 0.0356 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1895/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7705 |hm_loss 0.5193 |wh_loss 2.1561 |off_loss 0.0356 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1896/2110]|Tot: 0:00:41 |ETA: 0:00:00 |loss 0.7701 |hm_loss 0.5191 |wh_loss 2.1550 |off_loss 0.0355 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1897/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7697 |hm_loss 0.5188 |wh_loss 2.1539 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1898/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7694 |hm_loss 0.5186 |wh_loss 2.1527 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1899/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7690 |hm_loss 0.5183 |wh_loss 2.1516 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1900/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7686 |hm_loss 0.5181 |wh_loss 2.1505 |off_loss 0.0355 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1901/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7682 |hm_loss 0.5178 |wh_loss 2.1493 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1902/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7679 |hm_loss 0.5176 |wh_loss 2.1482 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1903/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7675 |hm_loss 0.5174 |wh_loss 2.1471 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1904/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7671 |hm_loss 0.5171 |wh_loss 2.1460 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1905/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7667 |hm_loss 0.5169 |wh_loss 2.1448 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1906/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7663 |hm_loss 0.5166 |wh_loss 2.1437 |off_loss 0.0354 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1907/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7660 |hm_loss 0.5164 |wh_loss 2.1426 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1908/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7656 |hm_loss 0.5161 |wh_loss 2.1415 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1909/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7652 |hm_loss 0.5159 |wh_loss 2.1403 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1910/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7649 |hm_loss 0.5157 |wh_loss 2.1392 |off_loss 0.0353 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1911/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7645 |hm_loss 0.5154 |wh_loss 2.1381 |off_loss 0.0353 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1912/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7641 |hm_loss 0.5152 |wh_loss 2.1370 |off_loss 0.0352 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1913/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7637 |hm_loss 0.5149 |wh_loss 2.1359 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1914/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7634 |hm_loss 0.5147 |wh_loss 2.1347 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1915/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7630 |hm_loss 0.5144 |wh_loss 2.1336 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1916/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7626 |hm_loss 0.5142 |wh_loss 2.1325 |off_loss 0.0352 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1917/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7622 |hm_loss 0.5140 |wh_loss 2.1314 |off_loss 0.0352 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1918/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7619 |hm_loss 0.5137 |wh_loss 2.1303 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1919/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7615 |hm_loss 0.5135 |wh_loss 2.1292 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1920/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7611 |hm_loss 0.5132 |wh_loss 2.1281 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1921/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7608 |hm_loss 0.5130 |wh_loss 2.1270 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1922/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7604 |hm_loss 0.5128 |wh_loss 2.1259 |off_loss 0.0351 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1923/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7600 |hm_loss 0.5125 |wh_loss 2.1248 |off_loss 0.0350 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1924/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7597 |hm_loss 0.5123 |wh_loss 2.1237 |off_loss 0.0350 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1925/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7593 |hm_loss 0.5120 |wh_loss 2.1226 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1926/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7589 |hm_loss 0.5118 |wh_loss 2.1215 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1927/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7586 |hm_loss 0.5116 |wh_loss 2.1204 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1928/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7582 |hm_loss 0.5113 |wh_loss 2.1193 |off_loss 0.0350 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1929/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7578 |hm_loss 0.5111 |wh_loss 2.1182 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1930/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7575 |hm_loss 0.5108 |wh_loss 2.1171 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1931/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7571 |hm_loss 0.5106 |wh_loss 2.1160 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1932/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7567 |hm_loss 0.5104 |wh_loss 2.1149 |off_loss 0.0349 |Data 0.017s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1933/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7564 |hm_loss 0.5101 |wh_loss 2.1138 |off_loss 0.0349 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1934/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7560 |hm_loss 0.5099 |wh_loss 2.1127 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1935/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7556 |hm_loss 0.5097 |wh_loss 2.1116 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1936/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7553 |hm_loss 0.5094 |wh_loss 2.1105 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1937/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7549 |hm_loss 0.5092 |wh_loss 2.1094 |off_loss 0.0348 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1938/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7546 |hm_loss 0.5090 |wh_loss 2.1083 |off_loss 0.0348 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1939/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7542 |hm_loss 0.5087 |wh_loss 2.1072 |off_loss 0.0348 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1940/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7538 |hm_loss 0.5085 |wh_loss 2.1062 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1941/2110]|Tot: 0:00:42 |ETA: 0:00:00 |loss 0.7535 |hm_loss 0.5083 |wh_loss 2.1051 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1942/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7531 |hm_loss 0.5080 |wh_loss 2.1040 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1943/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7528 |hm_loss 0.5078 |wh_loss 2.1029 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1944/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7524 |hm_loss 0.5076 |wh_loss 2.1018 |off_loss 0.0347 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1945/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7520 |hm_loss 0.5073 |wh_loss 2.1007 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1946/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7517 |hm_loss 0.5071 |wh_loss 2.0997 |off_loss 0.0346 |Data 0.002s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1947/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7513 |hm_loss 0.5069 |wh_loss 2.0986 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1948/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7510 |hm_loss 0.5066 |wh_loss 2.0975 |off_loss 0.0346 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1949/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7506 |hm_loss 0.5064 |wh_loss 2.0964 |off_loss 0.0346 |Data 0.000s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1950/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7548 |hm_loss 0.5082 |wh_loss 2.1193 |off_loss 0.0346 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1951/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7587 |hm_loss 0.5100 |wh_loss 2.1392 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1952/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7623 |hm_loss 0.5119 |wh_loss 2.1558 |off_loss 0.0349 |Data 0.001s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1953/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7657 |hm_loss 0.5137 |wh_loss 2.1700 |off_loss 0.0350 |Data 0.004s(0.001s) |Net 0.022s
ctdet/coco_dla| val: [5][1954/2110]|Tot: 0:00:43 |ETA: 0:00:00 |loss 0.7684 |hm_loss 0.5154 |wh_loss 2.1795 |off_loss 0.0351 |Data 0.000s(0.001s) |Net 0.022s
Traceback (most recent call last):
  File "main.py", line 105, in <module>
    main(opt)
  File "main.py", line 82, in main
    log_dict_val, preds = trainer.val(epoch, val_loader)
  File "/root/c/src/lib/trains/base_trainer.py", line 116, in val
    return self.run_epoch('val', epoch, data_loader)
  File "/root/c/src/lib/trains/base_trainer.py", line 61, in run_epoch
    for iter_id, batch in enumerate(data_loader):
  File "/root/.pyenv/versions/3.6.9/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 336, in __next__
    return self._process_next_batch(batch)
  File "/root/.pyenv/versions/3.6.9/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 357, in _process_next_batch
    raise batch.exc_type(batch.exc_msg)
AttributeError: Traceback (most recent call last):
  File "/root/.pyenv/versions/3.6.9/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 106, in _worker_loop
    samples = collate_fn([dataset[i] for i in batch_indices])
  File "/root/.pyenv/versions/3.6.9/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 106, in <listcomp>
    samples = collate_fn([dataset[i] for i in batch_indices])
  File "/root/c/src/lib/datasets/sample/ctdet.py", line 40, in __getitem__
    height, width = img.shape[0], img.shape[1]
AttributeError: 'NoneType' object has no attribute 'shape'

