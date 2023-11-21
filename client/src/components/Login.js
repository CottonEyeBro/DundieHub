import React, { useState } from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";

function Login( {setUsers, setCheckUserSession} ) {

    const [showLogin, setShowLogin] = useState(true);
    // console.log(setUsers)

    return (
        <div className="login_page">
            {showLogin ? (
                <>
                    <LoginForm setUsers={setUsers} setCheckUserSession={setCheckUserSession} />
                    <p>
                        Don't have an account? &nbsp;
                        <button onClick={() => setShowLogin(false)}>Create account</button>
                    </p>
                </>
            ) : (
                <>
                    <SignUpForm setUsers={setUsers} setCheckUserSession={setCheckUserSession} />
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