const express=require("express")
const app=express()
const path=require("path")

app.use((req,res,next)=>{
    console.log(`${req.method} ${req.url}`)
    next()
})

app.use(express.json())

app.get('/',(req,res)=>{
    res.sendFile(path.join(__dirname,"public","index.html"))
})
app.get('/about',(req,res)=>{
    res.sendFile(path.join(__dirname,"public","about.html"))
})

app.post('/data',(req,res)=>{
    console.log('Data received')
})
PORT=3000

app.listen(PORT,()=>{
    console.log(`Server is running on port http://localhost:${PORT}`)
})