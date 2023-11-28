import React from "react";
import { useUserContext } from "../UserContext";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm"

function Login() {

    const { users, setUsers } = useUserContext();

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