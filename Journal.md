
# Progress Journal 


**Week 1** 

- *May 29th - 31st*
  - Documented the structure of A1 [cfg.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/cfg.py) [(here)](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/A1%20'cfg.py'%20description.md), A1 [netParams.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/netParams.py) [(here)](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/A1%20'netParams.py'%20description.md) 
and A1 [batch.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/batch.py) [(here)](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/A1%20'batch.py'%20description.md).
  - First official meeting to establish next steps : running a scaled batch script, setting up virtual machine on Google Cloud and running the batch script on the VM.

- *June 1st, 2nd*
	 - ran multicore sim of [tutorial 8](http://www.netpyne.org/tutorial.html#tutorial-8-running-batch-simulations) batch.py on terminal 
   - created 3x3 batch script for CA3 model, see [here](https://github.com/ireneee22/GSoC-23/blob/main/CA3batch.py)
   - ran multicore sim of 3x3 batch.py of CA3 model on terminal, issues documented [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/multicore%20simulation%20errors.md) and [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/batch%20simulation%20errors.md)
   - Set up UBUNTU Virtual Machine on Google Cloud and downloaded NEURON and NetPyNE related packages, MPI, etc. 

**Week 2**

- *June 5th - 7th*
  - issues with SSH keypair on VM   
  - meeting on useful LINUX commands, VM goals for the next week, SSH keypair issues

- *June 8th, 9th*
	- figured out SSH keypair on VM, see [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/Issues%20generating%20SSH%20keypair%20for%20Google%20Cloud%20VM.md)


**Week 3**

- *June 12th - 14th*
  - ran [init_demo.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/init_demo.py) and [CA3 batch.py](https://github.com/ireneee22/GSoC-23/blob/main/CA3batch.py) on VM.

- *June 15th - 16th*
  - meeting on VSC remote extension (see see [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/Issues%20generating%20SSH%20keypair%20for%20Google%20Cloud%20VM.md) , mods compiling issues on VM and .err files in batch output

 
**Week 3**

 - *June 19th - 20th*
   - fixed mods issues on VM (see [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/multicore%20simulation%20errors.md))
   - still had issues in batch.py output (.err files), partial solutions [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/batch%20simulation%20errors.md)

- *June 20th-21st*
  - made a [.md file](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/SCZparameters.md) with details of the SCZ params we'll sweep
  - tried to fix batch .err files 



