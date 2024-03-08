import '../ComponentsCss/ContenedoresICM.css';
import { useViewport } from '../useViewport';
const ContenedorICM=({colorFondo,titulo,encabezado,descripcion,imagen,colorLetra,
colorBoton,colorLboton,colorTitulo})=>{


    const {width,height}=useViewport();
    var breakWidth= width<900
    
    
    return(
    <div style={{backgroundColor: colorFondo, display: 'flex'}}>
        <div style={{margin:'10px',}}>
            {!breakWidth?<div class="event-container" style={{ color:colorLetra}}><div class="inf-side">
                <div class="aux-inf-side">
                    <div class="event-title" style={{color:colorTitulo}}>{titulo}</div>
                    <div class="event-details">
                    <h2 style={{fontSize:'15px'}}>{encabezado}</h2>
                        <p>{descripcion}</p>
                    </div>
                </div>
                <a href="#" class="buttonC"style={{color:colorBoton, backgroundColor:colorLboton}}>más</a>
            </div>
            <div class="img-side"><img src={imagen} alt="rhcp"></img></div></div>  

            :  
            
            <div class="event-container" style={{ color:colorLetra}}><div class="img-side"><img src={imagen} alt="rhcp"></img></div>
                <div class="inf-side" >
                    <div class="aux-inf-side">
                    <div class="event-title"style={{color:colorTitulo}}>{titulo}</div>
                        <div class="event-details" style={{color:colorLetra}}>
                            <h2 style={{fontSize:'15px'}}>{encabezado}</h2>
                            <p>{descripcion}</p>
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