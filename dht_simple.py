# import
import time
import board
import adafruit_dht

# 利用するGPIOピン設定
dhtDevice = adafruit_dht.DHT22(board.D4)

# 無限ループ
while True:
    try:
        # センサーより温度と湿度を取得
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        # 出力
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # 例外処理(RuntimeError)
        # 出力
        print(error.args[0])

        # 待機
        time.sleep(2.0)

        # 再実行
        continue

    except Exception as error:
        # 例外処理(その他)
        # オブジェクト破棄
        dhtDevice.exit()

        # エラーで終了
        raise error

    # 待機
    time.sleep(2.0)
