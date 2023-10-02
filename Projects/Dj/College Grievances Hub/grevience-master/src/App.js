import React ,{Component} from "react";
import LoginPage from "./components/LoginPage/LoginPage";
import Homepage from "./components/Homepage/Homepage";
import "./App.css"
import { BrowserRouter , Route ,Routes } from "react-router-dom";

class App extends Component{
  render(){
    return(
      <BrowserRouter basename="/">
        <div className="app-body">
          <Routes>
              <Route path="/" element={<LoginPage/>}/>
              <Route path="/home" element={<Homepage/>}/>
          </Routes>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
