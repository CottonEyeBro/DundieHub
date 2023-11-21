import React from "react";

function Footer() {

    return (
        <footer className="footer">
            <h3>Address: </h3><a href="https://www.google.com/maps/@34.2104502,-118.4365348,3a,75y,3.17h,91.45t/data=!3m6!1e1!3m4!1st6sGrKZAoJL25D3bfMEpFg!2e0!7i16384!8i8192?authuser=0&entry=ttu">1725 Slough Avenue, Suite 200, Scranton, PA</a>
            <h3>Email: </h3><a href="mailto:support@dundermifflin.com">support@dundermifflin.com</a>
            <div className="about">
                <h3>About DundieHub: </h3>
                <p>Final capstone project for my Flatiron School Full-Stack software engineering certification. Utilizes Flask, SQLAlchemy, React.js, and CSS to build a generic social media-clone for the cast of The Office.</p>
            </div>
        </footer>
    );
}

export default Footer;