import math
import matplotlib.pyplot as plt

S, M, n = 420, 10, 4
valid = sorted({i*i + i*j + j*j for i in range(5) for j in range(5)} - {0})[:8]
rows = []
print(f"{'N':>3}{'D/R':>8}{'ch/cell':>9}{'Capacity C':>12}{'S/I (dB)':>10}")
for N in valid:
    Q = math.sqrt(3*N); k = S // N; C = M*k*N
    si = (Q**n)/6; si_db = 10*math.log10(si)
    rows.append((N,Q,k,C,si_db))
    print(f"{N:>3}{Q:8.3f}{k:9d}{C:12d}{si_db:10.2f}")
req = 18.0
for N,Q,k,C,si_db in rows:
    if si_db >= req:
        print(f"\nSmallest cluster size meeting S/I >= {req} dB : N = {N}")
        break
Ns = [r[0] for r in rows]; ratios = [r[4] for r in rows]; channels = [r[2] for r in rows]
plt.figure(); plt.plot(Ns, ratios, marker='o', label='S/I (dB)'); plt.axhline(req, linestyle='--', label='18 dB requirement')
plt.xlabel('Cluster size N'); plt.ylabel('S/I (dB)'); plt.title('S/I versus Cluster Size'); plt.grid(True); plt.legend(); plt.tight_layout(); plt.savefig('experiment17_si.png', dpi=150)
plt.figure(); plt.plot(Ns, channels, marker='s'); plt.xlabel('Cluster size N'); plt.ylabel('Channels per cell'); plt.title('Channels per Cell versus Cluster Size'); plt.grid(True); plt.tight_layout(); plt.savefig('experiment17_channels.png', dpi=150)
plt.show()
