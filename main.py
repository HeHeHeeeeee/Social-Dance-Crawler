import requests
import os
from concurrent.futures import ThreadPoolExecutor


def main():
    # 指定要创建的文件夹路径
    download_folder_path = f"./下载的歌曲"
    if not os.path.exists(download_folder_path):
        # 文件夹不存在则创建
        os.makedirs(download_folder_path)

    # 读入音乐id列表
    id_list = []
    music_ids_path = "./music_ids.txt"
    with open(music_ids_path, "rt", encoding="utf-8") as f:
        id_list = f.readlines()

    # 创建线程池
    with ThreadPoolExecutor() as executor:
        executor.map(download_mp3, id_list, download_folder_path)

def download_mp3(id: int, download_folder_path: str):
    userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"

    api = f"https://www.dggwq.com/js/url.php?id={id}"
    #cookie = "Hm_lvt_e6186d8b90f5a34afb05cc151292844d=1690266344; PHPSESSID=cde672thcdj8o808vjo8gm2213; Hm_lvt_3b1546f0e4ee125a0dda33500e055418=1690267035; s_id=5391; s_name=13617915869; Hm_lpvt_3b1546f0e4ee125a0dda33500e055418=1690268396; Hm_lpvt_e6186d8b90f5a34afb05cc151292844d=1690270388"
    mp3_url = requests.get(url=api, headers={"User-Agent": userAgent})#, "Cookie": cookie})
    print(mp3_url)
    download_mp3 = requests.get(mp3_url).content
    download_path = download_folder_path + mp3_url.rsplit("/", 1)[-1]
    download_path = download_path.lsplit(".")[-1]
    with open(download_path, "wb") as f:
        f.write(download_mp3)
    print(f"下载完成: {download_path}")


if __name__ == "__main__":
    main()
