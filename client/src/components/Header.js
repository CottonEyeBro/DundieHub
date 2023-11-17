import React from "react";
import { NavLink } from 'react-router-dom';

function Header() {

    return (
        <>  
            <div className="header">
                <p>Welcome to DundieHub!</p>
                <NavLink to="/">Home</NavLink>
            </div>
            <div className = "topnav">
                <NavLink to="/login">Sign in/Sign up</NavLink>
            </div>
        </>
    )
}

export default Header