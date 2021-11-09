
# Spot Programming 🐶

Interact with Spot easily with simple commands and from your local host.
This is a basic program that allows users to interact with Spot and configure basic settings with ease.


# Requirements 

This program works with all operating systems including OS, Windows, and Linux.

The program was made in Python 3.9.1, but supports all versions of *python3*. 

A *pip3* installation is also required to install Boston Dynamics' libraries to interact with Spot. However, all those libraries should be pre-installed when downloading this library.

If you would like more information about the installation of Python and Pip3, visit their documentation, which is linked under "Extra Information".

A virutal enviornment is not compulsory needed, however, it is recommended.

## Package Installations

When downaloding this program on your machine, there were will be some external Spot libraries also beign downloaded on the machine as well. These 
libraries are all from Boston Dynamics to interact with Spot.

If you would like to intsall these libraries exteranlly the command follows:


# Commands 

# Extra Information

Boston Dynamics Documentation for Spot: https://dev.bostondynamics.com/docs/python/quickstart





# Spot Programming 🐶

Interact with Spot easily with simple commands and from your local host.
This is a basic program that allows users to interact with Spot and configure basic settings with ease.


# Requirements 

This program works with all operating systems including OS, Windows, and Linux.

The program was made in Python 3.9.1, but supports all versions of *python3*. 

A *pip3* installation is also required to install Boston Dynamics' libraries to interact with Spot. However, all those libraries should be pre-installed when downloading this library.

If you would like more information about the installation of Python and Pip3, visit their documentation, which is linked under "Extra Information".

A virutal enviornment is not compulsory needed, however, it is recommended.

## Package Installations

When downaloding this program on your machine, there were will be some external Spot libraries also beign downloaded on the machine as well. These 
libraries are all from Boston Dynamics to interact with Spot.

If you would like to intsall these libraries exteranlly the command follows:


# Commands 

# Extra Information

Boston Dynamics Documentation for Spot: https://dev.bostondynamics.com/docs/python/quickstart



## Demo

Insert gif or link to demo


# Spot Programming 🐶

Interact with Spot easily with simple commands and from your local host.
This is a basic program that allows users to interact with Spot and configure basic settings with ease.


# Requirements 

This program works with all operating systems including OS, Windows, and Linux.

The program was made in Python 3.9.1, but supports all versions of *python3*. 

A *pip3* installation is also required to install Boston Dynamics' libraries to interact with Spot. However, all those libraries should be pre-installed when downloading this library.

If you would like more information about the installation of Python and Pip3, visit their documentation, which is linked under "Extra Information".

A virutal enviornment is not compulsory needed, however, it is recommended.

## Package Installations

When downaloding this program on your machine, there were will be some external Spot libraries also beign downloaded on the machine as well. These 
libraries are all from Boston Dynamics to interact with Spot.

If you would like to intsall these libraries exteranlly the command follows:\
`python3 -m pip install bosdyn-client==3.0.1 bosdyn-mission==3.0.1 bosdyn-choreography-client==3.0.1` 

*Note*: if there are any version incompatibilities, for example, receiving this error message:\
`ERROR: bosdyn-core <VERSION_STRING> has requirement bosdyn-api==<VERSION_STRING>, but you
have bosdyn-api 3.0.1 which is incompatible.`

It is recommended that the user uninstalls the packages and reinstalling. The uninstalling commands are as follows:
* `python3 -m pip uninstall bosdyn-client bosdyn-mission bosdyn-api bosdyn-core`
* `python3 -m pip install bosdyn-client bosdyn-mission`

In order to know that we have installed the packages correctly, we can use the command:\
`python3 -m pip list --format=columns | grep bosdyn`

A sample output may be:\
<div align="center>
    bosdyn-api                   3.0.1
    bosdyn-choreography-client    3.0.1
    bosdyn-choreography-protos    3.0.1
    bosdyn-client                 3.0.1
    bosdyn-core                   3.0.1
    bosdyn-mission                3.0.1
</div>

*Note*: If packages are not installed correctly, then a sample error message may appear:\
`Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'bosdyn.client'`


# Setting up Spot

Before using this program with Spot, the Spot needs to be turned on, and pinged through the user's wifi.

It is also recommended that the user has tested their program and has ran some tests on the dog before tweaking the configurations.

If you need help with setting up or running a test, visit the Boston Dynamics' documentation on Spot, which can be found under "Extra Information" section of this documentation.


# Commands

There are multiple commmands to configure Spot. Each one has it's own use and for full information, it is highly recommended to visit Boston Dynamics' Documentation on each of their functions.

## Connecting Python to Spot 

This function is the first function that should be ran when connected to this program. Without connecting to Spot, the program's functions will not run and will return error messages.

Command: `/connect`

The user will be first prompted to type their username and password for Boston Dynamics. If the user does not have, it is recommended that they read their documentation, which can be found under the "Extra Information" section.
The user must successfully type in their username and password in order to connect to Spot. 

In order for the user to connect their Spot, their network id is necessary, which is the DNS of their wifi they used to turn on Spot. Moreover, when this command has been ran successfully, it will prompt
the user to type in a name for the dog, which can be anything they want.

After all the information is entered successfully, the user will be faced with the robot's name and it's information, Spot's Id, and more of Spot's information for reference.

However, if the user fails to connect Spot to the program, they must double check their username and password and their DNS and network-id. 


## Turning On 

When the user has successfully connected Spot to the program, they can now turn Spot on right from their machine. 

Command: `/turn_on`

If Spot is not already turn on, it will turn on. Do note that if there is some network issues or latency with the user's network, there may be some delay for the robot to recieve the commands from the program. In this case, the network must be fixed or improved as the program as fully relying on the user's 
network for connection.

## Capturing Images with Spot 

Spot has 5 "fisheye" cameras in addition to 5 depth cameras. Images can be captured from the program with integrated image sources. 

Command: `/capture_image`

The user must have Spot turned on and connected to take pictures. 

The user will first be faced with a list of sources, which are names of the pictures that have been taken. 
Next, the user will be prompted to take pictures with their Spot. This will run infinitely and will be showed on Spot's display until the user stops this process with `^C`.

*Note*: All pictures that have been taken are not stored in the program.


## Configuring E-Stops ("Motor Power Authority")

The E-Stop is a key safety feature of Spot which lets operators kills motor power immediately if a situation calls for it.
Note that in some circles, the term "E-Stop" implies a hardware power short-circuit, hence our semantic dancing, as Spot's Motor Power Authority is a networked software solution, not a hardware solution.

More information can be found on their documentation, which is liked under "Extra Information" Section.

### List E-Stops 

Command: `/e-stop`

The program will first fetch the first e-stop status and client. The client will then be appended to an array for e-stops which is stored locally for future reference when 
deleting an e-stop. However, it must be noted that the user has an option to accept or decline saving an e-stop.

The `stop_level: ESTOP_LEVEL_CUT` line indicates that power will not be enabled since the E-Stop level is CUT.

The `stop_level_details: "Not all endpoints are registered"` is a message that will only appear when the command is ran for the first time. Though, the line
indicates that there are no E-Stop Endpoints registered. An E-Stop Endpoint is the client component of the E-Stop system which lets a user immediately kill power. Spot may have more than one E-Stop
Endpoint registered at a time. 

### Creating a New E-Stop
Users can create a new E-stop.

*Safety Note*: The act of registering an endpoint will trigger an emergency stop on Spot, thus, should only 
be performed when Spot's motors are already powered off.

Command: `/create_estop`

There are a few things the user must choose in order to create an e-stop. They first must choose an e-stop client, which will be prompted 
for them - they will only have to type in a number that corresponds with their desired client. The next parameter the user must choose is the name of the e-stop, which 
can be anything they would like. 

The last factor is optional and is a timeout (delay in other words). The user will be prompted if they would like a timeout, and if not, the endpoint will be created without a timeout. However,
if the user wishes to add a timeout, it will is necessary that they enter a time in decimals. E-Stop endpoints are expected to regularly-check in to the robot to assure the robot is safely being controlled.
If it has been more than `estop_timeout` seconds, the motor power will be cut. Thus, tuning this number is important: too low a number, and the power may cut out due to transient network issues; too large a number and you run the risk 
of Spot operating without safe supervision.

It should be noted that the newly created e-stops will sent to an underlying array for referenece for the users. 

### Clearing the E-Stop
To change an E-Stop status and allow power, the endpoint needs to check in on a regular basis. The program uses the `EstopKeepAlive` class to tinker the checkins on a regular basis from a background thread. 

Command: `/clear_e_stop` 

The user will be faced with a list of e-stops and an option to clear a certain client. The user must type in a number that corresponds with the client, and the program will save the endpoint of the desired e-stop client.
The program will then clear the endpoint using the endpoint.

*Note*: If there are no-estops, the program will return a message stating:\
`"There are no e-stops logged"`

## Listing Leases 
The robot can have multiple clients but only one can control the robot even as other clients may be requesting data or acting as E-Stop endpoints. Thus, to view
all the leases users can use the command to view all the leases in the form of an array:

Command: `/list_leases`

*Note*: Like the E-Stop, lease holders need to periodically check in with Spot to indicate that they are still actively controlling the robot.
If it has been too long since a check-in, the robot will commence a *Comms Loss Procedure* - stitting down if it can, and then powering off.

All the leases will be saved under a "lease" array where all the past and recent leases are saved. This is engineered to allow for easy acquiring of Spot (read the section "Acquiring Spot" for more information).

## Acquiring Spot 
When taking lease control of Spot, the lease should first be acquired, and then the "keepalive" should be created 
to retain ownership of the lease resource. This program allows users to acquire a lease and create a keepalive efficiently.

Command: `/acquire_spot`

Similar to E-stops, the user will be faced with a number of leases and will have to choose a number that corresponds to their lease to take ownership of. 
After successfully choosing a lease, the user will become successfully the owner, and an updated list of leases of Spot will printed out. 

## Timesync for movements

A Timesync was required to coordinate clock skew between the device of the user and Spot. For safety, this allows
users to define a period of time for which a command will be valid. 

When a sample movement function is made, the program first creates a timesync class where each thread will make periodic calls to maintain
timesync. Each client is then issued a clock identifier which is used to validate that the client has performed timesync, for services that require
this functionality. 

## Stand (Sample Function)
The API the program runs on provides a helpr function to stand Spot. This command wraps several Robot-Command RPC calls.

Command: `/stand`

The way the commnd works is that a stand command is issued. The robot checks some basic pre conditions (power on, not faulted, no E-Stopped) and returns a 
command id. This command id can then be passed to the robot command feedback RPC. This call returns both high level feedback ("is the robo still processing the command?") as well as 
command specific feedback (in the case of stand, "is the robot standing"). 

## Rotating (Sample Function)
Similar to the Stand function (read section "Stand (Sample Function)" for more function.)

Command: `/rotatez`

When the user runs the command, they will prompted for a `yaw`, `roll`, and a `pitch` value. These values should be experimented on as they work 
as `x`, `y`, `z` values. 

After the running the command, the user should expect a roll around the z-axis over a certain distance.


## Raising up (Sample Function)

If Spot is sitting, users can command Spot to stand up with a simple command:

Comand: `/raiseup`

The user will be prompted to type in a certain height Spot should raise up to. This height correponds to the body height of the robot and should be typed in a decimal value.
The user should epxect the robot to raise up over a distance.

## Powering off (Sample Function)
To power Spot Off:

Command: `/off`

Any issue regarding this powering off means that the program has not been connected to the robot. 
Read the section "Setting up Spot" for more details.

# Extra Information

Boston Dynamics Documentation for Spot: https://dev.bostondynamics.com/docs/python/quickstart
Boston Dynamics Programming for Spot: https://dev.bostondynamics.com/docs/python/understanding_spot_programming

The *RobotCommandService* is the primary interface for commanding mobility. Mobility and mobility-related commands include `stand`, `sit`, `selfright`, `safe_power_off`, `velocity`, and `trajectory`. 
Thus, it is encouraged for users to tinker with this program and with their robot and unlock more functionality with Spot!

If there are any issues regarding the commands, there must be a connection error or the robot hasn't been turned on. Users should 
read the "Setting Up Spot" section of the documentation.


Made by 🧠 with ❤️