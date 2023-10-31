# Federated Learning with Side Window Filter

Use the side window filter to reduce the influence of attackers in federated learning.



## Requirements
torch
torchvision
pandas
matplotlib



## KeyCode
the code that add side window filter into federated learning is in ./models/Fed.py

change the radio of attackers in main_fed_with_attack.py line 65



## Run

Federated learning with MLP and CNN is produced by:
> python [main_fed.py](main_fed.py)

See the arguments in [options.py](utils/options.py). 

For example:
> python main_fed.py --dataset mnist --iid --num_channels 1 --model cnn --epochs 50 --gpu 0  --all_clients

`--all_clients` for averaging over all client models

Please change the radio of attackers in main_fed_with_attack.py line 65



## References

[1] H. B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas, ‘Communication-Efficient Learning of Deep Networks from Decentralized Data’. arXiv, Jan. 26, 2023. Accessed: Oct. 31, 2023. [Online]. Available: http://arxiv.org/abs/1602.05629

[2] H. Yin, Y. Gong, and G. Qiu, ‘Side Window Filtering’, in *2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, Long Beach, CA, USA: IEEE, Jun. 2019, pp. 8750–8758. doi: [10.1109/CVPR.2019.00896](https://doi.org/10.1109/CVPR.2019.00896).




## Based the code
Shaoxiong Ji. (2018, March 30). A PyTorch Implementation of Federated Learning. Zenodo. http://doi.org/10.5281/zenodo.4321561


