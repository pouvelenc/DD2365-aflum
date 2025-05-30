import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

Re_list = [10, 100, 1000, 10000]
file_paths_2 = {
    1: "DD2365 aflum/data/force_stats_2_1.npz",
    10: "DD2365 aflum/data/force_stats_2_10.npz",
    100: "DD2365 aflum/data/force_stats_2_100.npz",
    1000: "DD2365 aflum/data/force_stats_2_1000.npz",
    10000: "DD2365 aflum/data/force_stats_2_10000.npz"
}
file_paths_3 = {
    1: "DD2365 aflum/data/force_stats_3_1.npz",
    10: "DD2365 aflum/data/force_stats_3_10.npz",
    100: "DD2365 aflum/data/force_stats_3_100.npz",
    1000: "DD2365 aflum/data/force_stats_3_1000.npz",
    10000: "DD2365 aflum/data/force_stats_3_10000.npz"
}

cmap = cm.get_cmap("viridis", len(Re_list))
colors_list = [cmap(i) for i in range(len(Re_list))]


plt.figure(figsize=(6, 4))
for i, Re in enumerate(Re_list):
    data2 = np.load(file_paths_2[Re])
    data3 = np.load(file_paths_3[Re])

    beta_combined = np.concatenate([data2["beta_list"], data3["beta_list"]])
    lift_combined = np.concatenate([data2["avg_lift"], data3["avg_lift"]])

    sort_idx = np.argsort(beta_combined)
    beta_sorted = beta_combined[sort_idx]
    lift_sorted = lift_combined[sort_idx]

    plt.semilogx(beta_sorted, lift_sorted,
             label=f"Re = {Re}",
             color=colors_list[i])

plt.xlabel(r"beta")
plt.ylabel(r"lift force")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(6, 4))
for i, Re in enumerate(Re_list):
    data2 = np.load(file_paths_2[Re])
    data3 = np.load(file_paths_3[Re])

    beta_combined = np.concatenate([data2["beta_list"], data3["beta_list"]])
    drag_combined = np.concatenate([data2["avg_drag"], data3["avg_drag"]])

    sort_idx = np.argsort(beta_combined)
    beta_sorted = beta_combined[sort_idx]
    drag_sorted = drag_combined[sort_idx]

    plt.semilogx(beta_sorted, drag_sorted,
             label=f"Re = {Re}",
             color=colors_list[i])

plt.xlabel(r"beta")
plt.ylabel(r"drag force")
plt.legend()
plt.grid(True)
plt.show()
