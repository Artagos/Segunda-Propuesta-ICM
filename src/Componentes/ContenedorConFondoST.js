import '../ComponentsCss/ContenedoresConFondoST.css'
const CCFST=({fondo,titulo,colorTitulo})=>{
    
    return(
        <div class="containerFST" style={{background: 'url('+fondo+')center/cover no-repeat'}}>
            <div class="contentFST">
                <div class="titleFST" style={{color:colorTitulo}}>
                    {titulo}
                </div>
            </div>
        </div>
        )
}

export default CCFST;