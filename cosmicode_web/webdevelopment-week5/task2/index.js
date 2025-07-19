const express=require("express")
const app=express()
const path=require("path")
const { title } = require("process")
const PORT=3000

const posts=[]
let idCounter=1

app.use(express.json())

app.use(express.static(path.join(__dirname,"public")))

app.post("/post",(req,res)=>{
    const {title,content}=req.body
    if(!title || !content){
        res.status(404).json("Enter title or content")
    }
    else{
        const post={id:idCounter++,title,content}
        posts.push(post)
        res.status(200).json("uploaded successfully")
    }
})

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname,"public","index.html"))
})

app.get("/posts",(req,res)=>{
    res.json(posts)
})
app.put("/post/:id",(req,res)=>{
    const {title,content}=req.body
    const id=req.params.id
    const post=posts.find(p=>p.id==parseInt(id))
    if(!post){
        res.status(404).json("post not found")
    }
    else{
        if(title){
            post.title=title
        }
        if(content){
            post.content=content
        }
        res.status(200).json("Updated successfully")
    }
})

app.delete("/post/:id",(req,res)=>{
    const id=req.params.id
    const postInd=posts.findIndex(p=>p.id==parseInt(id))
    if(postInd==-1){
        res.status(404).json("post not found")
    }
    else{
        const deletepost=posts.splice(postInd,1)
        res.json({message:"Posts deleted successflly"})
    }
})

app.listen(PORT,()=>{
    console.log(`server listening on http://localhost:${PORT}`)
})