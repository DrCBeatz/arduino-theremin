import React from "react";
import "./Footer.css";

interface FooterProps {
  githubWebsiteLink: string;
  authorWebsiteLink: string;
  githubTitle: string;
  authorTitle: string;
}
const Footer = (props: FooterProps) => {
  return (
    <footer className="text-center">
      <a href={props.githubWebsiteLink} target="_blank" rel="noreferrer">
        {props.githubTitle}
      </a>
      <p>
        Website by{" "}
        <a href={props.authorWebsiteLink} target="_blank" rel="noreferrer">
          {props.authorTitle}
        </a>
      </p>
    </footer>
  );
};

export { Footer };
