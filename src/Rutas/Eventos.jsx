import ContenedorEventos from "../Componentes/ContenedorEventos";
import Navbar from "../Componentes/Navbar";
import React from "react";
import http from "./axiosAux";
const Eventos=()=>{
    const [eventos,setEventos]=React.useState([]);
    React.useEffect(()=>{
        http.get('entidades/eventos_semana/')
        .then(response => {
          console.log(response.data);
          setEventos(response.data);
        })
        .catch(error => {
          console.error('Error fetching (Eventos)', error);
        });
    },
    [])
    return(<div>
        <Navbar/>
        <ContenedorEventos eventos={eventos}/>
    </div>
    )
}

export default Eventos;
