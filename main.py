import numpy as np
import matplotlib.pyplot as plt

# 示例极坐标数据 (r, theta)
# r 是径向距离，theta 是角度 (弧度制)
r = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
theta = np.linspace(0, 2 * np.pi, len(r))  # 生成等间隔的角度 (0 到 2*pi)

# 1. 将极坐标转换为笛卡尔坐标 (x, y)
x = r * np.cos(theta)  # x = r * cos(θ)
y = r * np.sin(theta)  # y = r * sin(θ)

# 可视化极坐标转换后的笛卡尔坐标
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'bo-', label='Converted Cartesian Coordinates')
plt.title("Cartesian Coordinates from Polar Coordinates")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.savefig('Cartesian Coordinates.png')
plt.show()

# 2. 对笛卡尔坐标进行傅里叶变换 (可以使用复数 FFT)
signal = x + 1j * y  # 将 x 和 y 合并为复数信号（实部是 x，虚部是 y）

# 3. 执行快速傅里叶变换 (FFT)
fft_result = np.fft.fft(signal)

# 4. 提取傅里叶特征
# 幅度谱 (Magnitude Spectrum)
magnitude = np.abs(fft_result)

# 相位谱 (Phase Spectrum)
phase = np.angle(fft_result)

# 5. 可视化傅里叶特征 (幅度谱和相位谱)
plt.figure(figsize=(12, 6))

# 绘制幅度谱
plt.subplot(1, 2, 1)
plt.plot(magnitude, 'r-', label='Magnitude Spectrum')
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.grid(True)

# 绘制相位谱
plt.subplot(1, 2, 2)
plt.plot(phase, 'g-', label='Phase Spectrum')
plt.title("Phase Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.legend()
plt.savefig('PhaseSpectrum.png')
plt.show()

# 打印傅里叶变换的幅度和相位特征
print("Magnitude Spectrum:", magnitude)
print("Phase Spectrum:", phase)