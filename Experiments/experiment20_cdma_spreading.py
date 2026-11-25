import numpy as np
import matplotlib.pyplot as plt
W = np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])
bits = {1:[1,0,1,1], 2:[0,0,1,0], 3:[1,1,0,1]}
L, nbits = W.shape[1], 4
def bpsk(b): return 2*np.array(b)-1
tx = np.zeros(nbits*L)
spreads = {}
for u,b in bits.items():
    spread = np.repeat(bpsk(b),L)*np.tile(W[u],nbits)
    spreads[u] = spread
    print(f'User {u} data   : {b}')
    print(f'User {u} spread : {spread.astype(int)}')
    tx += spread
print('\nComposite transmitted signal:\n',tx.astype(int))
print('\nDespreading at receiver:')
for u,b in bits.items():
    corr = (tx*np.tile(W[u],nbits)).reshape(nbits,L).sum(axis=1)/L
    recovered = (corr>0).astype(int)
    print(f'User {u} correlator: {corr} -> bits {recovered.tolist()} {"OK" if recovered.tolist()==b else "ERROR"}')
plt.figure(); plt.step(range(len(spreads[1])), spreads[1], where='mid'); plt.xlabel('Chip index'); plt.ylabel('Amplitude'); plt.title('User 1 Spread Signal'); plt.grid(True); plt.tight_layout(); plt.savefig('experiment20_spread.png', dpi=150)
plt.figure(); plt.plot(tx, marker='o'); plt.xlabel('Chip index'); plt.ylabel('Composite amplitude'); plt.title('Composite CDMA Signal'); plt.grid(True); plt.tight_layout(); plt.savefig('experiment20_composite.png', dpi=150); plt.show()
