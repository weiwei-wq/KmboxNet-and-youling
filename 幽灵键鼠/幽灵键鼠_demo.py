
# 导入幽灵键鼠python库
import ghostbox as gb
import time


# 根据设备序号打开设备
print(gb.opendevice(0))
# 根据设备ID打开设备
#print(gb.opendevicebyid(123,456))
# 根据设备路径打开设备
#print(gb.opendevicebypath("\\\\?\\hid#vid_5188&pid_1801&mi_02#7&28610698&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}"))
# 判断当前是否已打开设备
#print(gb.isconnected())
# 关闭当前打开的设备
#print(gb.closedevice())
# 复位当前打开的设备
#print(gb.resetdevice())


# 获取当前连接设备的型号
print(gb.getmodel())
# 获取当前连接设备的序列号
#print(gb.getserialnumber())
# 获取当前连接设备的生产日期
#print(gb.getproductiondate())
# 获取当前连接设备的固件版本号
#print(gb.getfirmwareversion())


# 按下键盘上的指定键（根据键名）
#print(gb.presskeybyname("win"))
# 释放键盘上的指定键（根据键名）
#print(gb.releasekeybyname("win"))
# 按下键盘上的指定键（根据键值）
#print(gb.presskeybyvalue(91))
# 释放键盘上的指定键（根据键值）
#print(gb.releasekeybyvalue(91))
# 检测指定键的按键状态（根据键名）
#print(gb.iskeypressedbyname("win"))
# 检测指定键的按键状态（根据键值）
#print(gb.iskeypressedbyvalue(91))
# 按下并释放键盘上的指定键（根据键名）
# print(gb.pressandreleasekeybyname("win"))
# 按下并释放键盘上的指定键（根据键值）
#print(gb.pressandreleasekeybyvalue(91))
# 释放所有按下的键
#print(gb.releaseallkey())
# 组合按键
# print(gb.combinationkey("win+r"))
# 输入字符串
# time.sleep(3)
# print(gb.inputstring("MCUAPP_@o@_幽灵盒子_Ok"))
# 获取CapsLock（大写）锁定状态
#print(gb.getcapslock())
# 获取NumLock（数字键盘）锁定状态
#print(gb.getnumlock())
# 设置按字母键或输入字符串时是否区分大小写
#print(gb.setcasesensitive(1))
# 设置按键的随机延时
#print(gb.setpresskeydelay(50,100))
# 设置输入字符串的间隔时间范围
#print(gb.setinputstringintervaltime(20,300))
# 设置中文字符输入模式
# print(gb.setchineseinputmode(1))


# 按下指定的鼠标键
#print(gb.pressmousebutton(1))
# 释放已按下的鼠标键
#print(gb.releasemousebutton(1))
# 判断指定的鼠标键是否按下
#print(gb.ismousebuttonpressed(1))
# 按下并释放指定的鼠标键
#print(gb.pressandreleasemousebutton(1))
# 释放所有鼠标按键
#print(gb.releaseallmousebutton())
# 相对移动鼠标
#print(gb.movemouserelative(100,100))
# 移动鼠标到指定坐标
# print(gb.movemouseto(100,100))
# 获取鼠标X坐标
#print(gb.getmousex())
# 获取鼠标Y坐标
#print(gb.getmousey())
# 移动鼠标滚轮
#print(gb.movemousewheel(5))
# 设置鼠标按键随机延时
#print(gb.setpressmousebuttondelay(20,50))
# 设置鼠标移动随机延时
#print(gb.setmousemovementdelay(10,100))
# 设置鼠标移动速度
#print(gb.setmousemovementspeed(7))
# 设置鼠标移动模式
#print(gb.setmousemovementmode(2))


# 设置鼠标当前位置（针对不支持绝对值的鼠标）
#print(gb.setmouseposition(100,100))
# 设置鼠标绝对位置（针对支持绝对值的鼠标）
#print(gb.setmouseabsoluteposition(100,100))
# 设置被控端屏幕分辨率
#print(gb.setclientscreenresolution(1024,768))
# 获取被控端屏幕分辨率
#print(gb.getclientscreenresolution())


# 初始化加密狗
# print(gb.initializedongle())
# 设置读密码
# print(gb.setreadpassword("", "aa"))
# 设置写密码
# print(gb.setwritepassword("", "bb"))
# 将字符串写入设备
# print(gb.writestring("bb", "abc123", 0))
# 从设备读字符串
# print(gb.readstring("aa", 0, 6))
# 设置密钥
# print(gb.setcipher("bb", "ghost"))
# 加密字符串
# print(gb.encryptstring("ghostbox"))
# 解密字符串
# print(gb.decryptstring("67686F7374626F78"))


# 按下电源按钮
# print(gb.presspowerbutton())
# 释放电源按钮
# print(gb.releasepowerbutton())
# 按下并释放电源按钮
# print(gb.pressandreleasepowerbutton())
# 获取电源工作状态
# print(gb.getpowerstatus())


# 修改设备速度
# print(gb.setspeed(1))
# 修改设备ID
# print(gb.setdeviceid(1234,5678))
# 恢复设备默认ID
# print(gb.restoredeviceid())
# 设置产品名称
# print(gb.setproductname("幽灵键鼠V4"))
# 获取产品名称
# print(gb.getproductionname())

print(gb.sdktype(), gb.sdkversion())
