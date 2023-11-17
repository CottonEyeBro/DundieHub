import React, { useEffect, useState } from "react";
import LoginForm from "./LoginForm";
import { Link } from "react-router-dom";


function Login() {

    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('/users')
            .then((response) => response.json())
            .then((data) => setUsers(data))
    }, []);

    console.log(users)

    return (
        <div className="login_page">
            <h1>Login Page</h1>
            <LoginForm users={users} />
        </div>
    );
}

export default Login;