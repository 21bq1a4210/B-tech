import React from "react";
import "./Login.css"
import { Link } from "react-router-dom";

const LoginPage = () =>{
    return(

        <div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100">
				<form class="login100-form validate-form">
					<span class="login100-form-title">
						WELCOME
					</span>
					<Link to="/homepage" className="login100-social-link" style={{textDecoration:"none"}}>
						<button className="login100-social-card">
							<div class="wrapper">
								<div class="red"></div>
								<div class="green"></div>
								<div class="blue"></div>
								<div class="yellow"></div>
							</div>
							<span className="login100-social-label"> Continue With Microsoft</span>
						</button>
					</Link>
				</form>
			</div>
		</div>
	</div>
    );
}

export default LoginPage