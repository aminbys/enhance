Enhance is an amazing package written by Mark Hulsman to manage packages in user's home directory in Linux.
Original Author: https://github.com/mhulsman

Creating an environment
-----------------------

1. Download enhance: `wget https://github.com/aminbys/enhance/archive/master.zip`

2. Create the directory in which you will place your enhance environment, e.g. `mkdir env/enhance/`

3. Unpack the "master.zip" file and copy the contents in a folder in your enhance directory: `unzip ~/master.zip; mv enhance-master ~/env/package_manager`

4. Move to enhance directory: `cd env/enhance/`

5. Execute: `package_manager/enhance init generic`

6. Your directory structure shoud now look like this:

```bash
-bash-4.1$ tree -d
.
├── env
│   └── enhance
│       ├── package_manager
```

Viewing available/installed packages
------------------------------------
Note that you should be in the enhance directory for this to work: `cd ~/env/enhance/`

enhance list



Installing packages
--------

enhance install <packagename>


Starting environment
-----------

start_enhance

