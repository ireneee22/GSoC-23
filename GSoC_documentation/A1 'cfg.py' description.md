# [A1 cfg.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/cfg.py) description 

TODO: translate from italian

### Run Parameters

`cfg = specs.SimConfig()`

- creates a new instance of the SimConfig class and assigns it to the variable ‘cfg’-
- The **`SimConfig`** class in NetPyNE is a configuration object that stores various simulation parameters such as the duration of the simulation, the time step size, the type of output to be generated, and more.
- By creating a **`SimConfig`** object,we can set and customize various simulation parameters to configure how the simulation will run.

**`cfg.duration = 1.0*1e3`** 

- sets the value of the **`duration`** parameter in a configuration object **`cfg`**. 
-  specifies the total length of time for which the simulation will run.
- the `cfg` object is used to store simulation configuration parameters such as duration, time step size, network size etc.

`cfg.dt = 0.05`

- time step size is represented by ‘dt’
- time step is set to 0.05 ms
- the smaller the time step, the more accurate is the ability of the simulation to capture changes over time. Questo però a discapito del computational load
- **`cfg.dt`** to 0.05 means that the simulation will look at variations in the network every 0.05 milliseconds.

`cfg.verbose = 0`

- sets verbosity level of the simulation to 0.
- verbosity  = the amount of info that is printed to the console as the simulation is being run
- verbosity to 0 means that the simulation will run without printing any info to the console → useful for running simulation in batch mode

`cfg.hParams` 

- parameter used to specify the values of various parameters related to the biophysics of the network.

**`cfg.hParams['celsius'] = 37`**

- sets the temperature of the simulation (**`celsius`**) to 37 degrees Celsius.
- default temperature in NN simulations.

**`cfg.createNEURONObj = 1`**

- sets the `createNEURONObj`  configuration to 1, meaning that NetPyNE creates NEURON objects during initialization of simulation.
- default behavior, if need to manually create objects (non credo), set to 0

**`cfg.createPyStruct = 1`**

- sets the **`createPyStruct`** configuration parameter to 1, so NetPyNE will create a Python data structure to represent the network during the initialization of the simulation.
- default behavior, if need to manually create objects (non credo), set to 0

`cfg.printRunTime = 0.1`

- **`cfg.printRunTime = 0.1`** sets the **`printRunTime`** configuration parameter to 0.1, indicating that NetPyNE should print the *status* of the simulation every 0.1 seconds during runtime.
- setting to 0 may be useful if you're running large simulations

**`cfg.connRandomSecFromList = False`**

- sets `connRandomSecFromList` configuration parameter to `False`, indication that Netpyne should not randomly select sections from a list when creating synaptic connections.
-  useful for ensuring reproducibility of the simulation results, as the same sections will be used each time the simulation is run.

**`cfg.cvode_active = False`**

- `cvode`automatically adjusts  time step to achieve a desired level of accuracy and efficiency.
- instead of using `cvode`, we use the time step defined in `cfg.dt`.

**`cfg.cvode_atol = 1e-6`**

- serve for overall accuracy
- the **`cvode_atol`** configuration parameter sets the absolute tolerance value for the CVODE numerical integrator used by NEURON.
- By setting **`cfg.cvode_atol`** to **`1e-6`**, NetPyNE will use an absolute tolerance value of 1e-6 for the CVODE numerical integrator. This can be useful for improving the accuracy of the simulation results, particularly when simulating complex models with multiple compartments.

Caching ion channel densities: 

- In a computational simulation of a neuron or neural network, ion channels are modeled as dynamic processes that depend on the electrical and chemical properties of the neuron's membrane. The simulation must therefore calculate the conductance of each ion channel at every point in time, based on the current state of the neuron or network.
- Caching ion channel densities in the simulation involves storing the computed conductance values for each ion channel at each time point, and using these values to calculate the conductance in subsequent time steps, rather than recalculating the conductance from scratch at each time step. Questa cosa serve to reduce the computational cost

**`cfg.cache_efficient = True`**

- parliamo di caching ion channel densities in the simulation
- se **`cache_efficient`** è **`True`**, we use optimized method for caching ion channel densities in the simulation.
- altrimenti sarebbe computationally costly → Setting **`cache_efficient`** to **`True`** enables an optimized method that is more computationally efficient → memory efficient

`cfg.oneSynPerNetcon = False`

- In NEURON, a **`NetCon`** object is used to connect a **`pre-synaptic`** neuron to a **`post-synaptic`** neuron through a **`synapse`**.
- A single **`NetCon`** object can be connected to multiple synapses, allowing the pre-synaptic neuron to affect the post-synaptic neuron through multiple pathways.
- By default, **`cfg.oneSynPerNetcon`** is set to **`False`**, which means that a single **`NetCon`** object can be connected to multiple synapses. This is a more efficient approach in terms of memory usage because it reduces the number of **`NetCon`** objects that need to be created.
- Setting **`cfg.oneSynPerNetcon`** to **`True`** restricts each **`NetCon`** object to be connected to only a single synapse. Forse piu memory intensive

`cfg.includeParamsLabel = False`

- ricorda: the cfg object is used to specify various simulation configuration parameters.
- `includeParamsLabel` is a parameter which is a Boolean flag → it determines whether or not to include the parameters label in the output files of the simulation.
- when **`cfg.includeParamsLabel`** is set to **`True`**, the label of each parameter specified in the simulation configuration is included in the output files. 
This can be useful for identifying the values of specific parameters in the simulation results.
- when **`cfg.includeParamsLabel`** is set to **`False`**, the label of each parameter is not included in the output files. This can be useful for reducing the size of the output files, especially when the number of parameters being simulated is large.

`cfg.printPopAvgRates = [500, cfg.duration]`

- parameter used to specify when to print the average firing rates of populations during the simulation.
- takes a list with two elements: `[500, cfg.duration]`;
the average firing rates of populations will be printed: 
- every 500 ms during the simulation 
- AND at the end of the simulation (which has duration `cfg.duration`)
- the actual values of the population firing rates will be printed to the output files, along with other info about the simulation.
- this parameter is useful for analyzing activity of the network over time and can be used to ensure that the network is firing in a logical way.

`cfg.validateNetParams = True`

- If set to True, the netParams object will be checked for various errors such as missing sections, synapses…
- Setting **`cfg.validateNetParams = True`** is generally a good practice to ensure that the network is set up correctly and there are no issues before running a simulation.

---

### Recording

`cfg.allpops = ['NGF1', 'IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2', 'IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3', 'ITP4', 'ITS4', 'SOM4', 'PV4', 'VIP4', 'NGF4', 'IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A', 'IT5B', 'PT5B', 'CT5B', 'SOM5B', 'PV5B', 'VIP5B', 'NGF5B', 'IT6', 'CT6', 'SOM6', 'PV6', 'VIP6', 'NGF6', 'TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']`

- defines a list of names of ALL the populations of neurons in the model. 
Each population name is a string and represents a group of neurons che fra loro sono simili.

`cfg.allCorticalPops = ['NGF1', 'IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2', 'IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3’, 'ITP4', 'ITS4', 'SOM4', 'PV4', 'VIP4', 'NGF4', 'IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A', 'IT5B', 'PT5B', 'CT5B',  'SOM5B', 'PV5B', 'VIP5B', 'NGF5B', 'IT6', 'CT6', 'SOM6', 'PV6', 'VIP6', 'NGF6','TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']`

- all cortical pops included in the simulation, specifically:
    - **`NGF`**: Neurogliaform cells
    - **`IT`**: Intrinsically bursting cells
    - **`SOM`**: Somatostatin-expressing interneurons
    - **`PV`**: Parvalbumin-expressing interneurons
    - **`VIP`**: Vasoactive intestinal peptide-expressing interneurons
    - **`ITP`**: Intrinsically-tuned regular-spiking cells, projecting to pial surface
    - **`ITS`**: Intrinsically-tuned regular-spiking cells, projecting to subcortical targets
    - **`CT`**: Corticothalamic cells
    - **`PT`**: Pyramidal tract cells
    - **`TC`**: Thalamocortical cells
    - **`TCM`**: Thalamic reticular cells
    - **`HTC`**: High-threshold spiking cells
    - **`IRE`**: Irregular-spiking cells
    - **`TI`**: Bursting T-current cells
    - **`TIM`**: Modulated T-current cells
    - **`IC`**: Intrinsically bursting cells
    
    `cfg.allThalPops = ['TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']`
    
    - TC: thalamocortical relay cells
    - TCM: thalamocortical interneurons (midline)
    - HTC: high-threshold spiking interneurons (thalamic reticular nucleus)
    - IRE: low-threshold spiking interneurons (thalamic reticular nucleus)
    - IREM: low-threshold spiking interneurons (midline)
    - TI: thalamo-recipient interneurons
    - TIM: thalamo-recipient interneurons (midline)
    - IC: inferior colliculus neurons


`alltypes = ['NGF1', 'IT2', 'PV2', 'SOM2', 'VIP2', 'ITS4', 'PT5B', 'TC', 'HTC', 'IRE', 'TI']`

- list that contains specific population types that are of interest
- this list can be used to specify which populations of neurons to analyze or plot, without having to include all populations in the simulation

`cfg.recordTraces = {'V_soma': {'sec':'soma', 'loc': 0.5, 'var':'v'}}`

- dictionary used to specify the recording settings for the simulation.
- the : is used to separate the key and the value in a dictionary.
- in this case, it records:
    - membrane potential (difference in electrical charge between the inside and the outside of the cell) → `V_soma`
    - at the center of the soma `(**sec: 'soma'**, **loc: 0.5**)`
    - of each neuron `(**var: 'v'**)`
    

`cfg.recordStim = False`

- Boolean variable that determines whether or not to record the stimulus applied to the neuron during the simulation.
- in this case, the stimulus is not recorded → saves memory bc less storage needed to store stimulation output, faster stimulation….

`cfg.recordTime = False`

- if True, records time points at which the simulation is sampled (the time vector)

`cfg.recordStep = 0.1`

- the variables of interest are recorded every 0.1 ms during the simulation.
- ≠ from simulation time step. 
**`cfg.dt = 0.05`** sets the simulation time step to 0.05 ms. This means that the simulation will be advanced in steps of 0.05 ms, and the values of the variables of interest will be updated and recorded at every **`cfg.recordStep`** time step.
- Setting **`cfg.recordStep`** to a larger value than **`cfg.dt`** can help reduce the amount of data generated during a simulation, as the variables of interest are only recorded at a smaller number of time points.

`cfg.recordLFP = [[100, y, 100] for y in range(0, 2000, 100)]`

- This list specifies the (x, y, z) coordinates where LFP (local field potential) is recorded.
- In this case, LFP is recorded along the line at x=100, z=100, and varying y values from 0 to 2000.
- this line records LFP at multiple points along the y-axis (vertical) *at a single x-axis* (horizontal) location of 100.

**`cfg.recordLFP = [[x, 1000, 100] for x in range(100, 2200, 200)]`**

- it records LFP at multiple x-axis locations along the horizontal plane at a fixed vertical position of 1000.

DIFFERENCE BETWEEN THESE TWO LINES: 

The second line provides LFP recordings at different locations along the horizontal plane while fixing the vertical position, while the first line provides recordings at different vertical positions while fixing the horizontal location.

---

### Saving

`cfg.simLabel = 'v31_tune3’`

- labels current simulation
- useful if running multiple with different parameter values e poi le vuoi distinguere

`cfg.savePickle = True` 

- indicates that results will be saved in a binary format called “pickle”.
- this is a convenient way of saving complex data structures, such as the simulation results, into a file that can be easily read back into Python at a later time.

`cfg.saveJson = False` 

- the results will NOT be saved in the human-readable file JSON.

`cfg.saveDataInclude = ['simData', 'simConfig', 'netParams', 'net']`

- indicates that 4 types of data should be included in the saved output files:
    - **`simData`**: simulation output data, such as spike times and recorded traces
    - **`simConfig`**: simulation configuration information, such as the parameters used to run the simulation
    - **`netParams`**: network parameters, such as the connectivity matrix and cell properties
    - **`net`**: network object, which contains the full network definition and all associated objects
    

`cfg.backupCfgFile = None` 

- no backup is being saved

`cfg.gatherOnlySimData = False`

- determines whether only simulation data should be gathered and returned or whether the entire simulation configuration and parameters should be included.
- If set to **`False`** (the default value), both simulation data and configuration will be saved.

`cfg.saveCellSecs = True`

- determines whether to save detailed information about the cell section information.
- If it is set to **`True`**, then information such as the name of each cell section and the location of synapses within the cell will be saved.

`cfg.saveCellConns = False`

- connectivity info will not be saved

---

### Analysis and Plotting

`cfg.analysis['plotRaster'] = {'include': cfg.allpops, 'saveFig': True, 'showFig': False, 'popRates': True, 'orderInverse': True, 'timeRange': [0,cfg.duration], 'figSize': (14,12), 'lw': 0.3, 'markerSize': 3, 'marker': '.', 'dpi': 300}`

- sets the parameters for generating a raster plot of spiking activity in the network. Here's a breakdown of the different settings:
    - **`include`**: a list of population names to include in the plot
    - **`saveFig`**: whether to save the figure as an image file (e.g. PNG)
    - **`showFig`**: whether to show the figure on the screen
    - **`popRates`**: whether to display the population firing rates as a subplot below the raster plot
    - **`orderInverse`**: whether to reverse the order of the populations along the y-axis (default is top to bottom)
    - **`timeRange`**: the time window to plot, specified as a list with start and end times (in ms)
    - **`figSize`**: the size of the figure in inches (width, height)
    - **`lw`**: the line width for drawing spikes
    - **`markerSize`**: the size of the markers (i.e. dots) for drawing spikes
    - **`marker`**: the marker style (e.g. '.' for dots, 'o' for circles)
    - **`dpi`**: the resolution of the saved image file, in dots per inch (default is 100)
    

`cfg.analysis['plotLFP'] = {'plots': ['timeSeries'], 'electrodes': [10], 'maxFreq': 80, 'figSize': (8,4), 'saveData': False, 'saveFig': True, 'showFig': False}` 

- sets up a plot of the local field potential (LFP) recorded by a set of electrodes. It has the following parameters:
- **`plots`**: a list of types of plots to show. In this case, it only shows a time series plot of the LFP.
- **`electrodes`**: a list of electrode indices to plot the LFP from. In this case, it only plots the LFP from electrode 10.
- **`maxFreq`**: the maximum frequency to plot on the y-axis of the time-frequency plot. It is set to 80 Hz in this case.
- **`figSize`**: the size of the figure to save/display.
- **`saveData`**: whether to save the data used to create the plot.
- **`saveFig`**: whether to save the figure.
- **`showFig`**: whether to show the figure on the screen.

---

### Cells

`cfg.weightNormThreshold = 5.0` 

- sets threshold value to normalize the weight of connections in the network
- a weight vector with a norm of 7 will be set to 5 → prevents very strong connections which can lead to unstable behavior.

`cfg.weightNormScaling = {'NGF_reduced': 1.0, 'ITS4_reduced': 1.0}`

- it is a dictionary that allows the user to scale the weight normalization constant for specific cell types or connection types.
- it has two entries→ these correspond to diff types of cells in the network.
- 1.0 represents the scale factor that will be applied to the weight normalization constant for that cell or connection type.

---

### Synapses

`cfg.AMPATau2Factor = 1.0`

- parameter to modify the decay time constant of the AMPA receptor.
- by default, the decay time constant of the AMPA receptor is determined by the parameter **`tau2_AMPA`**, which is defined in the cell template file
- if **`cfg.AMPATau2Factor = 1.0`**, the **`tau2_AMPA`** value in the cell template will be used without modification.
- if **`cfg.AMPATau2Factor = 2.0`**, the decay time constant of the AMPA receptor will be doubled, resulting in a slower decay of the AMPA synaptic current.

Synaptic weight: 

It is a measure of the effectiveness of a synapse in transmitting a signal between two neurons. 
It refers to the magnitude of the postsynaptic response to the presynaptic action potential. 
It can be influenced by various factors such as the number of neurotransmitter receptors on the postsynaptic membrane, the amount of neurotransmitter released by the presynaptic neuron, and the properties of the ion channels involved in generating the synaptic potential. 
 Synaptic weight is an important parameter in computational models of neural networks, as it determines the extent to which different neurons are connected and able to influence each other's activity.

`cfg.synWeightFractionEE = [0.5, 0.5]` # E->E AMPA to NMDA ratio

- specifies the fraction of the total synaptic weight that is used for the two types of excitatory synapses (EE) : AMPA and NMDA.
- the list `[0.5, 0.5]` means that the synaptic weight is split equally between AMPA and NMDA receptors. 

EXAMPLE: if a synapse has a total weight of 0.5, then 0.25 weight is given to AMPA and 0.25 is given to NMDA. This value can be adjusted to modify the relative contribution of each type of receptor in the network.

`cfg.synWeightFractionEI = [0.5, 0.5]` # E->I AMPA to NMDA ratio

- determines the ratio of AMPA to NMDA synaptic conductances for connections from excitatory (E) neurons to inhibitory (I) neurons.
- the values are set to **`[0.5, 0.5]`**, which means that the conductance is split equally between AMPA and NMDA receptors.

`cfg.synWeightFractionSOME = [0.9, 0.1]` # SOM -> E GABAASlow to GABAB ratio

- sets the synaptic weight fraction between two types of neurons in the network: SOM interneurons and excitatory (E) neurons
- Specifically, it sets the ratio between the weights of two types of GABAergic synapses (GABAASlow and GABAB) that SOM interneurons form onto E neurons.
- in this case, 90% of the total synaptic weight from SOM interneurons to E neurons is due to GABAASlow, while the remaining 10% is due to GABAB.

`cfg.synWeightFractionNGF = [0.5, 0.5]` # NGF GABAA to GABAB ratio

- sets the ratio of the synaptic weights of two types of GABAergic synapses from NGF (neurogliaform) cells to excitatory (E) cells in the network.
- Specifically, it sets the ratio of the synaptic conductances for GABAA receptors to GABAB receptors
- in this case, equal ratio

`cfg.synWeightFractionENGF = [0.834, 0.166]` # NGF AMPA to NMDA ratio

- sets ratio of synaptic weight of AMPA to NMDA receptors for connections from excitatory neurons to NGF-expressing inhibitory neurons (ENGF, exc neurogliaform).
- ratio 5:1  → AMPA receptors have a higher contribution to synaptic transmission than the NMDA receptors for these connections

`cfg.singleCellPops = False`

- controls whether or not individual cells are considered populations for the purposes of connectivity.
- when set to `True`, each cell in the network is treated as a separate population and connectivity between cells is defined using **`netParams.connParams()`** rules for connecting populations. In this case, a separate set of connections is generated for each pair of cells in the network.
- When **`cfg.singleCellPops`** is set to **`False`** (the default), cells are grouped into populations according to their **`popLabel`** attribute. Connectivity is then defined using **`netParams.connParams()`** rules for connecting populations, which allows for more efficient specification of large-scale connectivity patterns.

`cfg.singlePop = '’` @Irene  

- the parameter specifies the name of a single population to stimulate in isolation
- here, set equal to an empty string ‘’  → when set equal to empty string, all populations are simulated.
- useful parameter if you want to isolate the effect of a particular population on the network dynamic

`cfg.removeWeightNorm = False`

- controls whether the synaptic weights in the network are normalized to a maximum value of 1.0
- if set to `True`, weight normalization is turned off
- if `False` (default), weight normalization is applied

`cfg.scale = 1.0`  @Irene  

- parameter that scales network size
- A value of 1.0 means the network is at its original size, and a value greater than 1.0 would increase the network size, while a value less than 1.0 lo diminiusice

`cfg.sizeY = 2000.0`

- specifies length of dorsal-ventral axis (top-bottom)

`cfg.sizeX = 200.0`

- specifies length of rostral-caudal axis (front-back)

`cfg.sizeZ = 200.0`

- specifies length of medial-lateral axis (left-right)

`cfg.scaleDensity = 1.0`  @Irene  # Should be 1.0 unless need lower cell density for test simulation or visualization

- 1.0 = default cell density
- lower cell density = fewer connections between cells → different network dynamics

---

### Connectivity

Difference with synapses: 

- connectivity is about the relative proportions of synaptic weights for different types of connections in the network
- synapses specifies specific synaptic parameters such as decay time constants and the AMPA to NMDA ratio for each type of synapse

The two sets of parameters define the synaptic weights. 

`cfg.synWeightFractionEE = [0.5, 0.5]` # E->E AMPA to NMDA ratio

- sets the ratio of AMPA to NMDA receptor weights for excitatory to excitatory synapses in the network.
- total synaptic weight split evenly between AMPA and NMDA receptors

`cfg.synWeightFractionEI = [0.5, 0.5]` # E->I AMPA to NMDA ratio

- sets ratio of AMPA to NMDA receptor weights for connections from excitatory neurons (E) to inhibitory neurons (I).
- both types of receptors are evenly weighted.
- AMPA receptors mediate fast synaptic transmission, while NMDA receptors mediate slower synaptic transmission and are important for synaptic plasticity.

`cfg.synWeightFractionIE = [0.9, 0.1]` # SOM -> E GABAASlow to GABAB ratio

- specifies ratio of GABAASlow to GABAB synaptic weights in inhibitory connections from SOM (somatostatin-positive interneurons) to excitatory neurons (E) in the network.
- the first value in the list corresponds to the weight of GABAASlow synapses and the second value corresponds to the weight of GABAB synapses.
- A higher value for GABAASlow weight will result in stronger and faster inhibition, while a higher value for GABAB weight will result in slower and weaker inhibition.

`cfg.synWeightFractionII = [0.9, 0.1] # SOM -> E GABAASlow to GABAB ratio`

- sets the ratio of GABAASlow to GABAB synapses in the inhibitory-to-inhibitory (II) connection.
- 90% of the synapses are GABAASlow and 10% are GABAB
- This ratio is specific to the SOM to SOM connection.

---

### Cortical

`cfg.addConn = 1`

- this parameter specifies whether to add additional connections to the network
- 1 means adding connections → cortical connections will now be added to the network

**Gain**: the amplification of the input signal received by a neuron. 
A neuron’s gain can be adjusted to control its sensitivity to input signals. 

→ higher input : stronger response to a given input signal 

`cfg.EEGain = 1.0`

- specifies the gain for the extracellular potential (ECP) input to the cells.
- we are speaking of the gain (amplification) of excitatory-to-excitatory synapses in the network.
- ECP is generated by activity of neurons in the surrounding tissue; EEGain allows scaling of this input to modulate its effects on the modeled cells
- 1.0 means the ECP input is used at full strength

`cfg.EIGain = 1.0`  

`cfg.IEGain = 1.0`
`cfg.IIGain = 1.0`

## E/I->E/I layer weights (L1-3, L4, L5, L6)

**Layer gain @Irene**  

Layer gain is the scaling factor for synaptic weights in each layer of the neural network. 

Changing the Layer Gain can be useful for modulating the strength of connectivity between different layers in the network. 

In the cortical microcircuit, we have the following layers of cortex: 

- '1': Layer 1
- '2': Layer 2
- '3': Layer 3
- '4': Layer 4
- '5A': Layer 5A
- '5B': Layer 5B
- '6': Layer 6

So in the following lines, we have specification of layer-specific gain values for each layer of the network → the gain determines the scaling factor for the total synaptic conductance, so it can control the strength of the inputs received by each layer.


```python
cfg.EELayerGain = {'1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0 , '5A': 1.0, '5B': 1.0, '6': 1.0}
cfg.EILayerGain = {'1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0 , '5A': 1.0, '5B': 1.0, '6': 1.0}
cfg.IELayerGain = {'1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0 , '5A': 1.0, '5B': 1.0, '6': 1.0}
cfg.IILayerGain = {'1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0 , '5A': 1.0, '5B': 1.0, '6': 1.0}
```

#E->I by target cell type

Here we are setting the *relative* gain of the specific connections from excitatory (E) to inhibitory(I) neurons in the network, based on TYPE of inhibitory neuron: 

`cfg.EICellTypeGain= {'PV': 1.0, 'SOM': 1.0, 'VIP': 1.0, 'NGF': 1.0}`

- This is a dictionary where each key is a type of inhibitory neuron: PV, SOM, VIP, NGF.
- corresponding values to each key are the gain for the connection from an excitatory neuron, to that precise type of inhibitory neuron
- gain determines strength of connection between pre-synaptic excitatory neuron and post-synaptic inhibitory neuron
- if it was set to 2 for one connection, that specific inhibitory neuron would have twice the strenght IN ITS CONNECTION TO AN EXCITATORY NEURON, with respect to the other inh. neurons in the dict.

Here we are doing the exact same thing, but in connections from inhibitory (I) to excitatory neurons (E). 

`cfg.IECellTypeGain= {'PV': 1.0, 'SOM': 1.0, 'VIP': 1.0, 'NGF': 1.0}`

- the synapse starts from the inhibitory cell and is received by excitatory cells, but the key in the dictonary still takes the name of the inhibitory neuron that the synapse starts from, not the neuron that receives the synapse.
- the synapse starts from an inhibitory cell and targets an excitatory cell. 
The dictionary keys use the names of the inhibitory cell types, not the excitatory cell types. This may seem counterintuitive at first, but it's a convention used in the field of computational neuroscience to specify connectivity parameters based on the presynaptic cell type.

#thalamic

`cfg.addIntraThalamicConn = 1.0`

- parameter in configuration dictionary ‘cfg’ that enables or disables addition of connections between thalamic cells
- 1, so connections will be added.
- This parameter is used by NetPyNE's **`addConn()`** method, which can add synaptic connections between any two cell groups in the network. . The **`addIntraThalamicConn`** parameter tells **`addConn()`** to include intra-thalamic connections when creating the network.

`cfg.addCorticoThalamicConn = 1.0`

`cfg.addThalamoCorticalConn = 1.0`

`cfg.thalamoCorticalGain = 1.0`

- parameter controlling strength of connections between thalamic neurons and cortical neurons.
- 1.0 means normal level strength

`cfg.intraThalamicGain = 1.0
cfg.corticoThalamicGain = 1.0`

`cfg.addSubConn = 1`

- used to enable/disable the addition of subcortical connections in the network
- 1 means they will be added, 0 means they’re disabled

## full weight conn matrix

```python
with open('conn/conn.pkl', 'rb') as fileObj: connData = pickle.load(fileObj)
cfg.wmat = connData['wmat']
```

- loads a connectivity matrix from a saved file → a pickle file called conn.pkl
- the rb flag opens the file in binary read mode
- in this file there’s a dict with key “wmat” → this key contains a 2D np array representing weight matrix of connectivity in the network.
- the `pickle.load()` function reads the file and returns the dict object which is associated to variable `connData.`
- now, the `cfg.wmat` parameter is assigned the weight matrix in the connData dictionary. 
This parameter is used to set the connectivity weights between neurons in the network.
- the connectivity matrix can provide information on which specific inhibitory neurons connect to which specific excitatory neurons and with what strength.

---

### Background Inputs

Background inputs refer to a type of input that is not specific to a particular group of neurons or synapse, but rather represents random or fluctuating activity that affects all neurons in the network in a non-selective manner.

`cfg.addBkgConn = 1`

- parameter is used to specify whether or not to add background inputs to the network.
- If set to 1, it adds a background input to each cell in the network based on the **`cfg.background`** parameter settings.
- background inputs are generated by Poisson spike trains, which simulate the activity of uncorrelated presynaptic neurons that are not part of the network. 
The purpose of adding background inputs is to create more realistic neural activity patterns and to introduce variability into the network dynamics.

`cfg.noiseBkg = 1.0` # firing rate random noise

- parameter that sets the level of random noise to add to the firing rate of background inputs.

The first line of code is the connections between: 
-a virtual cell representing background input 
-all other cells in the network 

The second line represents the level of random noise to add to the firing rate of the background input. Quindi agisce sulla virtual cell definita prima. 
This is important because if the background input is too regular, it can drive the network activity in a way that is not representative of biological neural networks. 

`cfg.delayBkg = 5.0  # (ms)`

- indicates that the background noise starts `cfg.delayBkg` ms after the simulation starts.

`cfg.startBkg = 0  # start at 0 ms`

- sets the time when the bkg noise stimulation should start, in ms. This means that the background noise starts at exactly **`cfg.startBkg`** milliseconds after the simulation starts.

DIFFERENZA: is that **`cfg.delayBkg`** sets a delay between the start of the simulation and the start of the background noise, while **`cfg.startBkg`** sets an absolute start time for the background noise.

`cfg.rateBkg = {'exc': 40, 'inh': 40}`

- dictionary specifying firing rates of bkg inputs to the network
- in this case on average each bkg input fires 40 times a second

`cfg.EbkgThalamicGain = 4.0`

- parameter determining strength of background excitation to the thalamus → important relay station between sensory organs and cortez
- 4.0 = bkg excitation will be 4x baseline

`cfg.IbkgThalamicGain = 4.0`

- same as above but the input comes from thalamocortical inhibitory cells

`cfg.cochlearThalInput = False` #{'numCells': 200, 'freqRange': [9*1e3, 11*1e3], 'toneFreq': 10*1e3, 'loudnessDBs': 50} # parameters to generate realistic auditory thalamic inputs using Brian Hears

- parameter set to False means the simulated network will not receive realistic auditory thalamic inputs.
- if set to True, network receives realistic auditory thalamic inputs generated using Brian Hears library

`cfg.ICThalInput = {}`  #'file': 'data/ICoutput/ICoutput_CF_9600_10400_wav_01_ba_peter.mat',
#'startTime': 500, 'weightE': 0.5, 'weightI': 0.5, 'probE': 0.12, 'probI': 0.26, 'seed': 1}

- dictionary specifiying parameters for inh/exc inputs to the thalamus coming from the inferior colliculus (IC) in the auditory pathway.
- The parameters are:
    - **`file`**: the path to the .mat file containing the simulated IC output.
    - **`startTime`**: the start time (in ms) for the IC input.
    - **`weightE`**: the weight of the excitatory input.
    - **`weightI`**: the weight of the inhibitory input.
    - **`probE`**: the probability of connection for excitatory neurons.
    - **`probI`**: the probability of connection for inhibitory neurons.
    - **`seed`**: the random seed for the IC input.
    

---

### Current inputs

`cfg.addIClamp = 0`

- flag determining whether to add a current clamp stimulus to the model
- 1 yes, 0 no

---

### NetStim inputs

`cfg.addNetStim = 0`

- flag specifying whether to add network-level Poisson distributed bkg input to cells or not. (poisson uguale stimolazione random)
- if 1, network level background is added.

**#LAYER 1** 

`cfg.NetStim1 = {'pop': 'NGF1', 'ynorm': [0,2.0], 'sec': 'soma', 'loc': 0.5, 'synMech': ['AMPA'], 'synMechWeightFactor': [1.0], 'start': 0, 'interval': 1000.0/60.0, 'noise': 0.0, 'number': 0.0, 'weight': 10.0, 'delay': 0}`

This code block defines a network-level Poisson distributed background input for layer 1 neurons. 

The parameters of the network-level random input are specified as a dict with keys and values: 

- ‘pop': 'NGF1' specifies the population name as 'NGF1' → this is the TARGET of the network-level distributed bkg input.
- 'ynorm': [0, 2.0] specifies the normalized range of y-axis for the 2D positioning of neurons, from 0 to 2.0.
- 'sec': 'soma' specifies the target section of neurons for receiving input as 'soma'.
- 'loc': 0.5 specifies the location of the synapse on the target section as 0.5 (midpoint).
- 'synMech': ['AMPA'] specifies the synaptic mechanism(s) as 'AMPA'.
- 'synMechWeightFactor': [1.0] specifies the weight factor(s) for the synaptic mechanism(s) as 1.0.
- 'start': 0 specifies the start time of the input as 0 ms.
- 'interval': 1000.0/60.0 specifies the interval between two spikes (in ms), which is set to 16.67 ms (60 Hz).
- 'noise': 0.0 specifies the level of noise as 0.0 (no noise).
- 'number': 0.0 specifies the number of spikes per interval as 0.0 (variable rate input).
- 'weight': 10.0 specifies the weight of the synapse as 10.0.
- 'delay': 0 specifies the delay of the synapse as 0 ms.

`cfg.tune = {}`

- dict used for setting parameters that are not specific to a particular network or cell type but rather for general overall simulation settings
- the purpose of the cfg.tune dict is to provide a centralized location for storing and modifying these global simulation parameters.
- this is a placeholder for potential future use

---

### @Irene  Set the baseline model parameters (remove this to use custom parameters)

```python
import json
filename = '../data/v34_batch25/trial_2142/trial_2142_cfg.json'
```

```python
with open(filename, 'rb') as f:
cfgLoad = json.load(f)['simConfig']
```

```python
updateParams = ['EEGain', 'EIGain', 'IEGain', 'IIGain',
('EICellTypeGain', 'PV'), ('EICellTypeGain', 'SOM'), ('EICellTypeGain', 'VIP'), ('EICellTypeGain', 'NGF'),
('IECellTypeGain', 'PV'), ('IECellTypeGain', 'SOM'), ('IECellTypeGain', 'VIP'), ('IECellTypeGain', 'NGF'),
('EILayerGain', '1'), ('IILayerGain', '1'),
('EELayerGain', '2'), ('EILayerGain', '2'),  ('IELayerGain', '2'), ('IILayerGain', '2'),
('EELayerGain', '3'), ('EILayerGain', '3'), ('IELayerGain', '3'), ('IILayerGain', '3'),
('EELayerGain', '4'), ('EILayerGain', '4'), ('IELayerGain', '4'), ('IILayerGain', '4'),
('EELayerGain', '5A'), ('EILayerGain', '5A'), ('IELayerGain', '5A'), ('IILayerGain', '5A'),
('EELayerGain', '5B'), ('EILayerGain', '5B'), ('IELayerGain', '5B'), ('IILayerGain', '5B'),
('EELayerGain', '6'), ('EILayerGain', '6'), ('IELayerGain', '6'), ('IILayerGain', '6'),
'thalamoCorticalGain', 'intraThalamicGain', 'EbkgThalamicGain', 'IbkgThalamicGain', 'wmat']
```

**`updateParams`** is used to update or modify specific parameters of the simulation configuration. It is used to selectively change some of the parameters without having to redefine the entire configuration from scratch.

here, **`updateParams`** contains a list of parameters that need to be updated. Some of these parameters were already defined earlier in the configuration, but they may need to be modified based on some specific conditions or experimental requirements.

By using **`updateParams`**, you can modify the values of these specific parameters without changing any other parameters in the configuration. Now → easier to manage and maintain the configuration, especially if it is complex and has many parameters.

```python
for p in updateParams:
if isinstance(p, tuple):
cfg.**dict**[p[0]].update({p[1]: cfgLoad[p[0]][p[1]]})
else:
cfg.**dict**.update({p: cfgLoad[p]})
```

Qui vedi che it’s iterating through the **`updateParams`** list and checking each parameter **`p`** in it. If the parameter is a tuple, it uses the first element of the tuple as a key to update a nested dictionary within the **`cfg`** dictionary with the value from the loaded configuration file (**`cfgLoad`**). If the parameter is not a tuple, it updates the **`cfg`** dictionary directly with the value from **`cfgLoad`**. In this way, the **`updateParams`** list allows specific parameters to be updated from a saved configuration file while keeping other parameters fixed at their original values.
