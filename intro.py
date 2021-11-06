import time
from spot import*

class Prompt:
    robot = None
    def __init__(self):
        self.intro()

    
    def intro(self):
        time.sleep(0.2)
        print('-'*25)
        print("/connect: To connect to your Spot")
        time.sleep(0.2)
        print('-'*25)
        
    
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

    
        