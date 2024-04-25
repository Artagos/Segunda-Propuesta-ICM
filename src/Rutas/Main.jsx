import React from "react"
import http from "./axiosAux";
import { MiniParser } from "./MiniParser";
import Navbar from "../Componentes/Navbar";
import ContenedorICM from "../Componentes/ContenedoresICM";
const Main =()=>{
    const [elements,setElements]=React.useState([]);
    
    //Fetching data 
    React.useEffect(()=>{
        http.get('entidades/banner_principal/')
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
        {/* Header  */}
        <Navbar seccion={"S_BannerPpal"}/>
        {/* Contenedores */}
        <ContenedorICM titulo={"wenoweno"} encabezado={"casasdasdawd"} descripcion={"lorem ipsum ametix candelix"} colorFondo={"black"} maxLength={10} imagen={"sadas"} />
          {elements.map((element)=>(MiniParser(element)))}
      </div>
    )
  }
  
export default Main
/* Pa despues
<div>
{elements.map((elements)=>(MiniParser(elements)))}*/    
