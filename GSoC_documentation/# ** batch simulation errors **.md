# batch simulation errors

- before running: substitute lines in [init.py](http://init.py) w/: 

*# read cfg and netParams from command line arguments if available; otherwise use default*

`simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='tut8_cfg.py', netParamsDefault='tut8_netParams.py')`

*# Create network and run `simulation*sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)`

If not working, substitute  `simulationsim.creatSimulateAnalzye` to `sim.creatSimulateAnalzye`

- make sure 'type' is set to mpi_bulletin and not mpi:

      b.batchLabel = 'tauWeight'
        b.saveFolder = 'ca3attempt_data'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                                'script': 'init.py',
                                'skip': True}
