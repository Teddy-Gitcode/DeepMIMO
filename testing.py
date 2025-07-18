#%% Imports

import os
import numpy as np
import deepmimo as dm
import matplotlib.pyplot as plt

from api_keys import DEEPMIMO_API_KEY

#%% V4 Conversion

# Example usage
rt_folder = './RT_SOURCES/asu_campus'

scen_name = os.path.basename(rt_folder)
dm.convert(rt_folder, overwrite=True, scenario_name=scen_name, vis_scene=True)

#%%

dataset = dm.load('asu_campus_3p5')

#%% AODT Conversion
import os
import deepmimo as dm
import pandas as pd

# aodt_scen_name = 'aerial_2025_6_18_16_43_21'  # new (1 user)
# aodt_scen_name = 'aerial_2025_6_22_16_10_16' # old (2 users)
aodt_scen_name = 'aerial_2025_6_18_16_43_21_dyn'  # new (1 user, dynamic)
folder = f'aodt_scripts/{aodt_scen_name}'
# df = pd.read_parquet(os.path.join(folder, 'db_info.parquet'))

# df.head()
aodt_scen = dm.convert(folder, overwrite=True)

#%%

aodt_scen = dm.load(aodt_scen_name, max_paths=500)

#%%
