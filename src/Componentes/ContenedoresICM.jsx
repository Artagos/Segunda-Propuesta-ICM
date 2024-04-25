import '../ComponentsCss/ContenedoresICM.css';
import React from 'react';
import { useViewport } from '../useViewport';
const ContenedorICM=({colorFondo,titulo,encabezado,descripcion,imagen,colorLetra,
colorBoton,colorLboton,colorTitulo})=>{

    let tituloJsx= new DOMParser().parseFromString(titulo, "text/xml");
    let descripcionJsx=new DOMParser().parseFromString(descripcion, "text/xml");
    let encabezadoJsx=new DOMParser().parseFromString(encabezado, "text/xml");

    const {width,height}=useViewport();
    var breakWidth= width<900
    
    
    return(
    <div style={{backgroundColor: colorFondo, display: 'flex'}}>
        <div style={{margin:'10px',}}>
            {!breakWidth?<div class="event-container" style={{ color:colorLetra}}><div class="inf-side">
                <div class="aux-inf-side">
                    <div class="event-title" style={{color:colorTitulo}}>{tituloJsx}</div>
                    <div class="event-details">
                    <h2 style={{fontSize:'15px'}}>{encabezadoJsx}</h2>
                        <p>{descripcionJsx}</p>
                    </div>
                </div>
                <a href="#" class="buttonC"style={{color:colorBoton, backgroundColor:colorLboton}}>más</a>
            </div>
            {imagen ?<div class="img-side"><img src={imagen} alt="rhcp"></img></div>:null} 
            
            </div> 

            :  

            <div  class="event-container" style={{ color:colorLetra}}>{imagen?<div class="img-side"><img src={imagen} alt="rhcp"></img></div>:null}
                <div  class="inf-side" >
                    <div  class="aux-inf-side">
                    <div  class="event-title"style={{color:colorTitulo}}>{tituloJsx}</div>
                        <div class="event-details" style={{color:colorLetra}}>
                            <h2 style={{fontSize:'15px'}}>{encabezadoJsx}</h2>
                            <p>{descripcionJsx}</p>
                        </div>
                    </div>
                    <a href="#" class="buttonC" style={{color:colorBoton, backgroundColor:colorLboton}}>más</a>
                </div>
            </div>
            }
        </div>
    </div>
    )
}

export default ContenedorICM;