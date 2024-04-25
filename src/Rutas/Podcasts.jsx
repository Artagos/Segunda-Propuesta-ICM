
import '../ComponentsCss/Podcasts.css';
import VideoPlayer from "../Componentes/VideoPlayer";
import Navbar from '../Componentes/Navbar';
import http from './axiosAux';
import React from 'react';

const Podcasts = () => {    
    const [elements,setElements]=React.useState([]);
    
    React.useEffect(()=>{
    http.get('entidades/podcasts/')
    .then(response => {
      console.log(response.data);
      setElements(response.data);
    })
    .catch(error => {
      console.error('Error fetching (Podcasts)', error);
    });
},
    [])

    return (
        <div>
            <Navbar/>
            <div className='stack'>
                {elements.map((element)=>(
                    <VideoPlayer url={element.link_podcast} light={element.foto} titulo={element.titulo} descripcion={element.descripcion}/>
                ))}
            </div>
        </div>
    )
}


export default Podcasts;