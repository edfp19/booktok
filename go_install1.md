So this took a while. 

1. first if you use webi again just make sure to find the path installation, for me it was 

.local/opt/go

we need to change goroot to that like 

export GOROOT=$HOME/.local/opt/go

echo 'export GOROOT=$HOME/.local/opt/go' >> ~/.bashrc

source ~/.bashrc

2. We need to add a path to our PATH variable

export PATH=$PATH:$GOROOT/bin

And done.
