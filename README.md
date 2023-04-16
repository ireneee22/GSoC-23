
# Replicating deviant Auditory Steady-State Response (ASSR) in an auditory cortex model (A1)


Auditory Steady-State Response (ASSR) refers to the cortical entrainment to frequency and phase of an auditory signal that is presented in a fixed “train of clicks”, in a gamma range rhythm (40 Hz). 
A hallmark of schizophrenia is a reduction in ASSR; this project aims at reproducing this phenomenon using an auditory cortex (A1) model with thalamocortical connectivity. The latter simulates a cortical column with a depth of 2000 μm and 200 μm diameter, containing over 12k neurons and 30M synapses. 

Specifically, we aim at reproducing results from an experiment looking at the effects of increased CB1 receptor availability and GABA receptor deficits, as these have been linked to the EEG abnormalities that characterize schizophrenia.

![ASSR](/Users/irenebernardi/Desktop/GSoC_files/README_pictures/ASSR_SZ.PNG/ "ASSR").

We will start by running batch simulation tasks to pull out connectivity rules from the A1 model, modifying GABA and CB1 Receptors. This step will be run on a scaled version of the A1, so that I will be able to use a personal computer, but I may employ cloud resources as well.Then, we will analyze parameter sweeps for local field potentials, using the LFPy toolbox. Afterwards, we will move to parameter optimization of the A1 model so that it reproduces the ASSR, using the Optuna HPO toolkit. Our ultimate goal is to reproduce the ASSR phenomenon in the A1 model. 


Our goals are: 
- Demonstrating A1 with parameter sweeps relevant to schizophrenia, by running batch simulation tasks.
- Characterizing the output of the parameter sweeps in step 1, using LFPy.
- Characterizing the parameter optimization of the A1 model so that it reproduces
the ASSR.
- Reproducing ASSR in A1.

