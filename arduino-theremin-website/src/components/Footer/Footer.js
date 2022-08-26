import React from 'react';


const Footer = (props) => {
    return (
        <footer className="text-center">
            <hr></hr>
            <a href={props.githubWebsiteLink} target="_blank" rel="noreferrer">{props.githubTitle}</a>
            <p>Website by <a href={props.authorWebsiteLink} target="_blank" rel="noreferrer">{props.authorTitle}</a></p>
        </footer>
    )
}

export default Footer;