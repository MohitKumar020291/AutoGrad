# AutoGrad  
Starting this project so I can use it in [____](https://github.com/MohitKumar020291/Classifying-Names-with-a-Character-Level-RNN), the development of autograd might stop at a certain level cause I am just implementing what is required - like I currently  
- Create a linear layer of neurons/basic numbers(in that case create neurons) - weights could be provided or randomly generated - create neurons of next layer - the next of neuron will be called with the weights till all the weights(summation) for all the neurons


Future
- A linear layer backprop
- Complete these articles : they are inspiration
  - Implementing triton
  - https://pytorch.org/docs/stable/autograd.html#torch.autograd.Function
  - https://pytorch.org/docs/stable/notes/autograd.html
   
   

    
I keeps forgetting how to clone a private repo, so it is for that
- go to terminal (git should be known to that)    
- write `ssh-keygen -C autograd` (autograd is a name could be of your choice) (right now I don't what autograd stands, I cannot find good resource, -C may be standing for comment so the autograd might be standing for comment)   
- How to fill : `Enter file in which to save the key (/home/username/.ssh/id_rsa): /home/username/.ssh/id_rsa_anyname` - try it keeping like id_rsa_anyname like id_rsa_autograd, also don't worry it can be anything for you - the only thing you need to change is that name `id_rsa_anyname`   
- If you want to enter any phrase write that or simple press `Enter`
- Get your key - `cat /home/username/.ssh/id_rsa_anyname.pub` , `cat` stands for concatenate used for read, display, and concatenate text files and `.pub` stands for the public key. Also, if you get's an error you might want to change the permission of the file, though it should not happen - using `chmod 700 /home/username/.ssh/id_rsa_anyname` - it means you have given an access to owner to do anything(read, write and execute) but others cannot do anything, if interested - google "file permission codes linux". After having permission, try again the cat command.    
- Copy the everything - it is your key     
- copy it : ctrl + shift + c    
- go to github settings -> ssh keys and gpg keys -> add new ssh key
- give title of your choice, key type is authentication, enter key, click on add ssh key.
- Now try cloning your repo using ssh key.       
- Also, if you somehow added a private key(which I don't know how to do) - then before cloing you would like to tell your terminal that which key to use by writing - `ssh -i ~/.ssh/id_rsa_autograd user@host`, without using ".pub", you are using a private key.     
