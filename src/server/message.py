import pickle

class Message():
    def __init__(self, message):

        self.message = message
        
    def serialize(self):
        pickleed_message = pickle.dumps(self.message)
        msg_len = len(pickleed_message)
        send_len = str(msg_len).encode('utf-8')
        send_len += b' ' * (128 - len(send_len))

        Serialized_Message = send_len + pickleed_message
        return Serialized_Message
        # Message is ready to send in the socket


