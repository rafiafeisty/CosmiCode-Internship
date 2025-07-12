import React from 'react'
import './Style.css'
import {Link} from 'react-router-dom'

const Header = () => {
  return (
    <>
    <div className="navbar">
        <h2>Ecommerce</h2>
        <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/cart">Cart</Link></li>
            <li><Link to="/about">About</Link></li>
        </ul>
    </div>
    </>
  )
}

export default Header
