import React from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm"

function Login( {setUsers} ) {

    return (
        <div className="login_page">
                <div>
                    <LoginForm setUsers={setUsers} />
                </div>
                <div>
                    <SignUpForm setUsers={setUsers} />
                </div>
        </div>
    )
}

export default Login;