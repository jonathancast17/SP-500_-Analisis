import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

sp500 = yf.download("^GSPC", start="2020-01-01")["Close"].squeeze()

cambio_diario = sp500.pct_change().dropna() * 100
fechas = cambio_diario.index.to_numpy()
valores = cambio_diario.to_numpy()
colores = ["red" if x < 0 else "green" for x in valores]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))

ax1.plot(sp500.index.to_numpy(), sp500.to_numpy(), color="steelblue")
ax1.set_title("S&P 500 — Precio Histórico")
ax1.set_ylabel("Precio USD")
ax1.grid(True, alpha=0.3)

ax2.bar(fechas, valores, color=colores, alpha=0.7, width=1)
ax2.set_title("Cambio Diario % — Rojos son caídas")
ax2.set_ylabel("Cambio %")
ax2.axhline(y=-3, color="darkred", linestyle="--", alpha=0.5)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
ax2.set_ylim(-15,10)
plt.savefig("sp500.png")
print("Gráfica guardada como sp500.png")

print("\n--- 10 PEORES DÍAS desde 2020 ---")
peores_idx = np.argsort(valores)[:10]
for i in peores_idx:
    print(f"  {fechas[i].astype('datetime64[D]')}: {valores[i]:.2f}%")
