import React from 'react';
import './Card.css';

interface CardProps {
    children: React.ReactElement
}

function Card(props: CardProps) {
    return <div className="card">{props.children}</div>
}

export default Card;