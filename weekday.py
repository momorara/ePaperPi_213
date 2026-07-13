#!/usr/bin/python
"""
2025/03/04  曜日を基本に表示
2025/04/08  赤ePperに対応した　土日は赤で表示

            これを午前1時ごろにcronで実行すると、日めくりカレンターとして機能する。
"""
import ep_lib
import datetime
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 240x128 の白黒ビットマップ作成（1bit）
width = 245
height = 121
image = Image.new("1", (width, height), 1)  # 1=白背景

draw = ImageDraw.Draw(image)

# DejaVuフォント指定
font_path = '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf' 
font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
font = ImageFont.truetype(font_path, 54)


def main():

    # 表示内容
    # 日付と曜日を表示
    # 14日火曜日
    # といった表示を行う

    # draw, image = ep_lib.image_set()  # eペーパーディスプレイ用の描画オブジェクトと画像を取得
    # ep_lib.clear_w(draw)  # 画面を白でクリア

    # 動作初回に表示
    wd_name = ["月","火","水","木","金","土","日"]
    now = datetime.datetime.now()
    wd_no = now.weekday()
    formatted_date = f"{int(now.day)}日"
    text = formatted_date + " " + wd_name[wd_no] + "曜"
    # draw.text((0, 30), mes, font=ep_lib.font_set("gos", 60), fill=0)
    

    print(text)
    # print(wd_no)
    # exit(0)

    # 文字描画
    draw.text((0, 40), text, font=font, fill=0)  # 0=黒
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


    # last_date = datetime.datetime.now().date()   # 現在の日付を取得
    # while True:

    #     time.sleep(60)  # 1分ごとにチェック
    #     current_date = datetime.datetime.now().date() 
    #     #日替わりのタイミングをチェック
    #     if current_date != last_date:
    #         print(f"日付が変わりました: {current_date}")
    #         last_date = current_date  # 日付を更新
            
    #         ep_lib.clear_w(draw)  # 画面を白でクリア

    #         # 表示文字を作って表示
    #         now = datetime.datetime.now()
    #         wd_no = now.weekday()
    #         formatted_date = f"{int(now.day)}日"
    #         mes = formatted_date + wd_name[wd_no] + "曜日"
    #         draw.text((0, 30), mes, font=ep_lib.font_set("gos", 60), fill=0)
    #         # ep_lib.ep_draw(0,0,image,0,1)


            

if __name__ == "__main__":
    main()
