# Plot Assistant
#
# Author:   Joseph A'Hearn
# Created:  06/26/2017
# Polished: 03/29/2022
#
# This program includes functions I often use in plots. 
#   

import matplotlib.pyplot as plt 

def initialize_plot(black=False):
	if (black):
		fig = plt.figure(facecolor='black')
	else:
		fig = plt.figure()
	return fig, fig.add_subplot(111)

def title_and_axes(fig, ax, title, xlabel, ylabel, xmin=None, xmax=None, ymin=None, ymax=None, fontsize=20):
	ax.set_title(title, fontsize=fontsize+2)
	ax.set_xlabel(xlabel, fontsize=fontsize)
	ax.set_ylabel(ylabel, fontsize=fontsize)
	plt.rc('xtick', labelsize=fontsize-2) 
	plt.rc('ytick', labelsize=fontsize-2) 
	if((xmin != None) and (xmax != None)):
		ax.set_xlim([xmin,xmax])
	if((ymin != None) and (ymax != None)):
		ax.set_ylim([ymin,ymax])
	return fig, ax 

def save_and_clear_plot(fig, axes, filename='Figure', ext='pdf', black=False):
	for ax in axes:
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.spines['bottom'].set_linewidth(0.5)
		ax.spines['left'].set_linewidth(0.5)
		ax.tick_params(axis='both', direction='in')
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()
		if(black):
			ax.spines['bottom'].set_color('white')
			ax.spines['left'].set_color('white')
			ax.title.set_color('white')
			ax.yaxis.label.set_color('white')
			ax.xaxis.label.set_color('white')
			ax.tick_params(axis='x', colors='white')
			ax.tick_params(axis='y', colors='white')
	if(black):
		axes[0].figure.savefig(filename + '.' + ext, facecolor=fig.get_facecolor(), transparent=True)
	else:
		axes[0].figure.savefig(filename + '.' + ext)
	plt.clf()

def quick_plot(x, y, title='', xlabel='', ylabel=''):
	fig, ax = initialize_plot()
	fig, ax = title_and_axes(fig, ax, title, xlabel, ylabel)
	ax.scatter(x, y)
	save_and_clear_plot(fig, [ax], filename='quick_plot_' + title, ext='png')