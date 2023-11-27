import React, { useState, useEffect } from "react";
import { NavLink } from 'react-router-dom';

function NavBar( {users, setUsers} ) {

    const [userSession, setUserSession] = useState(null)

    function handleLogoutClick() {
        
        fetch("/logout", { method: "DELETE" })
            .then((resp) => {
                if (resp.ok) {
                    setUsers(null);
          }
        });
      }

    useEffect(() => {
        fetch("/check_user_session").then((r) => {
        if (r.ok) {
            r.json().then(setUserSession);
        }
        });
    }, []);

    const userLogin = setUserSession ? true : false

    return (
        <div className="main-header">  
        <div className="header">
            <NavLink className="logo" to="/">DundieHub</NavLink>
            <p>Welcome to DundieHub!</p>
        </div>
        {userLogin ? (
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
                <div className="logout-button">
                    <button onClick={handleLogoutClick}>Logout</button>
                </div>
            </div>
        ) : (
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
        )}
        
        </div>
    )
}

export default NavBar;