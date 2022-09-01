import React from "react";
import "./MainNavigation.css";

const MainNavigation = () => {
  return (
    <div className="header">
      <nav>
        <div>
          <ul>
            <li className="logo">
              <img
                className="arduino-icon"
                src="headerLogo-arduino.svg"
                alt="Arduino icon"
              />
              <span className="brand">Arduino Theremin</span>
            </li>
            <li>
              <a
                href="https://github.com/DrCBeatz/arduino-theremin"
                target="_blank"
                rel="noreferrer"
              >
                Github
              </a>
            </li>
            <li>
              <a href="#video">Video</a>
            </li>
            <li>
              <a href="#midi-messages"><span className="midi-large">MIDI Messages</span><span className="midi-small">MIDI msgs</span></a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
};

export { MainNavigation };
