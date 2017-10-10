# Virtual Environments
Almost all code depends on libraries (which sometimes get called modules or packages). If you've used the "import" statement in Python to use code you didn't write, then you've used a library.

Managing all your libraries (called "dependency management") gets confusing very quickly. If you're working on more than one project at once, you'll be using different libraries for each project, or sometimes different versions of the same project.

If you try to use a standard environment, this is a problem. Python (and basically everything else) only allows you to install one version of a library at once.

The solution is *virtual environments*. A virtual environment is a copy of the python ecosystem (the interpreter, the packages, the package manager) that exists for a single project (or subproject, if you're doing something complicated). Any time you work on that project you activate the relevant virtual environment, and then you're working with a separate copy of everything. You can use whatever versions of whatever software you like, and you can be confident it won't affect any other projects.

There are two main tools for managing virtual environments in python: the virtualenv package and the conda package. conda is nearly strictly better, so we'll use that. You can download it [here](https://www.anaconda.com/download/#windows). (This includes more than just conda, but whatever.)

If you're on Windows, you'll need to use the "Anaconda prompt" program in order to actually use Anaconda/conda.

Once you have it downloaded, use [this page](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) to create a virtual environment for this repo. 
