#### Windows用户

##### 1. 下载项目并解压

##### 2.打开运行，输入cmd，打开终端 

> Win+R 输入cmd 

##### 3. 使用终端进入到项目的根目录下

首先进入到项目对应的磁盘中，然后执行

> cd path\to\project

##### 4. 初始化环境并登录

下载完成之后，执行下列命令并使用微信扫码登录

> flyai.bat init

登录成功之后，会自动下载运行所需环境

##### 5. 本地开发调试

执行

> flyai.bat test 

安装项目所需依赖，并运行 main.py

如果使用本地IDE开发，可以自行安装 requirements.txt 中的依赖，运行 main.py 即可

##### 6.提交训练到GPU

项目中如有新的引用，需加入到 requirements.txt 文件中

在终端下执行

> flyai.bat train

返回sucess状态，代表提交离线训练成功

默认训练成功后不公开在项目排行榜中，公开项目需在提交训练时执行

> flyai.bat train -p=1

完整训练设置执行代码示例：

> flyai.bat train -p=1 -b=32 -e=100

通过执行训练命令，本次训练循环 100 次，每次训练读取的数据量为 32 ，公开提交模型

#### Mac或Linux用户

##### 1. 下载项目并解压

##### 2. 使用终端进入到项目的根目录下
> cd /path/to/project

##### 3. 初始化环境并登录
授权flyai

> chmod +x ./flyai

下载完成之后，执行下列命令并使用微信扫码登录

>  ./flyai init

登录成功之后，会自动下载运行所需环境

##### 4. 本地开发调试
执行

> ./flyai test 

安装项目所需依赖，并运行 main.py

如果使用本地IDE开发，可以自行安装 requirements.txt 中的依赖，运行 main.py 即可

##### 5.提交训练到GPU
项目中如有新的引用，需加入到 requirements.txt 文件中

在终端下执行

> ./flyai train

返回sucess状态，代表提交离线训练成功，训练结束会以微信和邮件的形式发送结果通知

默认训练成功后不公开在项目排行榜中，公开项目需在提交训练时执行

> ./flyai train -p=1

完整训练设置执行代码示例：

> ./flyai train -p=1 -b=32 -e=100

通过执行训练命令，本次训练循环 100 次，每次训练读取的数据量为 32 ，公开提交模型



### [FlyAI——AI竞赛服务平台](https://flyai.com)

**扫描下方二维码，及时获取FlyAI最新消息，抢先体验最新功能。**



[![GPL LICENSE](https://www.flyai.com/images/coding.png)](https://flyai.com)





