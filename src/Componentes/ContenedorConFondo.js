import '../ComponentsCss/ContenedoresConFondo.css'
const CCF=({titulo,descripcion,fondo,colorTitulo})=>{
    
    return(
        <div class="containerF" style={{ background: 'url('+fondo+')center/cover no-repeat'  }}>
            <div class="contentF">
                <div class="titleF" style={{color:colorTitulo}}>{titulo}</div>
                <p class="paragraphF">{descripcion}</p>
            </div>
        </div>
        )
}

export default CCF;