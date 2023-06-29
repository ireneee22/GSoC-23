# [A1 netParams.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/netParams.py) description

TODO: translate from italian 


difference between cfg.py and netParams.py (taken from tut8) 

- `[tut8_netParams.py](http://www.netpyne.org/_downloads/5810ef33ffc308cf6c38dbb7dde1bd46/tut8_netParams.py)` : Defines the network model (netParams object). Includes “fixed” parameter values of cells, synapses, connections, stimulation, etc. Changes to this file should only be made for relatively stable improvements of the model. Parameter values that will be varied systematically to explore or tune the model should be included here by referencing the appropiate variable in the simulation configuration (cfg) module. Only a single netParams file is required for each batch of simulations.
    
    `[tut8_netParams.py](http://www.netpyne.org/_downloads/5810ef33ffc308cf6c38dbb7dde1bd46/tut8_netParams.py)`
    
- `[tut8_cfg.py](http://www.netpyne.org/_downloads/002a13ee17217bbeb58cf3a067d6e50b/tut8_cfg.py)` : Simulation configuration (simConfig object). Includes parameter values for each simulation run such as duration, dt, recording parameters etc. Also includes the model parameters that are being varied to explore or tune the network. When running a batch, NetPyNE will automatically create one cfg file for each parameter configuration (using this one as a starting point).
    
    `[tut8_cfg.py](http://www.netpyne.org/_downloads/002a13ee17217bbeb58cf3a067d6e50b/tut8_cfg.py)`
    

---

`netParams = specs.NetParams()`   # object of class NetParams to store the network parameters

- specs.Netparams() is a class used to create a network specification object.
- this line of code creates an empty network specification object taht can be used to define the properties of the network that you want to simulate.
- once you have created the ‘NetParams’ objects, you can start adding properties by calling its methods → esempio ‘**netParams.addCellParams()’**

```python
try:
from **main** import cfg  # import SimConfig object with params from parent module
except:
from cfg import cfg
```

---

# Network Parameters

### General network parameters

here you’re equating many things to cfg. scales → cfg is defined at the beginning and then many attributes of netParams objects are based on the values of the corresponding attributes in cfg. 

`netParams.scale = cfg.scale` # Scale factor for number of cells # NOT DEFINED YET! 3/11/19 # How is this different than scaleDensity?

`netParams.sizeX = cfg.sizeX` # x-dimension (horizontal length) size in um
`netParams.sizeY = cfg.sizeY` # y-dimension (vertical height or cortical depth) size in um
`netParams.sizeZ = cfg.sizeZ` # z-dimension (horizontal depth) size in um

`netParams.shape = 'cylinder'`# cylindrical (column-like) volume

- this lines sets the value of the shape attribute of the netParams object to cylinder.
- it’s the shape of neurons in the model  (so, all the membrane of the neuron is considered as a single compartment).

### General connectivity parameters

`netParams.scaleConnWeight = 1.0` # Connection weight scale factor (default if no model specified)

- because it is set to 1, we are simply using the weights of connections as they are specified in the connParams section of the cfg object.

`netParams.scaleConnWeightModels = { 'HH_reduced': 1.0, 'HH_full': 1.0}` #scale conn weight factor for each cell model

- this line has the goal of setting the value of the ‘scaleConnWeightModels’ attribute of the netParams object to a dictionary with 2 keys: 
-HH_reduced 
-HH_ full

The values for both keys are 1 → we rely on cfg

`netParams.scaleConnWeightNetStims = 1.0` #0.5  # scale conn weight factor for NetStims

- sets value of the `‘scaleConnWeightNetStims’` attribute of the `‘netParams’` object to 1.
- it determines the scaling factor for the synaptic weights of the connections originating from `‘NetStim’` objects (source of external Poisson distributed stimulation).
- because =1, we refer to specification of `‘connParams’` section of cfg object.

`netParams.defaultThreshold = 0.0` # spike threshold, 10 mV is `NetCon` default, lower it for all cells

- `defaultThreshold` attribute of `netParams` object specifies the default threshold voltage for all the neurons in the network (minimum membrane voltage that a neuron needs to reach in order to generate an action potential or spike)
- because set to 0 → each neuron will generate a spike as soon as it receives any positive synaptic input.

`netParams.defaultDelay = 2.0` # default conn delay (ms)

- specifies default synaptic delay for all connections in the network
- synaptic delay : time delay between the arrival of a presynaptic spike at the synapse and the generation of a postsynaptic potential
- default to 2 : it takes 2 ms for postsyn spike to start

`netParams.propVelocity = 500.0` # propagation velocity (um/ms)

- `propVelocity` attribute specifies the propagation velocity of the action potentials or spikes along the axons of the neurons in the network.
- This attribute is used to calculate the conduction delays of the connections in the network, based on the distance between the presynaptic and postsynaptic neurons.
- Setting **`propVelocity`** to **`500.0`** means that the propagation velocity of the action potentials is set to 500 meters per second.

`netParams.probLambda = 100.0`  # length constant (lambda) for connection probability decay (um)

- the attribute **`probLambda`**  of the **`netParams`** object is set to have value **`100.0`**.
- The **`probLambda`** attribute specifies the probability density of connections between neurons in the network. Specifically, it is used to calculate the probability of connection between a pair of neurons based on their distance.
- Setting **`probLambda`** to **`100.0`** means that the probability density of connections between neurons is set to 100 connections per millimeter.
- Higher values of **`probLambda`** will result in a higher density of connections between neurons, while lower values will result in a lower density of connections.


### Cell parameters

`Etypes = ['IT', 'ITS4', 'PT', 'CT']`

- excitatory cell types:  IT (intrinsically bursting), ITS4 (sparsely spiking), PT (regular spiking pyramidal), and CT (fast spiking).

`Itypes = ['PV', 'SOM', 'VIP', 'NGF']`

- inhibitory cell types: PV (parvalbumin-positive interneurons), SOM (somatostatin-positive interneurons), VIP (vasoactive intestinal polypeptide-positive interneurons), and NGF (neurogliaform cells).

`cellModels = ['HH_reduced', 'HH_full']` # List of cell models

- different Hodgkin-Huxley-based models that simulate the neuron behavior in network

`layer = {'1': [0.00, 0.05], '2': [0.05, 0.08], '3': [0.08, 0.475], '4': [0.475, 0.625], '5A': [0.625, 0.667], '5B': [0.667, 0.775], '6': [0.775, 1], 'thal': [1.2, 1.4], 'cochlear': [1.6, 1.8]}` # normalized layer boundaries

- dict where:
- each key represents the names of the different layers
- values are lists of 2 normalized values defining lower and upper boundaries of each layer
- values are normalized values → quindi they do not have a specific unit of measure. Normalization  makes simulations more generic and independent of the specific physical properties of the system being modeled.
- layer boundaries are normalized between 0 and 1, where 0 represents the bottom of the network and 1 represents the top.

```python
layerGroups = { '1-3': [layer['1'][0], layer['3'][1]],  # L1-3
'4': layer['4'],                      # L4
'5': [layer['5A'][0], layer['5B'][1]],  # L5A-5B
'6': layer['6']}                        # L6
```

- The **`layerGroups`** dictionary defines groups of layers in the network by combining the boundaries of multiple layers from the **`layer`** dictionary. The keys of the dictionary represent the names of the different layer groups, while the values are lists of two normalized values → they define the lower and upper boundaries of each layer group.
- Example: the first entry in the dictionary is **`'1-3': [layer['1'][0], layer['3'][1]]`**, which means that layer group 1-3 includes the layers from 1 to 3, inclusive. The lower boundary of layer group 1-3 is the same as the lower boundary of layer 1, which is accessed by indexing the **`layer`** dictionary with the key **`'1'`** and the first element of its associated value (i.e., **`layer['1'][0]`**). The upper boundary of layer group 1-3 is the same as the upper boundary of layer 3, which is accessed by indexing the **`layer`** dictionary with the key **`'3'`** and the second element of its associated value (i.e., **`layer['3'][1]`**).

---

### Load cell rules previously saved using netpyne format

```python
cellParamLabels = ['IT2_reduced', 'IT3_reduced', 'ITP4_reduced', 'ITS4_reduced',
'IT5A_reduced', 'CT5A_reduced', 'IT5B_reduced',
'PT5B_reduced', 'CT5B_reduced', 'IT6_reduced', 'CT6_reduced',
'PV_reduced', 'SOM_reduced', 'VIP_reduced', 'NGF_reduced',
'RE_reduced', 'TC_reduced', 'HTC_reduced', 'TI_reduced']
```

- list of different cell types and corresponding cell parameter labels.

```python
for ruleLabel in cellParamLabels:
netParams.loadCellParamsRule(label=ruleLabel, fileName='cells/' + ruleLabel + '_cellParams.json')  # Load cellParams for each of the above cell subtype
```

- loops through the list above of **`cellParamLabels`** and loads the corresponding cell parameter files for each subtype.
- The **`loadCellParamsRule`** function is called for each label with the **`label`** parameter set to the current **`ruleLabel`** and the **`fileName`** parameter set to the appropriate file path for that cell subtype.

#change weightNorm

```python
for k in cfg.weightNormScaling:
for sec in netParams.cellParams[k]['secs'].values():
for i in range(len(sec['weightNorm'])):
sec['weightNorm'][i] *= cfg.weightNormScaling[k]
```

- updates weightNorm parameter for each section WITHIN each cell model, by scaling it with the corresponding value in **`cfg.weightNormScaling`**
- it loops through each k in `**cfg.weightNormScaling`(which corresponds to a cell type)**
- then it loops through each section of that cell type
- this parameter specifies the normalization factor to apply to the synaptic weights for each section , in each cell model

---

### Population parameters

#Load densities 

```python
with open('cells/cellDensity.pkl', 'rb') as fileObj: density = pickle.load(fileObj)['density']
density = {k: [x * cfg.scaleDensity for x in v] for k,v in density.items()} # Scale densities
```

- using open(), the `cellDensity.pkl` file is opened in binary read.
- contents of the pkl file are loaded onto the `‘density’`variable.
- the density variable is a dictionary containing the density values of different cell types in different layers of the model
- the code scales the density values by multiplying each value in the dict with `cfg.scaleDensity`, a scaling factor specified in cfg.
- the resulting density dictionary with this new scaled density values is used later in the code to create the network model

##layer 1 

```python
netParams.popParams['NGF1'] = {'cellType': 'NGF', 'cellModel': 'HH_reduced','ynormRange': layer['1'], 'density': density[('A1','nonVIP')][0]}
```

- qui stiamo proprio aggiungendo a new population of cells in layer 1
- this is population NGF1
- cellModel : HH_reduced
- ynormRange : layer 1 → qui specifica la profondità in cui si trova questa popolazione ; we established layer boundaries earlier in the code
- density: facciamo riferimento al dizionario che avevamo già stabilito

Gli stessi concetti apply to the following layers: 

#LAYER 2 

```python
netParams.popParams['IT2'] =     {'cellType': 'IT',  'cellModel': 'HH_reduced',  'ynormRange': layer['2'],   'density': density[('A1','E')][1]}     #

netParams.popParams['SOM2'] =    {'cellType': 'SOM', 'cellModel': 'HH_reduced',   'ynormRange': layer['2'],   'density': density[('A1','SOM')][1]}
```

```python
netParams.popParams['PV2'] =     {'cellType': 'PV',  'cellModel': 'HH_reduced',   'ynormRange': layer['2'],   'density': density[('A1','PV')][1]}
```

```python
netParams.popParams['VIP2'] =    {'cellType': 'VIP', 'cellModel': 'HH_reduced',   'ynormRange': layer['2'],   'density': density[('A1','VIP')][1]}

netParams.popParams['NGF2'] =    {'cellType': 'NGF', 'cellModel': 'HH_reduced',   'ynormRange': layer['2'],   'density': density[('A1','nonVIP')][1]}
```

e altri layers—-

### THALAMIC POPULATIONS (from prev model)

`thalDensity = density[('A1','PV')][2] * 1.25`

```python
netParams.popParams['TC'] =     {'cellType': 'TC',  'cellModel': 'HH_reduced',  'ynormRange': layer['thal'],   'density': 0.75*thalDensity}
netParams.popParams['TCM'] =    {'cellType': 'TC',  'cellModel': 'HH_reduced',  'ynormRange': layer['thal'],   'density': thalDensity}
netParams.popParams['HTC'] =    {'cellType': 'HTC', 'cellModel': 'HH_reduced',  'ynormRange': layer['thal'],   'density': 0.25*thalDensity}
netParams.popParams['IRE'] =    {'cellType': 'RE',  'cellModel': 'HH_reduced',  'ynormRange': layer['thal'],   'density': thalDensity}
netParams.popParams['IREM'] =   {'cellType': 'RE', 'cellModel': 'HH_reduced',   'ynormRange': layer['thal'],   'density': thalDensity}
netParams.popParams['TI'] =     {'cellType': 'TI',  'cellModel': 'HH_reduced',  'ynormRange': layer['thal'],   'density': 0.33 * thalDensity} ## Winer & Larue 1996; Huang et al 1999
netParams.popParams['TIM'] =    {'cellType': 'TI',  'cellModel': 'HH_reduced',  'ynormRange': layer['thal'],   'density': 0.33 * thalDensity} ## Winer & Larue 1996; Huang et al 1999
```

```python
if cfg.singleCellPops:
for pop in netParams.popParams.values(): pop['numCells'] = 1
```

- qui praticamente dà per scontato che `cfg.singleCellPops` is set to True ; quindi poi dice:
- per ogni popolazione in `netParams.popParams`, il valore `numCells` sarà 1
- infatti setting **`singleCellPops`** to **`True`** means that only one cell will be created for each population defined in the **`netParams.popParams`** dictionary, instead of the default behavior which creates a population of multiple cells with the specified **`size`** parameter. This is useful for simulating small networks with only a few cells or for testing and debugging individual cells.

## List of E and I pops to use later on

```python
Epops = ['IT2', 'IT3', 'ITP4', 'ITS4', 'IT5A', 'CT5A', 'IT5B', 'CT5B' , 'PT5B', 'IT6', 'CT6']  # all layers
```

```python
Ipops = ['NGF1',                            # L1
'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A
```

```python
'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
'PV6', 'SOM6', 'VIP6', 'NGF6']      # L6
```

---

### Synaptic mechanism parameters

#from M1 detailed netParams.py

```python
netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1NMDA': 15, 'tau2NMDA': 150, 'e': 0}

netParams.synMechParams['AMPA'] = {'mod':'MyExp2SynBB', 'tau1': 0.05, 'tau2': 5.3*cfg.AMPATau2Factor, 'e': 0}

netParams.synMechParams['GABAB'] = {'mod':'MyExp2SynBB', 'tau1': 3.5, 'tau2': 260.9, 'e': -93}

netParams.synMechParams['GABAA'] = {'mod':'MyExp2SynBB', 'tau1': 0.07, 'tau2': 18.2, 'e': -80}

netParams.synMechParams['GABAA_VIP'] = {'mod':'MyExp2SynBB', 'tau1': 0.3, 'tau2': 6.4, 'e': -80}  # Pi et al 2013

netParams.synMechParams['GABAASlow'] = {'mod': 'MyExp2SynBB','tau1': 2, 'tau2': 100, 'e': -80}

netParams.synMechParams['GABAASlowSlow'] = {'mod': 'MyExp2SynBB', 'tau1': 200, 'tau2': 400, 'e': -80}
```

- tau1 , tau2 = parameters describing the time constant of the decay of the postsynaptic conductance of the synaptic current.
- decay time constants of postsynaptic conductance = time constants that govern the decay of the conductance change induced by a presynaptic action potential → IN QUANTO TEMPO DECADE L’ACTION POTENTIAL

names of synaptic mechanisms for each cell type

`ESynMech = ['AMPA', 'NMDA']` -> excitatory cells

`SOMESynMech = ['GABAASlow','GABAB']` → synaptic mechanisms used for somatostatin-positive (SOM+) inhibitory cells.

`SOMISynMech = ['GABAASlow']` synaptic mechanisms that are typically used for somatostatin-negative (SOM-) inhibitory cells.

`PVSynMech = ['GABAA']` synaptic mechanisms that are typically used for parvalbumin-positive (PV+) inhibitory cells.
`VIPSynMech = ['GABAA_VIP']` synaptic mechanisms that are typically used for vasoactive intestinal peptide-positive (VIP+) inhibitory cells.

`NGFSynMech = ['GABAA', 'GABAB']` synaptic mechanisms that are typically used for neurogliaform cells.

---

### Local connectivity parameters

#load data from conn pre-processing file @irene the file that can’t be found on Spyder

```python
with open('conn/conn.pkl', 'rb') as fileObj: connData = pickle.load(fileObj)
pmat = connData['pmat']
lmat = connData['lmat']
wmat = connData['wmat']
bins = connData['bins']
connDataSource = connData['connDataSource']
```

- loads pre-processed connectivity data from the `conn.pkl` file, which is stored in the conn folder.
- the file contains:
    - 'pmat': a matrix that specifies the probability of connection between pairs of pre- and post-synaptic cells.
    - 'lmat': a matrix that specifies the Euclidean distance between pairs of pre- and post-synaptic cells.
    - 'wmat': a matrix that specifies the weight of the synaptic connection between pairs of pre- and post-synaptic cells.
    - 'bins': a list of tuples, where each tuple represents a layer and contains two floats that specify the upper and lower bounds of the layer in microns.
    - 'connDataSource': a string that specifies the source of the connectivity data.

`wmat = cfg.wmat` 

- this assigns the weight matrix for synaptic connections fra pre e post synaptic neurons in base al parameter: `cfg.wmat`

`layerGainLabels = ['1', '2', '3', '4', '5A', '5B', '6']`

- se ti ricordi questi sono i numeri assegnati a ogni layer che avevamo già stabilito sopra

---

### E → E

Come vedi sotto siamo in `Epops`, quindi tutte le pops di excitatory neurons.

```python
if cfg.addConn and cfg.EEGain > 0.0:
for pre in Epops:
for post in Epops:
for l in layerGainLabels:  # used to tune each layer group independently
if connDataSource['E->E/I'] in ['Allen_V1', 'Allen_custom']:
prob = '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post])
else:
prob = pmat[pre][post]
netParams.connParams['EE_'+pre+'*'+post+'*'+l] = {
'preConds': {'pop': pre},
'postConds': {'pop': post, 'ynorm': layer[l]},
'synMech': ESynMech,
'probability': prob,
'weight': wmat[pre][post] * cfg.EEGain * cfg.EELayerGain[l],
'synMechWeightFactor': cfg.synWeightFractionEE,
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 1,
'sec': 'dend_all'}
```

- qui attingiamo dalla connectivity data stored in **`pmat`**, **`lmat`**, and **`wmat`** to add connections between `Epops`.
- For each pair of pre- and post-synaptic populations, the connectivity probability **`pmat[pre][post]`** is multiplied by a layer-dependent factor that depends on the Euclidean distance **`lmat[pre][post]`** between the pre- and post-synaptic cells and a global gain factor **`cfg.EEGain`**. The layer-dependent factor is determined by the **`layerGainLabels`** list, which specifies the layer boundaries.
- The resulting probability is used to determine the presence or absence of a connection between the two populations, and if a connection is present, it is given a weight specified by **`wmat[pre][post] * cfg.EEGain * cfg.EELayerGain[l]`**. The weight is applied to both AMPA and NMDA receptors (**`ESynMech`**). The synapses are placed on dendritic compartments (**`sec = 'dend_all'`**), and their delay is determined by the distance between the pre- and post-synaptic cells and the conduction velocity of the axon (**`delay': 'defaultDelay+dist_3D/propVelocity'`**).

### **E → I**

```python
if cfg.addConn and cfg.EIGain > 0.0:
for pre in Epops:
for post in Ipops:
for postType in Itypes:
if postType in post: # only create rule if celltype matches pop
for l in layerGainLabels:  # used to tune each layer group independently
if connDataSource['E->E/I'] in ['Allen_V1', 'Allen_custom']:
prob = '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post])
else:
prob = pmat[pre][post]
```

```
                    if 'NGF' in post:
                        synWeightFactor = cfg.synWeightFractionENGF
                    else:
                        synWeightFactor = cfg.synWeightFractionEI
                    netParams.connParams['EI_'+pre+'_'+post+'_'+postType+'_'+l] = {
                        'preConds': {'pop': pre},
                        'postConds': {'pop': post, 'cellType': postType, 'ynorm': layer[l]},
                        'synMech': ESynMech,
                        'probability': prob,
                        'weight': wmat[pre][post] * cfg.EIGain * cfg.EICellTypeGain[postType] * cfg.EILayerGain[l],
                        'synMechWeightFactor': synWeightFactor,
                        'delay': 'defaultDelay+dist_3D/propVelocity',
                        'synsPerConn': 1,
                        'sec': 'proximal'}

```

- Uses same matrices matrices and parameters as the first block, but also includes the `Itypes` parameters to specify the different types of inhibitory neurons that the E neurons can connect to.

### I → E

```python
if cfg.addConn and cfg.IEGain > 0.0:
```

```
if connDataSource['I->E/I'] == 'Allen_custom':

    ESynMech = ['AMPA', 'NMDA']
    SOMESynMech = ['GABAASlow','GABAB']
    SOMISynMech = ['GABAASlow']
    PVSynMech = ['GABAA']
    VIPSynMech = ['GABAA_VIP']
    NGFSynMech = ['GABAA', 'GABAB']

```

```python
for pre in Ipops:
for preType in Itypes:
if preType in pre:  # only create rule if celltype matches pop
for post in Epops:
for l in layerGainLabels:  # used to tune each layer group independently
```

```python
                        prob = '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post])

                        if 'SOM' in pre:
                            synMech = SOMESynMech
                        elif 'PV' in pre:
                            synMech = PVSynMech
                        elif 'VIP' in pre:
                            synMech = VIPSynMech
                        elif 'NGF' in pre:
                            synMech = NGFSynMech

                        netParams.connParams['IE_'+pre+'_'+preType+'_'+post+'_'+l] = {
                            'preConds': {'pop': pre},
                            'postConds': {'pop': post, 'ynorm': layer[l]},
                            'synMech': synMech,
                            'probability': prob,
                            'weight': wmat[pre][post] * cfg.IEGain * cfg.IECellTypeGain[preType] * cfg.IELayerGain[l],
                            'synMechWeightFactor': cfg.synWeightFractionEI,
                            'delay': 'defaultDelay+dist_3D/propVelocity',
                            'synsPerConn': 1,
                            'sec': 'proximal'}

```

- code block creating inhibitory connections from interneurons to excitatory cells

### I → I

if cfg.addConn and cfg.IIGain > 0.0:

```python
if connDataSource['I->E/I'] == 'Allen_custom':

    for pre in Ipops:
        for post in Ipops:
            for l in layerGainLabels:

                prob = '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post])

                if 'SOM' in pre:
                    synMech = SOMISynMech
                elif 'PV' in pre:
                    synMech = PVSynMech
                elif 'VIP' in pre:
                    synMech = VIPSynMech
                elif 'NGF' in pre:
                    synMech = NGFSynMech

                netParams.connParams['II_'+pre+'_'+post+'_'+l] = {
                    'preConds': {'pop': pre},
                    'postConds': {'pop': post,  'ynorm': layer[l]},
                    'synMech': synMech,
                    'probability': prob,
                    'weight': wmat[pre][post] * cfg.IIGain * cfg.IILayerGain[l],
                    'synMechWeightFactor': cfg.synWeightFractionII,
                    'delay': 'defaultDelay+dist_3D/propVelocity',
                    'synsPerConn': 1,
                    'sec': 'proximal'}

```

- defines connections among diff pops of inhibitory neurons.
- . It first checks if the configuration parameter **`cfg.addConn`** is True and if the inhibitory gain parameter **`cfg.IIGain`** is greater than zero. If both conditions are satisfied, it proceeds to create the connections.
- The connections are created based on the connection data source specified in **`connDataSource`**, which is set to 'Allen_custom' in this case for I-to-E/I connections.
- For each pre-synaptic population **`pre`**, post-synaptic population **`post`**, and layer group **`l`**, the code block creates a connection with a probability defined by **`pmat[pre][post]`** and **`lmat[pre][post]`** and a weight defined by **`wmat[pre][post]`**. The weight is modulated by **`cfg.IIGain`** and **`cfg.IILayerGain[l]`**.
- inoltre specifies the synapse mechanism to be used in the connections based on the pre-synaptic population **`pre`**. If **`pre`** is one of several specific types of inhibitory cells (**`SOM`**, **`PV`**, **`VIP`**, or **`NGF`**), the synapse mechanism is set accordingly. The delay and number of synapses per connection are also specified.

---

# Thalamic connectivity parameters

### Intrathalamic

`TEpops = ['TC', 'TCM', 'HTC']
TIpops = ['IRE', 'IREM', 'TI', 'TIM']`

(exc and inh)

qui sotto aggiungiamo intrathalamic connections fra pre e post in queste due popolazioni:

```python
if cfg.addConn and cfg.addIntraThalamicConn:
    for pre in TEpops+TIpops:
        for post in TEpops+TIpops:
            if post in pmat[pre]:
                # for syns use ESynMech, SOMESynMech and SOMISynMech 
                if pre in TEpops:     # E->E/I
                    syn = ESynMech
                    synWeightFactor = cfg.synWeightFractionEE
                elif post in TEpops:  # I->E
                    syn = SOMESynMech
                    synWeightFactor = cfg.synWeightFractionIE
                else:                  # I->I
                    syn = SOMISynMech
                    synWeightFactor = [1.0]
                    
                netParams.connParams['ITh_'+pre+'_'+post] = { 
                    'preConds': {'pop': pre}, 
                    'postConds': {'pop': post},
                    'synMech': syn,
                    'probability': pmat[pre][post],
                    'weight': wmat[pre][post] * cfg.intraThalamicGain, 
                    'synMechWeightFactor': synWeightFactor,
                    'delay': 'defaultDelay+dist_3D/propVelocity',
                    'synsPerConn': 1,
                    'sec': 'soma'}
```

- if statement checks if intra-thalamic connections should be added and iterates over each pair of thalamic pops
- if a connection probability exists between the pre and post synaptic pops (defined in pmat) → a connection rule is created and added to netParams.
- The synapses used for each connection rule depend on the populations involved in the connection. If the pre-synaptic population is an excitatory thalamic population (**`TEpops`**), then the synapses used are **`ESynMech`**. If the post-synaptic population is an excitatory thalamic population, then the synapses used are **`SOMESynMech`**. Otherwise, the post-synaptic population is an inhibitory thalamic population, and the synapses used are **`SOMISynMech`**.

### Corticothalamic

```python
if cfg.addConn and cfg.addCorticoThalamicConn:
for pre in Epops:
for post in TEpops+TIpops:
if post in pmat[pre]:
netParams.connParams['CxTh_'+pre+'_'+post] = {
'preConds': {'pop': pre},
'postConds': {'pop': post},
'synMech': ESynMech,
'probability': pmat[pre][post],
'weight': wmat[pre][post] * cfg.corticoThalamicGain,
'synMechWeightFactor': cfg.synWeightFractionEE,
'delay': 'defaultDelay+dist_3D/propVelocity',
'synsPerConn': 1,
'sec': 'soma'}
```

- **`if post in pmat[pre]`** checks if the target post has a connection probability defined in the pmat matrix for the source pre population.
- here, the code is checking if a cortical population `pre` has a connection probability to a thalamic population `post`. 
If the ‘post’ population is not in the ‘pmat’ matrix population, NON VERRANNO CREATI I PARAMETRI.

---

### Thalamocortical

Qui è come sopra, ma al contrario: 

```python
if cfg.addConn and cfg.addThalamoCorticalConn:
    for pre in TEpops+TIpops:
        for post in Epops+Ipops:
            if post in pmat[pre]:
                # for syns use ESynMech, SOMESynMech and SOMISynMech 
                if pre in TEpops:     # E->E/I
                    syn = ESynMech
                    synWeightFactor = cfg.synWeightFractionEE
                elif post in Epops:  # I->E
                    syn = SOMESynMech
                    synWeightFactor = cfg.synWeightFractionIE
                else:                  # I->I
                    syn = SOMISynMech
                    synWeightFactor = [1.0]

                netParams.connParams['ThCx_'+pre+'_'+post] = { 
                    'preConds': {'pop': pre}, 
                    'postConds': {'pop': post},
                    'synMech': syn,
                    'probability': '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post]),
                    'weight': wmat[pre][post] * cfg.thalamoCorticalGain, 
                    'synMechWeightFactor': synWeightFactor,
                    'delay': 'defaultDelay+dist_3D/propVelocity',
                    'synsPerConn': 1,
                    'sec': 'soma'}
```

---

### Subcellular connectivity (synaptic distribution)

#Set target sections (somatodendritic distribution of synapses) 

**E → E2/3, 4** 

```python
if cfg.addSubConn:
netParams.subConnParams['E->E2,3,4'] = {
'preConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'postConds': {'pops': ['IT2', 'IT3', 'ITP4', 'ITS4']},
'sec': 'proximal',
'groupSynMechs': ESynMech,
'density': 'uniform'}
```

- the postsynaptic exc cells in questo caso sono in layer 2,3,4
- synapses are located in the proximal dendrites and soma
- density of synapses is uniform across cells
- `preConds` and `postConds` sono dizionari che ti dicono le condizioni che devono essere sodisfatte dai pre and post synaptic neurons in order for a connection to be formed between them.
- nota che sec, groupsynmechs e density sono uguali per pre and post

**E → E5, 6**

```python
netParams.subConnParams['E->E5,6'] = {
'preConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'postConds': {'pops': ['IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6']},
'sec': 'all',
'groupSynMechs': ESynMech,
'density': 'uniform'}
```

- differences with code block above: **`netParams.subConnParams['E->E2,3,4']`**, the **`sec`** parameter is set to **`'proximal'`**, which means that the connection is targeting the proximal section of the dendrites and the soma of the postsynaptic neurons (<200um).
- qui invece, **`netParams.subConnParams['E->E5,6']`**, the **`sec`** parameter is set to **`'all'`**, which means that the connection is targeting all sections of the dendrites and the soma of the postsynaptic neurons.

**E → I** 

```python
netParams.subConnParams['E->I'] = {
'preConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'postConds': {'cellType': ['PV','SOM','NGF', 'VIP']},
'sec': 'all',
'groupSynMechs': ESynMech,
'density': 'uniform'}
```

**NGF1 → E : apic_tuft**

Qui nello specifico stiamo stabilendo la connessione fra cellule NGF1 and **apical tuft dendrites of excitatory cells.**

```python
netParams.subConnParams['NGF1->E'] = {
    'preConds': {'pops': ['NGF1']},
    'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
    'sec': 'apic_tuft',
    'groupSynMechs': NGFSynMech,
    'density': 'uniform'}

```

- questa differenza è specificata in sec
- density uniforme vuol dire che, throughout the section, synapses are uniformly distributed

**NGF2,3,4 -> E2,3,4: apic_trunk**

```python
netParams.subConnParams['NGF2,3,4->E2,3,4'] = {
    'preConds': {'pops': ['NGF2', 'NGF3', 'NGF4']},
    'postConds': {'pops': ['IT2', 'IT3', 'ITP4', 'ITS4']},
    'sec': 'apic_trunk',
    'groupSynMechs': NGFSynMech,
    'density': 'uniform'}

```

**NGF2,3,4 -> E5,6: apic_uppertrunk**

```python
netParams.subConnParams['NGF2,3,4->E5,6'] = {
'preConds': {'pops': ['NGF2', 'NGF3', 'NGF4']},
'postConds': {'pops': ['IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6']},
'sec': 'apic_uppertrunk',
'groupSynMechs': NGFSynMech,
'density': 'uniform'}
```

**NGF5,6 -> E5,6: apic_lowerrunk**

```python
netParams.subConnParams['NGF5,6->E5,6'] = {
'preConds': {'pops': ['NGF5A', 'NGF5B', 'NGF6']},
'postConds': {'pops': ['IT5A', 'CT5A', 'IT5B', 'PT5B', 'CT5B', 'IT6', 'CT6']},
'sec': 'apic_lowertrunk',
'groupSynMechs': NGFSynMech,
'density': 'uniform'}
```


**SOM -> E: all_dend (not close to soma, altrimenti scriveremmo proximal)**

```python
netParams.subConnParams['SOM->E'] = {
'preConds': {'cellType': ['SOM']},
'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'sec': 'dend_all',
'groupSynMechs': SOMESynMech,
'density': 'uniform'}
```

- connections between soma targeting inhibitory interneurons (SOM) and excitatory cells

**PV -> E: proximal**

```python
netParams.subConnParams['PV->E'] = {
    'preConds': {'cellType': ['PV']},
    'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
    'sec': 'proximal',
    'groupSynMechs': PVSynMech,
    'density': 'uniform'}

```

- between parvalbumin-expressing interneurons and exc neurons

**TC -> E: proximal**

```python
netParams.subConnParams['TC->E'] = {
'preConds': {'cellType': ['TC', 'HTC']},
'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'sec': 'proximal',
'groupSynMechs': ESynMech,
'density': 'uniform'}
```

- nello specifico, presynaptic → thalamocortical and hyperpolarization-activated nucleotide-gated cells (HTC), che sonon un sottotipo di thalamocortical cells.

**TCM -> E: apical**

```python
netParams.subConnParams['TCM->E'] = {
    'preConds': {'cellType': ['TCM']},
    'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
    'sec': 'apic',
    'groupSynMechs': ESynMech,
    'density': 'uniform'}

```

- TCM stands for "thalamocortical (TC) matrix cells". These are a subtype of TC cells, role in sensory processing and perception.

---

### Background inputs

```python
if cfg.addBkgConn:
# add bkg sources for E and I cells
netParams.stimSourceParams['excBkg'] = {'type': 'NetStim', 'start': cfg.startBkg, 'rate': cfg.rateBkg['exc'], 'noise': cfg.noiseBkg, 'number': 1e9}
netParams.stimSourceParams['inhBkg'] = {'type': 'NetStim', 'start': cfg.startBkg, 'rate': cfg.rateBkg['inh'], 'noise': cfg.noiseBkg, 'number': 1e9}
```

- **`NetStim`** is a type of **`stimSource`** in the NEURON simulation environment. It represents a stochastic input source that generates spikes according to a Poisson process.
- each stimSourceParams entry corresponds to a Netstim object → generates random spike trains with the specified rate and noise parameters.
- **`start`** parameter specifies the time when the stimulation starts (in ms)
- **`number`** parameter is the maximum number of spikes that can be generated by the **`NetStim`** object.  Visto che è così enorme il numero, sono praticamente spikes infinite

```python
if cfg.cochlearThalInput:
from input import cochlearInputSpikes
numCochlearCells = cfg.cochlearThalInput['numCells']
cochlearSpkTimes = cochlearInputSpikes(numCells = numCochlearCells,
duration = cfg.duration,
freqRange = cfg.cochlearThalInput['freqRange'],
toneFreq=cfg.cochlearThalInput['toneFreq'],
loudnessDBs=cfg.cochlearThalInput['loudnessDBs'])
```

- qui si basa su config per cochlear thalamic input → generates a set of spike times for cochlear input cells, which will then be used to stimulate the thalamic network.

```python
netParams.popParams['cochlea'] = {'cellModel': 'VecStim', 'numCells': numCochlearCells, 'spkTimes': cochlearSpkTimes, 'ynormRange': layer['cochlear']}
```

- these are the cells that will receive the cochlear stimulation
- **`cellModel`** 'VecStim' means they do not have any cell-specific dynamic, but instead receive spike times directly as input

```python
if cfg.ICThalInput:
    # load file with IC output rates
    from [scipy.io](http://scipy.io/) import loadmat
    import numpy as np    

    data = loadmat(cfg.ICThalInput['file'])
    fs = data['RsFs'][0][0]
    ICrates = data['BE_sout_population'].tolist()
    ICtimes = list(np.arange(0, cfg.duration, 1000./fs))  # list with times to set each time-dep rate

    ICrates = ICrates * 4 # 200 cells

    numCells = len(ICrates)

```

- Here, the code checks if **`cfg.ICThalInput`** is true, and if so, it loads a mat file that contains the output rates of the Inferior Colliculus (IC) neurons, which is a midbrain structure involved in auditory processing.
- It then creates a list of times to set each time-dependent rate, and multiplies the **`ICrates`** by 4 to simulate 200 cells.
- Finally, the code sets **`numCells`** as the length of **`ICrates`**.

#Option 1: create population of DynamicNetStims with time-varying rates
#`netParams.popParams['IC'] = {'cellModel': 'DynamicNetStim', 'numCells': numCells, 'ynormRange': layer['cochlear'],
    #    'dynamicRates': {'rates': ICrates, 'times': ICtimes}}`

#Option 2:

```python
   
    from input import inh_poisson_generator

    maxLen = min(len(ICrates[0]), len(ICtimes))
    spkTimes = [[x+cfg.ICThalInput['startTime'] for x in inh_poisson_generator(ICrates[i][:maxLen], ICtimes[:maxLen], cfg.duration, cfg.ICThalInput['seed']+i)] for i in range(len(ICrates))]
    netParams.popParams['IC'] = {'cellModel': 'VecStim', 'numCells': numCells, 'ynormRange': layer['cochlear'],
        'spkTimes': spkTimes}

```

- `netParams.popParams['IC']` is a group of inhibitory cells receiving input from the inferior colliculus (IC) via a Poisson spike generator.
- The input firing rates are read from a file and the spike times are generated using the **`inh_poisson_generator`** function from the **`input`** module.

**#excBkg/I -> thalamus + cortex**

```python
with open('cells/bkgWeightPops.json', 'r') as f:
        weightBkg = json.load(f)
    pops = list(cfg.allpops)
    pops.remove('IC')

    for pop in ['TC', 'TCM', 'HTC']:
        weightBkg[pop] *= cfg.EbkgThalamicGain 

    for pop in ['IRE', 'IREM', 'TI', 'TIM']:
        weightBkg[pop] *= cfg.IbkgThalamicGain 

    for pop in pops:
        netParams.stimTargetParams['excBkg->'+pop] =  {
            'source': 'excBkg', 
            'conds': {'pop': pop},
            'sec': 'apic', 
            'loc': 0.5,
            'synMech': ESynMech,
            'weight': weightBkg[pop],
            'synMechWeightFactor': cfg.synWeightFractionEE,
            'delay': cfg.delayBkg}

        netParams.stimTargetParams['inhBkg->'+pop] =  {
            'source': 'inhBkg', 
            'conds': {'pop': pop},
            'sec': 'proximal',
            'loc': 0.5,
            'synMech': 'GABAA',
            'weight': weightBkg[pop],
            'delay': cfg.delayBkg}
```

- defines syn connections and bkg stimulation to all cell pops except inhibitory cells.
- The synaptic weight and delay values for these connections are determined by the values in the **`weightBkg`** dictionary, which is read from the **`cells/bkgWeightPops.json`** file. The **`weightBkg`** dictionary has keys corresponding to the cell populations and values that represent the synaptic weight values for each population.
- The **`excBkg->pop`** connections are defined using the **`stimTargetParams`** parameter dictionary. These connections originate from the **`excBkg`** source and have a condition **`{'pop': pop}`** that targets a specific population (**`pop`**). These connections have a synaptic mechanism of **`ESynMech`** (an excitatory AMPA receptor), a weight value that is taken from the **`weightBkg`** dictionary, and a delay value of **`cfg.delayBkg`**.
- the **`inhBkg->pop`** connections are defined using **`stimTargetParams`**. These connections originate from the **`inhBkg`** source and target a specific population (**`pop`**). These connections have a synaptic mechanism of **`GABAA`**, a weight value that is taken from the **`weightBkg`** dictionary, and a delay value of **`cfg.delayBkg`**.

**#cochlea -> thal**

```python
if cfg.cochlearThalInput:
    netParams.connParams['cochlea->ThalE'] = {
        'preConds': {'pop': 'cochlea'},
        'postConds': {'cellType': ['TC', 'HTC']},
        'sec': 'soma',
        'loc': 0.5,
        'synMech': ESynMech,
        'probability': cfg.probInput['ThalE'],
        'weight': cfg.weightInput['ThalE'],
        'synMechWeightFactor': cfg.synWeightFractionEE,
        'delay': cfg.delayBkg}

    netParams.connParams['cochlea->ThalI'] = {
        'preConds': {'pop': 'cochlea'},
        'postConds': {'cellType': ['RE']},
        'sec': 'soma',
        'loc': 0.5,
        'synMech': ESynMech,
        'probability': cfg.probInput['ThalI'],
        'weight': cfg.weightInput['ThalI'],
        'synMechWeightFactor': cfg.synWeightFractionEI,
        'delay': cfg.delayBkg}

```

- defining conections between cochlea and thalamus in the network
- **first connection rule**: 
**`cochlea->ThalE`**, defines the connection between the **`cochlea`** population (representing the input from the auditory nerve) and the excitatory thalamic cell types **`TC`** and **`HTC`**.
 The connection is made on the **`soma`** compartment at the **`0.5`** location. 
The **`probability`** parameter determines the probability of a connection being made between a pre-synaptic **`cochlea`** cell and a post-synaptic **`TC`** or **`HTC`** cell.
 The **`weight`** parameter determines the strength of the synaptic connection. 
The **`synMechWeightFactor`** parameter determines the fraction of the **`weight`** parameter that is assigned to the specific synaptic mechanism (**`ESynMech`**) used for this connection. 
The **`delay`** parameter determines the delay of the synaptic connection.
- **second connection rule:** 
**`cochlea->ThalI`**, defines the connection between the **`cochlea`** population and the inhibitory thalamic cell type **`RE`**. The parameters have similar meanings as in the first connection rule, but some of the values may be different

**#cochlea/IC -> thal**

```python
if cfg.ICThalInput:
    netParams.connParams['IC->ThalE'] = {
        'preConds': {'pop': 'IC'},
        'postConds': {'cellType': ['TC', 'HTC']},
        'sec': 'soma',
        'loc': 0.5,
        'synMech': ESynMech,
        'probability': cfg.ICThalInput['probE'],
        'weight': cfg.ICThalInput['weightE'],
        'synMechWeightFactor': cfg.synWeightFractionEE,
        'delay': cfg.delayBkg}

    netParams.connParams['IC->ThalI'] = {
        'preConds': {'pop': 'IC'},
        'postConds': {'cellType': ['RE', 'TI']},
        'sec': 'soma',
        'loc': 0.5,
        'synMech': 'GABAA',
        'probability': cfg.ICThalInput['probI'],
        'weight': cfg.ICThalInput['weightI'],
        'delay': cfg.delayBkg}
```

- **`netParams.connParams['IC->ThalE']`** creates connections from IC cells to excitatory thalamic cells (TC and HTC), with the **`preConds`** specifying the population of IC cells as **`'pop': 'IC'`** and the **`postConds`** specifying the populations of thalamic cells as **`'cellType': ['TC', 'HTC']`**.
- The **`probability`** and **`weight`** parameters determine the probability and strength of the synaptic connections, respectively.
- **`synMechWeightFactor`** determines the fraction of the total conductance that comes from this synapse's conductance mechanism.
- **`netParams.connParams['IC->ThalI']`** creates connections from IC cells to inhibitory thalamic cells (RE and TI), with similar parameters as the excitatory connections, but with the **`synMech`** set to **`'GABAA'`** to indicate the GABAergic inhibitory synapse type.

---

### NetStim inputs (to simulate short external stimuli; not bkg)

```python
if cfg.addNetStim:
for key in [k for k in dir(cfg) if k.startswith('NetStim')]:
params = getattr(cfg, key, None)
[pop, ynorm, sec, loc, synMech, synMechWeightFactor, start, interval, noise, number, weight, delay] = \
[params[s] for s in ['pop', 'ynorm', 'sec', 'loc', 'synMech', 'synMechWeightFactor', 'start', 'interval', 'noise', 'number', 'weight', 'delay']]
```

- if boolean true, code loops through all attributes of `cfg` that start with string `NetStim` and puts them in a dictionary called `params`.
- la linea sotto is basically unpacking the dict to obtain variables for **`pop`**, **`ynorm`**, **`sec`**, **`loc`**, **`synMech`**, **`synMechWeightFactor`**, **`start`**, **`interval`**, **`noise`**, **`number`**, **`weight`**, and **`delay`**. These variables are used to define the properties of a network stimulation to be added to the simulation.

### add stim source

---

```python
netParams.stimSourceParams[key] = {'type': 'NetStim', 'start': start, 'interval': interval, 'noise': noise, 'number': number}
        
        if not isinstance(pop, list):
            pop = [pop]

        for eachPop in pop:
            # connect stim source to target 
            print(key, eachPop)
            netParams.stimTargetParams[key+'_'+eachPop] =  {
                'source': key, 
                'conds': {'pop': eachPop, 'ynorm': ynorm},
                'sec': sec, 
                'loc': loc,
                'synMech': synMech,
                'weight': weight,
                'synMechWeightFactor': synMechWeightFactor,
                'delay': delay}
```

- The **`stimSourceParams`** dictionary specifies the parameters of the NetStim source, including **`start`** (start time of the first spike), **`interval`** (mean time between spikes), **`noise`** (amount of noise to add to the spike intervals), and **`number`** (number of spikes to generate).
- The code checks whether the **`pop`** parameter is a list, and if not, converts it to a list. The **`pop`** parameter specifies the populations to which the NetStim source will be connected.
- For each population specified in **`pop`**, the code creates a **`stimTargetParams`** dictionary that specifies the parameters of the synapse between the NetStim source and the target population. The **`conds`** parameter specifies the conditions that the target cells must meet to receive stimulation. The **`sec`** and **`loc`** parameters specify the location of the synapse on the target cells. The **`synMech`**, **`weight`**, **`synMechWeightFactor`**, and **`delay`** parameters specify the properties of the synapse.

