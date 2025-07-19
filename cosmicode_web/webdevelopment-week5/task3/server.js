require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth');
const path=require("path")
const app = express();

app.use(express.json());
app.use('/api/auth', authRoutes);

app.use(express.static(path.join(__dirname,"public")))

const auth = require('./middleware/auth');
app.get('/admin', auth(['admin']), (req, res) => res.send('Admin only'));
app.get('/dashboard', auth(['user', 'admin']), (req, res) => res.send('Dashboard'));

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    app.listen(3000, () => console.log('Server running on http://localhost:3000'));
  })
  .catch(err => console.error(err));

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname,"public","login.html"))
})