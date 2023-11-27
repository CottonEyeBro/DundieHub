import React, { useState } from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm"

function Login( {setUsers, setCheckUserSession} ) {

    // const [showLogin, setShowLogin] = useState(true);
    // console.log(setUsers)

    return (
        <div className="login_page">
                <div>
                    <LoginForm setUsers={setUsers} setCheckUserSession={setCheckUserSession} />
                </div>
                <div>
                    <SignUpForm setUsers={setUsers} setCheckUserSession={setCheckUserSession} />
                </div>
        </div>
    )
}

export default Login;