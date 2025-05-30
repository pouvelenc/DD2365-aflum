import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

Re_list = [20, 40, 60, 80, 100]
file_paths = {
    20:    "DD2365 aflum/data/force_stats_4_20.npz",
    40:   "DD2365 aflum/data/force_stats_4_40.npz",
    60:  "DD2365 aflum/data/force_stats_4_60.npz",
    80: "DD2365 aflum/data/force_stats_4_80.npz",
    100:"DD2365 aflum/data/force_stats_4_100.npz",
}

all_betas = set()
for R in Re_list:
    D = np.load(file_paths[R])
    all_betas.update(D["beta_list"].tolist())
all_betas = sorted(all_betas)

lift_vs_Re = {β: [] for β in all_betas}
drag_vs_Re = {β: [] for β in all_betas}

for R in Re_list:
    D = np.load(file_paths[R])
    betas = D["beta_list"]
    lifts  = D["avg_lift"]
    drags  = D["avg_drag"]
    for β in all_betas:
        idx = np.where(betas == β)[0]
        if idx.size:
            lift_vs_Re[β].append(lifts[idx[0]])
            drag_vs_Re[β].append(drags[idx[0]])
        else:
            lift_vs_Re[β].append(np.nan)
            drag_vs_Re[β].append(np.nan)

cmap = cm.get_cmap("viridis", len(all_betas))
colors = [cmap(i) for i in range(len(all_betas))]

plt.figure(figsize=(6,4))
for i, beta in enumerate(all_betas):
    plt.plot(Re_list, lift_vs_Re[beta],
             color=colors[i],
             label=f"beta={beta}")
plt.xlabel("Re")
plt.ylabel("lift force")
plt.legend()
plt.grid(True, ls="--", lw=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
for i, beta in enumerate(all_betas):
    plt.plot(Re_list, drag_vs_Re[beta],
             color=colors[i],
             label=f"beta={beta}")
plt.xlabel("Re")
plt.ylabel("drag force")
plt.legend()
plt.grid(True, ls="--", lw=0.5)
plt.tight_layout()
plt.show()
