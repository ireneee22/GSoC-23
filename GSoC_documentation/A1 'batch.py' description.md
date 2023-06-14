# [A1 Batch.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/batch.py) description 

TODO: translate italian 

**Purpose of batch:** 
By running the batch simulation multiple times with different parameter values, you can analyze the results and observe how the model's behavior varies across different parameter settings. This way we find insights into the sensitivity of the model to specific parameters and help understand how different factors influence the simulation outcomes.

The **`batch.py`** file contains the definition of the **`Batch`** class and some example functions for creating and running batch simulations.

The **`b`** object being returned is an instance of the Batch class, which is a custom class used for managing batch simulations and parameter optimization 

**Parameter sweep:** 

Systematically varying the values of certain parameters in order to examine their effects on the simulation output.

For each parameter, the batch simulation is executed multiple times, with each iteration corresponding to a specific combination of parameter values.

 **`ODict`** stands for "Ordered Dictionary," which is a dictionary-like object in the **`netpyne.specs`** module.

 fitness function  → defines objective or goal which the algorithm seeks to optimize.

`from netpyne.batch import Batch`

`from netpyne import specs`

`import numpy as np`

---

### Weight normalization

Weight of synaptic connections for background input 

```python
def bkgWeights(pops=[], weights=list(range(50))):

params = specs.ODict()
params['singlePop'] = pops
params['weightBkg'] = weights
```

starting from: 

`def bkgWeights(pops=[], weights=list(range(50))):`

- function taht takes two optional arguments: ‘pops’ and ‘weights’. Weight can have values da 0 a 49.
1. **variable initialization:**
    - `params = specs.ODict()`
    creates ordered dict ‘params’, using the 0Dict class from ‘specs’ module. 
    This dictionary stores parameters for the simulation.
    
2. **parameter assignment:**
    - **`params['singlePop'] = pops`**
    This assignes the value of the `pops` argument to the `singlePop` key in the `params` dictionary che abbiamo appena creato.
    - `params['weightBkg'] = weights` 
    This assigns the value of the `weights` argument to the `weightBkg` key in the `params` dictionary. Consideriamo i valori da 0 a 49 inclusive.
    
    Stai semplicemente dando dei nuovi nomi a queste due keys del dizionario, to make it more readable
    

---

### Set initial config

`initCfg = {}`

- dizionario degli initial configuration parameters, che stiamo per specificare:

**# sim and recording params**

`initCfg['duration'] = 10.0 * 1e3`

- sets duration to 10 secs

`initCfg['singleCellPops'] = True`

- determines whether to simulate individual cells within populations (**`True`**) or consider populations as single entities (**`False`**).

`initCfg['singlePopForNetstim'] = True`

- specifies whether to use a single population for network stimulation (**`True`**) or use separate populations for each stimulus (**`False`**).

`initCfg['removeWeightNorm'] = False`

- determines whether to remove weight normalization for synaptic connections (**`True`**) or keep weight normalization enabled (**`False`**).

`initCfg[('analysis','plotTraces','include')] = [0]`

- this parameter specifies a list of cell indices or IDs to include when plotting traces. In the provided code, only cell index 0 is included.
- tuple → nested

`initCfg[('analysis','plotTraces','timeRange')] = [0, 3000]`

- traces will be plotted from time 0 ms to 3000 ms.

`initCfg[('analysis', 'plotRaster')] = False`

- not plotting raster

```python
initCfg[('rateBkg', 'exc')] = 40
initCfg[('rateBkg', 'inh')] = 40
```

- sets background firing rate (in Hz) for inhibitory neurons and excitatory neurons, to 40 Hz.

**#Turn off components not required** 

stiamo sempre dando valori alle keys dell’`initconfig` dict.

```python
    initCfg['addBkgConn'] = True 
#we add background connections
    initCfg['addConn'] = False #this would be sufficient on its own i think
#no general connection between pops will be included!
    initCfg['addIntraThalamicConn'] = False
    initCfg['addCorticoThalamicConn'] = False
    initCfg['addCoreThalamoCorticalConn'] = False
    initCfg['addMatrixThalamoCorticalConn'] = False
#no stimulus-specific subconnectivity
    initCfg['stimSubConn'] = False

    initCfg['addIClamp'] = False

    initCfg['addNetStim'] = False
```

`initCfg['addIClamp']` → no intracellular current clamp stimulus will be added to neurons 

`initCfg['addNetStim']` →  network-level stimulations, sono external stimuli to the network such as spike trains or random spike patterns.

```python

#create batch object
b = Batch(params=params, netParamsFile='netParams_bkg.py', cfgFile='cfg_cell.py', initCfg=initCfg)
    b.method = 'grid'

    return b
```

**`b = Batch(params=params, netParamsFile='netParams_bkg.py', cfgFile='cfg_cell.py', initCfg=initCfg)`**

- creates a batch object named b. 
The Batch object is initialized with the following arguments:
    - params : dict previously defined, w various params for batch sim → parametri da esplorare nella batch simulation
    - netparamsFile  → specifies file name of the network parameters configuration file associated con la simulazione.
    - cfgFile → specifies file name (**`'cfg_cell.py'`**)that contains the configuration settings for the simulation
    - initCfg → dict che abbiamo già creato, adds additional configuration parameters for the simulation

`b.method = ‘grid’` 

- sets the **`method`** attribute of the **`Batch`** object **`b`** to **`'grid'`**. The **`'grid'`** method suggests that the batch simulation will use a grid search approach, where different combinations of parameter values will be explored systematically.
This returns the created **`Batch`** object **`b`** from the function.

Overall: 

- this code creates a function that creates and configures a `Batch` object for conducting batch simulations.
- The **`Batch`** object allows for the automated execution of multiple simulations with different parameter combinations, using network parameters and configuration settings specified in separate files.
- The use of the **`'grid'`** method suggests that the batch simulations will involve exploring parameter values in a grid-like manner → li combina a tabella

---

### Weight Normalization

Weight of synaptic connection for specific pops and segments
of the network.

```python
def weightNorm(pops=[], rule = None, segs = None, allSegs = True, weights=list(np.arange(0.01, 0.2, 0.01)/100.0)):
```

The weightNorm function above takes the following arguments (ovvero questa funzione si applica a tali parametri): 

1. **`pops=[]`**
Empty list specifying the pops to which weight norm should be applied to → as is empty, weightnorm is applied to all pops
2. **`rule=None`**
  weight normalization rule to be applied is optional and can be set to **`None`** if no specific rule is needed.
3.  **`segs=None`**
specifies the segments or compartments within the populations to which the weight normalization should be applied. It is optional and can be set to **`None`** if no specific segments are targeted.
4.  **`allSegs=True`**
a boolean flag that determines whether the weight normalization should be applied to all segments if no specific segments are provided. By default, it is set to **`True`**, meaning all segments will be considered if no specific segments are specified.
5. **`weights=list(np.arange(0.01, 0.2, 0.01)/100.0)`**: This argument is a list that defines a range of weight values to be used for weight normalization. By default, it is set to a list generated using **`np.arange(0.01, 0.2, 0.01)/100.0`**, which creates a list of weight values ranging from 0.01 to 0.2 with a step of 0.01, divided by 100.0.

#add params

`from cfg_cell import cfg
from netParams_cell import netParams`

- By importing these objects, the code gains access to the pre-defined configuration settings and network parameters specified in the respective files → questo fondamnentale sennò batch non va
- These imported objects are then used in conjunction with the **`Batch`** class and other code in **`batch.py`** to define and execute batch simulations.

```python
excludeSegs = ['axon']
    if not segs:
        secs = []
        locs = []
        for secName,sec in netParams.cellParams[rule]['secs'].items():
            if secName not in excludeSegs:
                if allSegs:
                    nseg = sec['geom']['nseg']
                    for iseg in range(nseg):
                        secs.append(secName) 
                        locs.append((iseg+1)*(1.0/(nseg+1)))
                else:
                    secs.append(secName) 
                    locs.append(0.5)
```

- `excludeSegs` is defined as a list containing the areas to exclude (axon)
- `if not segs :`  vuol dire che CONTROLLA se segs argument è vuoto, SE IT EVALUATES TO FALSE. Se è vuoto,  si prendono due azioni: 
- secs = [] → empty list that will store the segments where weight normalization will be applied
- locs = [] → empty list storing the location of these segments
- `for secName, sec in netParams.cellParams[rule]['secs'].items():`
    - **`netParams.cellParams[rule]['secs']`** is accessing the section-specific parameters for a particular cell type defined by the **`rule`** within the **`cellParams`** attribute.
    - The **`.items()`** method is used to iterate over the key-value pairs in the **`netParams.cellParams[rule]['secs']`** dictionary.  Each iteration assigns the current key to the variable **`secName`** and the corresponding value to the variable **`sec`**.
    - So, in each iteration of the loop, **`secName`** represents the name of a section (e.g., soma, dend, axon), and **`sec`** represents a dictionary containing the properties or parameters specific to that section.
    - By using this loop, you can access the section names and their respective parameters defined in **`netParams.cellParams[rule]['secs']`**. This allows you to iterate over the sections and perform actions based on their properties or use them in further calculations or manipulations within the weight normalization process.
- `if secName not in excludeSegs:`
it checks if the **`secName`** is not in the **`excludeSegs`** list. If it's not excluded, the code proceeds with the following actions.
Se invece secName is in excludeSegs → semplicemente viene esclusa
- `if allSegs:`
Questa in realtà vuol dire -> if `allSegs` is true
allSegs is a Boolean determining whether weight normalization is applied to all segments or only a single location.
- `nseg = sec['geom']['nseg']`
nseg vuol dire number of segments. 
Here we are retrieving the value of the `nseg` parameter from the `geom` dictionary, within the `sec` dictionary.
    - **`sec`** represents a dictionary that contains properties or parameters specific to a section (segment) of a cell.
    - **`sec['geom']`** accesses the **`'geom'`** key within the **`sec`** dictionary, which likely contains geometric properties of the section.
    - **`sec['geom']['nseg']`** retrieves the value associated with the **`'nseg'`** key within the **`geom`** dictionary. The **`'nseg'`** parameter represents the number of segments that a section should be divided into for more detailed modeling. It determines the granularity of the section in terms of smaller segments.
- `for iseg in range(nseg):`
we are iterating through each segment in nseg, using the iseg variable
- `secs.append(secName) 
locs.append((iseg+1)*(1.0/(nseg+1)))`
sempre if allSegs is True:
- we append the section name to the secs list 
- compute the corresponding location of the sec based on the index of the segment and the total number of segments
- `else:
                    secs.append(secName) 
                    locs.append(0.5)`
if `allSegs` is False, meaning only a single location per cell is weight normalized (NOT a single section, a single location per section!), we append the `secName` to the `secs` list, and a fixed location of 0.5 is appended to the locs list.

**Overall, this code block sets the segment names and locations for weight normalization by either including all segments (`allSegs=True`) or considering a single location per section (`allSegs=False`). It excludes segments specified in `excludeSegs` and populates the `secs` and `locs` lists accordingly.**

**Differenza fra secs e segs** 

- **`secs`** refers to the list that stores the names of sections (segments) where weight normalization will be applied. Each element in the **`secs`** list represents a section (segment) name.
- On the other hand, **`segs`** is an argument passed to the **`weightNorm`** function. It represents a subset of segments within a section where weight normalization may be applied.

To summarize, **`secs`** refers to the list of section (segment) names where weight normalization is applied, while **`segs`** is an argument that allows you to selectively specify a subset of segments within sections for weight normalization.

```python
params = specs.ODict()
    params[('NetStim1', 'pop')] = pops
    params[('NetStim1', 'sec')] = secs
    params[('NetStim1', 'loc')] = locs
    params[('NetStim1', 'weight')] = weights
```

- params is an empty dictionary created using the **`ODict`** class from the **`specs`** module.
- each key in `params` is a compound key consisting of two elements: **`'NetStim1'`** and another string ('pop', 'sec', 'loc', or 'weight').
- The purpose of using **`'NetStim1'`** as part of the compound key is to provide a unique identifier or label for a specific set of parameters within the NetStim configuration. It helps in organizing and distinguishing different configurations or instances of the NetStim stimulus.
- By using a compound key with **`'NetStim1'`**, it is possible to have multiple instances of NetStim configurations with different sets of parameters. Each instance can be accessed and identified using the common key element, which is **`'NetStim1'`** in this case.
- For example, **`params[('NetStim1', 'pop')] = pops`** assigns the value of **`pops`** to the **`'pop'`** parameter within the NetStim configuration labeled as **`'NetStim1'`**. Similarly, other parameters like **`'sec'`**, **`'loc'`**, and **`'weight'`** can be assigned for the specific NetStim configuration identified as **`'NetStim1'`**.

`groupedParams = [('NetStim1', 'sec'), ('NetStim1', 'loc')]`

- **`groupedParams = [('NetStim1', 'sec'), ('NetStim1', 'loc')]`** creates a list containing two tuples.
- Each tuple in **`groupedParams`** represents a compound key that will be used to access specific parameters within the NetStim configuration.
- The first element of each tuple, **`'NetStim1'`**, serves as an identifier or label for a specific configuration or set of parameters within the NetStim.
- The second element of each tuple can be **`'sec'`** or **`'loc'`**, representing specific parameters within the NetStim configuration.

Purpose of grouped parameters: The purpose of having grouped parameters in a batch simulation is to specify combinations of parameters that should be varied together as a group. 

---

### Set initial configuration

```python
initCfg = {}
    # sim and recoring params
    initCfg['duration'] = 1.0 * 1e3
    initCfg['singleCellPops'] = True
    initCfg['removeWeightNorm'] = True
    initCfg[('analysis','plotTraces','include')] = []
    initCfg[('analysis','plotTraces','timeRange')] = [0, 1000]
```

```python
## turn off components not required
    #initCfg[('analysis', 'plotRaster')] = False
    initCfg['addConn'] = False
    initCfg['addIntraThalamicConn'] = False
    initCfg['addIntraThalamicConn'] = False
    initCfg['addCorticoThalamicConn'] = False
    initCfg['addCoreThalamoCorticalConn'] = False
    initCfg['addMatrixThalamoCorticalConn'] = False
    initCfg['addBkgConn'] = False
    initCfg['stimSubConn'] = False #no stimulus sub connections -> no delivery of external input to targeted cells
    initCfg['addIClamp'] = 0 #no current clamp added 
    #it's not false so it's added, we just set it to 0 
```

```python
## set netstim params
    initCfg['addNetStim'] = True
    initCfg[('NetStim1', 'synMech')] = ['AMPA','NMDA'] #network will be stimulated through both AMPA and NMDA synapses
    initCfg[('NetStim1','synMechWeightFactor')] = [0.5,0.5]
    initCfg[('NetStim1', 'start')] = 700 #inizia at 700 ms
    initCfg[('NetStim1', 'interval')] = 1000 #ci sono 1k ms FRA OGNI STIMOLO! -> determines time delay between each stimulus event
    initCfg[('NetStim1','ynorm')] = [0.0, 2.0] #specifies vertical range in which stimulus will be applied within the network
    initCfg[('NetStim1', 'noise')] = 0 #amount of noise (randomness) added to NetStim stimulation -> 0 means no additional noise
    initCfg[('NetStim1', 'number')] = 1 #only 1 netstim object created
    initCfg[('NetStim1', 'delay')] = 1 
    #stimulation starts 700 ms after sim start, and first spike starts 1 ms after start of stim
    #first spike starts at 701ms
```

**weight factor**: quanta influenza o forza sul network ha ciascuna sinapsi. Non è che va diviso fra le due sinapsi, semplicemente la netstim è eccitatoria e si divide in AMPA e NMDA; inoltre entrambe hanno 0.5 il che vuol dire che hanno an equal, moderate impact on the network activity during the stimulation.

```python
b = Batch(params=params, netParamsFile='netParams_cell.py', cfgFile='cfg_cell.py', initCfg=initCfg, groupedParams=groupedParams)
    b.method = 'grid'

    return b
```

---

### F-I CURVE

f-I curves, also known as frequency-current curves or input-output curves, are plots that show the relationship between the input current (stimulus) applied to a neuron or neuronal population and the resulting firing rate (output) of the neuron(s).

```python
def fIcurve(pops = [], amps = list(np.arange(0.0, 6.5, 0.5)/10.0) ):
    params = specs.ODict()
#amps are 0.0, 0.5, 1.0.. divided by 10
```

- function used to define a batch simulation for generating f-I curves
- **`pops = []`**: This parameter specifies the populations for which the f-I curves will be generated. It is a list where each element represents a population.
- **`amps = list(np.arange(0.0, 6.5, 0.5)/10.0)`**: This parameter specifies the amplitudes of current clamp stimulation that will be applied to the populations. It is a list where each element represents an amplitude.
- The function initializes an ordered dictionary called **`params`** using **`specs.ODict()`**. This dictionary will store the parameters for the batch simulation.

```python
params['singlePop'] = pops
params[('IClamp1', 'amp')] = amps
```

#initialize config 

```python
		initCfg = {}
    initCfg['duration'] = 2.0*1e3
    initCfg['addIClamp'] = True
    initCfg['addNetStim'] = False #non capisco
    initCfg['weightNorm'] = True
    initCfg[('IClamp1','sec')] = 'soma' #where iclamp stimulus is added
    initCfg[('IClamp1','loc')] = 0.5 #applied mid-soma
    initCfg[('IClamp1','start')] = 750
    initCfg[('IClamp1','dur')] = 1000
    initCfg[('analysis', 'plotTraces', 'timeRange')] = [0, 2000]
    initCfg['printPopAvgRates'] = [750,1750] #non è un intervallo attenta
    #se volessi range dovresti usare parentesi
    initCfg[('hParams', 'celsius')] = 37
```

#turn off components not required 

```python
		initCfg['addBkgConn'] = False
    initCfg['addConn'] = False
    initCfg['addIntraThalamicConn'] = False
    initCfg['addIntraThalamicConn'] = False
    initCfg['addCorticoThalamicConn'] = False
    initCfg['addCoreThalamoCorticalConn'] = False
    initCfg['addMatrixThalamoCorticalConn'] = False
    initCfg['stimSubConn'] = False
    initCfg['addNetStim'] = False
```

```python
		groupedParams = [] 

    b = Batch(params=params, netParamsFile='netParams_cell.py', cfgFile='cfg_cell.py', initCfg=initCfg, groupedParams=groupedParams)
    b.method = 'grid'

    return b
```

---

### Custom

**Here we are defining a custom batch simulation for a specific purpose.**

```python

def custom_spont(filename):
    params = specs.ODict()

    if not filename:
        filename = 'data/v34_batch25/trial_2142/trial_2142_cfg.json'

    # from prev 
    import json
    with open(filename, 'rb') as f:
        cfgLoad = json.load(f)['simConfig']
    cfgLoad2 = cfgLoad

    
    params[('seeds', 'conn')] = list(range(1)) #[4321+(17*i) for i in range(5)]
    params[('seeds', 'stim')] = list(range(1)) #[1234+(17*i) for i in range(5)]
    '''list contains 0s only, for reproducibility
random number generators RNGs are set to 0 so that 
the same sequence of random numbers is generated each
time '''
    groupedParams = []
```

- The function takes a **`filename`** parameter, which is optional. If no filename is provided, it assumes a default value of **`'data/v34_batch25/trial_2142/trial_2142_cfg.json'`**. This file is then loaded to extract certain configuration information.
- The **`params`** dictionary is initialized using **`specs.ODict()`**. This dictionary will store the parameters that will be varied during the batch simulation.
- Two parameters, **`'seeds.conn'`** and **`'seeds.stim'`**, are added to the **`params`** dictionary. These parameters control the random number generator seeds for connectivity and stimulus generation, respectively. The values for these parameters are specified as lists of integers.
- The **`groupedParams`** list is initialized as an empty list. This list will be used to define groups of parameters that are varied together during the batch simulation. In this case, no parameters are grouped together.
- **`custom_spont`** function sets up a batch simulation where the random number generator seeds for connectivity and stimulus generation can be varied. The specific values for these parameters can be defined when calling the function.

Nello specifico: 

```python
import json
    with open(filename, 'rb') as f:
        cfgLoad = json.load(f)['simConfig']
    cfgLoad2 = cfgLoad
```

- the JSON file is being loaded and used to retrieve specific data from the 'simConfig' section. The purpose of using the JSON file is to obtain configuration settings or parameters that were previously saved and stored in that file.
- The line **`cfgLoad2 = cfgLoad`** simply assigns the value of **`cfgLoad`** to the variable **`cfgLoad2`**. This line creates a new reference to the same JSON object, so modifying **`cfgLoad`** or **`cfgLoad2`** will affect both variables.

#initial config 

```python
initCfg = {} # set default options from prev sim
    
    initCfg['duration'] = 11500
    initCfg['printPopAvgRates'] = [1500, initCfg['duration']] 
    initCfg['scaleDensity'] = 1.0
    initCfg['recordStep'] = 0.05

    # plotting and saving params
    initCfg[('analysis','plotRaster','timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotTraces', 'timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotSpikeStats', 'timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotLFP', 'timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotCSD', 'timeRange')] = [1500, 1700]

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False
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
                    ('EELayerGain', '6'), ('EILayerGain', '6'), ('IELayerGain', '6'), ('IILayerGain', '6')
```

- each element in the list represents a parameter to be updated or modified
- the strings in the list represent INDIVIDUAL parameters that will be updated  → for example, EEGain
- the tuples represent specific parameter VALUES that need to be updated. 
Each tuple consists of two elements → the first element represents the parameter name, the second the specific VALUE within that parameter
Example: 
**`('EICellTypeGain', 'PV')`** represents the parameter **`'EICellTypeGain'`** with the value **`'PV'`**.
- By iterating through the **`updateParams`** list, you can update the corresponding parameters or values in your simulation or model configuration.

```python
for p in updateParams:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad[p]})
```

- for each element p in the updateParams list:
    - IF P IS A TUPLE → The code extracts the corresponding value from the **`cfgLoad`** dictionary using the first element of the tuple as the key for the outer dictionary and the second element as the key for the inner dictionary. It then updates the **`initCfg`** dictionary by adding a new key-value pair, where the key is **`p`** (the tuple) and the value is the extracted value from **`cfgLoad`**.
    - IF P IS NOT A TUPLE  (so it’s an individual parameter to be updated) → The code extracts the corresponding value from the **`cfgLoad`** dictionary using **`p`** as the key and updates the **`initCfg`** dictionary by adding a new key-value pair, where the key is **`p`** (the parameter) and the value is the extracted value from **`cfgLoad`**.
    
    this code snippet is populating the **`initCfg`** dictionary with parameter values extracted from the **`cfgLoad`** dictionary based on the elements in the **`updateParams`** list. This allows you to update and configure the initial configuration (**`initCfg`**) for your batch simulation based on the loaded configuration (**`cfgLoad`**) and the specified parameters (**`updateParams`**).
    

Below, same thing but for a diff set of parameters, for thalamus: 

 

```python
updateParams2 = ['thalamoCorticalGain', 'intraThalamicGain', 'EbkgThalamicGain', 'IbkgThalamicGain', 'wmat']

    for p in updateParams2:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad2[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad2[p]})
```

then run batch:


```python
b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)
    b.method = 'grid'

    return b
```

---

### Other Custom Batch sim (speech related activity)

```python
# Custom
# ----------------------------------------------------------------------------------------------
def custom_speech(filename):
    params = specs.ODict()

    if not filename:
        filename = 'data/v34_batch25/trial_2142/trial_2142_cfg.json'

    # from prev 
    import json
    with open(filename, 'rb') as f:
        cfgLoad = json.load(f)['simConfig']
    cfgLoad2 = cfgLoad

    params[('seeds', 'conn')] = [4321+(17*i) for i in range(5)]
    params[('seeds', 'stim')] = [1234+(17*i) for i in range(5)]
    #pattern used here is incrementing the base value by 17 for each index in the range.

    groupedParams = []

    # --------------------------------------------------------
    # initial config
    initCfg = {} # set default options from prev sim
    
    initCfg['duration'] = 4500
    initCfg['printPopAvgRates'] = [1500, 4500] 
    initCfg['scaleDensity'] = 1.0
    initCfg['recordStep'] = 0.05

    # plotting and saving params
    initCfg[('analysis','plotRaster','timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotTraces', 'timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotSpikeStats', 'timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotLFP', 'timeRange')] = initCfg['printPopAvgRates']
    #initCfg[('analysis', 'plotCSD', 'timeRange')] = [1500, 1700]

    initCfg['ICThalInput'] = {'file': 'data/ICoutput/ICoutput_CF_9600_10400_wav_01_ba_peter.mat', 
                            'startTime': 2500, 
                            'weightE': 0.25,#1.0, #WEIGHT of input from thalamus to network exc cells
                            'weightI': 0.25,#1.0, 
                            'probE': 0.12, #each excitatory cell has a 12% chance of receiving thalamic input.
                            'probI': 0.12, #0.25 
                            'seed': 1}  

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False
    
    # from prev - best of 50% cell density
    updateParams = ['EEGain', 'EIGain', 'IEGain', 'IIGain',
                    ('EICellTypeGain', 'PV'), ('EICellTypeGain', 'SOM'), ('EICellTypeGain', 'VIP'), ('EICellTypeGain', 'NGF'),
                    ('IECellTypeGain', 'PV'), ('IECellTypeGain', 'SOM'), ('IECellTypeGain', 'VIP'), ('IECellTypeGain', 'NGF'),
                    ('EILayerGain', '1'), ('IILayerGain', '1'),
                    ('EELayerGain', '2'), ('EILayerGain', '2'),  ('IELayerGain', '2'), ('IILayerGain', '2'), 
                    ('EELayerGain', '3'), ('EILayerGain', '3'), ('IELayerGain', '3'), ('IILayerGain', '3'), 
                    ('EELayerGain', '4'), ('EILayerGain', '4'), ('IELayerGain', '4'), ('IILayerGain', '4'), 
                    ('EELayerGain', '5A'), ('EILayerGain', '5A'), ('IELayerGain', '5A'), ('IILayerGain', '5A'), 
                    ('EELayerGain', '5B'), ('EILayerGain', '5B'), ('IELayerGain', '5B'), ('IILayerGain', '5B'), 
                    ('EELayerGain', '6'), ('EILayerGain', '6'), ('IELayerGain', '6'), ('IILayerGain', '6')] 

    for p in updateParams:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad[p]})

    # good thal params for 100% cell density 
    updateParams2 = ['thalamoCorticalGain', 'intraThalamicGain', 'EbkgThalamicGain', 'IbkgThalamicGain', 'wmat']

    for p in updateParams2:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad2[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad2[p]})

    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)
    b.method = 'grid'

    return
```

---

### Evolutionary

Here we explore evolutionary parameter optimization.

```python
# Evol
# ----------------------------------------------------------------------------------------------
def evolRates():
    # --------------------------------------------------------
    # parameters
    params = specs.ODict()

    # bkg inputs
    params['EEGain'] = [0.5, 2.0]
    params['EIGain'] = [0.5, 2.0]

    params[('IELayerGain', '1-3')] = [0.5, 2.0]
    params[('IELayerGain', '4')] = [0.5, 2.0]
    params[('IELayerGain', '5')] = [0.5, 2.0]
    params[('IELayerGain', '6')] = [0.5, 2.0]

    params[('IILayerGain', '1-3')] = [0.5, 2.0]
    params[('IILayerGain', '4')] = [0.5, 2.0]
    params[('IILayerGain', '5')] = [0.5, 2.0]
    params[('IILayerGain', '6')] = [0.5, 2.0]
    
    params['thalamoCorticalGain'] = [0.5, 2.0]  
    params['intraThalamicGain'] = [0.5, 2.0] 
    params['corticoThalamicGain'] = [0.5, 2.0]

    groupedParams = []

    # --------------------------------------------------------
    # initial config
    initCfg = {}
    initCfg['duration'] = 1500
    initCfg['printPopAvgRates'] = [[500, 750], [750, 1000], [1000, 1250], [1250, 1500]]
    initCfg['dt'] = 0.05 #timestep

    initCfg['scaleDensity'] = 0.5

    # plotting and saving params
    initCfg[('analysis','plotRaster','timeRange')] = [500,1500]
    initCfg[('analysis', 'plotTraces', 'timeRange')] = [500,1500]

    initCfg[('analysis', 'plotTraces', 'oneFigPer')] = 'trace'

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False
```

gain: increasing the gain value for a specific connection will amplify the strength or impact of that connection in the network.

nota qui: 

1. The **`params`** dictionary now includes ranges for various parameters related to background inputs (**`EEGain`** and **`EIGain`**), layer-specific gains for inhibitory neurons (**`IELayerGain`** and **`IILayerGain`**), thalamo-cortical gain (**`thalamoCorticalGain`**), intra-thalamic gain (**`intraThalamicGain`**), and cortico-thalamic gain (**`corticoThalamicGain`**).
2. The **`groupedParams`** list is empty, indicating that the parameters are not grouped together for this batch simulation. → penso voglia dire che non vogliamo modularli insieme
3. The **`saveCellSecs`** and **`saveCellConns`** are set to **`False`**, indicating that individual cell sections and cell connections are not saved during the simulation.

**Fitness function  → defining which value we want**

Final value of fitness function must be low (bc maximize set to false)

```python
# fitness function
    fitnessFuncArgs = {} #see args below
    pops = {}
    
    ## Exc pops
    Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6', 'TC', 'TCM', 'HTC']  # all layers + thal + IC

    Etune = {'target': 5, 'width': 20, 'min': 0.05} #solo un dict w tuning params
    for pop in Epops:
        pops[pop] = Etune #adesso all pops avranno questi params
    
    ## Inh pops 
    Ipops = ['NGF1',                            # L1
            'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
            'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
            'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
            'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A  
            'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
            'PV6', 'SOM6', 'VIP6', 'NGF6',       # L6
            'IRE', 'IREM', 'TI']  # Thal 

    Itune = {'target': 10, 'width': 30, 'min': 0.05}
    for pop in Ipops:
        pops[pop] = Itune
    
    fitnessFuncArgs['pops'] = pops
    fitnessFuncArgs['maxFitness'] = 1000  
    fitnessFuncArgs['tranges'] = initCfg['printPopAvgRates']

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        tranges = kwargs['tranges']

        popFitnessAll = []

        for trange in tranges:
            popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness) 
                if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] > v['min'] else maxFitness for k, v in pops.items()])
        
        popFitness = np.mean(np.array(popFitnessAll), axis=0)
        
        fitness = np.mean(popFitness)

        popInfo = '; '.join(['%s rate=%.1f fit=%1.f' % (p, np.mean(list(simData['popRates'][p].values())), popFitness[i]) for i,p in enumerate(pops)])
        print('  ' + popInfo)

        return fitness
```

 
**Definizione precisa:** 
'IT2' → layer 2 pyramidal cells
 'IT3' → layer 3 pyramidal cells
 'ITP4' → layer 4 pyr in primary somatosens cortex

'ITS4' → Layer 4 spiny stellate cells
 'IT5A' → Layer 5A pyramidal cells 
'CT5A' → Layer 5A corticospinal cells
 'IT5B' → Layer 5B pyramidal cells
'PT5B' → Layer 5B tufted pyramidal cells
 'CT5B' → Layer 5B corticospinal cells
 'IT6' → Layer 6 pyramidal cells
 'CT6' → Layer 6 corticospinal cells
 'TC' → Thalamocortical cells
TCM' → Thalamocortical modulatory cells 
'HTC' → Hyperpolarization-activated cyclic nucleotide-gated (HCN) channel-expressing thalamocortical cells

- **`pops`** is a dictionary that defines the target rates and fitness parameters for different neuron populations. For excitatory populations (**`Epops`**), the target rate (**`target`**), width of the fitness function (**`width`**), and minimum rate threshold (**`min`**) are specified. Similarly, for inhibitory populations (**`Ipops`**), corresponding target rates and fitness parameters are defined.
- **`fitnessFuncArgs`** is a dictionary that holds the arguments for the fitness function. It includes the **`pops`** dictionary, a maximum fitness value (**`maxFitness`**), and the time ranges (**`tranges`**) for which the fitness will be evaluated.
- `fitnessFuncArgs['maxFitness'] = 1000`   questo è un valore che usi poi to compare different batch sims, per vedere how close each one is to the desired value → 1000 è il valore dato alle popolazioni che underperform
- **`fitnessFunc`** is the actual fitness function that takes the simulation data and the **`kwargs`** dictionary as input. It calculates the fitness based on the provided arguments. The function iterates over the time ranges (**`tranges`**) and calculates the fitness for each population based on the difference between the simulated rates and the target rates. The fitness is calculated as the mean of the fitness values for all populations.

nello specifico (ricordati che k è la popolazione): 

```python
#qui calcoliamo fitnessvalue of firing rate per ogni popolazione
popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness)
if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] > v['min'] else maxFitness for k, v in pops.items()])
```

The expression **`min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness)`** calculates the fitness value for a specific population (**`k`**) and time range (**`trange`**). Let's break it down:

1. **`v['target']`**: The target rate for the population **`k`**. It represents the desired rate that the population should exhibit.
2. **`simData['popRates'][k]['%d_%d'%(trange[0], trange[1])]`**: The simulated rate for the population **`k`** during the specified time range. It represents the actual rate obtained from the simulation.
3. **`abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])`**: Calculates the absolute difference between the target rate and the simulated rate.
4. **`abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']`**: Divides the absolute difference by **`v['width']`** to normalize the difference based on the specified width. This allows for a more flexible fitness calculation.
5. **`np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width'])`**: Calculates the exponential of the normalized difference. This transformation helps emphasize smaller differences and penalize larger differences in fitness calculation.
6. **`min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness)`**: Takes the minimum value between the calculated fitness value and the **`maxFitness`** value. If the fitness value exceeds **`maxFitness`**, it is capped at **`maxFitness`**. This step ensures that fitness values do not exceed a certain threshold.

The purpose of taking the minimum value in this context is to prevent extremely large fitness values. If the difference between the target rate and the simulated rate is significant, the fitness value would be large. However, by taking the minimum value with **`maxFitness`**, the fitness value is bounded and limited to a maximum threshold. This helps maintain a manageable range of fitness values and avoids skewing the optimization process due to outliers.

You defined VMIN in Etune/Itune!

Lower fitness value here is considered better il che ha senso in termini di numeri → infatti maximize is set to false!!!

```python
#from IPython import embed; embed()

    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)

    b.method = 'evol'

    # Set evol alg configuration
    b.evolCfg = {
        'evolAlgorithm': 'custom',
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'pop_size': 100,
        'num_elites': 2 # number of elite individuals that are preserved from one generation to the next.
        'mutation_rate': 0.5 #probability of a parameter being mutated
        'crossover': 0.5, #prob of genetic crossover
        'maximize': False, # maximize fitness function -> LOWER FITNESS VALUE IS CONSIDERED BETTER
        'max_generations': 200,
        'time_sleep': 150, # 2.5min wait this time before checking again if sim is completed (for each generation)
        'maxiter_wait': 5, # max number of times to check if sim is completed (for each generation)
        'defaultFitness': 1000, # set fitness value in case simulation time is over
        'scancelUser': 'ext_salvadordura_gmail_com'
    }

    return b
```

**Evolutionary algorithm**: The basic idea behind an evolutionary algorithm is to maintain a population of candidate solutions, often represented as individuals or chromosomes, which undergo a process of selection, reproduction, and variation over multiple generations. The algorithm iteratively evaluates the fitness of each individual in the population, selects the fittest individuals based on their fitness values, and applies genetic operators such as mutation and crossover to create new offspring.


---

### Adaptive Stochastic Descent (ASD)

What i found online but conferma che sia pertinent: 
→ ASD is used when standard optimization methods fail to find a satisfactory solution for parameter fitting. 

→ algorithm that replicates essential aspects of manual parameter fitting in an automated way. 

→ ASD forms probabilistic assumptions about: 
-which parameters have the greatest effect on the objective function
-optimal step sizes for each parameter

- **`asdRates()`**. This function creates a **`Batch`** object for performing an optimization using an ASD (Automatic Spiking Dynamics) algorithm. The purpose of this optimization is to adjust the values of certain parameters in a neural network simulation to match desired target rates of population activity.
- The **`params`** variable is initialized as an ordered dictionary. It will store the parameters to be modified during the optimization process.
- The variable **`x0`** represents a matrix of initial parameter values (gain values)
- Various parameters related to the background inputs and gains of different layers in the network are specified using the **`params`** dictionary.
- The **`groupedParams`** variable is initialized as an empty list. This variable can be used to group parameters together for simultaneous modification.
- The **`initCfg`** dictionary stores the initial configuration settings for the simulation. It includes the simulation duration, time intervals for printing average population rates, time step size, scaling density, and various analysis and saving options.
- The **`fitnessFuncArgs`** dictionary is used to store arguments for the fitness function that evaluates the goodness-of-fit between the simulated population rates and the desired target rates.
- The **`fitnessFunc`** is defined as the fitness function. It takes the simulation data (**`simData`**) and other keyword arguments (**`kwargs`**) as input and calculates the fitness value based on the difference between the simulated and target rates.
- A **`Batch`** object is created, specifying the parameters to modify, the network parameters file, configuration file, initial configuration, and grouped parameters.
- The optimization configuration (**`optimCfg`**) is defined. It includes the fitness function, fitness function arguments, step size, learning rates, maximum number of iterations and time, convergence criteria, verbosity, and other settings.
- Finally, the **`Batch`** object is returned.

```python
def asdRates():

    # --------------------------------------------------------
    # parameters
    params = specs.ODict()

    x0 = [[1.4338777102469733, 1.1625828604622033, 1.091037051695174, 1.8712819675755956, 0.7397134465049761, 1.367569320349433, 1.418339439423966, 0.6274719645228012, 0.5675561437477121, 1.5174286644853214, 1.6851404284735372, 1.063075099977045, 0.673804518651403],
    [1.4117825668705553, 1.4562645192525767, 0.6966421717946888, 1.1564048776911902, 0.5082691576672945, 1.8650994583365461, 0.5247660780373347, 1.3887063888108127, 0.8359523062412009, 0.786403002769916, 1.0872681212597493, 1.9355702398668257, 0.8456162169403141],
    [1.4796339232563818, 1.2494919865726666, 1.2106074885592537, 0.5914377334878493, 0.7956691184253843, 1.1044833499655324, 1.8970275010959088, 1.2806598565853817, 1.0339389242169903, 1.2449536297089994, 1.653463860326919, 0.5816973165681442, 1.8408576413375228],
    [1.3154950966436703, 1.0095763680475387, 1.3046938357412072, 1.337690869825955, 1.3419352351670506, 2.0, 1.806386376748424, 1.785015289487499, 1.3006272106913037, 1.6797508518217605, 1.5625342091955938, 0.9733859948789619, 0.8423443321780072],
    [1.4081465013179777, 0.6909751558458218, 1.476256983214676, 1.4388900372032694, 0.5, 1.4292511768559795, 0.6980418301090989, 1.1884408015079058, 1.8830229460800467, 1.1514878860870101, 0.9636536753602729, 1.283310375368901, 1.2234380160367202]]

    # bkg inputs
    params['EEGain'] = [0.5, 2.0, [x[0] for x in x0]] #lower and upper boundary, il valore vero lo vedi dall'index che rimanda a x0
    params['EIGain'] = [0.5, 2.0, [x[1] for x in x0]]

    params[('IELayerGain', '1-3')] = [0.5, 2.0, [x[2] for x in x0]]
    params[('IELayerGain', '4')] = [0.5, 2.0, [x[3] for x in x0]]
    params[('IELayerGain', '5')] = [0.5, 2.0, [x[4] for x in x0]]
    params[('IELayerGain', '6')] = [0.5, 2.0, [x[5] for x in x0]]

    params[('IILayerGain', '1-3')] = [0.5, 2.0, [x[6] for x in x0]]
    params[('IILayerGain', '4')] = [0.5, 2.0, [x[7] for x in x0]]
    params[('IILayerGain', '5')] = [0.5, 2.0, [x[8] for x in x0]]
    params[('IILayerGain', '6')] = [0.5, 2.0, [x[9] for x in x0]]
    
    params['thalamoCorticalGain'] = [0.5, 2.0, [x[10] for x in x0]]
    params['intraThalamicGain'] = [0.5, 2.0, [x[11] for x in x0]]
    params['corticoThalamicGain'] = [0.5, 2.0, [x[12] for x in x0]]

    groupedParams = []

    # --------------------------------------------------------
    # initial config
    initCfg = {}
    initCfg = {}
    initCfg['duration'] = 1500
    initCfg['printPopAvgRates'] = [[500, 750], [750, 1000], [1000, 1250], [1250, 1500]]
    #sopra, TIME RANGE, non punti singoli! 4 prints total
    initCfg['dt'] = 0.05

    initCfg['scaleDensity'] = 0.5

    # plotting and saving params
    initCfg[('analysis','plotRaster','timeRange')] = [500,1500]
    initCfg[('analysis', 'plotTraces', 'timeRange')] = [500,1500]
    initCfg[('analysis', 'plotTraces', 'oneFigPer')] = 'trace'
    initCfg['recordLFP'] = None
    initCfg[('analysis', 'plotLFP')] = False

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    # --------------------------------------------------------
    # fitness function
    fitnessFuncArgs = {}
    pops = {}
    
    ## Exc pops
    Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6', 'TC', 'TCM', 'HTC']  # all layers + thal + IC

    Etune = {'target': 5, 'width': 20, 'min': 0.05}
    for pop in Epops:
        pops[pop] = Etune
    
    ## Inh pops 
    Ipops = ['NGF1',                            # L1
            'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
            'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
            'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
            'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A  
            'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
            'PV6', 'SOM6', 'VIP6', 'NGF6',       # L6
            'IRE', 'IREM', 'TI']  # Thal 

    Itune = {'target': 10, 'width': 30, 'min': 0.05}
    for pop in Ipops:
        pops[pop] = Itune
    
    fitnessFuncArgs['pops'] = pops
    fitnessFuncArgs['maxFitness'] = 1000
    fitnessFuncArgs['tranges'] = initCfg['printPopAvgRates']

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        tranges = kwargs['tranges']

        popFitnessAll = []

        for trange in tranges:
            popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness) 
                if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] > v['min'] else maxFitness for k, v in pops.items()])
        
        popFitness = np.mean(np.array(popFitnessAll), axis=0)
        
        fitness = np.mean(popFitness)

'''qui sotto we join fitness values and firing rates
for each pop '''

        popInfo = '; '.join(['%s rate=%.1f fit=%1.f' % (p, np.mean(list(simData['popRates'][p].values())), popFitness[i]) for i,p in enumerate(pops)])
        print('  ' + popInfo)

        return fitness
        
    # create Batch object with paramaters to modify, and specifying files to use
    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)

    b.method = 'asd'

    b.optimCfg = {
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'stepsize':     0.1,     #   Initial step size as a fraction of each parameter
        'sinc':         1.5,       #   Step size learning rate (increase)
        'sdec':         1.5,       #   Step size learning rate (decrease)
        'pinc':         2,       #   Parameter selection learning rate (increase)
        'pdec':         2,       #   Parameter selection learning rate (decrease)
        #'pinitial':     None,    #    Set initial parameter selection probabilities
        #'sinitial':     None,    #    Set initial step sizes; if empty, calculated from stepsize instead
        'maxiters':     300,    #    Maximum number of iterations (1 iteration = 1 function evaluation)
        'maxtime':      360000,    #    Maximum time allowed, in seconds
        'abstol':       1e-6,    #    Minimum absolute change in objective function
        'reltol':       1e-3,    #    Minimum relative change in objective function
        #'stalliters':   10*len(params)*len(params),  #    Number of iterations over which to calculate TolFun (n = number of parameters)
        #'stoppingfunc': None,    #    External method that can be used to stop the calculation from the outside.
        #'randseed':     None,    #    The random seed to use
        'verbose':      2,       #    How much information to print during the run
        #'label':        None    #    A label to use to annotate the output
        'time_sleep': 60, # 1min wait this time before checking again if sim is completed (for each generation)
        'maxiter_wait': 12,  # max number of times to check if sim is completed (for each generation)
        'popsize': 5
    }

    return b
```

In summary, the **`asdRates()`** function sets up a **`Batch`** object for performing an optimization using the ASD algorithm. The goal is to adjust the parameters of a neural network simulation to match desired target rates of population activity.

---

### Adaptive Stochastic Descent w/ optunaRates

By combining ASD with Optuna, the **`optunaRates`** function takes advantage of the exploratory power of ASD to quickly search the parameter space and identify promising regions.

HPO cerca automaticamente i valori migliori dei parametri in un ML model. 
Hyperparameters → settings che non sono imparati from the data, they’re set before the training process begins (e.g. number of layers).

Optuna picks which sets of hyperparameters to try next based on the results of previous trials.

→ l’obiettivo qui è trovare valore per questi hyperparameters che risultino in simulated firing rates that closely match the target rates specified in the opt. process. 

Optuna performs automated search for optimal parameter values → saves time w respect to manual tuning (ASD) or grid methods.

Cosa cambia: 

- define a function called **`optunaRates()`** that creates a **`Batch`** object for performing optimization using the Optuna library. The purpose of this function is to optimize the parameters of a neural network model based on a fitness function.

```python
# Adaptive Stochastic Descent (ASD)
# ----------------------------------------------------------------------------------------------
def optunaRates():

    # --------------------------------------------------------
    # parameters
    params = specs.ODict()

    # bkg inputs
    params['EEGain'] = [0.1, 1.0]

    params[('EILayerGain', '1-3')] = [0.1, 3.0]
    params[('EILayerGain', '4')] = [0.1, 3.0]
    params[('EILayerGain', '5')] = [0.1, 3.0]
    params[('EILayerGain', '6')] = [0.1, 3.0]

    params[('IELayerGain', '1-3')] = [0.1, 3.0]
    params[('IELayerGain', '4')] = [0.1, 3.0]
    params[('IELayerGain', '5')] = [0.1, 3.0]
    params[('IELayerGain', '6')] = [0.1, 3.0]

    params[('IILayerGain', '1-3')] = [0.1, 3.0]
    params[('IILayerGain', '4')] = [0.1, 3.0]
    params[('IILayerGain', '5')] = [0.1, 3.0]
    params[('IILayerGain', '6')] = [0.1, 3.0]

    params[('EICellTypeGain', 'PV')] = [max(cfgLoad['EICellTypeGain']['PV']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['PV']+rangeV2, maxV)]
    params[('EICellTypeGain', 'SOM')] = [max(cfgLoad['EICellTypeGain']['SOM']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['SOM']+rangeV2, maxV)]
    params[('EICellTypeGain', 'VIP')] = [max(cfgLoad['EICellTypeGain']['VIP']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['VIP']+rangeV2, maxV)]
    params[('EICellTypeGain', 'NGF')] = [max(cfgLoad['EICellTypeGain']['NGF']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['NGF']+rangeV2, maxV)]

    # params['thalamoCorticalGain'] = [0.25, 2.0]
    # params['intraThalamicGain'] = [0.25, 2.0]
    # params['corticoThalamicGain'] = [0.25, 2.0]

    groupedParams = []

    # --------------------------------------------------------
    # initial config
    initCfg = {}
    initCfg = {}
    initCfg['duration'] = 2000
    initCfg['printPopAvgRates'] = [[1000, 1250], [1250, 1500], [1500, 1750], [1750, 2000]]
    initCfg['dt'] = 0.05

    initCfg['scaleDensity'] = 0.5

    # plotting and saving params
    initCfg[('analysis','plotRaster','timeRange')] = [1000,2000]
    initCfg[('analysis', 'plotTraces', 'timeRange')] = [1000,2000]
    initCfg[('analysis', 'plotTraces', 'oneFigPer')] = 'trace'
    initCfg['recordLFP'] = None
    initCfg[('analysis', 'plotLFP')] = False

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False

    # --------------------------------------------------------
    # fitness function
    fitnessFuncArgs = {}
    pops = {}
    
    ## Exc pops
    Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6', 'TC', 'TCM', 'HTC']  # all layers + thal + IC

    Etune = {'target': 5, 'width': 20, 'min': 0.05}
    for pop in Epops:
        pops[pop] = Etune
    
    ## Inh pops 
    Ipops = ['NGF1',                            # L1
            'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
            'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
            'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
            'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A  
            'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
            'PV6', 'SOM6', 'VIP6', 'NGF6',       # L6
            'IRE', 'IREM', 'TI']  # Thal 

    Itune = {'target': 10, 'width': 30, 'min': 0.05}
    for pop in Ipops:
        pops[pop] = Itune
    
    fitnessFuncArgs['pops'] = pops
    fitnessFuncArgs['maxFitness'] = 1000
    fitnessFuncArgs['tranges'] = initCfg['printPopAvgRates']

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        tranges = kwargs['tranges']

        popFitnessAll = []

        for trange in tranges:
            popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness) 
                if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] > v['min'] else maxFitness for k, v in pops.items()])
        
        popFitness = np.mean(np.array(popFitnessAll), axis=0)
        
        fitness = np.mean(popFitness)

        popInfo = '; '.join(['%s rate=%.1f fit=%1.f' % (p, np.mean(list(simData['popRates'][p].values())), popFitness[i]) for i,p in enumerate(pops)])
        print('  ' + popInfo)

        return fitness
        
    # create Batch object with paramaters to modify, and specifying files to use
    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)

    b.method = 'optuna'

    b.optimCfg = {
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'maxFitness': fitnessFuncArgs['maxFitness'],
        'maxiters':     1e6,    #    Maximum number of iterations (1 iteration = 1 function evaluation)
        'maxtime':      None,    #    Maximum time allowed, in seconds
        'maxiter_wait': 16,
        'time_sleep': 60,
        'popsize': 1  # unused - run with mpi 
    }

    return b
```

---

**Optuna optimization w/optunaRatesLayers**

Quindi qui abbiamo layer-related hyperparameters.

```python
def optunaRatesLayers():

    '''
    # from prev
    import json
    with open('data/v32_batch14/trial_981/trial_981_cfg.json', 'rb') as f:
        cfgLoad = json.load(f)['simConfig']
    '''

    # best from grid search
    import json
    # with open('data/v32_batch4/trial_15057/trial_15057_cfg.json', 'rb') as f:
    #     cfgLoad = json.load(f)['simConfig']

    # good thal params for 100% cell density 
    with open('data/v34_batch5/v34_batch5_0_2_0_0_2_0_2_2_cfg.json', 'rb') as f:
        cfgLoad2 = json.load(f)['simConfig']

    cfgLoad = cfgLoad2

```

```python

    # --------------------------------------------------------
    # parameters
    params = specs.ODict()

    rangeV = 0.25
    rangeV2 = 1.0
    minV = 0.1
    maxV = 4.0 #sta solo per valore

    # params based on v32_batch8 grid search best solutions; plus added L2 and L3 IE specific gains since those were problematic layers
    params['EEGain'] = [0.1, 0.5] #2 values for flexibility
    params['EIGain'] = [1.3, 1.7] 
    params['IEGain'] = [0.8, 1.7] 
    params['IIGain'] = [0.3, 0.7] 
    params[('EICellTypeGain', 'PV')] = [0.8, 1.7] 
    params[('EICellTypeGain', 'SOM')] = [0.3, 0.7] 
    params[('EICellTypeGain', 'VIP')] = [1.3, 1.7] 
    params[('EICellTypeGain', 'NGF')] = [1.3, 1.7] 

   #qui stabiliamo gain for layers
    params[('IELayerGain', '2')] = [max(cfgLoad2['IELayerGain']['2']-rangeV, minV), min(cfgLoad2['IELayerGain']['2']+rangeV, maxV)]
    params[('IELayerGain', '3')] = [max(cfgLoad2['IELayerGain']['3']-rangeV, minV), min(cfgLoad2['IELayerGain']['3']+rangeV, maxV)]
    params[('IELayerGain', '4')] = [max(cfgLoad2['IELayerGain']['4']-rangeV, minV), min(cfgLoad2['IELayerGain']['4']+rangeV, maxV)]
    params[('IELayerGain', '5A')] = [max(cfgLoad2['IELayerGain']['5A']-rangeV, minV), min(cfgLoad2['IELayerGain']['5A']+rangeV, maxV)]
    params[('IELayerGain', '5B')] = [max(cfgLoad2['IELayerGain']['5B']-rangeV, minV), min(cfgLoad2['IELayerGain']['5B']+rangeV, maxV)]

   #non so perché this is commented out
    '''
    params[('EICellTypeGain', 'PV')] = [max(cfgLoad['EICellTypeGain']['PV']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['PV']+rangeV2, maxV)]
    params[('EICellTypeGain', 'SOM')] = [max(cfgLoad['EICellTypeGain']['SOM']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['SOM']+rangeV2, maxV)]
    params[('EICellTypeGain', 'VIP')] = [max(cfgLoad['EICellTypeGain']['VIP']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['VIP']+rangeV2, maxV)]
    params[('EICellTypeGain', 'NGF')] = [max(cfgLoad['EICellTypeGain']['NGF']-rangeV2, minV), min(cfgLoad['EICellTypeGain']['NGF']+rangeV2, maxV)]
    params[('IECellTypeGain', 'PV')] = [max(cfgLoad['IECellTypeGain']['PV']-rangeV, minV), min(cfgLoad['IECellTypeGain']['PV']+rangeV, maxV)]
    params[('IECellTypeGain', 'SOM')] = [max(cfgLoad['IECellTypeGain']['SOM']-rangeV, minV), min(cfgLoad['IECellTypeGain']['SOM']+rangeV, maxV)]
    params[('IECellTypeGain', 'VIP')] = [max(cfgLoad['IECellTypeGain']['VIP']-rangeV, minV), min(cfgLoad['IECellTypeGain']['VIP']+rangeV, maxV)]
    params[('IECellTypeGain', 'NGF')] = [max(cfgLoad['IECellTypeGain']['NGF']-rangeV, minV), min(cfgLoad['IECellTypeGain']['NGF']+rangeV, maxV)]
    params[('EILayerGain', '1')] = [minV, maxV] #(cfgLoad['EILayerGain']['1']-rangeV2, minV), min(cfgLoad['EILayerGain']['1']+rangeV, maxV)]
    params[('IILayerGain', '1')] = [minV, maxV] #(cfgLoad['IILayerGain']['1']-rangeV2, minV), min(cfgLoad['IILayerGain']['1']+rangeV, maxV)]
    params[('EELayerGain', '2')] = [max(cfgLoad['EELayerGain']['2']-rangeV, minV), min(cfgLoad['EELayerGain']['2']+rangeV, maxV)]
    params[('EILayerGain', '2')] = [max(cfgLoad['EILayerGain']['2']-rangeV, minV), min(cfgLoad['EILayerGain']['2']+rangeV, maxV)]
    params[('IELayerGain', '2')] = [max(cfgLoad['IELayerGain']['2']-rangeV, minV), min(cfgLoad['IELayerGain']['2']+rangeV, maxV)]
    params[('IILayerGain', '2')] = [max(cfgLoad['IILayerGain']['2']-rangeV, minV), min(cfgLoad['IILayerGain']['2']+rangeV, maxV)]
    params[('EELayerGain', '3')] = [max(cfgLoad['EELayerGain']['3']-rangeV, minV), min(cfgLoad['EELayerGain']['3']+rangeV, maxV)]
    params[('EILayerGain', '3')] = [max(cfgLoad['EILayerGain']['3']-rangeV, minV), min(cfgLoad['EILayerGain']['3']+rangeV, maxV)]
    params[('IELayerGain', '3')] = [max(cfgLoad['IELayerGain']['3']-rangeV, minV), min(cfgLoad['IELayerGain']['3']+rangeV, maxV)]
    params[('IILayerGain', '3')] = [max(cfgLoad['IILayerGain']['3']-rangeV, minV), min(cfgLoad['IILayerGain']['3']+rangeV, maxV)]
    params[('EELayerGain', '4')] = [max(cfgLoad['EELayerGain']['4']-rangeV, minV), min(cfgLoad['EELayerGain']['4']+rangeV, maxV)]
    params[('EILayerGain', '4')] = [max(cfgLoad['EILayerGain']['4']-rangeV, minV), min(cfgLoad['EILayerGain']['4']+rangeV, maxV)]
    params[('IELayerGain', '4')] = [max(cfgLoad['IELayerGain']['4']-rangeV, minV), min(cfgLoad['IELayerGain']['4']+rangeV, maxV)]
    params[('IILayerGain', '4')] = [max(cfgLoad['IILayerGain']['4']-rangeV, minV), min(cfgLoad['IILayerGain']['4']+rangeV, maxV)]
    params[('EELayerGain', '5A')] = [minV, maxV] # [max(cfgLoad['EELayerGain']['5A']-rangeV2, minV), min(cfgLoad['EELayerGain']['5A']+rangeV, maxV)]
    params[('EILayerGain', '5A')] = [minV, maxV] # [max(cfgLoad['EILayerGain']['5A']-rangeV2, minV), min(cfgLoad['EILayerGain']['5A']+rangeV, maxV)]
    params[('IELayerGain', '5A')] = [minV, maxV] # [max(cfgLoad['IELayerGain']['5A']-rangeV2, minV), min(cfgLoad['IELayerGain']['5A']+rangeV, maxV)]
    params[('IILayerGain', '5A')] = [minV, maxV] # [max(cfgLoad['IILayerGain']['5A']-rangeV2, minV), min(cfgLoad['IILayerGain']['5A']+rangeV, maxV)]
    params[('EELayerGain', '5B')] = [minV, maxV] # [max(cfgLoad['EELayerGain']['5B']-rangeV2, minV), min(cfgLoad['EELayerGain']['5B']+rangeV, maxV)]
    params[('EILayerGain', '5B')] = [minV, maxV] # [max(cfgLoad['EILayerGain']['5B']-rangeV2, minV), min(cfgLoad['EILayerGain']['5B']+rangeV, maxV)]
    params[('IELayerGain', '5B')] = [minV, maxV] # [max(cfgLoad['IELayerGain']['5B']-rangeV2, minV), min(cfgLoad['IELayerGain']['5B']+rangeV, maxV)]
    params[('IILayerGain', '5B')] = [minV, maxV] # [max(cfgLoad['IILayerGain']['5B']-rangeV2, minV), min(cfgLoad['IILayerGain']['5B']+rangeV, maxV)]
    params[('EELayerGain', '6')] = [minV, maxV] # [max(cfgLoad['EELayerGain']['6']-rangeV2, minV), min(cfgLoad['EELayerGain']['6']+rangeV, maxV)]
    params[('EILayerGain', '6')] = [minV, maxV] # [max(cfgLoad['EILayerGain']['6']-rangeV2, minV), min(cfgLoad['EILayerGain']['6']+rangeV, maxV)]
    params[('IELayerGain', '6')] = [minV, maxV] # [max(cfgLoad['IELayerGain']['6']-rangeV2, minV), min(cfgLoad['IELayerGain']['6']+rangeV, maxV)]
    params[('IILayerGain', '6')] = [minV, maxV] # [max(cfgLoad['IILayerGain']['6']-rangeV2, minV), min(cfgLoad['IILayerGain']['6']+rangeV, maxV)]
    '''

    groupedParams = []

    
```

```python
# --------------------------------------------------------
    # initial config
    initCfg = {}
    initCfg['duration'] = 2500
    initCfg['printPopAvgRates'] = [[1500, 1750], [1750, 2000], [2000, 2250], [2250, 2500]]
    initCfg['dt'] = 0.05

    initCfg['scaleDensity'] = 1.0

    # plotting and saving params
    initCfg[('analysis','plotRaster','markerSize')] = 10

    initCfg[('analysis','plotRaster','timeRange')] = [1500, 2500]
    initCfg[('analysis', 'plotTraces', 'timeRange')] = [1500, 2500]

#below, assigning "trace" to oneFigPer"
initCfg[('analysis', 'plotTraces', 'oneFigPer')] = 'trace'
    initCfg['recordLFP'] = None
    initCfg[('analysis', 'plotLFP')] = False

    initCfg['saveCellSecs'] = False
    initCfg['saveCellConns'] = False
    
#dont know why commented out
    '''
    initCfg['EEGain'] = 1.0 	
    initCfg['EIGain'] = 1.0 	
    initCfg['IEGain'] = 1.0 	
    initCfg['IIGain'] = 1.0 	
    initCfg.update({'thalamoCorticalGain': cfgLoad['thalamoCorticalGain'],
                    'intraThalamicGain': cfgLoad['intraThalamicGain'],
                    'EbkgThalamicGain': cfgLoad['EbkgThalamicGain'],
                    'IbkgThalamicGain': cfgLoad['IbkgThalamicGain']})
    print(initCfg)
    '''

    # from prev - best of 50% cell density
    #CREATING a dict of params TO CHANGE (strings and tuples)
    updateParams = ['EEGain', 'EIGain', 'IEGain', 'IIGain',
                    ('EICellTypeGain', 'PV'), ('EICellTypeGain', 'SOM'), ('EICellTypeGain', 'VIP'), ('EICellTypeGain', 'NGF'),
                    ('IECellTypeGain', 'PV'), ('IECellTypeGain', 'SOM'), ('IECellTypeGain', 'VIP'), ('IECellTypeGain', 'NGF'),
                    ('EILayerGain', '1'), ('IILayerGain', '1'),
                    ('EELayerGain', '2'), ('EILayerGain', '2'),  ('IELayerGain', '2'), ('IILayerGain', '2'), 
                    ('EELayerGain', '3'), ('EILayerGain', '3'), ('IELayerGain', '3'), ('IILayerGain', '3'), 
                    ('EELayerGain', '4'), ('EILayerGain', '4'), ('IELayerGain', '4'), ('IILayerGain', '4'), 
                    ('EELayerGain', '5A'), ('EILayerGain', '5A'), ('IELayerGain', '5A'), ('IILayerGain', '5A'), 
                    ('EELayerGain', '5B'), ('EILayerGain', '5B'), ('IELayerGain', '5B'), ('IILayerGain', '5B'), 
                    ('EELayerGain', '6'), ('EILayerGain', '6'), ('IELayerGain', '6'), ('IILayerGain', '6')] 

    
#updates the initCfg dictionary with values from the cfgLoad dictionary based on the specified parameters in the updateParams list. It handles both direct keys and nested keys using tuples to access and update the values.
for p in updateParams:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad[p]})

    # good thal params for 100% cell density 
    updateParams2 = ['thalamoCorticalGain', 'intraThalamicGain', 'EbkgThalamicGain', 'IbkgThalamicGain']

    for p in updateParams2:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad2[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad2[p]})

    # --------------------------------------------------------
    # fitness function
    fitnessFuncArgs = {}
    pops = {} #will hold tuning params for each pop
    
    ## Exc pops
    Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6', 'TC', 'TCM', 'HTC']  # all layers + thal + IC
    #Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'TC', 'TCM', 'HTC']  # all layers + thal + IC

    #target is target FR 
    #width is the acceptable range around the FR
    #min is minimum firing rate
    #Etune = {'target': 5, 'width': 20, 'min': 0.05}
    Etune = {'target': 5, 'width': 5, 'min': 0.5}
    
    for pop in Epops:
        pops[pop] = Etune
    
    ## Inh pops 
    Ipops = ['NGF1',                            # L1
            'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
            'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
            'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
            'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A  
            'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
            'PV6', 'SOM6', 'VIP6', 'NGF6',       # L6
            'IRE', 'IREM', 'TI']  # Thal 
    # Ipops = [#'NGF1',  
    #         'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
    #         'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
    #         'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
    #         #'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A 
    #         #'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
    #         #'PV6', 'SOM6', 'VIP6', 'NGF6',  # L6
    #         'IRE', 'IREM', 'TI']  # Thal 

    #Itune = {'target': 10, 'width': 30, 'min': 0.05}
    Itune = {'target': 10, 'width': 15, 'min': 0.5}

    for pop in Ipops:
        pops[pop] = Itune
    
    fitnessFuncArgs['pops'] = pops
    fitnessFuncArgs['maxFitness'] = 1000
    fitnessFuncArgs['tranges'] = initCfg['printPopAvgRates']

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        tranges = kwargs['tranges']

        popFitnessAll = []

        for trange in tranges:
            popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness) 
                if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] >= v['min'] else maxFitness for k, v in pops.items()])
        
        popFitness = np.mean(np.array(popFitnessAll), axis=0)
        
        fitness = np.mean(popFitness)

        popInfo = '; '.join(['%s rate=%.1f fit=%1.f' % (p, np.mean(list(simData['popRates'][p].values())), popFitness[i]) for i,p in enumerate(pops)])
        print('  ' + popInfo)

        return fitness
        
    # create Batch object with paramaters to modify, and specifying files to use
    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)

    b.method = 'optuna'

    b.optimCfg = {
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'maxFitness': fitnessFuncArgs['maxFitness'],
        'maxiters':     1e6,    #    Maximum number of iterations (1 iteration = 1 function evaluation)
        'maxtime':      None,    #    Maximum time allowed, in seconds
        'maxiter_wait': 45,
        'time_sleep': 120,
        'popsize': 1  # unused - run with mpi 
    }

    return b
```

- `params[('IELayerGain', '2')] = [max(cfgLoad2['IELayerGain']['2'] - rangeV, minV), min(cfgLoad2['IELayerGain']['2'] + rangeV, maxV)]`
    
    piano piano: 
    - **`cfgLoad2['IELayerGain']['2']`** retrieves layer 2 from the cfgLoad2 dictionary.
    
    -**`max(cfgLoad2['IELayerGain']['2'] - rangeV, minV)`** computes the maximum value between the result of subtracting **`rangeV`** from **`cfgLoad2['IELayerGain']['2']`** and **`minV`**. This ensures that the resulting value does not go below the minimum value.
    
    -**`min(cfgLoad2['IELayerGain']['2'] + rangeV, maxV)`** computes the minimum value between the result of adding **`rangeV`** to **`cfgLoad2['IELayerGain']['2']`** and **`maxV`**. This ensures that the resulting value does not exceed the maximum value.
    
    -**`[max(cfgLoad2['IELayerGain']['2'] - rangeV, minV), min(cfgLoad2['IELayerGain']['2'] + rangeV, maxV)]`** creates a list with two elements: the maximum value (from step 4) and the minimum value (from step 5).
    
    - Finally, **`params[('IELayerGain', '2')] = [max(cfgLoad2['IELayerGain']['2'] - rangeV, minV), min(cfgLoad2['IELayerGain']['2'] + rangeV, maxV)]`** assigns the created list to the key **`('IELayerGain', '2')`** in the **`params`** dictionary.
    
    This code calculates a range of values for the gain of a specific layer (layer 2) based on an initial gain value, a range, and minimum/maximum constraints. The resulting range is then stored in the **`params`** dictionary with the key **`('IELayerGain', '2')`**
    

- the **`Etune`** tuning parameter configuration is assigned to the **`pop`** key of the **`pops`** dictionary. Each population in the **`Epops`** list corresponds to a key in the **`pops`** dictionary, and the value associated with that key is the **`Etune`** tuning parameter configuration.

As this happens in the fitness function, these populations will be tuned during the fitness evaluation process.
- poi nello specifico: 
`def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        tranges = kwargs['tranges']`

-Questa funzione takes simData and additional keyword arguments as input. 
→ calculates FITNESS VALUE based on these params (how well the model performs according to certain criteria). 
        
-inside the **`fitnessFunc`**, the keyword arguments **`pops`**, **`maxFitness`**, and **`tranges`** are extracted from **`kwargs`**. These arguments are used in the fitness calculation.

-The variable **`popFitnessAll`** is initialized as an empty list to store the fitness values for each population and time range.

-the fitness calculation is performed for each time range in **`tranges`:**

        `for trange in tranges:
popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness)` 

Qui sopra: for each population k in pops, the fitness value is calculated based on the difference between the target rate (**`v['target']`**) and the simulated population rate (**`simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])`**. 

The fitness value is then normalized using a width parameter (**`v['width']`**) and limited to the **`maxFitness`** value.

 If the simulated population rate is below the minimum rate (**`v['min']`**), the fitness is set to **`maxFitness`:**

`if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] >= v['min'] else maxFitness for k, v in pops.items()])`

The fitness values for each population and time range are stored in popFitnessAll:
        `popFitness =np.mean(np.array(popFitnessAll), axis=0)`

The overall fitness viene calcolata tramite la media di popFitness:
        `fitness = np.mean(popFitness)`
- The **`popInfo`** variable is created to store a formatted string that contains information about each population's average rate and fitness value.
It’s printed to the console for display.
        `popInfo = '; '.join(['%s rate=%.1f fit=%1.f' % (p, np.mean(list(simData['popRates'][p].values())), popFitness[i]) for i,p in enumerate(pops)])
        print('  ' + popInfo)` 

Nello specifico:
    1. **`enumerate(pops)`** is used to iterate over the **`pops`** dictionary, which contains information about the populations and their corresponding fitness tuning parameters.
    2. For each population, the following information is collected:
        - **`%s`** is a placeholder for the population name (**`p`**).
        - **`rate=%.1f`** formats the average rate of the population. **`np.mean(list(simData['popRates'][p].values()))`** retrieves the population rate values from the **`simData`** dictionary, calculates their mean using **`np.mean`**, and formats it as a float with one decimal point.
        - **`fit=%1.f`** formats the fitness value for the population. **`popFitness[i]`** retrieves the fitness value from the **`popFitness`** array based on the current index (**`i`**).
    3. The formatted strings for each population are joined together using **`'; '.join()`**, which inserts a semicolon followed by a space between each population's information.
    4. Finally, the string **`popInfo`** contains the joined information for all populations.
    
    The line **`print(' ' + popInfo)`** prints the **`popInfo`** string, adding an indentation of two spaces at the beginning. This output provides a summary of the average rate and fitness values for each population in a readable format.
    

- `return fitness` → this is the output of the fitness function, corresponding to the mean of  `popFitnessvalue`.
- # create Batch object with parameters to modify, and specifying files to use
    `b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)`

    `b.method = 'optuna'`

The optimization configuration for the Batch object is set, it includes the fitness function, the fitness function arguments, max fitness, max num of iterations, max time allowed, waiting time for improvement(`maxiter_wait`) time to sleep between iterations, popsize. : 
    `b.optimCfg = {
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'maxFitness': fitnessFuncArgs['maxFitness'],
        'maxiters':     1e6,    #    Maximum number of iterations (1 iteration = 1 function evaluation)
        'maxtime':      None,    #    Maximum time allowed, in seconds
        'maxiter_wait': 45,
        'time_sleep': 120,
        'popsize': 1  # unused - run with mpi` 
    `}`

    `return b`

---

**Optuna optimization**

- capire how this differs, is it just optuna but for different thalamic layers?

```python
def optunaRatesLayersThalL12345A5B6():

    # from prev
    import json
    with open('data/v34_batch15/trial_5955/trial_5955_cfg.json', 'rb') as f:
        cfgLoad = json.load(f)['simConfig']
```

```python
# parameters
    params = specs.ODict()

    rangeV1 = 0.2
    rangeV2 = 0.25
    rangeV3 = 2.0

    scaleLow = 0.9
    scaleHigh = 1.1

    scaleLow2 = 0.5
    scaleHigh2 = 1.5

    minV = 0.1
    maxV = 5.0
```

#cell-type specific parameters

**E → I** 

```python
	params[('EICellTypeGain', 'PV')] = [max(cfgLoad['EICellTypeGain']['PV']*scaleLow2, minV), min(cfgLoad['EICellTypeGain']['PV']*scaleHigh2, maxV)]
  params[('EICellTypeGain', 'SOM')] = [max(cfgLoad['EICellTypeGain']['SOM']*scaleLow2, minV), min(cfgLoad['EICellTypeGain']['SOM']*scaleHigh2, maxV)]
  params[('EICellTypeGain', 'VIP')] = [max(cfgLoad['EICellTypeGain']['VIP']*scaleLow2, minV), min(cfgLoad['EICellTypeGain']['VIP']*scaleHigh2, maxV)]
  params[('EICellTypeGain', 'NGF')] = [max(cfgLoad['EICellTypeGain']['NGF']*scaleLow2, minV), min(cfgLoad['EICellTypeGain']['NGF']*scaleHigh2, maxV)]
```

**I → E** 

```python
params[('IECellTypeGain', 'PV')] = [max(cfgLoad['IECellTypeGain']['PV']*scaleLow, minV), min(cfgLoad['IECellTypeGain']['PV']*scaleHigh, maxV)]
params[('IECellTypeGain', 'SOM')] = [max(cfgLoad['IECellTypeGain']['SOM']*scaleLow, minV), min(cfgLoad['IECellTypeGain']['SOM']*scaleHigh, maxV)]
params[('IECellTypeGain', 'VIP')] = [max(cfgLoad['IECellTypeGain']['VIP']*scaleLow, minV), min(cfgLoad['IECellTypeGain']['VIP']*scaleHigh, maxV)]
params[('IECellTypeGain', 'NGF')] = [max(cfgLoad['IECellTypeGain']['NGF']*scaleLow, minV), min(cfgLoad['IECellTypeGain']['NGF']*scaleHigh, maxV)]
```

**L1**  

```python
params[('EILayerGain', '1')] = [max(cfgLoad['EILayerGain']['1']*scaleLow, minV), min(cfgLoad['EILayerGain']['1']*scaleHigh, maxV)]
params[('IILayerGain', '1')] = [max(cfgLoad['IILayerGain']['1']*scaleLow, minV), min(cfgLoad['IILayerGain']['1']*scaleHigh, maxV)]
```

**L2**  

```python
params[('EELayerGain', '2')] = [max(cfgLoad['EELayerGain']['2']*scaleLow2, minV), min(cfgLoad['EELayerGain']['2']*scaleHigh2, maxV)]
params[('EILayerGain', '2')] = [max(cfgLoad['EILayerGain']['2']*scaleLow2, minV), min(cfgLoad['EILayerGain']['2']*scaleHigh2, maxV)]
params[('IELayerGain', '2')] = [max(cfgLoad['IELayerGain']['2']*scaleLow2, minV), min(cfgLoad['IELayerGain']['2']*scaleHigh2, maxV)]
params[('IILayerGain', '2')] = [max(cfgLoad['IILayerGain']['2']*scaleLow2, minV), min(cfgLoad['IILayerGain']['2']*scaleHigh2, maxV)]
```

**L3** 

```python
params[('EELayerGain', '3')] = [max(cfgLoad['EELayerGain']['3']*scaleLow2, minV), min(cfgLoad['EELayerGain']['3']*scaleHigh2, maxV)]
params[('EILayerGain', '3')] = [max(cfgLoad['EILayerGain']['3']*scaleLow2, minV), min(cfgLoad['EILayerGain']['3']*scaleHigh2, maxV)]
params[('IELayerGain', '3')] = [max(cfgLoad['IELayerGain']['3']*scaleLow2, minV), min(cfgLoad['IELayerGain']['3']*scaleHigh2, maxV)]
params[('IILayerGain', '3')] = [max(cfgLoad['IILayerGain']['3']*scaleLow2, minV), min(cfgLoad['IILayerGain']['3']*scaleHigh2, maxV)]
```

Etc. etc. for: **L4** **L5A, L5B L6**

`groupedParams = []` 

**initCfg → parameters SPECIFIC to this batch:**

```python
initCfg = {}
initCfg['duration'] = 2500
initCfg['printPopAvgRates'] = [[1500, 1750], [1750, 2000], [2000, 2250], [2250, 2500]]
initCfg['dt'] = 0.05 #dt is time step

initCfg['scaleDensity'] = 1.0
```

```python

# plotting and saving params
initCfg[('analysis','plotRaster','markerSize')] = 10

initCfg[('analysis','plotRaster','timeRange')] = [1500, 2500]
initCfg[('analysis', 'plotTraces', 'timeRange')] = [1500, 2500]
initCfg[('analysis', 'plotTraces', 'oneFigPer')] = 'trace'
initCfg['recordLFP'] = None
initCfg[('analysis', 'plotLFP')] = False
```

```python
initCfg['saveCellSecs'] = False
initCfg['saveCellConns'] = False
```

below you're creating a list of params to update:
(first is best of 50% cell density)

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
('EELayerGain', '6'), ('EILayerGain', '6'), ('IELayerGain', '6'), ('IILayerGain', '6')]
```

l’update effettivo avviene nei forloops sotto: 
Qui sotto we iterate over the updateParams list → for each p, we check if single value or tuple.
If tuple → the parameter requires accessing a nested dict. 
In this case, we update the corresponding values from the cfgLoad dict onto the initCfg.
If single value → we directly update it in initCfg with its value from cfgLoad.

```python
for p in updateParams:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad[p]})
```

Poi qui creiamo una lista 2, **`updateParams2`**, che contiene ALTRI parameteri se we want cell density to be at 100%: 

```python
updateParams2 = ['thalamoCorticalGain', 'intraThalamicGain', 'EbkgThalamicGain', 'IbkgThalamicGain']

    for p in updateParams2:
        if isinstance(p, tuple):
            initCfg.update({p: cfgLoad[p[0]][p[1]]})
        else:
            initCfg.update({p: cfgLoad[p]})

    print(initCfg) #qui vedrai la cfg modificata
    #con questi nuovi parametri aggiunti
```

**FONDAMENTALE** → ogni volta che you update initCfg, usando the items of the list `updateParams`, the value of each p in updateParams is stored in the `cfgLoad` dictionary, using the parameter names as keys.

**THE DATA THAT IS LOADED FROM THE JSON FILE IS THEN STORED IN THE CFGLOAD VARIABLE!!!**

poi fitness function, creating batch object: 

```python
# fitness function
    fitnessFuncArgs = {}
    pops = {}
    
    ## Exc pops
    Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6', 'TC', 'TCM', 'HTC']  # all layers + thal + IC
    #Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'TC', 'TCM', 'HTC']  # all layers + thal + IC

    #Etune = {'target': 5, 'width': 20, 'min': 0.05}
    Etune = {'target': 5, 'width': 5, 'min': 0.5}
    
    for pop in Epops:
        pops[pop] = Etune
    
    ## Inh pops 
    Ipops = ['NGF1',                            # L1
            'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
            'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
            'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
            'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A  
            'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
            'PV6', 'SOM6', 'VIP6', 'NGF6',       # L6
            'IRE', 'IREM', 'TI']  # Thal 
    # Ipops = [#'NGF1',  
    #         'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
    #         'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
    #         'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
    #         #'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A 
    #         #'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
    #         #'PV6', 'SOM6', 'VIP6', 'NGF6',  # L6
    #         'IRE', 'IREM', 'TI']  # Thal 

    #Itune = {'target': 10, 'width': 30, 'min': 0.05}
    Itune = {'target': 10, 'width': 15, 'min': 0.5}

    for pop in Ipops:
        pops[pop] = Itune
    
    fitnessFuncArgs['pops'] = pops
    fitnessFuncArgs['maxFitness'] = 1000
    fitnessFuncArgs['tranges'] = initCfg['printPopAvgRates']

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        pops = kwargs['pops']
        maxFitness = kwargs['maxFitness']
        tranges = kwargs['tranges']

        popFitnessAll = []

        for trange in tranges:
            popFitnessAll.append([min(np.exp(abs(v['target'] - simData['popRates'][k]['%d_%d'%(trange[0], trange[1])])/v['width']), maxFitness) 
                if simData['popRates'][k]['%d_%d'%(trange[0], trange[1])] >= v['min'] else maxFitness for k, v in pops.items()])
        
        popFitness = np.mean(np.array(popFitnessAll), axis=0)
        
        fitness = np.mean(popFitness)

        popInfo = '; '.join(['%s rate=%.1f fit=%1.f' % (p, np.mean(list(simData['popRates'][p].values())), popFitness[i]) for i,p in enumerate(pops)])
        print('  ' + popInfo)

        return fitness
        
    # create Batch object with paramaters to modify, and specifying files to use
    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py', initCfg=initCfg, groupedParams=groupedParams)

    b.method = 'optuna'

    b.optimCfg = {
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'maxFitness': fitnessFuncArgs['maxFitness'],
        'maxiters':     1e6,    #    Maximum number of iterations (1 iteration = 1 function evaluation)
        'maxtime':      None,    #    Maximum time allowed, in seconds
        'maxiter_wait': 45,
        'time_sleep': 120,
        'popsize': 1  # unused - run with mpi 
    }

    return b
```

---

**Run configurations**

Qui abbiamo diff options for running the simulation on diff systems. 
**All skips are set to true così sei tu che decidi quale vuoi davvero, e lo metti falso**

```python
# Run configurations
# ----------------------------------------------------------------------------------------------
#b sta per batch, type is type of simulation

#MESSAGE PASSING INTERFACE, BULLETIN STYLE OUPTUT
#sets script to be executed as init_cell.py
#skips execution
def setRunCfg(b, type='mpi_bulletin'):
    if type=='mpi_bulletin':
        b.runCfg = {'type': 'mpi_bulletin', 
            'script': 'init_cell.py', 
            'skip': True}

#on local machine e.g. 2x-3x with 4 cores:
#set to mpiexec -n 4 nrniv -python -mpi init.py
    elif type=='mpi_direct':
        b.runCfg = {'type': 'mpi_direct',
            'nodes': 1,
            'coresPerNode': 96,
            'script': 'init.py',
            'mpiCommand': 'mpirun',
            'skip': True}

    elif type=='hpc_torque':
        b.runCfg = {'type': 'hpc_torque',
             'script': 'init.py',
             'nodes': 3,
             'ppn': 8,
             'walltime': "12:00:00",
             'queueName': 'longerq',
             'sleepInterval': 5,
             'skip': True}

    elif type=='hpc_slurm_comet':
        b.runCfg = {'type': 'hpc_slurm', 
            'allocation': 'shs100', # bridges='ib4iflp', comet m1='shs100', comet nsg='csd403'
            #'reservation': 'salva1',
            'walltime': '6:00:00',
            'nodes': 4,
            'coresPerNode': 24,  # comet=24, bridges=28
            'email': 'salvadordura@gmail.com',
            'folder': '/home/salvadord/m1/sim/',  # comet='/salvadord', bridges='/salvi82'
            'script': 'init.py', 
            'mpiCommand': 'ibrun', # comet='ibrun', bridges='mpirun'
            'skipCustom': '_raster.png'}

    elif type=='hpc_slurm_gcp':
        b.runCfg = {'type': 'hpc_slurm', 
            'allocation': 'default', # bridges='ib4iflp', comet m1='shs100', comet nsg='csd403', gcp='default'
            'walltime': '24:00:00', #'48:00:00',
            'nodes': 1,
            'coresPerNode': 80,  # comet=24, bridges=28, gcp=32
            'email': 'salvadordura@gmail.com',
            'folder': '/home/ext_salvadordura_gmail_com/A1_layers/',  # comet,gcp='/salvadord', bridges='/salvi82'
            'script': 'init.py',
            'mpiCommand': 'mpirun', # comet='ibrun', bridges,gcp='mpirun' 
            'nrnCommand': 'nrniv -mpi -python', #'python3',
            'skipCustom': '_raster.png'}
            #'custom': '#SBATCH --exclude=compute[17-64000]'} # only use first 16 nodes (non-preemptible for long runs )
            # --nodelist=compute1

    elif type=='hpc_slurm_bridges':
        b.runCfg = {'type': 'hpc_slurm', 
            'allocation': 'ib4iflp', # bridges='ib4iflp', comet m1='shs100', comet nsg='csd403'
            'walltime': '06:00:00',
            'nodes': 2,
            'coresPerNode': 28,  # comet=24, bridges=28
            'email': 'salvadordura@gmail.com',
            'folder': '/home/salvi82/m1/sim/',  # comet='/salvadord', bridges='/salvi82'
            'script': 'init.py', 
            'mpiCommand': 'mpirun', # comet='ibrun', bridges='mpirun'
            'skip': True}
```

---

---

**Main code**

```python
# ----------------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':

    cellTypes = ['IT2', 'PV2', 'SOM2', 'VIP2', 'NGF2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6', 'TC', 'HTC', 'IRE', 'TI']

    b = custom_spont('data/v34_batch25/trial_2142/trial_2142_cfg.json')
    # b = optunaRatesLayersThalL12345A5B6()
    # b = optunaRatesLayersWmat()

    # b = bkgWeights(pops = cellTypes, weights = list(np.arange(1,100)))
    # b = fIcurve(pops=['ITS4']) 

    b.batchLabel = 'v34_batch68' 
    b.saveFolder = 'data/'+b.batchLabel

    setRunCfg(b, 'hpc_slurm_gcp') #'hpc_slurm_gcp') #'mpi_bulletin') #'hpc_slurm_gcp')
    b.run() # run batch
```

run *after* you created batch
