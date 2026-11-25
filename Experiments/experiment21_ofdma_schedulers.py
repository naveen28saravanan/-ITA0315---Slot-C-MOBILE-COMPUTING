import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(1)
U, TTI = 6, 2000
mean_snr_db = np.array([25,20,15,10,5,0])
mean_snr = 10**(mean_snr_db/10)ate = np.log2(1 + mean_snr*rng.exponential(1.0,(TTI,U)))
def jain(x): return x.sum()**2/(len(x)*(x**2).sum())
def simulate(policy):
    served=np.zeros(U); avg=np.ones(U)
    for t in range(TTI):
        if policy=='RR': u=t%U
        elif policy=='MaxCI': u=np.argmax(rate[t])
        else: u=np.argmax(rate[t]/avg)
        served[u]+=rate[t,u]
        instant=np.zeros(U); instant[u]=rate[t,u]
        avg=0.99*avg+0.01*instant
    return served/TTI
results={}
print(f"{'Scheduler':>10} | "+' '.join(f'U{i+1:>5}' for i in range(U))+' | Total | Jain')
for policy in ('RR','MaxCI','PF'):
    th=simulate(policy); results[policy]=th
    print(f'{policy:>10} | '+' '.join(f'{v:6.3f}' for v in th)+f' | {th.sum():6.3f} | {jain(th):.3f}')
plt.figure()
for policy, throughput in results.items(): plt.plot(range(1,U+1), throughput, marker='o', label=policy)
plt.xlabel('User'); plt.ylabel('Throughput (b/s/Hz)'); plt.title('Per-user Throughput by Scheduler'); plt.grid(True); plt.legend(); plt.tight_layout(); plt.savefig('experiment21_user_throughput.png', dpi=150)
plt.figure(); policies=list(results); totals=[results[p].sum() for p in policies]; fairness=[jain(results[p]) for p in policies]
plt.bar(policies,totals); plt.xlabel('Scheduler'); plt.ylabel('Total throughput (b/s/Hz)'); plt.title('Total Throughput Comparison'); plt.tight_layout(); plt.savefig('experiment21_total_throughput.png', dpi=150)
plt.figure(); plt.bar(policies,fairness); plt.xlabel('Scheduler'); plt.ylabel("Jain's fairness index"); plt.title('Fairness Comparison'); plt.ylim(0,1); plt.tight_layout(); plt.savefig('experiment21_fairness.png', dpi=150); plt.show()
