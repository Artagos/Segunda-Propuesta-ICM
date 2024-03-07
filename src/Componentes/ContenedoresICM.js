import '../ComponentsCss/ContenedoresICM.css';
import { useViewport } from '../useViewport';
const ContenedorICM=({colorFondo,titulo,encabezado,descripcion,imagen,colorLetra,
colorBoton,colorLboton,colorTitulo})=>{


    const {width,height}=useViewport();
    var breakWidth= width<900
    console.log(width)
    
    return(
    <div>
        {!breakWidth?<div class="event-container" style={{backgroundColor: colorFondo, color:colorLetra}}><div class="inf-side">
            <div class="aux-inf-side">
                <div class="event-title" style={{color:colorTitulo}}>{titulo}</div>
                <div class="event-details">
                    <h4 >{encabezado}</h4>
                    <p>{descripcion}</p>
                </div>
            </div>
            <a href="#" class="buttonC"style={{colorFondo:colorBoton, backgroundColor:colorLboton}}>más</a>
        </div>
        <div class="img-side"><img src={imagen} alt="rhcp"></img></div></div>  

        :  
        
        <div class="event-container" style={{backgroundColor: colorFondo, color:colorLetra}}><div class="img-side"><img src={imagen} alt="rhcp"></img></div><div class="inf-side">
            <div class="aux-inf-side">
            <div class="event-title"style={{color:colorTitulo}}>{titulo}</div>
                <div class="event-details" style={{color:colorLetra}}>
                    <h4 >{encabezado}</h4>
                    <p>{descripcion}</p>
                    </div>
            </div>
            <a href="#" class="buttonC" style={{colorFondo:colorBoton, backgroundColor:colorLboton}}>más</a>
        </div></div>
        }
    </div>
    )
}

export default ContenedorICM;