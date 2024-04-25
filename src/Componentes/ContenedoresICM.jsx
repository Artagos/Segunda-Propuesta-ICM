import '../ComponentsCss/ContenedoresICM.css';
import React from 'react';
import { useViewport } from '../useViewport';
import htmlCorte from '../Rutas/auxMethods.js';

const ContenedorICM=({colorFondo,titulo,encabezado,descripcion,imagen,colorLetra,
colorBoton,colorLboton,colorTitulo,maxLength})=>{
    const [showFullText, setShowFullText] = React.useState(false);

    const toggleShowFullText = () => {
        setShowFullText(!showFullText);
    };

    let tituloJsx= new DOMParser().parseFromString(titulo, "text/xml");
    let descripcionJsx=new DOMParser().parseFromString(descripcion, "text/xml");
    let encabezadoJsx=new DOMParser().parseFromString(encabezado, "text/xml");

    let newDescripcion= descripcion.slice(0,maxLength)+"...";
    let newDescripcionJsx= htmlCorte(newDescripcion,descripcion);
    const {width,height}=useViewport();
    var breakWidth= width<900
    
    
    return(
    <div style={{backgroundColor: colorFondo, display: 'flex'}}>
        <div style={{margin:'10px',}}>
            {!breakWidth?<div class="event-container" style={{ color:colorLetra}}><div class="inf-side">
                <div class="aux-inf-side">
                    <div dangerouslySetInnerHTML={{__html: titulo}}/>
                    <div class="event-details">
                    <div dangerouslySetInnerHTML={{__html: encabezado}}/>
                        {showFullText ?descripcion:(descripcion.length<=maxLength?<div dangerouslySetInnerHTML={{__html: descripcion}}/>:<div dangerouslySetInnerHTML={{__html: newDescripcionJsx}}/>)}
                    </div>
                </div>
                {descripcion.length>=maxLength?<a onClick={toggleShowFullText} class="buttonC"style={{color:colorBoton, backgroundColor:colorLboton}}>{showFullText ? 'Menos' : 'Mas'}</a>:null}
            </div>
            {imagen ?<div class="img-side"><img src={imagen} alt="rhcp"></img></div>:null} 
            
            </div> 

            :  
            
            <div class="event-container" style={{ color:colorLetra}}>{imagen?<div class="img-side"><img src={imagen} alt="rhcp"></img></div>:null}
                <div class="inf-side" >
                    <div class="aux-inf-side">
                    <div dangerouslySetInnerHTML={{__html: titulo}}/>
                        <div class="event-details" style={{color:colorLetra}}>
                        <div dangerouslySetInnerHTML={{__html: encabezado}}/>
                        {showFullText ?descripcion:(descripcion.length<=maxLength?<div dangerouslySetInnerHTML={{__html: descripcion}}/>:<div dangerouslySetInnerHTML={{__html: newDescripcionJsx}}/>)}
                        </div>
                    </div>
                    {descripcion.length>=maxLength?<a onClick={toggleShowFullText} class="buttonC"style={{color:colorBoton, backgroundColor:colorLboton}}>{showFullText ? 'Menos' : 'Mas'}</a>:null}
                </div>
            </div>
            }
        </div>
    </div>
    )
}

export default ContenedorICM;