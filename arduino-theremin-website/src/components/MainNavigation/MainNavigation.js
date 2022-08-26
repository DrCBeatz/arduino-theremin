import React from 'react';
import "./MainNavigation.css"
// import classes from './MainNavigation.module.css';

const MainNavigation = () => {
    return (
        <div className="header">
            <nav>
                <div>
                    <ul>
                        <li>
                            <a href="https://github.com/DrCBeatz/arduino-theremin" target="_blank" rel="noreferrer">Github</a>
                        </li>
                        <li>
                            <a hret="#">Video</a>
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