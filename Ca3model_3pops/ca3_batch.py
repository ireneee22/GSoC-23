from netpyne import specs
from netpyne.batch import Batch
import os 

# Specify the folder path
ca3_data_path = ('/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/ca3_data')

os.makedirs('ca3_data', exist_ok = True)

def batchWeight():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['connWeight'] = [0.4e-3, 0.9e-3, 1.4e-3]
        params['delay'] = [2, 4, 6]
        params['loc'] = [0.25, 0.5, 0.75]

        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/cfg.py', netParamsFile='/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/netParams.py')

        
        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'batchWeight'
        b.saveFolder = '/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/ca3_data/'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                                'script': '/Users/irenebernardi/Desktop/GSoC_files/netpyne/examples/ca3model_3pops/init.py',
                                'skip': True}

        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        batchWeight()
