import time
from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import Actions


# 滑块验证码
def get_tracks(distance):
    """
    根据滑块距离获取滑块轨迹
    :param distance: 滑块距离
    :return: 滑块轨迹
    """
    v = 0
    t = 0.3  # 时间间隔
    track = []
    current = 0
    mid = distance * 4 / 5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t  # 加速度
        move = v0 * t + 0.5 * a * t * t  # 位移
        current += move
        track.append(round(move))
    return track


page = ChromiumPage()
ac = Actions(page)
page.get(
    "https://neris.csrc.gov.cn/shixinchaxun/searchResult?obj_name=%E9%97%AE%E9%97%AE&real_cardnumber=%E9%97%AE%E9%97%AE"
)
page.ele("@class=searchBtn").click()
time.sleep(5)
page.ele("@class=verify-move-block").hover()

ele = page.ele("@class=verify-move-block")
ac.hold(ele)
# ac.hold("@class=verify-move-block")


distance = 150
tracks = get_tracks(distance)
for track in tracks:
    print(f"滑动距离：{track}")
    ac.move(track, 0)

ac.release(ele)
# ac.release("@class=verify-move-block")
