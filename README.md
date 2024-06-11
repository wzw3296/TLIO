Important Notes:

Please read the paper: https://arxiv.org/abs/2007.01867 first

Original github : https://github.com/CathIAS/TLIO

The whole project is under the server directory [SSH:128.122.136.173]:  /home/wzw/Desktop/imuProject/TLIO
(Register a Unav ID first if you do not have)

The best way to continue the project is to run and modify the code on the server.
If you cannot access the server, only running on the local, please download the data [here](https://drive.google.com/file/d/10Bc6R-s0ZLy9OEK_1mfpmtDg3jIu8X6g/view?usp=share_link) additionaly and unzip it under the TLIO folder(the name "golden-new-format-cc-by-nc-with-imus" do not change). 

To initialize the project environment on the sever:

cd ~/Desktop/imuProject/TLIO
conda activate TLIO


train command:
python src/main_net.py --mode train --root_dir golden-new-format-cc-by-nc-with-imus --out_dir models/resnet --epochs 100

test command: 
python src/main_net.py --mode test --root_dir golden-new-format-cc-by-nc-with-imus --model_path models/resnet/checkpoint_best.pt --out_dir test_outputs --rpe_window 0.6

The whole dataset(including training and test set) is under the folder dir:  golden-new-format-cc-by-nc-with-imus. To modify the dataset or train/test the new models, you can add or remove contents in the dir golden-new-format.. folder, then change the data_folder names in the train_list.txt, test_list.txt or val_list.txt. Then use the train command or test command.(train_list.txt, test_list.txt or val_list.txt are used to assign the dataset to be used in the test or training process.)

Using the train command, the output model is under the dir: /home/wzw/Desktop/imuProject/TLIO/models/resnet, which is checkpoint_best.pt.
You can change the training epochs steps by changing the last para 100 in the train command.

Using the test command, the output is under the dir:  /home/wzw/Desktop/imuProject/TLIO/test_outputs. The output folder names are those in the test_list.txt. 

At present, the results can show that short distance can be predicted and followed, long cannot.(You can see the test_outputs folder: view.png) 
More command details can be found in the src/main_net.py, detail information see the refer paper and codes.

