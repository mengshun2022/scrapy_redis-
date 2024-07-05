import time
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Actions

path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # 请改为你电脑内Chrome可执行文件路径
ChromiumOptions().set_browser_path(path).save()


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

page.get("https://www.douban.com/")
tab = page.get_tab()  # 获取当前页面句柄

pas_login = page.ele("xpath:/html/body/div[1]/div[1]/ul[1]/li[2]")
pas_login.click()


ele = page.ele('xpath://*[@id="username"]')
ele.input("17550032980")

ele = page.ele('xpath://*[@id="password"]')
ele.input("111111")


ele = page.ele("xpath:/html/body/div[1]/div[2]/div[1]/div[5]/a")
ele.click()
time.sleep(3)
# 滑块验证

iframes = page.eles('xpath://iframe[@id="tcaptcha_iframe_dy"]')

if iframes:
    # 存在验证码

    iframe = page.get_frame(iframes[0])

    # 按住滑块
    ele = iframe.ele('xpath://div[@id="tcOperation"]/div[6]')
    ele.hover()
    if ele:
        
        # ac.hold("@class=verify-move-block")
        # ac.move(1000, 0)
        # ac.release('@class=verify-move-block')
        ac.hold(ele)

        # 移动滑块
        distance = 180
        tracks = get_tracks(distance)
        for track in tracks:
            print(f"滑动距离：{track}")
            ac.move(track, 0)
        ac.release(ele)

    else:
        print("滑块验证失败")
else:
    print("无滑块验证码")
