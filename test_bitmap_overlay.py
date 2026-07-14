"""
2026/07/14  画像と文字を表示させる方法
            1.ピットマップ上に文字を書く
            2.ビットマップを保存
            3.ビットマップにpngファィルを重ねて書く
            4.必要に応じて1ビット形式に変換
            5.ePaper上に描画
            といった手順で文字と画像を表示できる
"""
from PIL import Image, ImageDraw, ImageFont
import ep_lib
import time

# 246x121 の白黒ビットマップ作成（1bit）
width = 246
height = 121
image = Image.new("1", (width, height), 1)  # 1=白背景

draw = ImageDraw.Draw(image)

# DejaVuフォント指定
# font_path = '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf' 
font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'

# 表示テキスト
text1 = "TKJ"
# DejaVuフォントサイズ指定
font = ImageFont.truetype(font_path, 60)
# 文字描画
draw.text((120, 10), text1, font=font, fill=0)  # 0=黒

# 表示テキスト
text2 = "製作所"
# DejaVuフォントサイズ指定
font = ImageFont.truetype(font_path, 36)
# 文字描画
draw.text((120, 70), text2, font=font, fill=0)  # 0=黒
# 保存
image.save("output.bmp")



# 背景画像（BMPでもPNGでも可）
background = Image.open("output.bmp").convert("RGBA")
# 重ねるPNG画像（透過あり）
overlay = Image.open("bmp/QR_TKJ.png").convert("RGBA")

# (0, 0) の位置に重ねる
background.paste(overlay, (0, 0), overlay)
# 1ビット形式に変換
background= background.convert("1", dither=Image.NONE)
# 保存
background.save("output1.bmp")

print("画面を初期化して、白くする。")
ep_lib.clear_w()

# 描画
image_path = 'output1.bmp'
BorW = 0 # 0:白地に黒　,1:黒字に白
ep_lib.bmp(0,0,image_path,BorW,1)

ep_lib.close()


