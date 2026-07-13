"""
2026/2/27   日本語を書く場合は、bitmap上に書いたのち、そのbitmapファィルを表示する。
            図形を書く場合もbitmap上に書いたのち、そのbitmapファィルを表示する。
"""
from PIL import Image, ImageDraw, ImageFont
import ep_lib
import time

# 240x128 の白黒ビットマップ作成（1bit）
width = 245
height = 121
image = Image.new("1", (width, height), 1)  # 1=白背景

draw = ImageDraw.Draw(image)

# DejaVuフォント指定
font_path = '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf' 
font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
font = ImageFont.truetype(font_path, 48)

# 表示テキスト（※日本語は表示されない可能性あり）
text = "こんにちは"
text = "27日"

# 文字描画
draw.text((0, 40), text, font=font, fill=0)  # 0=黒
#ピットマップ上に図形を追加する場合
# draw.line((10,10,50,50))
# draw.point((100,50))
# draw.rectangle((50, 30, 60, 40), fill=0)
# draw.ellipse((160, 30, 200, 70), fill=0)

# 保存
image.save("output.bmp")

print("保存完了: output.bmp")


print("画面を初期化して、白くする。")
ep_lib.clear_w()

x,y = 0,0
BorW = 0 # 0:白地に黒　,1:黒字に白
image_path = 'output.bmp'
ep_lib.bmp(x,y,image_path,BorW,1)


# 既存の画像を開く 白黒画像に限る
bitmap = Image.open("output.bmp")
draw.bitmap((0, 0), bitmap, fill=None)
time.sleep(0)

ep_lib.close()


