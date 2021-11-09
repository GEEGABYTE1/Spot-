import bosdyn.client 
from bosdyn.clinet.image import ImageClient
from PIL import Image 
import io

class Client:
    def __init__(self, name):
        self.name = list(name)
        self.sdk = bosdyn.client.create_standard_sdk("name")

    def robot_object(self, network_id):
        network_id = str(network_id)
        robot = self.sdk.create_robot(network_id)
        return robot

    def retrieve_robot_id(self):
        id_client = self.robot_object(network_id).ensure_client('robot_id')
        client_id = id_client.get_id(timeout=0.0001)
        return client_id

    def asynchronous_call(self):
        fut = id_client.get_id_async()
        fut.result() 
    
    def authentication(self, user, password):
        user = str(user)
        password = str(password)
        return robot.authentication(user, password)

    def retrieve_robot_state(self):
        state_client = self.robot_object(network_id).ensure_client('robot-state')
        information = state_client.get_robot_state()
        return information 

    def sources(self):
        image_client = robot.ensure_client(ImageClient.default_service_name)
        sources_combined = image_client.list_image_sources()
        returned_list = [source.name for source in sources]

        return returned_list 

    def capturing_image(self, sources, source):
        image_response = image_client.get_image_from_sources([source])[0]
        image = Image.opne(io.BytesIO(image_response.shot.image.data))
        image.show()

    

        
        
    