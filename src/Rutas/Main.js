import React from "react"
import CCF from "../Componentes/ContenedorConFondo"
import ContenedorICM from "../Componentes/ContenedoresICM"
import axios from 'axios';
import { MiniParser } from "./MiniParser";
const Main =()=>{
    const [elements,setElements]=React.useState([]);
    
    //Fetching data
    React.useEffect(()=>{
        axios.get('http://127.0.0.1:8000/api/entidades/seccion/banner')
        .then(response => {
            console.log(response.data);
          setElements(response.data);
        })
        .catch(error => {
          console.error('Error fetching (Banner Principal)', error);
        });
    },
    [])
    

    return(
        <div>
          {elements.map((elements)=>(MiniParser(elements)))}    
        </div>
    )
}

export default Main