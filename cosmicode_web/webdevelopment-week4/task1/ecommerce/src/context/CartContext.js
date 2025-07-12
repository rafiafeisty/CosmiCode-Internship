import React, { useEffect } from 'react'
import { useState,createContext } from 'react'

export const myContext=createContext()

const CartContext = ({children}) => {
    const [cart,setcart]=useState(()=>{
        const saved=localStorage.getItem('cart')
        return saved?JSON.parse(saved):[]
    })
    useEffect(()=>{
        localStorage.setItem('cart',JSON.stringify(cart))
    })
    const addCart=(product)=>{
        setcart(prev=>[...prev,product])
    }
    const removeCart=(id)=>{
        setcart(prev=>prev.filter(item=>item.id!==id))
    }
  return (
    <myContext.Provider value={{cart,addCart,removeCart}}>
        {children}
    </myContext.Provider>
  )
}

export default CartContext
