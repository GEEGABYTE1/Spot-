import time
from spot import*

class Prompt:
    robot = None
    connection = None
    e_stops = []
    e_stop_endpoints = {} 
    leases = []
    def __init__(self):
        self.intro()

    
    def intro(self):
        time.sleep(0.2)
        print('-'*25)
        print("/connect: To connect to your Spot")
        time.sleep(0.2)
        print('-'*25)
        print("/turn_on: Turn your Spot on")
        time.sleep(0.2)
        print('-'*25)
        print("/capture_image: To capture images with your Spot")
        time.sleep(0.2)
        print('-'*25)
        print("/e-stop: To configure Motor Power Authority")
        time.sleep(0.2)
        print('-'*25)
        print("/create_estop: To create an e-stop")
        time.sleep(0.2)
        print('-'*25)
        print("/clear_e_stop: To delete or clear an e-stop")
        time.sleep(0.2)
        print('-'*25)
        print("/list_leases: List previous leases of your Spot")
        time.sleep(0.2)
        print('-'*25)
        print("/acquire_spot: Acquire your Spot")


        
    
        while True:
            print('\n')
            user_prompt = str(input(': '))
            user_prompt = user_prompt.lower()
            user_prompt = user_prompt.strip(" ")
            if user_prompt == '/connect':
                user_robot_info = self.connect() 
                self.robot = user_robot_info[0]
                user_robot_obj = user_robot_info[1]
                user_robot_id = user_robot_info[-1]

                user_authentication = self.authentication()

                if user_authentication:
                    robot_information = self.robot.retrieve_robot_state()
                    print("Here is {name}'s information: {}".format(robot_information, name=self.robot.name))
                    time.sleep(0.2)
                    print("Robot Id: {}".format(user_robot_id))
                    time.sleep(0.2)
                    print("More Robot Information: {}".format(user_robot_obj))
                    time.sleep(0.2)
                    self.connection = True
            
            elif user_prompt == '/capture_image':
                if self.log_in():
                    time.sleep(0.1)
                    sources = self.robot.sources()
                    print("Here are your sources listed within Spot: ")
                    for i in sources:
                        print(str(i) + "\n")
                    saved_source_prompt = str(input("Which source would you like to save to capture a photo?: "))
                    saved_source_prompt = saved_source_prompt.strip(" ")
                    self.robot.capturing_image(sources, saved_source_prompt)
                

            elif user_prompt == '/e-stop':
                if self.log_in():
                    print("Note: E-Stop must only be used when there may be an emergency issue.")
                    e_stop_robot = self.robot.e_stop()
                    e_stop_status = e_stop_robot[0]
                    e_stop_client = e_stop_robot[-1]
                    
                    print("\n" + "E-Stop Status: {}".format(e_stop_status))
                    while True:
                        saving_estop_prompt = str(input("Would you like to save your e-stop? type (y/n): "))
                        saving_estop_prompt = saving_estop_prompt.strip(" ")
                        if saving_estop_prompt == 'y':
                            self.e_stops.append(e_stop_client)
                            print("e-stop successfully added. ")
                            break
                        elif saving_estop_prompt == 'n':
                            print("e-stop not added")
                            break 
                        else:
                            print("That command does not seem valid. ")
                
            
            elif user_prompt == '/create_estop':
                if self.log_in():
                    if len(self.e_stops) > 0:
                        for estop in range(len(self.e_stops)):
                            print('{}: {}'.format(estop, self.e_stops[estop]))
                    try: 
                        while True:
                            num = int(input("Please type in a number that corresponds to your desired e_stop: "))
                            if num > len(list(self.e_stop_endpoints.keys())):
                                print("That number is too large! ")
                        else:
                            break
                        client = self.e_stops[num]
                        client_name = str(input("Please type in a name for your e-stop client: "))
                        timeout = None
                        while True:
                            timeout_prompt = str(input("Would you like to configure the time of the timeout? type (y/n): "))
                            if timeout_prompt == 'y':
                                timeout = float(input("Please type in a time for a timeout in SECONDS: "))
                                break 
                            else:
                                print("Timeout not added")
                                break 
                        
                        if timeout == None:
                            e_stop_created = self.robot.create_e_stop(client, client_name)
                        else:
                            e_stop_created = self.robot.create_e_stop(client, client_name, timeout)

                        self.e_stop_endpoints[client] = e_stop_created
                        print("e-stop successfully added! ")
                    except:
                        print("There has been an error")
                
                
            
            elif user_prompt == '/clear_e_stop':
                if len(list(self.e_stop_endpoints.values())) > 0:
                    counter = 0
                    for client, endpoint in self.e_stop_endpoints.items():
                        print("{num} ~ {client}: {endpoint}".format(num=counter, client=client, endpoint=endpoint))
                        counter += 1

                    while True:
                        num = int(input("Please type in a number that corresponds to your desired e_stop: "))
                        if num > len(list(self.e_stop_endpoints.keys())):
                            print("That number is too large! ")
                        else:
                            break

                        specified_client = list(self.e_stop_endpoints.keys())[num]
                        desired_endpoint = self.e_stop_endpoints[specified_client]
                        self.clear_e_stop(desired_endpoint)
                        print("\n Clear successful")
                else:
                    print("There are no e-stops logged")
            
            elif user_prompt == '/list_leases':
                if self.log_in():
                    leases_list_robot = self.robot.spot_leases()[0]
                    leases_client_robot = self.robot.spot_leases()[1]
                    self.leases.append(leases_client_robot)
                    print(leases_list_robot)
            
            elif user_prompt == '/acquire_spot':
                if self.log_in():
                    for client in range(len(self.leases)):
                        print('{}: {}'.format(client, self.leases[client]))
                    
                    while True:
                            num = int(input("Please type in a number that corresponds to your desired lease client to be acquired: "))
                            if num > len(list(self.e_stop_endpoints.keys())):
                                print("That number is too large! ")
                            else:
                                break
                    
                    desired_lease = self.leases[num]
                    updated_leases = self.become_owner(desired_lease)
                    print("You have successfully acquired this Spot")
                    time.sleep(0.2)
                    print(updated_leases) 
            
            elif user_prompt == '/turn_on':
                if self.log_in():
                    self.robot.turn_on()
                    status = self.robot.is_powered_on()
                    if status == True:
                        print("Your Spot is turned on")
                    else:
                        print("Your Spot is turned off currently")                

                

    def log_in(self):
        if self.connection == True:
            return True 
        else:
            print("There is no connection to spot")
            return False
                    

    def connect(self):
        time.sleep(0.2)
        user_name = str(input("Please type in the name of your Spot: "))
        robot_client = Client(user_name)
        
        user_networkid = str(input("Please type in the network id you wish for Spot to be on: "))
        user_robot_obj = robot_client.robot_object(user_networkid)

        robot_id = robot_client.retrieve_robot_id()
        
        return [robot_client, user_robot_obj, robot_id]
    
    def authentication(self):
        user_user = str(input('Please type in the username: '))
        time.sleep(0.2)
        print("Note: This program does not save your information anywhere")
        user_pass = str(input('Please type in your password: '))
        status = self.robot.authentication(user_user, user_password)

        return status




test = Prompt()

print(test)

    
        