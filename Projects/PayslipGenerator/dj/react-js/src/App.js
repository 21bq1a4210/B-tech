import React ,{Component} from "react";
import LoginPage from "./components/LoginPage/LoginPage";
import HomePage from "./components/HomePage/HomePage"
import "./App.css"
import { BrowserRouter , Route ,Routes } from "react-router-dom";

class App extends Component{
  render(){
    return(
      <BrowserRouter basename="/">
        <div className="app-body">
          <Routes>
              <Route path="/" element={<LoginPage/>}/>
              <Route path="/homepage" element={<HomePage/>}/>
          </Routes>
        </div>
      </BrowserRouter>
    );
  }
}

export default App