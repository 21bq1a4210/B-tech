import React ,{Component}from "react";
import DashBoard from "../Dashboard/DashBoard";
import Payslips from "../Payslips/Payslips";
import Update from "../Update/Update";
import "./HomePage.css"


class HomePage extends Component {
    constructor(){
        super();
        this.state = {
            frame:<DashBoard/>
        }
    }
    
    changeFrame(event){
        this.setState({frame : event.target.value});
        console.log(event.target.value)
    }

    render(){
        return(
            <div className="homepage-body">
                <div className="homepage-menu">
                    <div className="homepage-menu-logo"></div>
                    <span className="line-break"></span>
                    <button className="homepage-button dashboard" value={<DashBoard/>} onClick={this.changeFrame}>
                        <span className="material-symbols-outlined">navigate_next</span>
                        Dash board
                    </button>
                    <button className="homepage-button payslips"
                        value={<Payslips/>}
                        onClick = {this.changeFrame}
                        >
                        <span className="material-symbols-outlined">navigate_next</span>
                        Pay slips
                    </button>
                    <button className="homepage-button update" 
                        value={<Update/>}
                        onClick={this.changeFrame}                    
                    >
                        <span className="material-symbols-outlined">navigate_next</span>
                        Update
                    </button>
                </div>
                <div className="homepage-content">
                    {this.state.frame}
                </div>
            </div>
        );
    }
}


export default HomePage