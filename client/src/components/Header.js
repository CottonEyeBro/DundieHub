import React from "react";
import { NavLink } from 'react-router-dom';

function Header() {

    return (
        <>  
            <div class="header">
                <h1>DundieHub</h1>
                <p>Welcome to DundieHub!</p>
            </div>
            <div className = "topnav">
                <a><NavLink to="/login">Sign in/Sign up</NavLink></a>
            </div>
        </>
    )
}

export default Header