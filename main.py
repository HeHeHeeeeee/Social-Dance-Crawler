from threading import BoundedSemaphore
import requests
import os
from concurrent.futures import ThreadPoolExecutor


def main():
    social_dance_download = Social_Dance_Download()
    # 指定要创建的文件夹路径
    download_folder_path = "下载的歌曲"
    if not os.path.exists(download_folder_path):
        # 文件夹不存在则创建
        os.makedirs(download_folder_path)

    # 读入音乐id列表
    id_list = []
    music_ids_path = "music_ids.txt"
    with open(music_ids_path, "rt", encoding="utf-8") as f:
        id_list = f.readlines()

    # 创建线程池
    with ThreadPoolExecutor() as executor:
        executor.map(social_dance_download.download_mp3, id_list, [download_folder_path for _ in range(len(id_list))])
    # for idd in id_list:
    #     print(idd)
    #     social_dance_download.download_mp3(id=idd, download_folder_path=download_folder_path)

class Social_Dance_Download:

    def __init__(self):
        self.num = 1
        self.sem = BoundedSemaphore(1)

    def download_mp3(self, id, download_folder_path: str):
        userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"

        api = f"https://www.dggwq.com/js/url.php?id={id}"
        # 获取歌曲链接
        mp3_url = requests.get(url=api, headers={"User-Agent": userAgent})
        mp3_url = mp3_url.content.decode("utf-8")
        # 下载歌曲
        download_mp3 = requests.get(mp3_url)

        # 分离出歌曲名
        song_name = mp3_url.rsplit("/", 1)[-1]
        song_name = song_name.split(".", maxsplit=1)[-1]
        # print(song_name)

        # 获取锁，避免文件数量更新不一致
        self.sem.acquire()
        song_name = str(self.num) + "." + song_name
        # 拼接文件路径
        download_path = os.path.join(download_folder_path ,song_name)
        self.num = self.num+1
        self.sem.release()
        
        # print(download_path)
        # 写入文件
        try:
            with open(download_path, "wb") as f:
                f.write(download_mp3.content)
        except:
            print("文件写入错误")

        # print(download_path)
        
        print(f"下载完成: {song_name}")


if __name__ == "__main__":
    main()
    # social_dance_download = Social_Dance_Download()
    # social_dance_download.download_mp3(63275, "./下载的歌曲")
