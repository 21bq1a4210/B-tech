import React, {Component } from 'react';

class ColorChanger extends Component{
    constructor(props) {
        super(props);
        this.state = {
            textColor: 'black' , // Initial text color
        };
    }

    handleColorChange = (color) => {
        this.setState({ textColor : color});
    };

    render(){
        const { textColor} = this.state;

        return(
            <div>
                <h1 style={{ color: textColor}}>Text Color Changer</h1>
                <p style={{ color: textColor}}>
                    This is a sample text. Change the color using the Buttons
                </p>

                <button onClick={() => this.handleColorChange('red')}>Red</button> 
                <button onClick={()=>this.handleColorChange('blue')}>Blue</button>
                <button onClick={()=>this.handleColorChange('green')}>Green</button>
            </div>
        );
    }
}

export default ColorChanger;