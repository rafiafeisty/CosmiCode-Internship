import React from "react";
import Product from "../data/Product.js";
import ProductCard from "./ProductCard";
import "./Style.css";

const ProductList = () => {
  return (
    <>
      <center>
        <h1 className="product-head">All Products</h1>
      </center>
      <div className="card-loop">
        {Product.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </>
  );
};

export default ProductList;
