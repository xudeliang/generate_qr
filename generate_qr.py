import qrcode
from PIL import Image
import time

def generate_qr(url):
    # 生成二维码对象
    qr = qrcode.QRCode(
        version=1,  # 控制二维码大小，1是最小
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # 每个点的像素大小
        border=4,  # 边框宽度（单位：点）
    )
    qr.add_data(url)
    qr.make(fit=True)

    # 生成图片
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # 当前毫秒时间戳
    millis = int(time.time() * 1000)
    filename = f"{millis}.jpg"

    # 保存图片
    img.save(filename)
    print(f"✅ 已保存二维码为: {filename}")

# 示例调用
if __name__ == "__main__":
    url = "https://google.com"
    generate_qr(url)