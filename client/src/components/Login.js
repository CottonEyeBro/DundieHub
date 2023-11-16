import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";


function Login() {

    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('/users')
            .then((response) => response.json())
            .then((data) => console.log(data))
    }, []);

    return (
        <div className="login_page">
            <h1>Login Page</h1>
        </div>
    );
}

export default Login;