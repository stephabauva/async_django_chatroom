from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    #connect
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #add group chat
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        #send messages into group chat
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'tester_message',
                'tester': 'hello world',
            }
        )
    #send message via websocket
    async def tester_message(self, event):
        tester = event['tester'] # the event

        await self.send(text_data=json.dumps({
            'tester': tester
        }))


    #disconnect
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    pass