import subprocess

runs = {
        "florida":
        {
            "CNN": (1, 'e25c6b40324643c3afc1cf42981b11b5'),
            "13x13": (0, 'e1d15a0615ca489aa6a17ec60247d0af'),
            "9x9": (0, '3f48868c52404eb0a833897aa4642871'),
            "5x5": (0, '1824682ae27c48669665cf042052d584'),
            "NFS": (0, 'feda42500d2b45549be96f1bf62b0b03'),
            "PFS 500 13x13": ("partialFS_c5", '3d2ea1e5f805454ea485a3a7c783fd5a'),
            "PFS 500 9x9": ("partialFS_c5", 'caf7f501306848f8bc746605c4994e31'),
            "PFS 500 5x5": ("partialFS_c5", '90375b9266eb442cb15073895e14d691'),
            "PFS 50 13x13": ("partialFS", '5c9745ff961e46f9af206d36b6567fae'),
            "PFS 50 9x9": ("partialFS", '3858c673c9344e7caf24144335981752'),
            "PFS 50 5x5": ("partialFS", '328e5221158147a9ba9b41ab2ac385c7'),
        },
       "central":
        {
            "CNN": (1, 'fbe44b0423204805bc6af4d7d6ac562e'),
            "13x13": (0, 'bcf7e7cfa8ab4c4196ad6a2bb18e8601'),
            "9x9": (0, '079a94c41ad3482996cc2b9f95adba8d'),
            "5x5": (0, '202ea9f8a73b401fa22e62c24d9ab2d0'),
            "NFS": (0, '0c5ee480663f4f9eb7200f8879aa1244'),
            "PFS 500 13x13": ("partialFS_c5", 'c5154f8f03c74cba924d789357e5ca84'),
            "PFS 500 9x9": ("partialFS_c5", 'e54c953370974e2db09a37e9c0c7cdb5'),
            "PFS 500 5x5": ("partialFS_c5", '1570ac86f8e94e83b85447618ca576f5'),
            "PFS 50 13x13": ("partialFS", 'eedf0cd864204866b98e5de5e710f9c3'),
            "PFS 50 9x9": ("partialFS", '1d568d304d7546f78c57e98ff1366b9d'),
            "PFS 50 5x5": ("partialFS", '9400ee7db2004aa3b03e91ff710061eb'),
        },
        "west":
        {
            "CNN": (1, 'f76c0170818244629de4544805f93a59'),
            "13x13": (0, 'c4ec13e65fe74b399fc9e325a9966fef'),
            "9x9": (0, '6abe7a9940c04b47819689070100e5e6'),
            "5x5": (0, '70f5be887eff42e8a216780752644b2f'),
            "NFS": (0, 'db9f0fae83c949eaad5d1176a43dae47'),
            "PFS 500 13x13": ("partialFS_c5", '2e78fba6814545f0be62896cd14b031f'),
            "PFS 500 9x9": ("partialFS_c5", 'ad5772150e7547ee8d14aa7bac192f54'),
            "PFS 500 5x5": ("partialFS_c5", 'c5c5e0e8aad5411783329f31db91ff78'),
            "PFS 50 13x13": ("partialFS", 'faa34028b516487185c994f48621050a'),
            "PFS 50 9x9": ("partialFS", '2faf762448b54ae2b96234d6c77c38b3'),
            "PFS 50 5x5": ("partialFS", '4f0574ec4f7147f1b0555cafeb1cc98f'),
        }
}

for region in runs:
    subprocess.run(["echo", f"Starting transfer of {region}"])
    for model in runs[region]:
        enum, hc = runs[region][model]
        # Move generator models over
        nvmepath = f"/home/nannau/nvmeblack/Annau-2022/models/store/{hc}"
        if subprocess.call(["test", "-e", nvmepath]) == 0:
            subprocess.run(["echo", "Removing existing directories!"])
            subprocess.run(["rm", "-rf", nvmepath])

        # subprocess.run(["mkdir", nvmepath])
        subprocess.run([
            "rsync",
            "-avR",
            f"/home/nannau/msc/Fall_2021/DoWnGAN/DoWnGAN/mlflow_experiments/{enum}/{hc}/artifacts/./Generator/Generator_999", 
            nvmepath]
        )

