# super resolution
pytorchを使用して画像の超解像を実行できます。

このリポジトリではSRGAN<sup>1)</sup>とEDSR<sup>2)</sup>の2種類の超解像をサポートしています。

実行環境と使用方法は下記の通りです。

<br>

## 実行環境(env)
- Python 3.7.9
- Pytorch 1.3.1
- Numpy 1.19.2
- Opencv 3.4.2
- Matplotlib 3.3.2
- Pillow 8.0.1

<br>

## 使用方法(usage)
1. リポジトリをクローンします。
```
git clone https://github.com/itch0323/super_resolution.git
cd super_resolution
```

<br>

2. ディレクトリを移動し、anacondaで作成した環境を読み込んで切り替えます。
```
conda env create sr -f=setup/sr.yml
conda activate pytorch
```

<br>

3. データセットをダウンロードし、整形します。1Gb程度の空き容量が必要になるため注意してください。
```
sh setup.sh
```

### 【ダウンロードに失敗した場合】

- ダウンロードできない場合はサイト<a href="https://www.kkaneko.jp/data/od/celeba.html">このサイト</a>の手順に従い、データセットをダウンロードします。次に setup/create_datasets.py 内の変数 path にデータセットのディレクトリパスを設定し、下記スクリプトを実行してください。
```
python setup/create_datasets.py
```

<br>

4. 超解像を実行します。
- SRGAN
```
cd srgan
python srgan.py
```
<br>

- EDSR
```
cd edsr_img
python edsr_img.py
```
<br>

画像ではなくバイナリを読み込んで超解像を行うプログラムも用意しました。
```
cd edsr_bin
python edsr_bin.py
```
<br>

5. jupyter notebook上で作成したモデルを試すことができます。

<br>

## 論文
<p>1) Christian Ledig, Lucas Theis, Ferenc Huszar, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew Aitken, Alykhan Tejani, Johannes Totz, Zehan Wang, Wenzhe Shi.<a href="https://arxiv.org/abs/1609.04802">　Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network</a>

<p>2) Bee Lim, Sanghyun Son, Heewon Kim, Seungjun Nah, Kyoung Mu Lee.<a href="https://arxiv.org/abs/1707.02921">　Enhanced Deep Residual Networks for Single Image Super-Resolution</a>