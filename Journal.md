
# Progress Journal 

**GOALS FOR THE FIRST TWO WEEKS (May 29th - June 12th)**

- Small-medium task, high priority: scaling the A1 model for parameter sweeps.
- Medium  task, medium priority: demonstrating batch scripts with the A1 model with relevant parameters, based on literature and synaptic weights.
- Small task, low priority: documenting the use of NetPyNE batch tools versus refactoring batch tools.

**Week 1** 

- *May 29th - 31st*
  - Documented the structure of [cfg.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/cfg.py), [netParams.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/netParams.py) and [batch.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/batch.py), available HERE (una volta tradotte dall'italiano)
  - First meeting to establish next steps : running a scaled batch script, setting up virtual machine on Google Cloud and running the batch script on the VM.

- *June 1st, 2nd*
	 - ran multicore sim of tutorial 8 batch.py on terminal 
   - created 3x3 batch script for CA3 model, available [here](https://github.com/ireneee22/GSoC-23/blob/main/CA3batch.py)
   - ran multicore sim of 3x3 batch.py of CA3 model on terminal, issues documented [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/multicore%20simulation%20errors.md) and [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/batch%20simulation%20errors.md)
   - Set up UBUNTU Virtual Machine on Google Cloud and downloaded NEURON and NetPyNE related packages, MPI, etc. 

**Week 2**

- *June 5th - 7th*
  - issues with SSH keypair on VM   
  - meeting on useful LINUX commands, VM goals for the next week 

- *June 8th, 9th*
	- figured out SSH keypair on VM, documented [here](https://github.com/ireneee22/GSoC-23/blob/main/GSoC_documentation/Issues%20generating%20SSH%20keypair%20for%20Google%20Cloud%20VM.md)


**Week 3**
- *June 12th - 14th*
  - ran [init_demo.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/init_demo.py) and [CA3 batch.py](https://github.com/ireneee22/GSoC-23/blob/main/CA3batch.py), issues documented HERE 
 issues with libnrnmech.so
 
-current issues: VSC remote ext 


