import React, { useState } from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";

function Login( {setUsers} ) {

    const [showLogin, setShowLogin] = useState(true);
    console.log(setUsers)

    return (
        <div className="login_page">
            {showLogin ? (
                <>
                    <LoginForm setUsers={setUsers} />
                    <p>
                        Don't have an account? &nbsp;
                        <button onClick={() => setShowLogin(false)}>Create account</button>
                    </p>
                </>
            ) : (
                <>
                    <SignUpForm setUsers={setUsers} />
                    <p>
                        Already have an account? &nbsp;
                        <button onClick={() => setShowLogin(true)}>Log in</button>
                    </p>
                </>
            )}
        </div>
    );
}

export default Login;