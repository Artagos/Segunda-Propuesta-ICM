import React from "react"
import CCF from "../Componentes/ContenedorConFondo"
import ContenedorICM from "../Componentes/ContenedoresICM"
import axios from 'axios';
const Main =()=>{
    const [elements,setElements]=React.useState();
    React.useEffect(()=>{
        axios.get('/api/entidades/seccion/banner')
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
        
        <CCF/>
        <ContenedorICM/>
        
        </div>
    )
}

export default Main