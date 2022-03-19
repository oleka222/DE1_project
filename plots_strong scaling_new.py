# -*- coding: utf-8 -*-
"""
@author: irina
"""
import matplotlib.pyplot as plt


# in seconds
avg_time_all = [1526.19531790415, 846.378622611363,603.957156022389,363.007424910863, 227.397211551666, 189.157458305358]
avg_time_lr = [1316.17756708463, 699.946985880533, 512.492019414901, 303.27927160263, 178.970550457636, 136.926097869873]

num_cores = [1, 2, 4, 8, 12, 16] 

#in minutes
avg_time_all_minutes = [x/60 for x in avg_time_all]
avg_time_lr_minutes = [x/60 for x in avg_time_lr]

speedup_minutes = [avg_time_all_minutes[0]/x for x in avg_time_all_minutes]
speedup_lr_minutes = [avg_time_lr_minutes[0]/x for x in avg_time_lr_minutes]

'''Calculations and plots in minutes'''
'''Execution times plot'''
fig, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize = (12,5))
axs[0].plot(num_cores, avg_time_all_minutes)
axs[1].plot(num_cores, avg_time_lr_minutes)
axs[0].set_ylabel('Time (minutes)')
axs[0].set_xlabel('Number of cores')
axs[1].set_xlabel('Number of cores')
axs[0].set_title('Execution time of the whole algorithm')
axs[1].set_title('Execution time of the log regression part')

'''Speedup plot'''
fig, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize = (12,5))
axs[0].plot(num_cores, speedup_minutes)
axs[1].plot(num_cores, speedup_lr_minutes)
axs[0].set_ylabel('Speedup')
axs[0].set_xlabel('Number of cores')
axs[1].set_xlabel('Number of cores')
axs[0].set_title('Speedup of the whole algorithm')
axs[1].set_title('Speedup of the log regression part')
axs[0].grid()
axs[1].grid()

