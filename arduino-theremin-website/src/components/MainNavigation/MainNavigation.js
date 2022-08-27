import React from 'react';
import "./MainNavigation.css"

const MainNavigation = () => {
    return (
        <div className="header">
            <nav>
                <div>
                    <ul>
                        <li className="logo"><img className="arduino-icon" src="headerLogo-arduino.svg" /><span className="brand">Arduino Theremin</span></li>
                        <li>
                            <a href="https://github.com/DrCBeatz/arduino-theremin" target="_blank" rel="noreferrer">Github</a>
                        </li>
                        <li>
                            <a href="#">Instructions</a>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    )
}

export default MainNavigation;