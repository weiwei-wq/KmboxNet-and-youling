import kmNet
import time

# -------------------------- 1. 配置设备基础参数（必须替换为你的设备信息） --------------------------
DEVICE_IP = "192.168.2.88"    # 替换为 kmbox 设备 IP
DEVICE_PORT = "6234"          # 替换为 kmbox 设备通信端口
DEVICE_MAC = "12345"          # 替换为 kmbox 设备 MAC 地址
MONITOR_PORT = 8888           # 监控功能端口（1024-49151 之间，避免与系统冲突）
DELAY = 0.5                   # 操作延迟（秒），模拟人工操作节奏


# -------------------------- 2. 初始化函数（所有 API 调用的前提） --------------------------
def init_kmbox():
    """初始化 kmbox 设备连接，返回是否成功"""
    print("=" * 50)
    print("开始初始化 kmbox 设备...")
    init_result = kmNet.init(DEVICE_IP, DEVICE_PORT, DEVICE_MAC)
    if init_result == 0:
        print(f"初始化成功！设备 IP：{DEVICE_IP}，端口：{DEVICE_PORT}")
        return True
    else:
        print(f"初始化失败！错误码：{init_result}")
        print("请检查：1. 设备网络是否通畅 2. IP/端口/MAC 是否正确 3. kmNet.pyd 版本是否匹配")
        return False


# -------------------------- 3. 鼠标控制 API 演示（基础版 + 加密版） --------------------------
def demo_mouse_apis():
    """演示所有鼠标控制 API（基础函数 + 加密函数示例）"""
    print("\n" + "=" * 50)
    print("开始演示鼠标控制 API...")

    # 3.1 基础版：快速移动（无轨迹）
    print(f"\n[基础版] 鼠标快速移动：向右 100 单位，向下 50 单位")
    kmNet.move(100, 50)
    time.sleep(DELAY)

    # 3.2 基础版：鼠标左键控制（按下 → 松开）
    print(f"[基础版] 鼠标左键：按下 → 延迟 {DELAY}s → 松开")
    kmNet.left(1)  # 按下
    time.sleep(DELAY)
    kmNet.left(0)  # 松开
    time.sleep(DELAY)

    # 3.3 基础版：鼠标右键控制（按下 → 松开）
    print(f"[基础版] 鼠标右键：按下 → 延迟 {DELAY}s → 松开")
    kmNet.right(1)  # 按下
    time.sleep(DELAY)
    kmNet.right(0)  # 松开
    time.sleep(DELAY)

    # 3.4 基础版：鼠标中键控制（按下 → 松开）
    print(f"[基础版] 鼠标中键：按下 → 延迟 {DELAY}s → 松开")
    kmNet.middle(1)  # 按下
    time.sleep(DELAY)
    kmNet.middle(0)  # 松开
    time.sleep(DELAY)

    # 3.5 基础版：鼠标滚轮控制（上滚 → 下滚）
    print(f"[基础版] 鼠标滚轮：上滚 1 单位 → 下滚 1 单位")
    kmNet.wheel(-1)  # 上滚
    time.sleep(DELAY)
    kmNet.wheel(1)   # 下滚
    time.sleep(DELAY)

    # 3.6 基础版：鼠标综合控制（左键按下 + 移动 + 滚轮）
    print(f"[基础版] 鼠标综合控制：左键按下 + 右移 20 + 下移 10 + 滚轮下滚 2")
    kmNet.mouse(1, 20, 10, 2)  # 1=左键按下，x=20，y=10，wheel=2
    time.sleep(DELAY)
    kmNet.mouse(0, 0, 0, 0)    # 左键松开，停止移动/滚轮
    time.sleep(DELAY)

    # 3.7 基础版：模拟人为移动（无跳跃，耗时 300ms）
    print(f"[基础版] 模拟人为移动：目标 (300, 200)，耗时 300ms")
    kmNet.move_auto(300, 200, 300)
    time.sleep(DELAY)

    # 3.8 基础版：二阶贝塞尔曲线移动（自定义轨迹）
    print(f"[基础版] 贝塞尔曲线移动：目标 (400, 300)，耗时 400ms，控制点 (-50,-60)、(70,80)")
    kmNet.move_beizer(400, 300, 400, -50, -60, 70, 80)
    time.sleep(DELAY)

    # 3.9 加密版示例（enc_前缀，用法与基础版一致，防抓包）
    print(f"\n[加密版] 演示 enc_left（鼠标左键按下 → 松开，加密传输）")
    kmNet.enc_left(1)  # 加密版左键按下
    time.sleep(DELAY)
    kmNet.enc_left(0)  # 加密版左键松开
    time.sleep(DELAY)
    print("提示：其他加密函数（enc_move/enc_right/enc_wheel 等）用法与对应基础版完全一致")


# -------------------------- 4. 键盘控制 API 演示（基础版 + 加密版） --------------------------
def demo_keyboard_apis():
    """演示键盘控制 API（基础函数 + 加密函数示例）"""
    print("\n" + "=" * 50)
    print("开始演示键盘控制 API...")
    # 按键值参考：A=4，Ctrl=17，C=67（需以 kmbox 官方附录为准）
    KEY_A = 4       # A 键
    KEY_CTRL = 17   # Ctrl 键
    KEY_C = 67      # C 键

    # 4.1 基础版：单次按键（A 键按下 → 松开）
    print(f"[基础版] 单次按键：A 键按下 → 延迟 {DELAY}s → 松开")
    kmNet.keydown(KEY_A)
    time.sleep(DELAY)
    kmNet.keyup(KEY_A)
    time.sleep(DELAY)

    # 4.2 基础版：组合键（Ctrl + C，复制功能）
    print(f"[基础版] 组合键：Ctrl 按下 → C 按下 → 延迟 {DELAY}s → 依次松开 C、Ctrl")
    kmNet.keydown(KEY_CTRL)
    time.sleep(0.2)  # 微小延迟，确保组合键生效
    kmNet.keydown(KEY_C)
    time.sleep(DELAY)
    kmNet.keyup(KEY_C)
    time.sleep(0.2)
    kmNet.keyup(KEY_CTRL)
    time.sleep(DELAY)

    # 4.3 加密版示例（enc_keydown/enc_keyup，防抓包）
    print(f"[加密版] 演示 enc_keydown/enc_keyup（A 键按下 → 松开，加密传输）")
    kmNet.enc_keydown(KEY_A)
    time.sleep(DELAY)
    kmNet.enc_keyup(KEY_A)
    time.sleep(DELAY)
    print("提示：enc_keydown/enc_keyup 用法与基础版一致，支持组合键加密")


# -------------------------- 5. 监控类 API 演示（物理键鼠状态查询） --------------------------
def demo_monitor_apis():
    """演示物理键鼠监控 API（开启监控 → 查询状态 → 关闭监控）"""
    print("\n" + "=" * 50)
    print("开始演示监控类 API...")
    print(f"提示：监控将持续 5 秒，实时查询物理鼠标左键/中键状态（按下=1，松开=0）")

    # 5.1 开启监控（指定端口，避免冲突）
    monitor_result = kmNet.monitor(MONITOR_PORT)
    if monitor_result != 0:
        print(f"监控开启失败！可能端口 {MONITOR_PORT} 被占用，请更换端口（如 8889）")
        return
    print(f"监控已开启，端口：{MONITOR_PORT}")
    time.sleep(1)  # 等待监控连接稳定

    # 5.2 循环查询物理鼠标状态（持续 5 秒）
    start_time = time.time()
    while time.time() - start_time < 5:
        left_state = kmNet.isdown_left()    # 查询左键状态
        middle_state = kmNet.isdown_middle()# 查询中键状态
        print(f"当前物理鼠标状态：左键={left_state}，中键={middle_state}", end="\r")
        time.sleep(0.5)  # 每 0.5 秒查询一次
    print()  # 换行，避免覆盖最后一行输出

    # 5.3 关闭监控
    kmNet.monitor(0)
    print(f"监控已关闭")


# -------------------------- 6. 主函数（按顺序执行所有 Demo） --------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("kmNet 模块全 API 调用 Demo 开始运行")
    print("=" * 50)

    # 第一步：初始化设备（初始化失败则退出）
    if not init_kmbox():
        exit()

    # 第二步：演示鼠标控制 API
    demo_mouse_apis()

    # 第三步：演示键盘控制 API
    demo_keyboard_apis()

    # 第四步：演示监控类 API
    demo_monitor_apis()

    print("\n" + "=" * 50)
    print("kmNet 模块全 API Demo 运行结束")
    print("=" * 50)