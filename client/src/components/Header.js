import React from "react";
import { NavLink } from 'react-router-dom';

function Header() {

    return (
        <>  
            <div className="header">
                <p>Welcome to DundieHub!</p>
                <NavLink to="/">Home</NavLink>
            </div>
            <div className = "login">
                <NavLink to="/login">Sign in/Sign up</NavLink>
            </div>
            <div className="feed">
                <NavLink to="/feed">Main Feed</NavLink>
            </div>
            <div className="user-profile">
                <NavLink to="/user-profile">User Profile</NavLink>
            </div>
            <div className="group-profile">
                <NavLink to="/group-profile">Group Profile</NavLink>
            </div>
        </>
    )
}

export default Header