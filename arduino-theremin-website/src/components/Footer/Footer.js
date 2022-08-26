import React from 'react';
import './Footer.css';

const Footer = (props) => {
    return (
        <footer className="text-center">
            <a href={props.githubWebsiteLink} target="_blank" rel="noreferrer">{props.githubTitle}</a>
            <p>Website by <a href={props.authorWebsiteLink} target="_blank" rel="noreferrer">{props.authorTitle}</a></p>
        </footer>
    )
}

export default Footer;