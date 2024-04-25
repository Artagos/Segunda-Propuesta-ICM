import '../ComponentsCss/ContenedoresConFondoST.css'
const CCFST=({fondo,titulo,colorTitulo})=>{
    let tituloJsx= new DOMParser().parseFromString(titulo, "text/xml");
    
    

    return(
        <div class="containerFST" style={{background: 'url('+fondo+')center/cover no-repeat'}}>
            <div class="contentFST">
                <div class="titleFST" style={{color:colorTitulo}}>
                    {tituloJsx}
                </div>
            </div>
        </div>
        )
}

export default CCFST;