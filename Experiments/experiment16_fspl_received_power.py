import numpy as np
import matplotlib.pyplot as plt

def fspl_db(d_km, f_mhz):
    return 20*np.log10(d_km) + 20*np.log10(f_mhz) + 32.44

Pt_dbm, Gt_db, Gr_db = 43.0, 15.0, 0.0
distances = np.array([0.1, 0.5, 1, 2, 5, 10])

for f in (900, 1800):
    print(f"\nFrequency = {f} MHz")
    print(f"{'d (km)':>8}{'FSPL (dB)':>12}{'Pr (dBm)':>11}{'Pr (W)':>14}")
    for d in distances:
        L = fspl_db(d, f)
        Pr = Pt_dbm + Gt_db + Gr_db - L
        Pr_w = 10**(Pr/10) / 1000
        print(f"{d:8.1f}{L:12.2f}{Pr:11.2f}{Pr_w:14.3e}")

plt.figure()
for f in (900, 1800):
    losses = fspl_db(distances, f)
    received = Pt_dbm + Gt_db + Gr_db - losses
    plt.plot(distances, losses, marker='o', label=f'FSPL {f} MHz')
plt.xlabel('Distance (km)'); plt.ylabel('Free-space path loss (dB)')
plt.title('FSPL versus Distance'); plt.grid(True); plt.legend(); plt.tight_layout()
plt.savefig('experiment16_fspl.png', dpi=150)

plt.figure()
for f in (900, 1800):
    received = Pt_dbm + Gt_db + Gr_db - fspl_db(distances, f)
    plt.plot(distances, received, marker='o', label=f'Received power {f} MHz')
plt.xlabel('Distance (km)'); plt.ylabel('Received power (dBm)')
plt.title('Received Power versus Distance'); plt.grid(True); plt.legend(); plt.tight_layout()
plt.savefig('experiment16_received_power.png', dpi=150)
plt.show()
