import pylab
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import brewer2mpl

#colorbrewer2 Dark2 qualitative color table
dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 7).mpl_colors

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 50
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 28
rcParams['patch.edgecolor'] = 'white'
rcParams['patch.facecolor'] = dark2_colors[1]
rcParams['font.family'] = 'sans-serif'


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks
    
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()

def drawGraph(totPopList, stateList, figName, xLimit, gTitle):
	grad = pd.DataFrame({'totPopList' : totPopList, 'stateList': stateList})

	plt.figure(figsize=(65, 70))

	totPopList = grad.totPopList[grad.totPopList > 0]
	state = grad.stateList[grad.totPopList > 0]
	pos = np.arange(len(totPopList))

	plt.title('Total disabled population in India by states')
	plt.title(gTitle)
	plt.barh(pos, totPopList)

	#add the numbers to the side of each bar
	for p, c, ch in zip(pos, state, totPopList):
		plt.annotate(str(ch), xy=(ch + 1, p + .5), va='center')

	#customize ticks
	ticks = plt.yticks(pos + .5, state)
	xt = plt.xticks()[0]
	plt.xticks(xt, [' '] * len(xt))

	#minimize chartjunk
	remove_border(left=False, bottom=False)
	plt.grid(axis = 'x', color ='white', linestyle='-')

	#set plot limits
	plt.ylim(pos.max() + 1, pos.min() - 1)
	plt.xlim(0, xLimit)

	pylab.savefig(figName+".png")

if __name__ == "__main__":
	## Testing
	totPopList = [1, 2, 3, 6]
	stateList = ['a', 'b', 'c', 'd']
	drawGraph(totPopList, stateList)
