# PicPong
* 现在markdown越用越频繁了, md好用是好用, 但就是贴图片的时候有些麻烦: 要截图->上传图片->复制图片url, 于是做了个简单的工具: `截图->传图->生成图片url`三合一

## 依赖
* python版本建议3.10
* package依赖见`requirements.txt`

## 配置
* 根目录的`config.json`里面的`SecretToken`填自己的sm.ms的Token, 如果没有则到https://sm.ms 自行申请

## 效果

* 截图上传(也可以用快捷键`ctrl+shift+alt+F8`)

![GIF1.gif](https://i.loli.net/2018/10/25/5bd1b6bc0ce73.gif)

* 上传后自动将图片url复制到剪贴板, 直接粘贴即可

![GIF2.gif](https://i.loli.net/2018/10/25/5bd1b75390dec.gif)

* 也可以选择图片上传

![GIF4.gif](https://i.loli.net/2018/10/25/5bd1b786a5f92.gif)

* 也可以直接拖到框中上传

![GIF5.gif](https://i.loli.net/2018/10/25/5bd1b7c38eded.gif)