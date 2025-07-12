import logo from "./logo.svg";
import "./App.css";
import Header from "./components/Header";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProductList from "./components/ProductList";
import Cart from "./components/Cart";
import CartContext from "./context/CartContext";
import About from './components/About'
import Footer from "./components/Footer";
function App() {
  return (
    <>
    <CartContext>
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<ProductList />}></Route>
          <Route path="/cart" element={<Cart />}></Route>
          <Route path="/about" element={<About />}></Route>
        </Routes>
      </Router>
      </CartContext>
      <Footer/>
    </>
  );
}

export default App;
