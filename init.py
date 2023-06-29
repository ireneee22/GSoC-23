"""
init.py

Starting script to run NetPyNE-based CA3 model.

from netpyne import sim

#cfg, netParams = sim.loadFromIndexFile('index.npjson')
#sim.createSimulateAnalyze(netParams = netParams, cfg = cfg)

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/cfg.py', netParamsDefault='/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/netParams.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams='/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/netParams.py', simConfig='/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/cfg.py')

"""

from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)
