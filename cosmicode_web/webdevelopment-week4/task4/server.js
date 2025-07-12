const express=require("express")
const webSocket=require("ws")
const http=require("http")

const app=express()
const server=http.createServer(app)
const wss=new webSocket.Server({server:server})

app.use(express.static('public'))

const client=new Set()

function broadcast(message){
    client.forEach((client)=>{
        if(client.readyState==webSocket.OPEN){
            client.send(JSON.stringify(message))
        }
    })
}

wss.on('connection', (ws) => {
  console.log('New client connected');
  client.add(ws);

  ws.send(JSON.stringify({
    type: 'system',
    message: 'Welcome to the chat!'
  }));


  ws.on('message', (data) => {
    try {
      const message = JSON.parse(data);
      if (message.type === 'chat') {
        broadcast({
          type: 'chat',
          username: message.username || 'Anonymous',
          message: message.message,
          timestamp: new Date().toISOString()
        });
      }
    } catch (error) {
      console.error('Error processing message:', error);
    }
  });
  ws.on('close', () => {
    console.log('Client disconnected');
    client.delete(ws);
  });
  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});