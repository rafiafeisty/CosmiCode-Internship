const mongoose = require("mongoose");

const userschema = new mongoose.Schema({
  id: { type: Number, required: true, unique: true },
  title: { type: String, required: true },
  content: { type: String, required: true },
  comments: [ 
    {
      text: { type: String, required: true },
      created_at: { type: Date, default: Date.now }
    }
  ]
});


module.exports = mongoose.model("user", userschema);
