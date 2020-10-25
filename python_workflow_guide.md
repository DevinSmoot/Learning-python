## Python Workflow

#### Workflow Overview

1. Create virtual environment folder
2. Install virtual environment packages
3. Create virtual environment
4. Creat dockerfile (not needed but recommended)
5. Write code
6. Write tests
7. Profit

#### Workflow in depth

1. Create virtual environment:
   1. `mkdir ~/python_venv`
2. Install virtual environment packages:
   1. Python 2.7
      1. `pip install virtualenv`
   2. Python 3.x
      1. Included with Python 3.x
3. Create virtual environment:
   1. Python 2.7
      1. `virtualenv <NameOfVirtualEnv>`
      2. Activate virtual environemnt: `source ./<NameOfVirtualEnv>/bin/activate`
      3. Once finished working with virtual environment, deactivate: `deactivate`
   2. Python 3.x
      1. `python3 -m venv <NameOfVirtualEnv>`
      2. Activate virtual environment: `source <NameOfVirtualEnv>/bin/activate`
      3. Once finished working with virtual environment, deactivate: `deactivate`
4. <Unknown>
5. Write code
6. Write tests
7. Profit
