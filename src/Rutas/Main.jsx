import React from "react"
import axios from 'axios';
import { MiniParser } from "./MiniParser";
import ContenedorICM from "../Componentes/ContenedoresICM";
import CCFST from "../Componentes/ContenedorConFondoST";
import CCF from "../Componentes/ContenedorConFondo";
import Navbar from "../Componentes/Navbar";
const Main =()=>{
    const [elements,setElements]=React.useState([]);
    
    //Fetching data 
    React.useEffect(()=>{
        axios.get('http://127.0.0.1:8000/api/entidades/seccion/banner')
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
        <CCFST titulo={'Empresas y Negocios'} fondo={'https://cdn.pixabay.com/photo/2024/01/26/23/53/building-8534894_1280.jpg'}/>
        
        <ContenedorICM colorTitulo={'black'} titulo={'HISTORIA'} encabezado={'lore ipsum amet'} 
        descripcion={'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In egestas erat imperdiet sed. Dolor sit amet consectetur adipiscing elit ut aliquam. Id faucibus nisl tincidunt eget nullam. Pellentesque habitant morbi tristique senectus et netus et. Aliquet nec ullamcorper sit amet risus nullam eget felis eget. Rhoncus urna neque viverra justo nec ultrices dui sapien. At varius vel pharetra vel turpis nunc eget lorem. Turpis egestas integer eget aliquet. Facilisi cras fermentum odio eu feugiat pretium nibh. In egestas erat imperdiet sed euismod. Tortor id aliquet lectus proin nibh. Et tortor consequat id porta nibh venenatis cras sed. Nibh venenatis cras sed felis eget velit. Eu lobortis elementum nibh tellus molestie nunc non. Ullamcorper dignissim cras tincidunt lobortis feugiat vivamus. Sit amet purus gravida quis blandit turpis cursus. Turpis tincidunt id aliquet risus feugiat in. Nibh mauris cursus mattis molestie a iaculis.'} colorFondo={'orange'} 
        colorBoton={'white'} colorLboton={'black'} colorLetra={'white'} imagen={'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtX2YGWBQQjfP8LWR4lltIJBEKzWv0R8XrHg&usqp=CAU'}/>
        
        <CCF colorTitulo={'black'} fondo={"https://media.revistagq.com/photos/64bf739cfdec95d9b3fbd8cf/4:3/w_1064,h_798,c_limit/oppenheimer-blanco-negro.jpeg"} titulo={"Titulo por defecto"} descripcion={"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}/>
        
      </div>
    )
  }

export default Main
/* Pa despues
<div>
            {elements.map((elements)=>(MiniParser(elements)))}    
          </div>*/