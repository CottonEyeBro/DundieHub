import React, { useState, useEffect } from "react";
import { NavLink, useHistory } from 'react-router-dom';
import { useUserContext } from "../UserContext";

function NavBar() {

    const [userSession, setUserSession] = useState(null)
    const { users, setUsers } = useUserContext();

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

    const user_id = userSession?.id

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
                <div className="signed-in-navbar">
                    {clog ? (
                        <>
                            <div className="group-profile">
                                <button className="group-profile-button"><NavLink to="/group-profile">Group Profile</NavLink></button>
                            </div>
                            <div className="user-profile">
                                <button className="user-profile-button"><NavLink to={`/${user_id}`}>User Profile</NavLink></button>
                            </div>
                            <div className="feed">
                                <button className="main-feed-button"><NavLink to="/feed">Main Feed</NavLink></button>
                            </div>
                        </>
                    ) : (
                        <></>
                    )}
                </div>
            </div>
        </div>
    )
}

export default NavBar;