![ObFile banner](https://user-images.githubusercontent.com/68228966/92695177-bb6dc080-f365-11ea-81a4-8236bf1068fb.jpg)

# ObFile
ObFile is a python compiler and obfuscator for Windows. It can compile your python programs into exe and you can even add your own custom icons to it. You can also obfuscate the files and compile them into exe.

ObFile uses **PYINSTALLER** and **PYARMOR** to compile and obfuscate the python files. The credit also goes to the developers of both of these modules. 

* Released : 5/09/20
* Last Updated : 10/09/20

# Changelogs
* Removed VBScript messageboxes
* Updated os.system commands to `subprocess.call`

# Update 1.1.1
* Updated : 10/09/2020
* Removed Time delay commands to enhance user-interaction
* Popup message whenever the file processing completes
* Updated Menu
* Bug fixes
* Fixed Spaces and indents
* Added setup file (to install all modules)
* Updated `os.system` to `subprocess.call`

# How to use it?
It is easy to use the program. 
* Open CMD in that folder and run the following command
* `python setup.py`

**Before the program starts, it will install several modules required**
**It will take some time, but please be patient :slightly_smiling_face:**

**After it installs all modules, it will display  the menu as shown below**
![Capture](https://user-images.githubusercontent.com/68228966/92302197-e03dee80-ef87-11ea-9ab1-c425c64af53b.PNG)

**Press Enter to continue**
 
 You will see a menu like this
 
 ![2](https://user-images.githubusercontent.com/68228966/92302222-03689e00-ef88-11ea-99d1-865a91a953d5.PNG)
 
 # Installation
 
 Use the Git clone command to install the program, or directly install it as zip file
 
 https://github.com/kavinjindal/ObFile.git
 
# Compatible OS

ObFile is compatible only with Windows

**Using the Program**
 * Type `use 1` to compile your file
 * Type ` use 2` to obfuscate your file
 * Type ` use 3 ` to obfuscate and compile your file
 * Type ` use 4 ` to view the help section
 * Type ` use 5 ` to quit the program
 
 **Using the Compiler tool**
 
 ![3](https://user-images.githubusercontent.com/68228966/92302312-df598c80-ef88-11ea-878f-bd2e9624ae89.PNG)
 
To use the **Compiler** tool, press enter:
* Type `use 1` to Compile your file with icon **(icons only with .ico file extension are supported)**
* Type `use 2` to Compile your file without an icon
* Type `use 3` to Quit the Program

If you type ` use 1 `, you will see a window like this

![4](https://user-images.githubusercontent.com/68228966/92302374-58f17a80-ef89-11ea-98c4-3b835a17e6de.PNG)

You will have to copy the path of your file in the field and press enter

Then you will see a field for entering path of icon. Copy paste the icon path and press enter. 

After that, the program will start its compiling process(it will take some time)

![5](https://user-images.githubusercontent.com/68228966/92302826-cd79e880-ef8c-11ea-9337-2eacb8c598db.PNG)

After the compiling process ends, check the dist folder in the ObFile folder.

You will see the program has executed..

**The same process takes place, when you obfuscate your file and compile it.**

# Important
* Make sure that the file path and icon path is correct or else, the program will show errors.
* The output of the obfuscated or compiled python file will be stored in the Folder of the ObFile program.

# Python Modules used:
* Pyarmor
* Pyinstaller
* Colorama
* Pyfiglet

# Python Version Support
* Python 3

# Contributors:
:computer:` Vedant Bhalgama ` - helping in codes

# Queries, Suggestions:

* You can report your issues here:

https://github.com/kavinjindal/ObFile/issues

* Or you can contact me on email here:

kavinsjindal@gmail.com

# Website:

https://kavinjindal17.wordpress.com/

# Discord Server:

https://discord.gg/fSzsGus

# Instant Devs Corp.

https://instantdevs.wordpress.com/


