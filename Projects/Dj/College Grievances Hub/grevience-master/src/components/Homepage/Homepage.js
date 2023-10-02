import React ,{Component}from "react";
import "./Homepage.css"


class Homepage extends Component{

    constructor(){
        super()
        this.state = {

        }
    }
    clicked = ()=>{
        if(document.getElementById("nav-container").style.width === "12%"){
            document.getElementById("nav-container").style.width = "5%";
            document.getElementById("sidenav").style.display = "none";
            document.getElementById("open-close-btn").style.marginRight="auto";
        }
        else{
            document.getElementById("nav-container").style.width = "12%"
            document.getElementById("sidenav").style.display="";
            document.getElementById("open-close-btn").style.marginRight = "10px"
        }
    }

   render(){
    return(
        <div className="home">
            <div className="home-title">
                <div className="home-title-logo"></div>
                <label>Vasireddy Venkatadri Institute of Technology</label>
                <div className="home-title-dd">
                    <button>Need Help ?</button>
                </div>
            </div>
            <div className="home-body">
                <div className="nav-container" id="nav-container">
                   <div className="open-close-btn" id="open-close-btn" onClick={this.clicked}></div>
                   <div id="sidenav" className="sidenav" style={{display:"none"}}>
                        <label href="#">Home</label>
                        <label href="#">Academics</label>
                        <label href="#">Placement</label>
                        <label href="#">Facilities</label>
                        <label href="#">About Us</label>    
                    </div>
                </div>
                <div className="form-container">
                    <h3>Grevience Form</h3>
                    <div className="g-form-container">
                        <form className="g-form">
                            <div className="g-form-name g-form-e">
                                <label className="l label-name g-form-name-l">Full Name of The Complaintant(student or faculty)</label>
                                <input type="text" className="g-form-name-in in input-name"/>
                            </div>
                            <div className="g-form-reg g-form-e">
                                <label className="l label-reg g-form-reg-l">Registration Number</label>
                                <input type="text" className="g-form-reg-in in input-reg"/>
                            </div>
                            <div className="g-form-email g-form-e">
                                <label className="g-form-email-l l label-email">Email</label>
                                <input type="email" className="g-form-email-in in input-email"/>
                            </div>
                            <div className="g-form-who g-form-e">
                                <label className="g-form-who-l l label-who">Who are you ?</label>
                                <div className="g-form-who-opt">
                                    <div>
                                        <input type="radio" value="student" id="whoareyou" name="who"/>
                                        <label>Student</label>
                                    </div>
                                    <div>
                                        <input type="radio" value="faculty" id="whoareyou" name="who"/>
                                        <label>Faculty</label>  
                                    </div>
                                </div>
                            </div>
                            <div className="g-form-dept g-form-e">
                                <label className="g-form-dept-l l label-dept">Department</label>
                                <select name="dept" className="in">
                                    <option value="cse">CSE</option>
                                    <option value="csm">CSM</option>
                                    <option value="cic">CIC</option>
                                    <option value="cso">CSO</option>
                                    <option value="it">IT</option>
                                    <option value="mech">MECH</option>
                                    <option value="civil">CIVIL</option>
                                    <option value="aiml">AIML</option>
                                    <option value="EEE">EEE</option>
                                    <option value="ECE">ECE</option>
                                    <option value="AIDS">AIDS</option>

                                </select>
                            </div>
                            <div className="g-form-year g-form-e">
                                <label className="g-form-year-l l label-year">Year</label>
                                <select name="year" id="year" className="in">
                                    <option value="1">1st year</option>
                                    <option value="2">2nd year</option>
                                    <option value="3">3rd year</option>
                                    <option value="4">4th year</option>
                                </select>
                            </div>
                            <div className="g-form-g g-form-e">
                                <label className="g-form-g-l l label-g">Type of Grevience</label>
                                <select name="g" id="g" className="in">
                                    <option value="academic">Academic</option>
                                    <option value="non-academic">Non-Academic</option>
                                    <option value="discrimination">Discrimination</option>
                                </select>
                            </div>
                            <div className="g-form-form g-form-e">
                                <label className="g-form-type label-type l">Grevience column</label>
                                <textarea placeholder="enter your complaints" className="input-textarea in" style={{resize:"none"}}>

                                </textarea>
                            </div>
                            <div className="g-form-submit g-form-e">
                                <input className="g-form-sub-in in input-submit" type="submit" value="Submit"/>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
   }
}


export default Homepage