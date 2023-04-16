#https://medium.com/@gili.karni/simulating-biological-neural-networks-with-netpyne-d1744c1f4a02
from netpyne import specs, sim
import matplotlib.pyplot as plt
#pylab is specific to docker
netParams = specs.NetParams()
simConfig = specs.SimConfig()
#no display environment variable -> fix?

##set network parameters##
#population parameters-> qui stai creando la popolazione
netParams.popParams ['population1']={'numCells':200, 'cellType':'PYR', 'cellModel': 'HH'} #Hodgkin-Huxley model, native to NetPyNE

#now modify cells at cellular level 
# First, we create a dict of cell rules. The conds refer to the cell's conditions
# and the secs refers to its sections
cellRule={'conds':{'cellModel':'HH', 'cellType': 'PYR'},  'secs': {}}
cellRule['secs']['soma']={'geom': {}, 'mechs': {}}

#soma's geometry
cellRule['secs']['soma']['geom']={'diam': 18.8, 'L': 18.8, 'Ra': 123.0}
# The soma's hh mechanism
cellRule['secs']['soma']['mechs']['hh']={'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}
# the initial cell's electric potential
cellRule['secs']['soma']['vinit']=-71

netParams.cellParams['PYR']=cellRule  # add rule dictionary to the cell params

#move to biophysical level other than cellular/morphological levels
# Synaptic mechanism parameters

# Exp2Syn is a two state kinetic scheme synapse where
# the rise time is set by tau1 and the decay time by tau2.
# the reversal potential is e.

netParams.synMechParams['AMPA']={
    'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}
netParams.synMechParams['NMDA']={
    'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}
netParams.synMechParams['GABA']={
    'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}

#we have AMPA, NMDA and GABA
# AMPA synapses
netParams.connParams['population1->population1_AMPA']={
    'preConds': {'pop': 'population1'},
    'postConds': {'pop': 'population1'},
    'weight': 0.1,
    'delay': '0.2+normal(13.0,1.4)', # delay min=0.2, mean=13.0, var = 1.4
    'synMech': 'AMPA'}

# NMDA synapses
netParams.connParams['population1->population1_NMDA']={
    'preConds': {'pop': 'population1'},
    'postConds': {'pop': 'population1'},
    'weight': 0.7,
    'delay': '0.2+normal(13.0,1.4)',  # delay min=0.2, mean=13.0, var = 1.4
    'synMech': 'NMDA'}

# GABA synapses
netParams.connParams['population1->population1_GABA']=\
    {'preConds': {'pop': 'population1'},
    'postConds': {'pop': 'population1'},
    'weight': 0.005,
    'delay': 5,
    'synMech': 'GABA'}

#an external stimulus is introduced to excite the network
#stimulus starts after 1 ms and has 30Hz electric current

# Stimulation parameters
netParams.stimSourceParams['background']={'type': 'NetStim', # network stimuli
                                          'rate': 30, # of 30 hz
                                          'noise': 0.5, 'start': 1}

netParams.stimTargetParams['background->population1']={'source': 'background',
                                           'conds': {'pop': 'population1'},
                                           'weight': 0.1,
                                           'delay': 'uniform(1,2)'}


# Simulation parameters
simConfig.duration = .5*1e3 # Duration of the simulation, in ms
simConfig.dt = 0.025 # Internal integration timestep to use
simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for
  #randomizers (connectivity, input stimulation and cell locations)
simConfig.verbose = False  # show detailed messages
simConfig.hParams = {'v_init': -75}

# Recording
simConfig.recordCells = []  # which cells to record from
simConfig.recordTraces = {'Vsoma':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = 0.1 # Step size in ms to save data

## Run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)
sim.runSim()                          # run parallel Neuron simulation
sim.gatherData()                      # gather spiking data and cell info from each node
#print raster
sim.analysis.plotRaster(syncLines=True)
#to save figures simConfig.analysis['plotRaster'] = {'saveFig': 'Raster.png'}
plt.savefig('Raster.png')
#print spike hist
sim.analysis.plotSpikeHist(include=['population1'])
#to save figures simConfig.analysis['plotSpikeHist'] = {'saveFig': 'SpikeHist.png'}
plt.savefig ('SpikeHist.png')


