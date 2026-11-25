import matplotlib.pyplot as plt

def erlang_b(E, m):
    B = 1.0
    for k in range(1, m+1):
        B = (E*B)/(k + E*B)
    return B

loads = [2, 5, 10, 20]
channels = [5, 10, 15, 20, 25, 30]
print('Blocking probability (%)')
print('E \\ m ' + ''.join(f'{m:>9}' for m in channels))
for E in loads:
    print(f'{E:>5} ' + ''.join(f'{100*erlang_b(E,m):9.3f}' for m in channels))
E, target = 10, 0.02
m = 1
while erlang_b(E,m) > target: m += 1
print(f'\nFor E = {E} Erlangs and GoS = {target*100:.0f}% -> channels required = {m}')
plt.figure()
for E in loads:
    mvals = list(range(1,31)); probs = [100*erlang_b(E,k) for k in mvals]
    plt.plot(mvals, probs, label=f'{E} Erlangs')
plt.xlabel('Number of channels'); plt.ylabel('Blocking probability (%)'); plt.title('Erlang B Blocking Probability'); plt.grid(True); plt.legend(); plt.tight_layout(); plt.savefig('experiment18_erlang_b.png', dpi=150); plt.show()
