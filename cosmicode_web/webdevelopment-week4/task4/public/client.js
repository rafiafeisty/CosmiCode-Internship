const ws=new WebSocket('ws://'+window.location.host)
const chatmessage=document.getElementById("messages")
const username=document.getElementById("name")
const message=document.getElementById("message")

ws.onopen=()=>{
    console.log("Connected to the server")
}
ws.onclose=()=>{
    console.log("Disconnected from the server")
}
ws.onerror=(error)=>{
    console.log("Error occurred: ",error)
}
ws.onmessage=(event)=>{
    const data=JSON.parse(event.data)
    displaymessage(data)
}
function displaymessage(data) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", data.type);

  if (data.type === "chat") {
    const time = new Date(data.timestamp).toLocaleTimeString();
    messageElement.innerHTML = `<strong>${data.username}</strong> [${time}]: ${data.message}`;
    messageElement.style.background="#9aefe3"
    messageElement.style.height="40px"
    messageElement.style.borderRadius="5px 5px 5px 5px"
    messageElement.style.padding="5px"
    messageElement.style.marginTop="5px"
  } else {
    messageElement.textContent = data.message;
  }

  chatmessage.appendChild(messageElement);
  chatmessage.scrollTop = chatmessage.scrollHeight; 
}

function sendmessage(){
    const username2=username.value||"Anonymous"
    const mess=message.value
    if(mess){
        ws.send(JSON.stringify({type:"chat",username:username2,message:mess,timestamp:new Date().getTime()}))
        message.value=""
    }
}