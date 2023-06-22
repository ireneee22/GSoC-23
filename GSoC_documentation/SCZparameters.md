# Relevant parameters in SCZ 

We will focus on PV, SOM, GAT1, and NMDA.

## **PV (Parvalbumin):**

 - Parvalbumin-expressing interneurons are inhibitory neurons. 
 - Play a role in regulating brain excitatory activity
 - fast spikining, contribute to gamma activity

   *In A1 netParams:*

   *In A1 cfg:*


## **SOM (Somatostatin):**
 - Somatostatin-expressing interneurons are inhibitory neurons.
 - Regulate network activity, shape synaptic integration, control plasticity.


   *In A1 netParams:*

   *In A1 cfg:**


## **GAT1 (GABA Transporter 1):**
  - regulates GABA reuptake, terminates GABAergic neurotransmissioncellular space. 
  - used to simulate adequate level of inhibitory neurotransmission/GABA dynamics.

   
   *In A1 netParams:*

   *In A1 cfg:*


## **NMDA (N-Methyl-D-Aspartate)**
 - ionotropic glutamate receptors, involved in LTP and LTD-> used to reflect synaptic plasticity 


   *In A1 netParams:*

  - 



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


