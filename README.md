# PyTorch-JAANet
This repository is a fork of the PyTorch implementation of [JAA-Net](http://openaccess.thecvf.com/content_ECCV_2018/papers/Zhiwen_Shao_Deep_Adaptive_Attention_ECCV_2018_paper.pdf), as well as [its extended journal version](https://arxiv.org/pdf/2003.08834.pdf). "*v1.py" is for the ECCV version, and "*v2.py" is for the IJCV version. This fork is used for CS 188 Deep Learning for Computer Vision class project at UCLA. The trained model can be found under data/snapshots in this repository, with 12 models in total, each being a snapshot after 1 epoch. Our dataset is significantly smaller, thus the model performs worse. Generated sample heatmaps using the trained model can be found under data/res/JAAv1/vis_map. The trained models from the original paper can be downloaded [here](https://sjtueducn-my.sharepoint.com/:f:/g/personal/shaozhiwen_sjtu_edu_cn/Eu3SDFcZYG9Ah5RdRYqfYxoBWDyWici_FdWJP8TnYFqaZw?e=ogNmZv). The original Caffe implementation can be found [here](https://github.com/ZhiwenShao/JAANet)

# Getting Started
## Installation
- This code was tested with PyTorch 1.1.0 and Python 3.5
- Clone this repo:
```
git clone https://github.com/HiccupHan/CS188-PyTorch-JAANet
cd PyTorch-JAANet
```

## Datasets
[BP4D](http://www.cs.binghamton.edu/~lijun/Research/3DFE/3DFE_Analysis.html)

Put BP4D dataset images into the folder "dataset" following the paths shown in the list files of the folder "data/list". Place AU annotation file in the same folder. The path file can be modified, and file write_all_path.py can be used for this purpose. Run
  ```
  python write_all_path.py --foldpath 'path to image folder' --outputpath 'path to output image path text file'
  ```
Currently BP4D_combine_1_2_path.txt are image paths for training and BP4D_part3_path.txt are paths for testing. The same naming scheme is used for AU annotation files ending in AUOccur.txt.

Check_data.py in the main folder was used for our purposes to check for mismatches in data and should be disregarded.

## Preprocessing
- Put the landmark annotation files into the folder "dataset". Files provided are BP4D_combine_1_2_land.txt for training, BP4D_part3_land.txt for testing, and BP4D_att_land.txt and BP4D_att2_land.txt for generating the sample attention heatmaps. 

- Conduct similarity transformation for face images:
  ```
  cd dataset
  python face_transform.py
  ```
- Compute the inter-ocular distance of each face image:
  ```
  cd dataset
  python write_biocular.py
  ```
- Compute the weight of the loss of each AU for the training set:
  - The AU annoatation files should be in the folder "data/list"
  ```
  cd dataset
  python write_AU_weight.py
  ```
- Remeber to modify the files and change file paths to your own in all three python files mentioned above.

## Training
- Train on BP4D with the first two folds for training and the third fold for testing:
```
python train_JAAv1.py --run_name='JAAv1' --gpu_id=0 --train_batch_size=16 --eval_batch_size=28 --train_path_prefix='data/list/BP4D_combine_1_2' --test_path_prefix='data/list/BP4D_part3' --au_num=12
```
- The codebase can train on DISFA dataset, for more details please visit the original codebase.
## Testing
- Test the models saved in different epochs:
```
python test_JAAv1.py --run_name='JAAv1' --gpu_id=0 --start_epoch=1 --n_epochs=12 --eval_batch_size=28 --test_path_prefix='data/list/BP4D_part3' --au_num=12
```
- Visualize attention maps
```
python test_JAAv1.py --run_name='JAAv1' --gpu_id=0 --pred_AU=False --vis_attention=True --start_epoch=5 --n_epochs=5 --test_path_prefix='data/list/BP4D_part3' --au_num=12
```

## Citation
- If you use this code for your research, DON'T. This code is intended only for viewing and recreational purposes. Please go to https://github.com/ZhiwenShao/PyTorch-JAANet and cite the original papers
```
@inproceedings{shao2018deep,
  title={Deep Adaptive Attention for Joint Facial Action Unit Detection and Face Alignment},
  author={Shao, Zhiwen and Liu, Zhilei and Cai, Jianfei and Ma, Lizhuang},
  booktitle={European Conference on Computer Vision},
  year={2018},
  pages={725--740},
  organization={Springer}
}
@article{shao2020jaa,
  title={J{\^A}A-Net: Joint Facial Action Unit Detection and Face Alignment via Adaptive Attention},
  author={Shao, Zhiwen and Liu, Zhilei and Cai, Jianfei and Ma, Lizhuang},
  journal={International Journal of Computer Vision},
  year={2020},
  publisher={Springer}
}
```
