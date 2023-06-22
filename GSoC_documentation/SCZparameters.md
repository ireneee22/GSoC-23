# Relevant parameters in SCZ 

We will focus on PV, SOM, GAT1, and NMDA.

## **PV (Parvalbumin):**

 - Parvalbumin-expressing interneurons are inhibitory neurons. 
 - Play a role in regulating brain excitatory activity
 - fast spikining, contribute to gamma activity

   *In A1 netParams:*

   **Cell parameters** 
  
  `Itypes = ['PV', 'SOM', 'VIP', 'NGF']`
  
   **Load cell rules previously saved using netpyne format**

  ```cellParamLabels = ['IT2_reduced', 'IT3_reduced', 'ITP4_reduced', 'ITS4_reduced',
     'IT5A_reduced', 'CT5A_reduced', 'IT5B_reduced',
     'PT5B_reduced', 'CT5B_reduced', 'IT6_reduced', 'CT6_reduced',
     'PV_reduced', 'SOM_reduced', 'VIP_reduced', 'NGF_reduced',
     'RE_reduced', 'TC_reduced', 'HTC_reduced', 'TI_reduced']
      ```

   **Population params, layer 2**

  ```netParams.popParams['PV2'] =     {'cellType': 'PV',  'cellModel': 'HH_reduced',   'ynormRange': layer['2'],   'density':              density[('A1','PV')][1]}
```

   **List of E and I pops to use later** 
   
  ```Ipops = ['NGF1',                            # L1
  'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
  'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
  'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
  'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A
  'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
  'PV6', 'SOM6', 'VIP6', 'NGF6']      # L6

  PVSynMech = ['GABAA'] # synaptic mechanisms that are typically used for parvalbumin-positive (PV+) inhibitory cells.

```


   **I -> E** 

```if cfg.addConn and cfg.IEGain > 0.0:
   if connDataSource['I->E/I'] == 'Allen_custom':

    ESynMech = ['AMPA', 'NMDA']
    SOMESynMech = ['GABAASlow','GABAB']
    SOMISynMech = ['GABAASlow']
    PVSynMech = ['GABAA']
    VIPSynMech = ['GABAA_VIP']
    NGFSynMech = ['GABAA', 'GABAB']

for pre in Ipops:
for preType in Itypes:
if preType in pre:  # only create rule if celltype matches pop
for post in Epops:
for l in layerGainLabels:  # used to tune each layer group independently
                        prob = '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post])

                        if 'SOM' in pre:
                            synMech = SOMESynMech
                        elif 'PV' in pre:
                            synMech = PVSynMech
                        elif 'VIP' in pre:
                            synMech = VIPSynMech
                        elif 'NGF' in pre:
                            synMech = NGFSynMech
```


   **PV -> E: proximal**

```netParams.subConnParams['PV->E'] = {
    'preConds': {'cellType': ['PV']},
    'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
    'sec': 'proximal',
    'groupSynMechs': PVSynMech,
    'density': 'uniform'}
 ```


   *In A1 cfg:*

  **Recording**

 ``` cfg.allpops = ['NGF1', 'IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2', 'IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3', 'ITP4', 'ITS4', 'SOM4', 'PV4', 'VIP4', 'NGF4', 'IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A', 'IT5B', 'PT5B', 'CT5B', 'SOM5B', 'PV5B', 'VIP5B', 'NGF5B', 'IT6', 'CT6', 'SOM6', 'PV6', 'VIP6', 'NGF6', 'TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']

cfg.allCorticalPops = ['NGF1', 'IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2', 'IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3’, 'ITP4', 'ITS4', 'SOM4', 'PV4', 'VIP4', 'NGF4', 'IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A', 'IT5B', 'PT5B', 'CT5B',  'SOM5B', 'PV5B', 'VIP5B', 'NGF5B', 'IT6', 'CT6', 'SOM6', 'PV6', 'VIP6', 'NGF6','TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']
```


`alltypes = ['NGF1', 'IT2', 'PV2', 'SOM2', 'VIP2', 'ITS4', 'PT5B', 'TC', 'HTC', 'IRE', 'TI']`


  **E->I layer gain**

`cfg.EICellTypeGain= {'PV': 1.0, 'SOM': 1.0, 'VIP': 1.0, 'NGF': 1.0}`

`cfg.IECellTypeGain= {'PV': 1.0, 'SOM': 1.0, 'VIP': 1.0, 'NGF': 1.0}`



## **SOM (Somatostatin):**
 - Somatostatin-expressing interneurons are inhibitory neurons.
 - Regulate network activity, shape synaptic integration, control plasticity.


   *In A1 netParams:*
   
   **Cell parameters**

   `Itypes = ['PV', 'SOM', 'VIP', 'NGF']`

   **Load cell rules previously saved using netpyne format**

      ```cellParamLabels = ['IT2_reduced', 'IT3_reduced', 'ITP4_reduced', 'ITS4_reduced',
         'IT5A_reduced', 'CT5A_reduced', 'IT5B_reduced','PT5B_reduced', 'CT5B_reduced', 'IT6_reduced', 'CT6_reduced',
         'PV_reduced', 'SOM_reduced', 'VIP_reduced', 'NGF_reduced','RE_reduced', 'TC_reduced', 'HTC_reduced', 'TI_reduced']
       ```
   
   **population parameters (Layer 2)**
  
  `netParams.popParams['SOM2'] =    {'cellType': 'SOM', 'cellModel': 'HH_reduced',   'ynormRange': layer['2'],   'density': density[('A1','SOM')][1]}`
  
   **List of I and E Pops to use later on**

    ```Ipops = ['NGF1',                            # L1
       'PV2', 'SOM2', 'VIP2', 'NGF2',      # L2
       'PV3', 'SOM3', 'VIP3', 'NGF3',      # L3
       'PV4', 'SOM4', 'VIP4', 'NGF4',      # L4
       'PV5A', 'SOM5A', 'VIP5A', 'NGF5A',  # L5A
       'PV5B', 'SOM5B', 'VIP5B', 'NGF5B',  # L5B
       'PV6', 'SOM6', 'VIP6', 'NGF6']      # L6
       ```

   **Synaptic mechanisms parameters**

    `SOMESynMech = ['GABAASlow','GABAB'] # synaptic mechanisms used for somatostatin-positive (SOM+) inhibitory cells.`

    `SOMISynMech = ['GABAASlow'] #synaptic mechanisms that are typically used for somatostatin-negative (SOM-) inhibitory cells.`


   **I -> E**
   
   ```if cfg.addConn and cfg.IEGain > 0.0:
   if connDataSource['I->E/I'] == 'Allen_custom':

    ESynMech = ['AMPA', 'NMDA']
    SOMESynMech = ['GABAASlow','GABAB']
    SOMISynMech = ['GABAASlow']
    PVSynMech = ['GABAA']
    VIPSynMech = ['GABAA_VIP']
    NGFSynMech = ['GABAA', 'GABAB']

    prob = '%f * exp(-dist_2D/%f)' % (pmat[pre][post], lmat[pre][post])

                        if 'SOM' in pre:
                            synMech = SOMESynMech
                        elif 'PV' in pre:
                            synMech = PVSynMech
                        elif 'VIP' in pre:
                            synMech = VIPSynMech
                        elif 'NGF' in pre:
                            synMech = NGFSynMech
```



**I->I**

```if connDataSource['I->E/I'] == 'Allen_custom':

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
```




**Thalamic connectivity params**

```if cfg.addConn and cfg.addIntraThalamicConn:
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
```


**Thalamocortical**

```if cfg.addConn and cfg.addThalamoCorticalConn:
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
```


**Subcellular connectivity**

**E->I**
 
 ```netParams.subConnParams['E->I'] = {
'preConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'postConds': {'cellType': ['PV','SOM','NGF', 'VIP']},
'sec': 'all',
'groupSynMechs': ESynMech,
'density': 'uniform'}
```

**SOM -> E: all_dend**

 ```netParams.subConnParams['SOM->E'] = {
'preConds': {'cellType': ['SOM']},
'postConds': {'cellType': ['IT', 'ITS4', 'PT', 'CT']},
'sec': 'dend_all',
'groupSynMechs': SOMESynMech,
'density': 'uniform'}
```

  
  *In A1 cfg:*

**Recording ** (all cells being recorded)

```cfg.allpops = ['NGF1', 'IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2', 'IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3', 'ITP4', 'ITS4', 'SOM4', 'PV4', 'VIP4', 'NGF4', 'IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A', 'IT5B', 'PT5B', 'CT5B', 'SOM5B', 'PV5B', 'VIP5B', 'NGF5B', 'IT6', 'CT6', 'SOM6', 'PV6', 'VIP6', 'NGF6', 'TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']```


```cfg.allCorticalPops = ['NGF1', 'IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2', 'IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3’, 'ITP4', 'ITS4', 'SOM4', 'PV4', 'VIP4', 'NGF4', 'IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A', 'IT5B', 'PT5B', 'CT5B',  'SOM5B', 'PV5B', 'VIP5B', 'NGF5B', 'IT6', 'CT6', 'SOM6', 'PV6', 'VIP6', 'NGF6','TC', 'TCM', 'HTC', 'IRE', 'IREM', 'TI', 'TIM', 'IC']```

```alltypes = ['NGF1', 'IT2', 'PV2', 'SOM2', 'VIP2', 'ITS4', 'PT5B', 'TC', 'HTC', 'IRE', 'TI']```

**Synapses**

```cfg.synWeightFractionSOME = [0.9, 0.1] # SOM -> E GABAASlow to GABAB ratio```

**Connectivity**

```cfg.synWeightFractionIE = [0.9, 0.1] # SOM -> E GABAASlow to GABAB ratio```

```cfg.synWeightFractionII = [0.9, 0.1] # SOM -> E GABAASlow to GABAB ratio```

**Layer gain**

```cfg.EICellTypeGain= {'PV': 1.0, 'SOM': 1.0, 'VIP': 1.0, 'NGF': 1.0}```

```cfg.IECellTypeGain= {'PV': 1.0, 'SOM': 1.0, 'VIP': 1.0, 'NGF': 1.0}```


## **GAT1:**
  - regulates GABA reuptake, terminates GABAergic neurotransmissioncellular space. 
  - used to simulate adequate level of inhibitory neurotransmission/GABA dynamics.

   
   *In A1 netParams:*
   not specified, all GABAergic
   
   *In A1 cfg:*
   not specified, all GABAergic

## **NMDA**
 - ionotropic glutamate receptors, involved in LTP and LTD-> used to reflect synaptic plasticity 


 *In A1 netParams:*

  -**Synaptic mechanisms parameters**

    `netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1NMDA': 15, 'tau2NMDA': 150, 'e': 0}`

   *In A1 cfg:*

   - **Synaptic weight** (measure of effectiveness of signal transmission between two neurons)
   
    `cfg.synWeightFractionEE = [0.5, 0.5] # E->E AMPA to NMDA ratio`

    `cfg.synWeightFractionEI = [0.5, 0.5] # E->I AMPA to NMDA ratio`

    `cfg.synWeightFractionENGF = [0.834, 0.166] # NGF AMPA (exc neurogliaform) to NMDA ratio`

   - **Connectivity** (Synaptic weight is about specific syn params, connectivity concerns relative proportions of syn weights for diff types of connections in network)

    `cfg.synWeightFractionEE = [0.5, 0.5] # E->E AMPA to NMDA ratio` (ratio of AMPA to NMDA receptor weights for excitatory to excitatory synapses in the network)

    `cfg.synWeightFractionEI = [0.5, 0.5] # E->I AMPA to NMDA ratio`

     `cfg.synWeightFractionEE = [0.5, 0.5] # E->E AMPA to NMDA ratio`
  
     `cfg.synWeightFractionEI = [0.5, 0.5] # E->I AMPA to NMDA ratio`

     `cfg.synWeightFractionENGF = [0.834, 0.166] # NGF AMPA to NMDA ratio`


