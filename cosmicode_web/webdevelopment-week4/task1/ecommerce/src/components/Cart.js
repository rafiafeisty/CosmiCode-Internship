import React from "react";
import { useContext } from "react";
import { myContext } from "../context/CartContext";
import "./Style.css";

const Cart = () => {
  const { cart, removeCart } = useContext(myContext);
  return (
    <>
      <h1 className="cart-head">Your Cart</h1>
      <div className="card-loop2">
        {cart.length === 0 ? (
          <p>No Cart to Display</p>
        ) : (
          cart.map((item, idx) => (
            <div className="card-main" key={idx}>
              <div className="card2">
                <img src={item.image} alt={item.name} />
                <div className="content2">
                  <h3><strong>Name: </strong>{item.name}</h3>
                  <p><strong>price: </strong>${item.price}</p>
                  <button onClick={() =>{
                    alert("Deleting from the cart")
                     removeCart(item.id)}} className="removecart">
                    Remove from Cart
                  </button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </>
  );
};

export default Cart;
