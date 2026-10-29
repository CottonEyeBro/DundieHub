import React from "react";
import { useUserContext } from "../UserContext";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm"

function Login() {

    const { setUsers } = useUserContext();

    return (
        <div className="login_page">
                <div className="demo-login-note">
                    <p>
                        Trying the demo? Log in with a character account from the{" "}
                        <a
                            href="https://github.com/CottonEyeBro/DundieHub#user-login-info"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            README
                        </a>.
                    </p>
                </div>
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