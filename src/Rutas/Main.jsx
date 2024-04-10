import React from "react"
import http from "./axiosAux";
import { MiniParser } from "./MiniParser";
import Navbar from "../Componentes/Navbar";
const Main =()=>{
    const [elements,setElements]=React.useState([]);
    
    //Fetching data 
    React.useEffect(()=>{
        http.get('entidades/seccion/banner')
        .then(response => {
          //console.log(response.data);
          setElements(response.data);
        })
        .catch(error => {
          console.error('Error fetching (Banner Principal)', error);
        });
    },
    [])
    

    return(
      <div>
        {/* Header  */}
        <Navbar seccion={"S_BannerPpal"}/>
        {/* Contenedores */}
          {elements.map((element)=>(MiniParser(element)))}
      </div>
    )
  }
  
export default Main
/* Pa despues
<div>
{elements.map((elements)=>(MiniParser(elements)))}*/    
