import React from "react";
import Login from "../Login/Login"
import TitleBar from "../TitleBar/TitleBar"
import "./LoginPage.css"

const LoginPage = () => {
    return(
        <div className="login-body">
            <TitleBar/>
            <Login />
        </div>
    );
}


export default LoginPage