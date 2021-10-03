# face-recognizer-experiment

基于 `opencv-python` 的人脸识别系统

---

> data_gen.py

获取人脸数据并存储

---

> trainner.py

训练模型

---

> reco.py

识别人脸

---

文件中`haarcascade_frontalface_alt.xml`需更改为自己环境中的路径

若要下载到本地参考，运行步骤：

1. `pip install pipenv`
2. 切换至此项目根目录`pipenv install`
3. 获取人脸数据`pipenv run data_gen.py`,生成目录，里面是人脸图片
4. 训练模型`pipenv run trainner.py`,生成`trainner.xml`
5. 识别人脸`pipenv run reco.py`

> 注：`reco.py` 里面的 `handle` 方法是对开发板的控制，若未连接开发板,仅在识别成功时显示 `user1` 字符串，识别失败时显示 `Unknown` 字符串.

实验时间:2021.09.22 - 2021.09.26
