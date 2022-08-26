import React from 'react';
import './VideoEmbed.css';

const VideoEmbed = (props) => {
    return (
            <div className="container">
                <iframe className="responsive-iframe" width="560" height="315" src={props.src} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
    )
}

export default VideoEmbed;