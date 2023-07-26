# 交谊舞爬虫
### 支持多线程
## 使用方法
#### 1.下载相关依赖
 pip install -r requirement.txt
#### 2.打开官网https://www.dggwq.com，选取想要下载的音乐，并获取音乐的id
进入歌曲详细页面后，歌曲id在网址上
![Alt text](image.png)
#### 3.在music_ids.txt中输入歌曲的id，每行输入一个
#### 4.启动main.py脚本，爬取音乐
   ```
   python main.py
   ```
#### 5.爬取的音乐在“下载的歌曲”文件夹中，自动编号