# Examples for Plot Assistant
#
# Author:   Joseph A'Hearn
# Created:  03/29/2022
#
# This program provides examples to show the features of plot_assistant.py. 
#   

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import plot_assistant as pa 

# generating some data that we will plot; feel free to replace these lines with your own data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.exp(-x/2)

# using the functions of plot_assistant
#   quick_plot example
pa.quick_plot(x, y, 'example', 'x', 'y')

#   black background and xlims,ylims example
fig, ax = pa.initialize_plot(True)
fig, ax = pa.title_and_axes(fig, ax, 'example 2', 'x', 'y', x[0], x[-1], np.amin(z), np.amax(z))
ax.plot(x, z, 'r--')
pa.save_and_clear_plot(fig, [ax], 'example_2', 'png', True)

#   multiple subplots example
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig, ax1 = pa.title_and_axes(fig, ax1, 'example 3', '', 'y')
fig, ax2 = pa.title_and_axes(fig, ax2, '', 'x', 'y')
ax1.xaxis.set_major_locator(ticker.NullLocator()) # removing xtick labels from the top plot because they coincide with those of the bottom plot
ax1.plot(x, 2*y*z, 'r-')
ax2.plot(x, y-z, 'g-')
plt.subplots_adjust(bottom=0.15, top=0.9, hspace=0.15) # customizing the subplot positions so that axis labels are not cut off
pa.save_and_clear_plot(fig, [ax1, ax2], 'example_3', 'png')