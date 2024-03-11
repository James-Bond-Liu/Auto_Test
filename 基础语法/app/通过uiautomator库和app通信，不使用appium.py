
import uiautomator2 as u2
import os

d = u2.connect_usb('37acf4fe')
#获取机器设备的信息
print(d.info) #获取设备的基础信息

print(d.window_size()) #获取窗口大小

print(d.app_current())#获取当前打开的app

print(d.serial)  #获取设备序列号

print(d.wlan_ip)  #获取无线局域网ip

#屏幕相关的操作

# 开关屏幕
d.screen_off()  #打开屏幕

d.screen_on()  #关闭屏幕

d.unlock()  #解锁屏幕

# 按键（软/硬）操作
d.press('back')

d.press('home')
'''
还支持如下按键的操作:
home、back、left、right、up、down、center、menu、search、enter、
recent(recent apps)、volume_up、volume_down、volume_mute、camera、power
'''

# 手势相关的操作，包括短按/长按/滑动/拖拽

# 点击操作
d.click(x, y)

#双击操作
d.double_click(x,y)

# 长按操作
d.long_click(x, y)

# 滑动操作
d.swipe(sx, sy, ex, ey)

d.swipe(sx, sy, ex, ey, steps=10)

# 拖拽操作
d.drag(sx, sy, ex, ey)

#屏幕相关的操作

# 获取并设置屏幕的旋转方向
orientation = d.orientation
d.set_orientation("l") # or "left"
d.set_orientation("r") # or "right"
d.set_orientation("n") # or "natural"

# 冻结/解冻旋转功能
d.freeze_rotation()  # 冻结旋转
d.freeze_rotation(False)  # 解冻旋转

# 屏幕截图
d.screenshot("home.png")

# 获取屏幕层级(hierachy)XML
xml = d.dump_hierarchy()

# 打开通知栏或快速设置栏
d.open_notification()
d.open_quick_settings()

# 启动App
d.app_start("com.meizu.mzbbs")

# 搜索
d(resourceId="com.meizu.mzbbs:id/j0").click()

# 输入关键字
d(resourceId="com.meizu.mzbbs:id/p9").set_text("flyme")

# 搜索按钮
d(resourceId="com.meizu.mzbbs:id/tp").click()

# 停止app
d.app_stop("com.meizu.mzbbs")

'''常用的定位方式'''
# ResourceId定位：
d(resourceId="com.meizu.mzbbs:id/tp").click()

# Text定位：
d(text="精选").click()

# Description定位：
d(description="..").click()

# ClassName定位：
d(className="android.widget.TextView").click()

#XPATH定位
d.xpath("//*[@content-desc='分享']").click()

