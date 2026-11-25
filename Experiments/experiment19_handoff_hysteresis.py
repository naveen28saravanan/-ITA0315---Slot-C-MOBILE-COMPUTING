import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(7)
D = 2000.0
P0, n, sigma = -30.0, 3.5, 4.0
x = np.arange(10, D, 5.0)
def rss(d, shadow): return P0 - 10*n*np.log10(d) + shadow
r1 = rss(x, rng.normal(0, sigma, x.size)); r2 = rss(D-x, rng.normal(0, sigma, x.size))
def run(H):
    serving, count, events = 1, 0, []
    for xi, a, b in zip(x, r1, r2):
        if serving == 1 and b > a + H:
            serving, count = 2, count+1; events.append((float(xi), '1->2'))
        elif serving == 2 and a > b + H:
            serving, count = 1, count+1; events.append((float(xi), '2->1'))
    return count, events
print(f"{'H (dB)':>7}{'Handoffs':>10}{'Ping-pongs':>12}")
for H in (0,2,4,6,8,10):
    h, events = run(H); print(f'{H:7d}{h:10d}{max(h-1,0):12d}')
h, events = run(6)
print('\nHandoff events with H = 6 dB (position in metres):', events)
plt.figure(); plt.plot(x, r1, label='BS1 RSS'); plt.plot(x, r2, label='BS2 RSS'); plt.xlabel('Mobile position (m)'); plt.ylabel('RSS (dBm)'); plt.title('Received Signal Strength along the Route'); plt.grid(True); plt.legend(); plt.tight_layout(); plt.savefig('experiment19_rss.png', dpi=150)
plt.figure(); hs = [0,2,4,6,8,10]; counts = [run(H)[0] for H in hs]; plt.plot(hs, counts, marker='o'); plt.xlabel('Hysteresis (dB)'); plt.ylabel('Handoffs'); plt.title('Handoffs versus Hysteresis'); plt.grid(True); plt.tight_layout(); plt.savefig('experiment19_hysteresis.png', dpi=150); plt.show()
