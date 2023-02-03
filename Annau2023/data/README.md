# Test Data Readme

The GANs were not trained on this data. This is the test data from the years 2000, 2006, 2010.

For convenience, the test data have been converted to a PyTorch extension `.pt` and organized as `lr` or    `hr` for low-resolution and high-resolution data, with the region in the filename. i.e. `{resolution}_test_{region}.pt`.

The test data is organized by experiment. The frequency separation data were preprocessed using an earlier version of the pipeline I am currently using. It was easier to organize the analysis code so that the files are preprocessed in the same way that they were while training the respective GANs.

### Folders
* `fs_data` contains the data that is preprocessed the same way as the data that was used to train the FS GANs (frequency separation GANs)
* `nfs_pfs` contains contains the data that is preprocessed the same way as the data that was used to train both the PFS GANs (partial frequency separation GANs) and NFS GANs (no frequency separation GANs)
* `idealized_data` contains the preprocessed files that only use the `u10` and `v10` wind components of either `era` (non idealized) or `wrf` (idealized, coarsened version of the HR data)
* `shapefiles` used for plotting
* `metric_evolution` for metric plots
* `full_domain` for Fig 1 full WRF domain netCDF files