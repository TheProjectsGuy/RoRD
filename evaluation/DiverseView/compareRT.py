# Compare R and t estimates with ground truth

# %% Import everything
import numpy as np
import os
import glob
from scipy.spatial.transform import Rotation as R

# %%

# %%

# %% Experimental section

# %% Read files
gt_folder = r"C:\Users\123av\Downloads\Datasets\DiverseView\preprocessed\data1\Trans"
gt_folder = os.path.realpath(os.path.expanduser(gt_folder))
assert os.path.isdir(gt_folder)
gtfs_npy = glob.glob(f"{gt_folder}/*.npy")
comp_folder = r"C:\Users\123av\OneDrive - International Institute of Information Technology\RRC\Opposing View Loop Closure\RoRD\RoRD Repo\Understanding\Undesctanding RoRD - Eval - DiverseView\Understanding RT Estimates\out_rord"
comp_folder = os.path.realpath(os.path.expanduser(comp_folder))
assert os.path.isdir(comp_folder)
compfs_npy = glob.glob(f"{comp_folder}/*.npy")

# %%
num_tfs = 0
t_vect_err = 0
r_vect_err = 0
for gt_f, c_f in zip(gtfs_npy, compfs_npy):
    gt_np = np.load(gt_f)
    c_np = np.load(c_f)
    f1, f2, n = gt_np.shape # Same shape
    num_tfs += n    # Number of transforms
    # Translation error
    t_diff = gt_np[0:3, 3, :] - c_np[0:3, 3, :]
    t_vect_err += np.sum(np.linalg.norm(t_diff, axis=0))
    # Rotation error
    R_gt = gt_np[0:3, 0:3, :].transpose(2, 0, 1)
    R_c = c_np[0:3, 0:3, :].transpose(2, 0, 1)
    R_gt_t = R_gt.transpose(0, 2, 1)
    RcRgt = R_c @ R_gt_t
    RcRgt_sp = R.from_matrix(RcRgt)
    RcRgt_axang = RcRgt_sp.as_rotvec()
    r_vect_err += np.sum(np.linalg.norm(RcRgt_axang, axis=1)/(2**(0.5)))

t_err = t_vect_err / num_tfs
r_err = r_vect_err / num_tfs
r_err_deg = r_err * (180/np.pi)

# %%
print(f"Folder: {os.path.basename(comp_folder)}")
print(f"\tT error: {t_err:.3f}, R (deg) err: {r_err_deg:.3f}")

# %%

# %%
