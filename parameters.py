
# -*- coding: utf-8 -*-
"""
PARAMETERS
@author: slauniai & khaahti
"""
import pathlib
import time


def parameters(folder=''):

    pgen = {'description': 'testcase',  # description written in result file
            'simtype': '2D', # 1D, TOP, 2D
            'start_date': '2007-08-01',  # '2007-08-01'
            'end_date': '2021-09-09', # 2021-09-09
            'spinup_end': '2008-12-31',  # '2008-12-31' / '2009-08-01' results after this are saved in result file
            'dt': 86400.0,
            'spatial_cpy': True,  # if False uses parameters from cpy['state']
            # else needs cf.dat, hc.dat, LAI_decid.dat, LAI_spruce.dat, LAI_pine.dat, (cmask.dat)
            'spatial_soil': True,  # if False uses soil_id, ditch_depth, ditch_spacing from psp
            'topmodel': True,
            # else needs soil_id.dat, ditch_depth.dat, ditch_spacing.dat
            'spatial_forcing': False,  # if False uses forcing from forcing file with pgen['forcing_id'] and cpy['loc']
            # else needs Ncoord.dat, Ecoord.dat, forcing_id.dat
            'gis_folder': str(pathlib.Path(folder+r'/parameters')),
            'forcing_file': str(pathlib.Path(folder+r'/forcing/Kenttarova_forcing_era5.csv')),
            'forcing_id': 0,  # used if spatial_forcing == False
            'ncf_file': folder + '_' + time.strftime('%Y%m%d%H%M') + r'.nc',  # added timestamp to result file name to avoid saving problem when running repeatedly
            'results_folder': r'D:\SpaFHy_2D_2021/',
            'save_interval': 366, # interval for writing results to file (decreases need for memory during computation)
            'variables':[ # list of output variables (rows can be commented away if not all variables are of interest)
                    ['parameters_lai_conif', 'leaf area index of conifers [m2 m-2]'],
                    ['parameters_lai_decid_max', 'leaf area index of decidious trees [m2 m-2]'],
                    ['parameters_lai_shrub', 'leaf area index of shrubs [m2 m-2]'],
                    ['parameters_lai_grass', 'leaf area index of grass [m2 m-2]'],
                    ['parameters_hc', 'canopy height [m]'],
                    ['parameters_cf', 'canopy closure [-]'],
                    ['parameters_soilclass', 'soil class index'],
                    ['parameters_elevation', 'elevation from dem [m]'],
                    ['parameters_lat', 'latitude [deg]'],
                    ['parameters_lon', 'longitude [deg]'],
                    ['parameters_ditches', 'ditches'],
                    ['parameters_cmask', 'cmask'],
                    ['parameters_sitetype', 'sitetype'],
                    ['parameters_twi', 'twi'],
                    ['forcing_air_temperature', 'air temperature [degC]'],
                    ['forcing_precipitation', 'precipitation [mm d-1]'],
                    ['forcing_vapor_pressure_deficit', 'vapor pressure deficit [kPa]'],
                    ['forcing_global_radiation', 'global radiation [Wm-2]'],
                    ['forcing_wind_speed','wind speed [m s-1]'],
                    #['bucket_pond_storage', 'pond storage [m]'],
                    ['bucket_moisture_top', 'volumetric water content of moss layer [m3 m-3]'],
                    ['bucket_moisture_root', 'volumetric water content of rootzone [m3 m-3]'],
                    ['bucket_potential_infiltration', 'potential infiltration [mm d-1]'],
                    ['bucket_surface_runoff', 'surface runoff [mm d-1]'],
                    ['bucket_evaporation', 'evaporation from soil surface [mm d-1]'],
                    ['bucket_drainage', 'drainage from root layer [mm d-1]'],
                    ['bucket_water_storage', 'bucket water storage (top and root) [mm d-1]'],
                    ['bucket_storage_change', 'bucket water storage change (top and root) [mm d-1]'],
                    ['bucket_water_closure', 'bucket water balance error [mm d-1]'],
                    ['bucket_return_flow', 'return flow from deepzone to bucket [mm d-1]'],
                    ['soil_water_storage', 'soil water storage (deeplayer) [m]'],
                    ['soil_ground_water_level', 'ground water level [m]'],
                    ['soil_lateral_netflow', 'subsurface lateral netflow [mm d-1]'],
                    ['soil_netflow_to_ditch', 'netflow to ditch [mm d-1]'],
                    ['soil_moisture_deep', 'volumetric water content of deepzone [m3 m-3]'],
                    ['soil_water_closure', 'soil water balance error [mm d-1]'],
                    ['soil_transpiration_limitation', 'transpiration limitation [-]'],
                    #['canopy_interception', 'canopy interception [mm d-1]'],
                    ['canopy_evaporation', 'evaporation from interception storage [mm d-1]'],
                    ['canopy_transpiration','transpiration [mm d-1]'],
                    #['canopy_stomatal_conductance','stomatal conductance [m s-1]'],
                    #['canopy_throughfall', 'throughfall to moss or snow [mm d-1]'],
                    ['canopy_snow_water_equivalent', 'snow water equivalent [mm]'],
                    ['canopy_water_closure', 'canopy water balance error [mm d-1]'],
                    #['canopy_phenostate', 'canopy phenological state [-]'],
                    #['canopy_leaf_area_index', 'canopy leaf area index [m2 m-2]'],
                    #['canopy_degree_day_sum', 'sum of degree days [degC]'],
                    #['canopy_fLAI', 'state of LAI'],
                    ['canopy_water_storage', 'canopy intercepted water storage'],
                    ['canopy_snowfall', 'canopy snowfall'],
                    ['top_baseflow', 'topmodel baseflow [mm d-1]'],
                    ['top_water_closure', 'topmodel water balance error [mm d-1]'],
                    ['top_returnflow', 'topmodel returnflow [mm d-1]'],
                    ['top_local_returnflow', 'topmodel local returnflow [mm d-1]'],
                    ['top_drainage_in', 'topmodel inflow from drainage [mm d-1]'],
                    ['top_saturation_deficit', 'topmodel saturation deficit [m]'],
                    ['top_local_saturation_deficit', 'topmodel local saturation deficit [mm]'],
                    ['top_saturated_area', 'topmodel saturated area [-]'],
                    ['top_storage_change', 'topmodel_water_storage_change [mm d-1]']

                    ]
             }

    f=1.0

    # canopygrid
    pcpy = {'flow' : {  # flow field
                     'zmeas': 2.0,
                     'zground': 0.5,
                     'zo_ground': 0.01
                     },
            'interc': {  # interception
                        'wmax': 1.5,  # storage capacity for rain (mm/LAI)
                        'wmaxsnow': 4.5,  # storage capacity for snow (mm/LAI)
                        },
            'snow': {  # degree-day snow model
                    'kmelt': 2.8934e-05,  # melt coefficient in open (mm/s)
                    'kfreeze': 5.79e-6,  # freezing coefficient (mm/s)
                    'r': 0.05  # maximum fraction of liquid in snow (-)
                    },
            'physpara': {
                        # canopy conductance
                        'amax': 10.0, # maximum photosynthetic rate (umolm-2(leaf)s-1)
                        'g1_conif': f * 2.1, # stomatal parameter, conifers
                        'g1_decid': f * 3.5, # stomatal parameter, deciduous
                        'q50': 50.0, # light response parameter (Wm-2)
                        'kp': 0.6, # light attenuation parameter (-)
                        'rw': 0.20, # critical value for REW (-),
                        'rwmin': 0.02, # minimum relative conductance (-)
                        # soil evaporation
                        'gsoil': 1e-2 # soil surface conductance if soil is fully wet (m/s)
                        },
            'spec_para': {
                        'conif': {'amax': 10.0, # maximum photosynthetic rate (umolm-2(leaf)s-1)
                                    'g1': 2.1, # stomatal parameter
                                    'q50': 50.0, # light response parameter (Wm-2)
                                    'lai_cycle': False,
                                     },
                        'decid': {'amax': 10.0, # maximum photosynthetic rate (umolm-2(leaf)s-1)
                                     'g1': 3.5, # stomatal parameter
                                     'q50': 50.0, # light response parameter (Wm-2)
                                     'lai_cycle': True,
                                     },
                        'shrub':    {'amax': 10.0, # maximum photosynthetic rate (umolm-2(leaf)s-1)
                                     'g1': 3.0, # stomatal parameter
                                     'q50': 50.0, # light response parameter (Wm-2)
                                     'lai_cycle': False,
                                     },
                        'grass':    {'amax': 10.0, # maximum photosynthetic rate (umolm-2(leaf)s-1)
                                     'g1': 5.0, # stomatal parameter
                                     'q50': 50.0, # light response parameter (Wm-2)
                                     'lai_cycle': True,
                                     },
                        },
            'phenopara': {
                        # seasonal cycle of physiology: smax [degC], tau[d], xo[degC],fmin[-](residual photocapasity)
                        'smax': 18.5, # degC
                        'tau': 13.0, # days
                        'xo': -4.0, # degC
                        'fmin': 0.05, # minimum photosynthetic capacity in winter (-)
                        # deciduos phenology
                        'lai_decid_min': 0.1, # minimum relative LAI (-)
                        'ddo': 45.0, # degree-days for bud-burst (5degC threshold)
                        'ddur': 23.0, # duration of leaf development (days)
                        'sdl': 9.0, # daylength for senescence start (h)
                        'sdur': 30.0, # duration of leaf senescence (days),
                         },
            'state': {  # following properties are used if spatial_cpy == False
                       'lai_conif': 3.5, # conifer 1-sided LAI (m2 m-2)
                       'lai_decid_max': 0.5, # maximum annual deciduous 1-sided LAI (m2 m-2)
                       'lai_shrub': 0.1,
                       'lai_grass': 0.2,
                       'hc': 16.0, # canopy height (m)
                       'cf': 0.6, # canopy closure fraction (-)
                       #initial state of canopy storage [mm] and snow water equivalent [mm]
                       'w': 0.0, # canopy storage mm
                       'swe': 0.0, # snow water equivalent mm
                       },
            'loc': {  # following coordinates used if spatial_forcing == False
                    'lat': 67.995,  # decimal degrees
                    'lon': 24.224
                    }
            }

    # soil profile
    psp = {
            # soil profile, following properties are used if spatial_soil = False
            'soil_id': 2.0,
            # organic (moss) layer
            'org_depth': 0.05, # depth of organic top layer (m)
            'org_poros': 0.9, # porosity (-)
            'org_fc': 0.3, # field capacity (-)
            'org_rw': 0.15, # critical vol. moisture content (-) for decreasing phase in Ef
            'maxpond': 0.0,
            # rootzone layer
            'root_depth': 0.3, # depth of rootzone layer (m)
            'root_sat': 0.6, # root zone saturation ratio (-)
            'root_fc': 0.33, # root zone field capacity
            'root_poros': 0.448, # root zone porosity
            'root_wp': 0.13, # root zone wilting point
            'root_ksat': 1e-05, # root zone hydraulic conductivity
            'root_beta': 4.7,
            # initial states
            'ground_water_level': -0.5,  # groundwater depth [m]
            'org_sat': 1.0, # organic top layer saturation ratio (-)
            'pond_storage': 0.0,  # initial pond depth at surface [m]
            'ditch_depth': -0.2   # initial ditch water level relative to ground surface (currently not dynamic) [m]
            }

    return pgen, pcpy, psp


def ptopmodel():
    """
    parameters of topmodel submodel
    """
    ptopmodel = {'dt': 86400.0, # timestep (s)
            'm': 0.025, # 0.025, scaling depth (m)
            'ko': 0.001, # transmissivity parameter (ms-1)
            'twi_cutoff': 99.5,  # cutoff of cumulative twi distribution (%)
            'so': 0.05 # initial saturation deficit (m)
           }
    return ptopmodel



def topsoil():
    """
    Properties of typical topsoils
    Following main site type (1-4) classification
    """
    topsoil = {
        'mineral':{
            'topsoil_id': 1,
            'org_depth': 0.05,
            'org_poros': 0.88,
            'org_fc': 0.33,
            'org_rw': 0.15
            },
        'fen':{
            'topsoil_id': 2,
            'org_depth': 0.05,
            'org_poros': 0.88,
            'org_fc': 0.514,
            'org_rw': 0.15
            },
        'peatland':{
            'topsoil_id': 3,
            'org_depth': 0.05,
            'org_poros': 0.88,
            'org_fc': 0.53,
            'org_rw': 0.15
            },
        'openmire':{
            'topsoil_id': 4,
            'org_depth': 0.05,
            'org_poros': 0.88,
            'org_fc': 0.53,
            'org_rw': 0.15
            }
        }
    return topsoil


def soilprofiles():
    """
    Properties of soil profiles.
    Note z is elevation of lower boundary of layer (soil surface at 0.0),
    e.g. z = [-0.05, -0.15] means first layer tickness is 5 cm and second 10 cm.
    Output 'soil_rootzone_moisture' is calculated for two first layers.
    """
    soilp = {
        'CoarseTextured':{
            'soil_id': 1.0,
            'z': [-0.5, -4.0],
            'pF': {  # vanGenuchten water retention parameters
                    'ThetaS': [0.348]*2,
                    'ThetaR': [0.03]*2,
                    'alpha': [0.054]*2,
                    'n': [1.293]*2},
            'saturated_conductivity': [1E-04, 1E-05],
                },
        'MediumTextured':{
            'soil_id': 2.0,
            'z': [-0.5, -4.0],
            'pF': {  # vanGenuchten water retention parameters
                    'ThetaS': [0.448]*2, # MEASURED AND OPTIMIZED PARAMETER
                    'ThetaR': [0.03]*2, # MEASURED AND OPTIMIZED PARAMETER
                    'alpha': [0.054]*2, # MEASURED AND OPTIMIZED PARAMETER
                    'n': [1.293]*2}, # MEASURED AND OPTIMIZED PARAMETER
            'saturated_conductivity': [1E-05, 1E-05],
                },
        'FineTextured':{
            'soil_id': 3.0,
            'z': [-0.05, -0.1, -0.8, -4.0],
            'pF': {  # vanGenuchten water retention parameters
                    'ThetaS': [0.443]*4,
                    'ThetaR': [0.03]*4,
                    'alpha': [0.054]*4,
                    'n': [1.293]*4},
            'saturated_conductivity': [1E-05]*4,
                },
        'Peat':{
            'soil_id': 4.0,
            'z': [-0.3, -0.6, -0.9, -1.2, -4.0],
            'pF': {  # vanGenuchten water retention parameters
                    'ThetaS': [0.88]*5,  # MEASURED AND OPTIMIZED PARAMETER
                    'ThetaR': [0.196]*5, # MEASURED AND OPTIMIZED PARAMETER
                    'alpha': [0.072]*5,  # MEASURED AND OPTIMIZED PARAMETER
                    'n': [1.255]*5}, # MEASURED AND OPTIMIZED PARAMETER
            'saturated_conductivity': [1E-04, 5E-05, 1E-05, 5E-07, 2E-07], # MEASURED
                },
        'Humus': {
            'soil_id': 5.0,
            'z': [-2.0],
            'pF': {  # vanGenuchten water retention parameters
                    'ThetaS': [0.44],
                    'ThetaR': [0.024],
                    'alpha': [0.053],
                    'n': [1.251]},
            'saturated_conductivity': [1E-06],
                },
            }
    return soilp


def rootproperties():
    """
    Defines 5 soil types: Fine, Medium and Coarse textured + organic Peat
    and Humus.
    Currently SpaFHy needs following parameters: soil_id, poros, dc, wp, wr,
    n, alpha, Ksat, beta
    """
    psoil = {
            'CoarseTextured':
                 {'root_airentry': 20.8,
                  'root_alpha': 0.024,
                  'root_beta': 3.1,
                  'root_fc': 0.21,
                  'root_ksat': 1E-04,
                  'root_n': 1.2,
                  'root_poros': 0.41,
                  'soil_id': 1.0,
                  'root_wp': 0.10,
                  'root_wr': 0.05,
                 },
             'MediumTextured':
                 {'root_airentry': 20.8,
                  'root_alpha': 0.024,
                  'root_beta': 4.7,
                  'root_fc': 0.33,
                  'root_ksat': 1E-05,
                  'root_n': 1.2,
                  'root_poros': 0.448,
                  'soil_id': 2.0,
                  'root_wp': 0.13,
                  'root_wr': 0.05,
                 },
             'FineTextured':
                 {'root_airentry': 34.2,
                  'root_alpha': 0.018, # van genuchten parameter
                  'root_beta': 7.9,
                  'root_fc': 0.34,
                  'root_ksat': 1E-05, # saturated hydraulic conductivity
                  'root_n': 1.16, # van genuchten parameter
                  'root_poros': 0.443, # porosity (-)
                  'soil_id': 3.0,
                  'root_wp': 0.25, # wilting point (-)
                  'root_wr': 0.07,
                 },
             'Peat':
                 {'root_airentry': 29.2,
                  'root_alpha': 0.08, # Menbery et al. 2021
                  'root_beta': 6.0,
                  'root_fc': 0.53, # MEASURED
                  'root_ksat': 3E-04, # MEASURED
                  'root_n': 1.75, # Menbery et al. 2021
                  'root_poros': 0.888, # MEASURED
                  'soil_id': 4.0,
                  'root_wp': 0.36, # Menbery et al. 2021
                  'root_wr': 0.0,
                 },
              'Humus':
                 {'root_airentry': 29.2,
                  'root_alpha': 0.123,
                  'root_beta': 6.0,
                  'root_fc': 0.35,
                  'root_ksat': 8e-06,
                  'root_n': 1.28,
                  'root_poros': 0.85,
                  'soil_id': 5.0,
                  'root_wp': 0.15,
                  'root_wr': 0.01,
                 },
            }
    return psoil