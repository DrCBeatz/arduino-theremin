import React from "react";
import "./VideoEmbed.css";

interface VideoEmbedProps {
  src: string;
}
const VideoEmbed = (props: VideoEmbedProps) => {
  return (
    <div className="video-container">
      <iframe
        className="responsive-iframe"
        width="560"
        height="315"
        src={props.src}
        title="YouTube video player"
        frameBorder="0"
        allowFullScreen
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      ></iframe>
    </div>
  );
};

export default VideoEmbed;
