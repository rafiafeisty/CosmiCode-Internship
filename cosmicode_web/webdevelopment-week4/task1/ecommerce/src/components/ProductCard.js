import React, { useContext } from "react";
import "./Style.css";
import { myContext } from "../context/CartContext";

const ProductCard = ({ product }) => {
  const { addCart } = useContext(myContext);
  return (
    <div className="card-main">
      <div className="card">
        <img src={product.image} alt={product.name} />
        <div className="content">
          <h3>{product.name}</h3>
          <p>${product.price}</p>
          <button
            onClick={() => {
              alert("Adding to Cart");
              addCart(product);
            }}
            className="cart"
          >
            Add To Cart
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
