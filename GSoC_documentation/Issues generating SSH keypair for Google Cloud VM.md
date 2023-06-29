# Issues generating SSH keypair for Google Cloud VM

Type of OS and of virtual machine:

    OS: MacOS 13.2.1
    Distributor ID: Ubuntu
    Description:	Ubuntu 20.04.6 LTS
    Deletion protection : Disabled
    Confidential VM service : Disabled 
    Machine type : e2-medium
    CPU platform : Intel Broadwell
    Architecture : x86/64
    HTTP traffic : On 
    HTTPS traffic : Off
    Boot Disk : 10 GB Balanced persistent disk


I kept getting this error: 

    Permission denied (publickey).
    lost connection

Things that helped: 

- manually pasting public key onto the VM metadata
- checking that public key on local machine matches the VM key 
- using `sudo nano /home/user/.ssh/authorized_keys` I checked that the public key was pasted correctly
- running `chmod 700 ~/.ssh` and `chmod 600 ~/.ssh/authorized_keys`
- editing VM’s sshd_config file to the following:  `PubkeyAuthentication yes`  and  `AuthorizedKeysFile .ssh/authorized_keys`
- checking active status of ssh through `sudo service ssh status` and running `sudo service ssh restart`
- deleting all keys from local and virtual machine and starting from scratch
- making sure I was connecting to the right username and not to the name of the VM itself 
- making sure user in .ssh/id_rsa is set to VM user
