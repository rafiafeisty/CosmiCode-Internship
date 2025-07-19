const express=require("express")
const jwt=require("jsonwebtoken")
const bcrypt=require("bcryptjs")
const User=require('../models/Users')
const path=require("path")
const router=express.Router()


router.post("/register",async (req,res)=>{
    const {username,password,role}=req.body
    const userexist=await User.findOne({username})
    if(userexist){
        res.status(400).json({message:"user already exists"})
    }
    const hashedpass=await bcrypt.hash(password,10)
    const newuser=new User({username,password:hashedpass,role})
    await newuser.save()
    res.status(201).json({message:"user saved"})
})

router.post("/login",async (req,res)=>{
    const {username,password}=req.body
    const userfind=await User.findOne({username})
    if(!userfind){
        res.status(400).json({message: "user not found"})
    }
    const ismatch=bcrypt.compare(password,userfind.password)
    if(!ismatch){
        res.status(400).json({message:"password doesn't match"})
    }
    const token=jwt.sign({id:userfind._id,role:userfind.role},process.env.JWT_SECRET,{expiresIn:'1h'})
    res.json({token,
        role:userfind.role
    })
})


module.exports=router