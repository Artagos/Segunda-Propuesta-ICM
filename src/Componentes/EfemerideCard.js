import React from 'react';
 // Importa los estilos CSS específicos para la tarjeta

const AnniversaryCard = ({ date, event }) => {
  return (
    <div className="anniversary-card">
      <div className="date-container">
        <p className="date-text">{date}</p>
      </div>
      <div className="event-container">
        <p className="event-text">{event}</p>
      </div>
    </div>
  );
};

export default AnniversaryCard;
