import React, { useState, useEffect } from "react";
import { NavLink, useHistory } from 'react-router-dom';

function NavBar( {users, setUsers} ) {

    const [userSession, setUserSession] = useState(null)

    const history = useHistory()

    useEffect(() => {
        fetch("/check_user_session").then((r) => {
            if (r.ok) {
                r.json().then(setUserSession);
            }
        });
    }, []);

    const clog = userSession ? true : false

    function handleLogoutClick() {
        
        fetch("/logout", { method: "DELETE" })
            .then((resp) => {
                if (resp.ok) {
                    setUsers(null);
                    history.push("/login");

                    setTimeout(() => {
                        window.location.reload()
                    }, 125)
                }
            });
    }

    return (
        <div className="main-header">  
        <div className="header">
            <NavLink className="logo" to="/">DundieHub</NavLink>
            <p>Welcome to DundieHub!</p>
        </div>
            <div className="navbar">
                <div className = "login">
                    {clog ? (
                        <div className="logout-div">
                            <button className="logout-button" onClick={handleLogoutClick}>Logout</button>
                        </div>
                    ) : (
                        <div className="login-div">
                            <button className="signin-signup-button"><NavLink to="/login">Sign in/Sign up</NavLink></button>
                        </div>
                    )}
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