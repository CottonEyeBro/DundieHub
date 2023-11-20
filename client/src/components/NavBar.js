import React from "react";
import { NavLink } from 'react-router-dom';

function NavBar() {

    return (
        <div className="main-header">  
            <div className="header">
                <NavLink className="logo" to="/">DundieHub</NavLink>
                <p>Welcome to DundieHub!</p>
            </div>
            <div className="navbar">
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
            </div>
        </div>
    )
}

export default NavBar;