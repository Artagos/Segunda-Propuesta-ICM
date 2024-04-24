import '../ComponentsCss/ContenedoresConFondo.css'
const CCF=({titulo,descripcion,fondo,colorTitulo})=>{
    let tituloJsx= new DOMParser().parseFromString(titulo, "text/xml");
    let descripcionJsx=new DOMParser().parseFromString(descripcion, "text/xml");
    

    return(
        <div class="containerF" style={{ background: 'url('+fondo+')center/cover no-repeat'  }}>
            <div class="contentF">
                <div class="titleF" style={{color:colorTitulo}}>{tituloJsx}</div>
                <p class="paragraphF">{descripcionJsx}</p>
            </div>
        </div>
        )
}

export default CCF;