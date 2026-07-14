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

import ep_lib

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    # 最大表示領域の確認
    ep_lib.rectangle(0,0,245,121,"B",0)
    ep_lib.write_buffer()

if __name__ == '__main__':
    main()
