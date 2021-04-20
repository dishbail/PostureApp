from channels.generic.websocket import AsyncWebsocketConsumer
import json
import sqlite3

# Create a SQL connection to the SQLite database
con = sqlite3.connect("../db.sqlite3")

cur = con.cursor

class DashConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self,close_code):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )


    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':val
            }
        )

        print ('>>>>',text_data)
        cur.execute('INSERT INTO Customer_posturerecord (posture_value, Customer_customer) VALUES('+ text_data+',' + self.user + ');') #update the posture record table

        # pass

    async def deprocessing(self,event):
        valOther=event['value']
        await self.send(text_data=json.dumps({'value':valOther}))
