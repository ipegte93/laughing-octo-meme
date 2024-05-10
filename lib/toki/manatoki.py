import lib
from lib import path
import os


def manatoki(number: int) -> None:
    PATH = path.MANATOKI
    FILTER = path.FILTER
    URL = f"manatoki{number}.net"
    TXT_LIST = os.listdir(PATH)

    with open(FILTER / "manatoki.txt", "w", encoding="utf-8") as f:  # INITIALIZE
        # f.writelines(URL+"###viewcomment\n")  # 댓글
        # f.writelines(URL+"##.comment-box\n")  # 댓글 입력창
        f.writelines(URL + "##.sticky-wrapper > header > div > *\n")  # 로고

    _manatoki = open(FILTER / "manatoki.txt", "a", encoding="utf-8")

    for txt in TXT_LIST:
        with open(PATH / txt, "r", encoding="utf-8") as f_r:
            data = f_r.read()
            data = lib.sort(data)

        with open(PATH / txt, "w", encoding="utf-8") as f_w:  # 정렬 후 저장
            _data = lib.list_str(data)
            f_w.write(_data)

        for i in range(len(data)):
            selecter = f'###webtoon-list-all > li[date-title="{data[i]}"]\n'
            data[i] = URL + selecter

        for i in data:
            _manatoki.writelines(i)

    _manatoki.close()