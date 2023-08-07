# ClearViewProcessor
Tools for image sharpening

### 実装しているフィルタ

## Retinex
Retinexとは...
Retinexフィルタは画像の輝度の補正を行うためのアルゴリズムの一つです。 光の乏しいところでもヒトの目は色を見分けられるのにカメラやビデオカメラはそれがちゃんと処理できません。 
Retinexフィルタの根幹をなすMSRCR (MultiScale Retinex with Color Restoration) とはヒトの目がその場の状況に合わせる生物学的構造をもっていることに着目したアルゴリズムです。 
レティネックスは1971年に登場した retina (網膜) と cortex (皮質) の合成語です。

![image](https://github.com/suke-toudara/ClearViewProcessor/assets/82552894/7b666ff5-b0c7-4e8f-a816-90103827aaa4)


・ガウシアンフィルタ部分　確率密度関数とかいろいろ使っているので激重
　⇨blurとかにすれば0,14まで軽くなった、ただし出力は微妙


## sample

![image](https://github.com/suke-toudara/ClearViewProcessor/assets/82552894/27f40a1a-6ce0-47ae-8e88-c492fec0754a)

 ![image](https://github.com/suke-toudara/ClearViewProcessor/assets/82552894/930ea1b3-872f-492f-b263-be37af2d1ce9)

## ホワイトバランス調整
ホワイトバランスの調整をして、なるべく自然色に戻してあげてる。
Lab空間に写してごにょごにょするだけ


