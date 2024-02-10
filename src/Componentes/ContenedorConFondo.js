import '../ComponentsCss/ContenedoresConFondo.css'
const CCF=({titulo,descripcion,fondo})=>{
    
    return(
        <div class="containerF" style={{ background: 'url('+fondo+')'  }}>
            <div class="contentF">
                <div class="titleF">{titulo}</div>
                <p class="paragraphF">{descripcion}</p>
            </div>
        </div>
        )
}

export default CCF;