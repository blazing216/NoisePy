import noisedbase
import numpy as np
import timeit
import GeoPolygon
import raytomo

# dset=raytomo.RayTomoDataSet('/scratch/summit/life9360/ALASKA_work/hdf5_files/ray_tomo_Alaska_20180716_phase.h5')
dset=raytomo.RayTomoDataSet('/scratch/summit/life9360/ALASKA_work/hdf5_files/ray_tomo_Alaska_20180720_phase_test.h5')
# dset=raytomo.RayTomoDataSet('/work3/leon/ray_tomo_Alaska_20180410.h5')
# dset=raytomo.RayTomoDataSet('../ray_tomo_Alaska_20180410.h5')
# dset=raytomo.RayTomoDataSet('/scratch/summit/life9360/ALASKA_work/hdf5_files/ray_tomo_Alaska_20180410_un_from_TA_AK.h5')
# dset.set_input_parameters(minlon=188, maxlon=238, minlat=52, maxlat=72,  data_pfx='raytomo_in_', smoothpfx='N_INIT_', qcpfx='QC_')
# dset.run_smooth(datadir='/scratch/summit/life9360/ALASKA_work/xcorr_working_dir/raytomo_input', outdir='../ray_tomo_working_dir')
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=True, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=False, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=False, anipara=1, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=False, anipara=2, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)


# dset.set_input_parameters(minlon=188, maxlon=238, minlat=52, maxlat=72,  data_pfx='raytomo_in_', smoothpfx='N_INIT_', qcpfx='QC_', pers=np.array([12.]))
# dset.run_smooth(datadir='/scratch/summit/life9360/ALASKA_work/xcorr_working_dir/raytomo_input', outdir='../ray_tomo_working_dir')
# # # dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=True, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# # # dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=False, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# # # dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=False, anipara=1, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# # # dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.1, isotropic=False, anipara=2, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175)
# 
# dset.run_qc(outdir='../ray_tomo_working_dir', crifactor=2., crilimit=6., \
#             dlon=0.2, dlat=0.1, isotropic=True, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1./1000., sigmaAni0=175)
# dset.run_qc(outdir='../ray_tomo_working_dir', crifactor=2., crilimit=6., \
#             dlon=0.2, dlat=0.1, isotropic=False, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=0., sigmaAni0=175, lengthcell=0.5)

# dset.run_qc(outdir='../ray_tomo_working_dir', crifactor=2., crilimit=20., \
#             dlon=0.2, dlat=0.1, isotropic=False, anipara=1, alphaAni4=1000, alphaAni0=850, betaAni0=1./1000., sigmaAni0=175)
# dset.run_qc(outdir='../ray_tomo_working_dir', crifactor=2., crilimit=20.,\
#             dlon=0.2, dlat=0.1, isotropic=False, anipara=2, alphaAni4=1000, alphaAni0=850, betaAni0=1./1000., sigmaAni0=175)

# dset.get_data4plot(dataid='qc_run_1', period=12.)
# dset.plot_vel_iso(vmin=2.9, vmax=3.5, fastaxis=False, projection='global')
# dset.plot_vel_iso(vmin=3.5, vmax=4.0)
# dset.plot_fast_axis()
# dset.generate_corrected_map(dataid='qc_run_0', glbdir='./MAPS', outdir='./REG_MAPS')
# dset.plot_global_map(period=50., inglbpfx='./MAPS/smpkolya_phv_R')

# dset.plot(1,1,'v', 10., clabel='C (km/s)')

# dset=raytomo.RayTomoDataSet('/scratch/summit/life9360/ALASKA_work/hdf5_files/ray_tomo_Alaska_20180410_gr.h5')
# dset.set_input_parameters(minlon=188, maxlon=238, minlat=52, maxlat=72, data_pfx='raytomo_in_', smoothpfx='N_INIT_', qcpfx='QC_')
# 
# dset.run_smooth(datadir='./raytomo_input', dlon=0.2, dlat=0.2, outdir='../ray_tomo_working_dir', datatype='gr')
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.2, isotropic=True, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175, datatype='gr')
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.2,isotropic=False, anipara=0, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175, datatype='gr')
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.2,isotropic=False, anipara=1, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175, datatype='gr')
# dset.run_qc(outdir='../ray_tomo_working_dir', dlon=0.2, dlat=0.2,isotropic=False, anipara=2, alphaAni4=1000, alphaAni0=850, betaAni0=1, sigmaAni0=175, datatype='gr')

# dset.get_uncertainty(runid=2, ineikfname='/scratch/summit/life9360/ALASKA_work/hdf5_files/eikonal_xcorr_tomo_Alaska_20180411.h5', percentage=0.9, num_thresh=100)
# dset.get_uncertainty(runid=2, ineikfname='/scratch/summit/life9360/ALASKA_work/hdf5_files/eikonal_xcorr_tomo_Alaska_TA_AK_20180411.h5', percentage=0.9, num_thresh=100)

# dset.interp_surface(dlon=0.5, dlat=0.5, runid = 2)