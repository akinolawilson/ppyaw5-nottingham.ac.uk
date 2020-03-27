import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import matplotlib.widgets as w
import numpy as np 
import random
from matplotlib import rc

class hopfieldModel:

    rc('text', usetex=True)
    rc('font', family='serif')
    global ax1
    global ax2
    global ax3
    global ax4
    global fig
    global tSweepTot
    global negativeSpinConfig
    global finishedButton
    global samplingButton
    global initialisingSpins
    global W
    global patternNumber
    global J
    global finished
    tSweepTot = 0
    fig = plt.figure(figsize=(20,20))    
    ax1 = fig.add_subplot(2,2,1) # plt.axes([0.05, 0.05, 0.4, 0.5])
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    
    fig.suptitle(r"Auto-associative Memory: Hopfield Model \& Monte-Carlo Markov Chain Sampling", y=0.95, fontsize=36)
    
    ax1.set_title(r'Pattern Configuration', fontsize=28)
    ax2.set_title(r'Search', fontsize=28)
    ax3.set_title(r'Initial Sampling Configuration', fontsize=28)
    ax4.set_title(r'Loss', fontsize=28)
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')  
    ax4.set_ylim([-1.05,0])
    ax4.set_xlabel(r'$t$', fontsize=18)
    finishedAxes = plt.axes([0.13, 0.005, 0.1, 0.075])
    finishedButton = w.Button(finishedAxes, 'Finish Pattern')
    finishedButton.label.set_fontsize(22)
    
    samplingAxes = plt.axes([0.25, 0.005, 0.1, 0.075])
    samplingButton = w.Button(samplingAxes, 'Begin Sampling')
    samplingButton.label.set_fontsize(22)
    finished, negativeSpinConfig, N, initialisingSpins, W, patternNumber, J  = 0,0,0,0,0,0,0

    def __init__(self, N):        
        hopfieldModel.N = N
        hopfieldModel.lossDivision = 1
        self.N = N        
        hopfieldModel.finished = finished
        hopfieldModel.patternNumber = 0
        hopfieldModel.W = np.random.rand(self.N**2, self.N**2)
        
        diagW = np.diag(np.diag(hopfieldModel.W))
        hopfieldModel.W  -= diagW  
        
        WRowSums = hopfieldModel.W.sum(axis=1)
        hopfieldModel.W =  hopfieldModel.W/ WRowSums[:, np.newaxis]

        hopfieldModel.negativeSpinConfig =  -1*np.ones((N,N))
        hopfieldModel.p1 = -1*np.ones((N,N))
        hopfieldModel.p2 = -1*np.ones((N,N))
        hopfieldModel.p3 = -1*np.ones((N,N))
        
        for y in range(N):
            for x in range(N):
                if hopfieldModel.negativeSpinConfig[y,x] == -1:
                    ax1.scatter(x,y, s=1000 ,color='red')
                if hopfieldModel.negativeSpinConfig[y,x] == 1:
                    ax1.scatter(x,y, s=1000, color='blue')
# =============================================================================
# removing 0 from initial spin configuration
        fillers = [-1,1]
        hopfieldModel.initialisedSpins = np.reshape(np.random.randint(-1, 2, N*N), (N,N))
        for i in range(N):
            for j in range(N):
                if hopfieldModel.initialisedSpins[i,j] == 0:
                    hopfieldModel.initialisedSpins[i,j] = random.choice(fillers)
                    
        for i in range(N):
            for j in range(N):
                if hopfieldModel.initialisedSpins[i,j] == -1: 
                    ax3.scatter(j,i, s=1000, color='red')
                if hopfieldModel.initialisedSpins[i,j] == 1:
                    ax3.scatter(j,i, s=1000, color='blue')
        
        plt.draw()   
        
    def onClick(event):
        if not event.inaxes == ax1:
            hopfieldModel.patternNumber += 1
            return
        global ix, iy
        ix, iy = event.xdata, event.ydata
        x, y = int(round(ix,1)), int(round(iy,1))
        print('Event button {}'.format(event.button))
        hopfieldModel.lossDivision += int(event.button)
        if hopfieldModel.patternNumber == 0 :
            hopfieldModel.p1[y,x] = 1
            for i in range(hopfieldModel.N):
                for j in range(hopfieldModel.N):
                    if hopfieldModel.p1[i,j] == -1:
                        ax1.scatter(j,i, s=1000, color='red')
                    if hopfieldModel.p1[i,j] == 1:
                        ax1.scatter(j,i, s=1000, color='blue')
            plt.draw()
                        
        elif hopfieldModel.patternNumber == 1:
            hopfieldModel.p2[y,x] = 1
            for i in range(hopfieldModel.N):
                for j in range(hopfieldModel.N):
                    if hopfieldModel.p2[i,j] == -1:
                        ax1.scatter(j,i, s=1000, color='red')
                    if hopfieldModel.p2[i,j] == 1:
                        ax1.scatter(j,i, s=1000, color='blue')
            plt.draw()
        
        elif hopfieldModel.patternNumber == 2:
            hopfieldModel.p3[y,x] = 1
            for i in range(hopfieldModel.N):
                for j in range(hopfieldModel.N):
                    if hopfieldModel.p3[i,j] == -1:
                        ax1.scatter(j,i, s=1000, color='red')
                    if hopfieldModel.p3[i,j] == 1:
                        ax1.scatter(j,i, s=1000, color='blue')
            plt.draw()
            
        elif hopfieldModel.patternNumber == 3:
            print('Maximum patterns entered')
            fig.canvas.mpl_disconnect(cid1)
            hopfieldModel.finished += 1
            hopfieldModel.J = 1/hopfieldModel.N**2 * ( hopfieldModel.p1 + hopfieldModel.p2 + hopfieldModel.p3)
        
    global cid1    
    cid1 = fig.canvas.mpl_connect('button_press_event', onClick)     

    def onPressFinished(event):
        finishedButton.on_clicked(hopfieldModel.patternRefresh)
    
    global cid2
    cid2 = fig.canvas.mpl_connect('button_press_event', onPressFinished)    
    
    def patternRefresh(event):
        for y in range(hopfieldModel.N):
            for x in range(hopfieldModel.N):
                if hopfieldModel.negativeSpinConfig[y,x] == -1:
                    ax1.scatter(x,y, s=1000 ,color='red')
                if hopfieldModel.negativeSpinConfig[y,x] == 1:
                    ax1.scatter(x,y, s=1000, color='blue')   
        plt.draw()
        
  ############      
        
    def beginSampling(event):
        if hopfieldModel.finished == 1:
            print('Beginning sampling')
            samplingButton.on_clicked(hopfieldModel.MH_MCMC())
    
    cid3 = fig.canvas.mpl_connect('button_press_event', beginSampling)
  #############  
    @classmethod     
    def MH_MCMC(cls):
        e = hopfieldModel.metropolisHastings(hopfieldModel.N,
                                             hopfieldModel.initialisedSpins,
                                             hopfieldModel.J,
                                             hopfieldModel.W)
        return e
         
    def metropolisHastings(N,
                           currentConfig,
                           J,
                           W):
        
        energyDifference = []
        tBounding = 1
        beta = 1
        tSweep = 0
        history = []
        J = J.flatten()[:,np.newaxis] @ J.flatten()[:,np.newaxis].T
        S = currentConfig.flatten()[:,np.newaxis] # (N**2, 1)
        
        while tSweep <= tBounding: # entire sweep
            
            Sprime = S            
            randomFlip = random.randint(0, N**2 -1)
            pair = tuple([randomFlip] + list(Sprime.flatten()))
            

            while pair in history:
                randomFlip = random.choice(np.arange(N**2))
                pair = tuple([randomFlip] + list(Sprime.flatten()))
                
            history.append(pair)            
            Sprime[randomFlip] = Sprime[randomFlip] *-1
            
            simPrior = -1/(N*N) * np.squeeze(  S.T @ J @ S )
            simProposed = -1/(N*N) * np.squeeze( Sprime.T @ J @ Sprime )
# =============================================================================     

# =============================================================================
            rand = random.random()    
            if rand <= min(1, np.exp(-beta*(simProposed - simPrior))):
                                    
                history.append(tuple([randomFlip] + list(Sprime.flatten())))          
                S = Sprime
                
                hopfieldModel.W +=  Sprime @ S.T
                
                
                Sprime = np.reshape(Sprime, (N,N))
                for i in range(N):
                    for j in range(N):
                        if Sprime[i,j] == -1: 
                            ax2.scatter(j,i, s=1000, color='red')

                            plt.show(block=False)
                        if Sprime[i,j] == 1:
                            ax2.scatter(j,i, s=1000, color='blue')
                
                S = Sprime.flatten()[:,np.newaxis]

                plt.draw()
                plt.pause(0.005)
                plt.show(block=False) 
                
                   
            tSweep += 1/(N**2)
            energyDifference.append((tSweep, simPrior))
            ax4.plot(*zip(*energyDifference), color='black') 
            plt.draw()
            plt.pause(0.005)
            plt.show(block=False)
            print(history)
            print('Passing through algorithm, temporal step number {} and similarity {}'.format(tSweep, simPrior))
            if tSweep >= 1:
                 tBounding +=1
                 
            if simPrior <= -1: 
                break
        return  energyDifference 
                

#%%
