from netpyne import specs

cfg = specs.SimConfig()

cfg.duration = 750
cfg.dt = 0.1
cfg.hparams = {'v_init': -65.0}
cfg.verbose = False
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStim = False
cfg.recordStep = 0.1            # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = '00'         # Set file output name
cfg.savePickle = False        # Save params, network and sim output to pickle file
cfg.saveDat = False
cfg.printRunTime = 0.1 
cfg.recordLFP = [[50, 50, 50]]

'''cfg.connWeight = {}
cfg.connWeight['PYR->BC_NMDA'] = 0.4e-3
cfg.connWeight['PYR->OLM_NMDA'] = 1.2e-3
cfg.connWeight['PYR->PYR_NMDA'] = 0.2e-3'''

cfg.connWeight = []
cfg.delay = []
cfg.loc = []

cfg.analysis['plotRaster'] = {'saveFig': True}
cfg.analysis['plotTraces'] = {'include': [0, 1, 800, 801, 1000, 1001], 'saveFig': True}  # Plot recorded traces for this list of cells
cfg.analysis['plotLFPTimeSeries'] = {'showFig': True, 'saveFig': True} 
cfg.printPopAvgRates = True 
#cfg.analysis['plotShape'] = {'includePre': ['all'],'includePost': [0,800,1000],'cvar':'numSyns','dist':0.7, 'saveFig': True}
