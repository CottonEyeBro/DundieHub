import React from "react";
import { NavLink } from 'react-router-dom';

function Header() {

    return (
        <>  
            <div class="header">
                <p>Welcome to DundieHub!</p>
                <a><NavLink to="/">Home</NavLink></a>
            </div>
            <div className = "topnav">
                <a><NavLink to="/login">Sign in/Sign up</NavLink></a>
            </div>
        </>
    )
}

export default Header