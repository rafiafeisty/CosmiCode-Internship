const express = require("express");
const app = express();
const path = require("path");
const { title } = require("process");
const mongoose = require("mongoose");
const user = require("./model/User");
require("dotenv").config();
const PORT = 3000;

const posts = [];
let idCounter = 1;

app.use(express.json());

app.use(express.static(path.join(__dirname, "public")));

app.post("/post", (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    res.status(404).json("Enter title or content");
  } else {
    const post = { id: idCounter++, title, content };
    posts.push(post);
    const newpost = new user({ id: idCounter, title, content });
    newpost.save();
    res.status(200).json("uploaded successfully");
  }
});

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.get("/posts", async (req, res) => {
  const allposts = await user.find();
  posts.push(allposts);
  res.json(allposts);
});

app.put("/post/:id", async (req, res) => {
  const { title, content } = req.body;
  const id = req.params.id;

  if (!title && !content) {
    return res.status(400).json("Provide title or content to update");
  }

  const updateFields = {};
  if (title) updateFields.title = title;
  if (content) updateFields.content = content;

  try {
    const updatedPost = await user.findOneAndUpdate(
      { id: id },
      { $set: updateFields },
      { new: true }
    );

    if (!updatedPost) {
      return res.status(404).json("Post not found");
    }

    res.status(200).json({ message: "Post updated successfully", updatedPost });
  } catch (err) {
    res.status(500).json("Error updating post");
  }
});
app.delete("/post/:id", async (req, res) => {
  const id = req.params.id;

  try {
    const deletedPost = await user.findOneAndDelete({ id: id });

    if (!deletedPost) {
      return res.status(404).json("Post not found");
    }

    res.json({ message: "Post deleted successfully", deletedPost });
  } catch (err) {
    res.status(500).json("Error deleting post");
  }
});

app.post('/comment/:id', async (req, res) => {
  const { content } = req.body;
  const id = req.params.id;

  try {
    const post = await user.findOne({ id: id });
    if (!post) {
      return res.status(404).json("Post not found");
    }

    post.comments.push({ text: content });
    await post.save();

    res.status(201).json({ message: "Comment added successfully" });
  } catch (error) {
    console.error(error);
    res.status(500).json("Error adding comment");
  }
});


app.get("/comment/:id", async (req, res) => {
  const id = req.params.id;

  try {
    const post = await user.findOne({ id: id });
    if (!post) {
      return res.status(404).json("Post not found");
    }

    res.json(post.comments);
  } catch (err) {
    res.status(500).json("Error fetching comments");
  }
});


app.listen(PORT, () => {
  console.log(`server listening on http://localhost:${PORT}`);
});


mongoose
  .connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    app.listen(3000, () =>
      console.log("Server running on http://localhost:3000")
    );
  })
  .catch((err) => console.error(err));
