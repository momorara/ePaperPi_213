#!/usr/bin/python
"""
描画領域はライブラリの関係で以下となる
0,0,240,127
ePaper のためのライブラリです。 
オリジナルのライブラリはjairoshさんの https://github.com/jairosh/raspberrypi-ssd1680/tree/master です。
 こちらは 「WeAct Studio 2.13" three-color e-paper display」用のものですが、 

ライセンスについては、オリジナルがGNU General Public License v3.0ですので、
本プログラムもGNU General Public License v3.0となります。

2024/07/08
ライブラリの名前をep_libとした
関数の名前も短くする。
mainから呼ぶときは text() だけで呼べるが、
importしたときは ep_lib.text() とする

2025/07/26　2.13にてテストした
"""

import raspberrypi_epd
import RPi.GPIO as GPIO
import numpy as np
from bdfparser import Font
import time
from PIL import Image
import random
import os

# Ejemplo de conexion
# BUSY          GPIO4
# RES           GPIO17
# D/C           GPIO27
# CS            GPIO22
# SCK           GPIO11 (SPI0 SCK)
# SDATA         GPIO10 (SPI0 MOSI)
# GND
# VCC

GPIO.setmode(GPIO.BCM)
busy_gpio, reset_gpio, dc_gpio, cs_gpio = 4,17,27,22
display = raspberrypi_epd.WeAct213(busy=busy_gpio, reset=reset_gpio, dc=dc_gpio, cs=cs_gpio)
display.init()

# 画面の向きを上下反転できます。
rotation = 270
# rotation = 90

# 画面を白くクリアする
def clear_w():
    display.set_rotation(rotation)
    display.fill(raspberrypi_epd.Color.WHITE)
    display.refresh(False)
    display.write_buffer()

# 画面を黒くクリアする
def clear_b():
    display.set_rotation(rotation)
    display.fill(raspberrypi_epd.Color.BLACK)
    display.refresh(False)
    display.write_buffer()

# バッファの内容をクリア
def clear_buffer():
    display.set_rotation(rotation)
    display.fill(raspberrypi_epd.Color.WHITE)
    # display.refresh(False)

# バッファの内容をePaperに書く
def write_buffer():
    display.write_buffer()

# ePaperライブラリを終了
# これをしないで、再起動するとワーニングが出る。
def close():
    display.close()
    GPIO.cleanup()
    # ePaperを書いた後i2cがおかしくなるので、i2cをリセットする
    os.system("sudo rmmod i2c_bcm2835")
    os.system("sudo modprobe i2c_bcm2835")


# ビットマップフォントを設定する
def set_font(n):
    if n == 1:display.set_font('fonts/spleen-8x16.bdf')
    if n == 2:display.set_font('fonts/luBS14.bdf')
    if n == 3:display.set_font('fonts/helvB14.bdf')
    # font-bitmapに矛盾がありwarningが出ますが、表示します。
    # fontの種類により表示位置がずれます。

# 文字を書く
def text(text,x,y,set):
    # 長い文字列を表示する場合、表示域をはみ出すとエラーになります。
    display.draw_text(text, x+4, y, raspberrypi_epd.Color.BLACK)
    if set == 1:
        display.write_buffer() # ePaperに表示

# 点を書く
def pixel(x,y,color,set):
    if color == 'B':
        display.draw_pixel( x+4, y, raspberrypi_epd.Color.BLACK)
    if color == 'W':
        display.draw_pixel( x+4, y, raspberrypi_epd.Color.WHITE)
    if set == 1:
        display.write_buffer() # ePaperに表示

# 線を書きます。
def line(x1,y1,x2,y2,color,set):
    if color == 'B':
        display.draw_line( x1+4,y1,x2+4,y2, raspberrypi_epd.Color.BLACK)
    if color == 'W':
        display.draw_line( x1+4,y1,x2+4,y2, raspberrypi_epd.Color.WHITE)
    if set == 1:
        display.write_buffer() # ePaperに表示

# 円を書きます。
def circle(x,y,r,color,set):
    if color == 'B':
        display.draw_circle( x+4, y, r,raspberrypi_epd.Color.BLACK)
    if color == 'W':
        display.draw_circle( x+4, y, r,raspberrypi_epd.Color.WHITE)
    if set == 1:
        display.write_buffer() # ePaperに表示

# 四角を書きます。
def rectangle(x,y,width,heigth,color,set):
    if color == 'B':
        display.draw_rectangle( x+4,y,width,heigth, raspberrypi_epd.Color.BLACK)
    if color == 'W':
        display.draw_rectangle( x+4,y,width,heigth, raspberrypi_epd.Color.WHITE)
    if set == 1:
        display.write_buffer() # ePaperに表示

# ビットマップファィルを描画
def bmp(x,y,path,BorW,set):
    # ビットマップファィルを読み込み bmp_img に渡す
    image = Image.open(path)
    bmp_img(x,y,image,BorW,set)

# ビットマップイメージを描画
def bmp_img(x,y,image,BorW,set):
    # x,yの位置にpathの示すビットマップファィルを描画
    # BorW 0:ビットをそのまま　1:ビットを反転して描画
    # set 0:バッファに書くだけ　0:ePaperに書く

    # 画面左上を0,0として、長い方を横:x、短い方を縦:yとする。
    # ビットマップの表示は画像のサイズ、表示位置、ePaperのバッファ領域を考慮して表示する必要がある
    # はみ出した場合は、描画されないか、エラーとなる
    # 240*128以内のビットマップ画像で、モノクロのみ対応

    # image = Image.open(path)
    # 画像の大きさを取得
    width, height = image.size
    print(f"width: {width}, height: {height}")
    # 読み込んだ画像の大きさ
    HEIGHT = 128
    WIDTH  = 240
    HEIGHT = height
    WIDTH  = width

    # 画像データの取得
    image_data = np.array(image)

    # # ディスプレイバッファを初期化
    # display.fill(raspberrypi_epd.Color.WHITE)

    display.set_rotation(rotation-90)
    dx = x # 画像描画位置を画面左上を0,0としての位置を変更する
    dy = HEIGHT -128 + y # y軸は左下が0なので変換が必要
    # 画像データをディスプレイバッファに書き込み
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # ePaperのデフォルトが縦長な画面のため
            y1 = HEIGHT -1 - y
            # print(y,x,y1)
            if image_data[y1, x] == BorW:  # 黒ピクセル
                display.draw_pixel(y+0-dy, x+4+dx, raspberrypi_epd.Color.BLACK)
                # draw_pixel(x,y,"B",0)
            else:  # 白ピクセル
                display.draw_pixel(y+0-dy, x+4+dx, raspberrypi_epd.Color.WHITE)
                # draw_pixel(x,y,"W",0)  
    if set == 1:
        display.write_buffer()  # ePaperに表示

def main():
    # print("画面を初期化して、黒くする。")
    # clear_b()

    print("画面を初期化して、白くする。")
    clear_w()

    # 最大表示領域の確認
    rectangle(0,0,245,121,"B",0)
    write_buffer()

    GPIO.cleanup()

if __name__ == '__main__':
    main()
