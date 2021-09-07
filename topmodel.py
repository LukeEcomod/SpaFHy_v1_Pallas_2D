# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 15:14:11 2017
@author: slauniai
******************************************************************************
TopModel (Beven & Kirkby) -implementation for SpatHy -integration
Topmodel() allows spatially varying soil depths and transmissivity
Topmodel_Homogenous() assumes constant properties and hydrologic similarity \n
retermined from TWI = log (a / tan(b))
(C) Samuli Launiainen, 2016-
Last edit: 7.2.2018 / Samuli Launiainen
******************************************************************************
"""

import numpy as np
# import matplotlib.pyplot as plt
eps = np.finfo(float).eps  # machine epsilon

class Topmodel_Homogenous():
    def __init__(self, pp, S_initial=None, outputs=False):
        """
        sets up Topmodel for the catchment assuming homogenous
        effective soil depth 'm' and sat. hydr. conductivity 'ko'.
        This is the 'classic' version of Topmodel where hydrologic similarity\
        index is TWI = log(a / tan(b)).
        
        Args:
            pp - parameter dict with keys:
                dt - timestep [s]
                ko - soil transmissivity at saturation [m/s]
                m -  effective soil depth (m), i.e. decay factor of Ksat with depth
                twi_cutoff - max allowed twi -index
                so - initial catchment average saturation deficit (m)
            cmask - catchment mask, 1 = catchment_cell
            cellarea - gridcell area [m2]
            flowacc - flow accumulation per unit contour length (m)
            slope - local slope (deg)
            S_initial - initial storage deficit, overrides that in 'pp'
            outputs - True stores outputs after each timestep into dictionary
        """
        if not S_initial:
            S_initial = pp['so']

        self.dt = float(pp['dt'])
        cmask = pp['cmask']
        flowacc = pp['flowacc']
        slope = pp['slope']
        self.CellArea = len(~np.isnan(cmask)) * 16
        dx = self.CellArea**0.5
        self.CatchmentArea = np.size(cmask[cmask == 1])*self.CellArea
        self.qr = np.full_like(cmask, 0.0)

        # topography
        self.a = flowacc*cmask  # flow accumulation grid
        self.slope = slope*cmask  # slope (deg) grid

        # effective soil depth [m]
        self.M = pp['m']
        # lat. hydr. conductivity at surface [m2/timestep]
        # self.To = pp['ko']*pp['m']*self.dt
        self.To = pp['ko']*self.dt
        
        """ 
        local and catchment average hydrologic similarity indices (xi, X).
        Set xi > twi_cutoff equal to cutoff value to remove tail of twi-distribution.
        This concerns mainly the stream network cells. 'Outliers' in twi-distribution are
        problem for streamflow prediction
        """
        slope_rad = np.radians(self.slope)  # deg to rad

        xi = np.log(self.a / dx / (np.tan(slope_rad) + eps))
        # apply cutoff
        clim = np.percentile(xi[xi > 0], pp['twi_cutoff'])
        xi[xi > clim] = clim
        self.xi = xi
  
        self.X = 1.0 / self.CatchmentArea*np.nansum(self.xi*self.CellArea)

        # baseflow rate when catchment Smean=0.0
        self.Qo = self.To*np.exp(-self.X)

        # catchment average saturation deficit S [m] is the only state variable
        s = self.local_s(S_initial)
        s[s < 0] = 0.0
        self.S = np.nanmean(s)

        # create dictionary of empty lists for saving results
        if outputs:
            self.results = {'S': [], 'Qb': [], 'Qr': [], 'Qt': [], 'qr': [],
                            'fsat': [], 'Mbe': [], 'R': []
                           }

    def local_s(self, Smean):
        """
        computes local storage deficit s [m] from catchment average
        """
        s = Smean + self.M*(self.X - self.xi)
        return s

    def subsurfaceflow(self):
        """subsurface flow to stream network (per unit catchment area)"""
        Qb = self.Qo*np.exp(-self.S / (self.M + eps))
        return Qb

    def run_timestep(self, R):
        """
        runs a timestep, updates saturation deficit and returns fluxes
        Args:
            R - recharge [m per unit catchment area] during timestep
        OUT:
            Qb - baseflow [m per unit area]
            Qr - returnflow [m per unit area]
            qr - distributed returnflow [m]
            fsat - saturated area fraction [-]
        Note: 
            R is the mean drainage [m] from bucketgrid.
        """
        #print(R)
        # initial conditions
        So = self.S
        s = self.local_s(So)

        # subsurface flow, based on initial state
        Qb = self.subsurfaceflow()
        #print(np.unique(Qb))
        #print(Qb)

        # update storage deficit and check where we have returnflow 
        S = So + Qb - R
        s = self.local_s(S)

        # returnflow grid
        self.qr = -s
        self.qr[self.qr < 0] = 0.0  # returnflow grid, m
        
        # average returnflow per unit area
        Qr = np.nansum(self.qr)*self.CellArea / self.CatchmentArea

        # now all saturation excess is in Qr so update s and S. 
        # Deficit increases when Qr is removed 
        S = S + Qr
        self.S = S

        # saturated area fraction
        ix = np.where(s <= 0)
        # fsat = np.max(np.shape(ix))*self.CellArea / self.CatchmentArea
        fsat = len(ix[0])*self.CellArea / self.CatchmentArea
        del ix
        
        # check mass balance
        dS = (So - self.S)
        dF = R - Qb - Qr
        mbe = dS - dF
        
        
        results = {
                'baseflow': Qb * 1e3,  # [mm d-1]
                'water_closure': mbe * 1e3, #     
                'saturated_area': self.S, # [mm]
                }

        return results



        # append results
        '''if hasattr(self, 'results'):
            self.results['R'].append(R)
            self.results['S'].append(self.S)
            self.results['Qb'].append(Qb)
            self.results['Qr'].append(Qr)
            self.results['qr'].append(qr)
            self.results['fsat'].append(fsat)
            self.results['Mbe'].append(mbe)
        return Qb, Qr, qr, fsat'''