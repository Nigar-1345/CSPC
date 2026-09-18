import time
import decay

N0 = 200000
rate = 0.4

# Pure-Python loop icra müddəti
t0 = time.perf_counter()
res_loop = decay.simulate_loop(N0, rate) if hasattr(decay, 'simulate_loop') else decay.simulate(N0, rate)
t_loop = time.perf_counter() - t0

# NumPy icra müddəti
t0 = time.perf_counter()
res_numpy = decay.simulate(N0, rate)
t_numpy = time.perf_counter() - t0

speedup = t_loop / t_numpy if t_numpy > 0 else 1.0

print(f"Loop time: {t_loop:.4f} s")
print(f"NumPy time: {t_numpy:.4f} s")
print(f"Speed-up: {speedup:.2f}x faster")