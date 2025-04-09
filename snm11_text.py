import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSV ファイルからデータを読み込む
data = pd.read_csv('snm_output2.csv', header=None, sep='\s+')

# 1列目と2列目をX軸基準でプロット (v(x) → v(Q))
plt.figure(figsize=(5, 5))
plt.plot(data[0], data[1], label="v(x) → v(Q)", color="b")

# 3列目と4列目をY軸基準でプロット (v(Q) → v(QB))
# plt.plot(data[3], data[1], label="v(Q) → v(QB)", color="r", linestyle="--")
plt.plot(data[1], data[0], label="v(Q) → v(QB)", color="r", linestyle="--")


# 4列目のデータを逆順にしてプロット
# plt.plot(data[3][::-1], data[2], label="v(QB) → v(Q) (reversed)", color="r", linestyle="--")

# 軸ラベルとタイトル
plt.xlabel("v(Q) (V)")
plt.ylabel("v(QB) (V)")
plt.title("SRAM Butterfly Curve")

# 軸の目盛りを 0 から 1.0 間隔で設定
plt.xticks(np.arange(0, max(data[0].max(), data[3].max()) + 1, 1))
plt.yticks(np.arange(0, max(data[1].max(), data[2].max()) + 1, 1))

# 凡例とグリッド
plt.legend()
plt.grid(True)

# プロット表示
plt.show()
