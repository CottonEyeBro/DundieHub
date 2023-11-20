import React, { useState } from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";

function Login( {onLogin} ) {

    const [showLogin, setShowLogin] = useState(true);

    return (
        <div className="login_page">
            {showLogin ? (
                <>
                    <LoginForm onLogin={onLogin} />
                    <p>
                        Don't have an account? &nbsp;
                        <button onClick={() => setShowLogin(false)}>Create account</button>
                    </p>
                </>
            ) : (
                <>
                    <SignUpForm onLogin={onLogin} />
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