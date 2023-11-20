import React, { useEffect, useState } from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";

function Login() {

    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('/users')
            .then((response) => response.json())
            .then((data) => setUsers(data))
    }, []);

    // console.log(users)

    return (
        <div className="login_page">
            <h1>Login Page</h1>
            <LoginForm users={users} />
            <SignUpForm />
        </div>
    );
}

export default Login;