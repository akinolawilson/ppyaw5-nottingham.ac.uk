# Monte-Carlo Markov Chain Simulation: Sampling of Hopfield Spin Model Visualization
________________________________________________________________________________________________________________________________________

## Overview 
________________________________________________________________________________________________________________________________________

This repository contains the class of a Hopfield network, a form of recurrent artificial neural network with associative memory.
In particular, this class allows the visualization of the sampling process from which the transition matrix for a maximum collection of 
three specified patterns is generated. By considering the problem as a collection of spins with binary values, variant of the Ising Model, 
one is able to sample the underlying distribution describing the pattern(s). Although this distribution may be complex, the implementing of
the Metropolis–Hastings algorithm, a Monte-Carlo Mark Chain sampling method, allows one to be able to sample from this distribution through
a sequences of random samples.  
<br>
## Prerequisites
________________________________________________________________________________________________________________________________________
To make use of the class, a user would need the following packages:-
* Numpy 
* Matplotlib
_______________________________________________________________________________________________________________________________________
## Example of instantiation

```
# Before executing the following instantiation of the class, ensure that the figure settings are set to floating graphics, i.e. not inline.
# Then run the file containing the class, this will open an empty figure window. Leave this open and then enter the following command 
network = hopfieldModel(N)
# N denotes the dimension of the _square_ lattice of binary spins.
# The figure will now contain 4 plots; the first a section to enter a maximum of three patterns. Simply click the red scatter plot to
# begin to enter of pattern. In between each specification of a pattern, press the button 'Finish Pattern'. After the last pattern, press
# the 'Begin Sampling' to kick start the sampling process. The second plot will reveal the sampling process, the third plot contains the initial
# configuration from which the random sequences of samples is generated, the last plot contains the loss throughout the sampling process.
network.W 
# Once completed, this class variable will contain the transition matrix associated with the pattern(s) entered. 
```
